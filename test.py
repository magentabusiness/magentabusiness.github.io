#!/usr/bin/env python3
import os
import re
import sys
import tkinter as tk
from tkinter import ttk, messagebox

SEARCH_SUBSTRING = "iot-gateway"

# Сколько символов слева/справа от вхождения показывать
CONTEXT_CHARS = 80

TEXT_EXTENSIONS = {
    ".md", ".markdown",
    ".html", ".htm",
    ".liquid",
    ".txt",
    ".scss", ".css",
    ".js", ".ts",
    ".yml", ".yaml", ".json",
}

SKIP_DIRS = {".git", ".idea", ".vscode", "node_modules", ".venv", "venv", "__pycache__"}

# --- Регексы для ссылок с iot-gateway ---

# Markdown: [text](/...iot-gateway...)
MD_LINK_RE = re.compile(
    r"\[(?P<text>[^\]]+)\]\((?P<url>[^)]+"
    + re.escape(SEARCH_SUBSTRING) +
    r"[^)]*)\)"
)

# HTML: <a href="/...iot-gateway...">text</a>
HTML_LINK_RE = re.compile(
    r"<a\s+[^>]*href=(?P<q>\"|')(?P<url>[^\"']*"
    + re.escape(SEARCH_SUBSTRING) +
    r"[^\"']*)(?P=q)[^>]*>(?P<text>.*?)</a>",
    re.IGNORECASE | re.DOTALL,
    )


def is_text_file(path: str) -> bool:
    ext = os.path.splitext(path)[1].lower()
    if ext in TEXT_EXTENSIONS:
        return True
    # на всякий случай пробуем как utf-8
    try:
        with open(path, "r", encoding="utf-8") as f:
            f.read(2048)
        return True
    except Exception:
        return False


def apply_replacements(content: str) -> str:
    """Удаляем ссылки с iot-gateway, оставляя текст."""
    def md_replace(m: re.Match) -> str:
        return m.group("text")

    def html_replace(m: re.Match) -> str:
        return m.group("text")

    new = MD_LINK_RE.sub(md_replace, content)
    new = HTML_LINK_RE.sub(html_replace, new)
    return new


def collect_files(root="."):
    """Собираем список файлов, где есть *ссылки* с iot-gateway (а не просто текст)."""
    candidates = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if not is_text_file(path):
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception:
                continue

            if SEARCH_SUBSTRING not in text:
                continue

            modified = apply_replacements(text)
            if modified != text:
                candidates.append(path)

    return candidates


def build_snippets(content: str):
    """
    Строим список фрагментов вокруг каждого вхождения SEARCH_SUBSTRING.
    Возвращает список кортежей (orig_snippet, mod_snippet).
    """
    snippets = []
    for m in re.finditer(re.escape(SEARCH_SUBSTRING), content):
        start = max(0, m.start() - CONTEXT_CHARS)
        end = min(len(content), m.end() + CONTEXT_CHARS)
        orig_snip = content[start:end]
        mod_snip = apply_replacements(orig_snip)
        snippets.append((orig_snip, mod_snip))
    return snippets


class IotGatewayRemoverApp:
    def __init__(self, root, files):
        self.root = root
        self.files = files
        self.total = len(files)
        self.index = 0

        self.full_original = ""
        self.full_modified = ""
        self.current_path = None
        self.changed_count = 0

        # список (orig_snip, mod_snip)
        self.snippets = []
        # ranges для подсветки контекста в text widgets
        self.snip_ranges_original = []
        self.snip_ranges_modified = []

        self.root.title("Удаление ссылок с iot-gateway")
        self.root.geometry("1400x800")

        self.create_widgets()
        self.bind_hotkeys()
        self.load_current_file()

    def create_widgets(self):
        # Верхняя панель
        top_frame = ttk.Frame(self.root, padding=5)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.file_label = ttk.Label(top_frame, text="", anchor="w")
        self.file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.counter_label = ttk.Label(top_frame, text="", anchor="e")
        self.counter_label.pack(side=tk.RIGHT)

        # Центральная область: две текстовые панели
        center_frame = ttk.Frame(self.root, padding=5)
        center_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        left_frame = ttk.Frame(center_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 2))

        right_frame = ttk.Frame(center_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(2, 0))

        left_label = ttk.Label(left_frame, text="Оригинал (фрагменты)", anchor="w")
        left_label.pack(side=tk.TOP, anchor="w")

        self.text_original = tk.Text(
            left_frame, wrap="word", undo=False, font=("Courier New", 10)
        )
        self.text_original.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        left_scroll = ttk.Scrollbar(
            left_frame, orient=tk.VERTICAL, command=self.text_original.yview
        )
        left_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_original.configure(yscrollcommand=left_scroll.set)

        right_label = ttk.Label(right_frame, text="После удаления ссылок (фрагменты)", anchor="w")
        right_label.pack(side=tk.TOP, anchor="w")

        self.text_modified = tk.Text(
            right_frame, wrap="word", undo=False, font=("Courier New", 10)
        )
        self.text_modified.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right_scroll = ttk.Scrollbar(
            right_frame, orient=tk.VERTICAL, command=self.text_modified.yview
        )
        right_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_modified.configure(yscrollcommand=right_scroll.set)

        # Низ: кнопки
        bottom_frame = ttk.Frame(self.root, padding=5)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.btn_accept = ttk.Button(
            bottom_frame, text="Принять (A)", command=self.on_accept
        )
        self.btn_accept.pack(side=tk.LEFT, padx=5)

        self.btn_skip = ttk.Button(
            bottom_frame, text="Пропустить (S)", command=self.on_skip
        )
        self.btn_skip.pack(side=tk.LEFT, padx=5)

        self.status_label = ttk.Label(
            bottom_frame, text="", anchor="e"
        )
        self.status_label.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        # Настройки текстовых полей
        self.text_original.config(state=tk.DISABLED)
        self.text_modified.config(state=tk.DISABLED)

        # Теги
        self.text_original.tag_configure(
            "ctx_red", background="#552222", foreground="#ffffff"
        )
        self.text_modified.tag_configure(
            "ctx_green", background="#225522", foreground="#ffffff"
        )
        self.text_original.tag_configure(
            "sub_highlight", background="#aa0000", foreground="#ffffff"
        )

    def bind_hotkeys(self):
        self.root.bind("<Key-a>", lambda e: self.on_accept())
        self.root.bind("<Key-A>", lambda e: self.on_accept())
        self.root.bind("<Key-s>", lambda e: self.on_skip())
        self.root.bind("<Key-S>", lambda e: self.on_skip())

    def load_current_file(self):
        if self.index >= self.total:
            self.finish()
            return

        path = self.files[self.index]
        self.current_path = path
        rel_path = os.path.relpath(path, os.getcwd())

        self.file_label.config(text=f"Файл: {rel_path}")
        self.counter_label.config(text=f"{self.index + 1} / {self.total}")
        self.status_label.config(
            text=f"Изменено файлов: {self.changed_count} из {self.total}"
        )

        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            messagebox.showerror("Ошибка чтения", f"Не удалось прочитать файл:\n{path}\n\n{e}")
            self.on_skip()
            return

        modified = apply_replacements(content)
        self.full_original = content
        self.full_modified = modified

        # Строим фрагменты по вхождениям
        self.snippets = build_snippets(content)
        if not self.snippets:
            # Теоретически не должно случиться, так как collect_files уже фильтрует
            self.on_skip()
            return

        self.update_text_widgets()

    def update_text_widgets(self):
        self.text_original.config(state=tk.NORMAL)
        self.text_modified.config(state=tk.NORMAL)

        self.text_original.delete("1.0", tk.END)
        self.text_modified.delete("1.0", tk.END)

        self.text_original.tag_remove("ctx_red", "1.0", tk.END)
        self.text_original.tag_remove("sub_highlight", "1.0", tk.END)
        self.text_modified.tag_remove("ctx_green", "1.0", tk.END)

        self.snip_ranges_original = []
        self.snip_ranges_modified = []

        total_snips = len(self.snippets)

        # Вставляем фрагменты по очереди
        for i, (orig_snip, mod_snip) in enumerate(self.snippets, start=1):
            header = f"=== Участок {i}/{total_snips} ===\n"

            # Оригинал
            start_idx_orig_header = self.text_original.index(tk.END)
            self.text_original.insert(tk.END, header)
            start_idx_orig_snip = self.text_original.index(tk.END)
            self.text_original.insert(tk.END, orig_snip + "\n\n")
            end_idx_orig_snip = self.text_original.index(tk.END)

            # Модифицированный
            start_idx_mod_header = self.text_modified.index(tk.END)
            self.text_modified.insert(tk.END, header)
            start_idx_mod_snip = self.text_modified.index(tk.END)
            self.text_modified.insert(tk.END, mod_snip + "\n\n")
            end_idx_mod_snip = self.text_modified.index(tk.END)

            # Сохраняем диапазоны для подсветки контекста
            self.snip_ranges_original.append((start_idx_orig_snip, end_idx_orig_snip))
            self.snip_ranges_modified.append((start_idx_mod_snip, end_idx_mod_snip))

        # Подсветка контекста
        for start, end in self.snip_ranges_original:
            self.text_original.tag_add("ctx_red", start, end)
        for start, end in self.snip_ranges_modified:
            self.text_modified.tag_add("ctx_green", start, end)

        # Доп. подсветка самих "iot-gateway" в оригинале
        start = "1.0"
        while True:
            pos = self.text_original.search(SEARCH_SUBSTRING, start, tk.END)
            if not pos:
                break
            end = f"{pos}+{len(SEARCH_SUBSTRING)}c"
            self.text_original.tag_add("sub_highlight", pos, end)
            start = end

        self.text_original.config(state=tk.DISABLED)
        self.text_modified.config(state=tk.DISABLED)

    def on_accept(self):
        if self.current_path is None:
            return
        try:
            with open(self.current_path, "w", encoding="utf-8") as f:
                f.write(self.full_modified)
            self.changed_count += 1
        except Exception as e:
            messagebox.showerror("Ошибка записи", f"Не удалось записать файл:\n{self.current_path}\n\n{e}")
        self.index += 1
        self.load_current_file()

    def on_skip(self):
        self.index += 1
        self.load_current_file()

    def finish(self):
        self.file_label.config(text="Обработка завершена.")
        self.counter_label.config(text=f"{self.total} / {self.total}")
        self.status_label.config(
            text=f"Готово. Изменено файлов: {self.changed_count} из {self.total}"
        )
        self.btn_accept.config(state=tk.DISABLED)
        self.btn_skip.config(state=tk.DISABLED)
        messagebox.showinfo(
            "Готово",
            f"Файлов с ссылками на '{SEARCH_SUBSTRING}': {self.total}\n"
            f"Изменено: {self.changed_count}\n"
            f"Пропущено: {self.total - self.changed_count}"
        )


def main():
    root_dir = "."
    print(f"Сканирование проекта в {os.path.abspath(root_dir)} ...")

    files = collect_files(root_dir)
    total = len(files)

    if total == 0:
        print(f"Ссылок с '{SEARCH_SUBSTRING}' не найдено.")
        # создадим root только для сообщения
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(
            "Нет работы",
            f"Ссылок с '{SEARCH_SUBSTRING}' не найдено."
        )
        root.destroy()
        return

    print(f"Найдено файлов с ссылками на '{SEARCH_SUBSTRING}': {total}")

    root = tk.Tk()
    app = IotGatewayRemoverApp(root, files)
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nРабота прервана пользователем.")
        sys.exit(0)
