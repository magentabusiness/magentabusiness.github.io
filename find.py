#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import sys
import tempfile
import shutil
import traceback

try:
    import tkinter as tk
    from tkinter import messagebox
except Exception:
    print("Ошибка: Tkinter недоступен. Установите python3-tk.", file=sys.stderr)
    raise

try:
    import cairosvg
except ImportError:
    print("Ошибка: требуется библиотека 'cairosvg'. Установите: pip install cairosvg", file=sys.stderr)
    sys.exit(1)


def find_svg_files(root_dir: str) -> list[str]:
    files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for name in filenames:
            if name.lower().endswith(".svg"):
                files.append(os.path.join(dirpath, name))
    files.sort()
    return files


def try_render_svg_to_png(svg_bytes: bytes, out_png_path: str) -> bool:
    try:
        cairosvg.svg2png(bytestring=svg_bytes, write_to=out_png_path)
        return True
    except Exception:
        return False


class App:
    def __init__(self, root, svgs_to_review, make_backup=True, dry_run=False):
        self.root = root
        self.root.title("SVG Color Approver")

        self.svgs = svgs_to_review
        self.idx = 0
        self.make_backup = make_backup
        self.dry_run = dry_run

        self.tmpdir = tempfile.mkdtemp(prefix="svg_preview_")

        self.path_label = tk.Label(root, text="", anchor="w", justify="left", wraplength=1200)
        self.path_label.pack(fill="x", padx=10, pady=(10, 6))

        self.images_frame = tk.Frame(root); self.images_frame.pack(fill="both", expand=True, padx=10)
        self.left_col = tk.Frame(self.images_frame); self.left_col.pack(side="left", fill="both", expand=True, padx=(0,5))
        self.right_col = tk.Frame(self.images_frame); self.right_col.pack(side="left", fill="both", expand=True, padx=(5,0))

        self.old_label = tk.Label(self.left_col, text="Оригинал", font=("TkDefaultFont", 10, "bold")); self.old_label.pack(pady=(0,4))
        self.old_canvas = tk.Label(self.left_col); self.old_canvas.pack(fill="both", expand=True)

        self.new_label = tk.Label(self.right_col, text="С заменой", font=("TkDefaultFont", 10, "bold")); self.new_label.pack(pady=(0,4))
        self.new_canvas = tk.Label(self.right_col); self.new_canvas.pack(fill="both", expand=True)

        self.buttons = tk.Frame(root); self.buttons.pack(fill="x", pady=10)
        self.approve_btn = tk.Button(self.buttons, text="✅ Утвердить (A)", command=self.approve_current); self.approve_btn.pack(side="left", padx=5)
        self.skip_btn = tk.Button(self.buttons, text="⏭ Пропустить (S)", command=self.skip_current); self.skip_btn.pack(side="left", padx=5)
        self.quit_btn = tk.Button(self.buttons, text="⛔ Выход (Q)", command=self.quit_app); self.quit_btn.pack(side="right", padx=5)

        self.status_label = tk.Label(root, text="", anchor="w"); self.status_label.pack(fill="x", padx=10, pady=(0,10))

        root.bind("<KeyPress-a>", lambda e: self.approve_current())
        root.bind("<KeyPress-A>", lambda e: self.approve_current())
        root.bind("<KeyPress-s>", lambda e: self.skip_current())
        root.bind("<KeyPress-S>", lambda e: self.skip_current())
        root.bind("<KeyPress-q>", lambda e: self.quit_app())
        root.protocol("WM_DELETE_WINDOW", self.quit_app)

        self.current_old_png = None
        self.current_new_png = None
        self.tk_old_img = None
        self.tk_new_img = None

        self.load_current()

    def cleanup_tmp(self):
        try: shutil.rmtree(self.tmpdir)
        except Exception: pass

    def quit_app(self):
        self.cleanup_tmp()
        self.root.destroy()

    def approve_current(self):
        if self.idx >= len(self.svgs): return
        path = self.svgs[self.idx]["path"]
        modified_text = self.svgs[self.idx]["modified_text"]
        if not self.dry_run:
            try:
                if self.make_backup:
                    backup_path = path + ".bak"
                    if not os.path.exists(backup_path):
                        shutil.copy2(path, backup_path)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(modified_text)
                self.status_label.config(text=f"Сохранено: {path}")
            except Exception as e:
                messagebox.showerror("Ошибка записи", f"Не удалось сохранить изменения:\n{path}\n\n{e}")
                return
        self.idx += 1
        self.load_current()

    def skip_current(self):
        if self.idx >= len(self.svgs): return
        path = self.svgs[self.idx]["path"]
        self.status_label.config(text=f"Пропущено (без изменений): {path}")
        self.idx += 1
        self.load_current()

    def load_current(self):
        if self.idx >= len(self.svgs):
            self.path_label.config(text="Готово! Просмотрены все файлы.")
            self.old_canvas.config(image="", text="")
            self.new_canvas.config(image="", text="")
            self.approve_btn.config(state="disabled")
            self.skip_btn.config(state="disabled")
            return

        item = self.svgs[self.idx]
        path = item["path"]
        original_text = item["original_text"]
        modified_text = item["modified_text"]

        self.path_label.config(text=f"[{self.idx+1}/{len(self.svgs)}] {path}")

        self.current_old_png = os.path.join(self.tmpdir, f"old_{self.idx}.png")
        self.current_new_png = os.path.join(self.tmpdir, f"new_{self.idx}.png")

        rendered_old = try_render_svg_to_png(original_text.encode("utf-8"), self.current_old_png)
        rendered_new = try_render_svg_to_png(modified_text.encode("utf-8"), self.current_new_png)

        if rendered_old and os.path.exists(self.current_old_png):
            self.tk_old_img = tk.PhotoImage(file=self.current_old_png)
            self.old_canvas.config(image=self.tk_old_img, text="")
        else:
            self.tk_old_img = None
            self.old_canvas.config(image="", text="(Не удалось отрендерить оригинал)")

        if rendered_new and os.path.exists(self.current_new_png):
            self.tk_new_img = tk.PhotoImage(file=self.current_new_png)
            self.new_canvas.config(image=self.tk_new_img, text="")
        else:
            self.tk_new_img = None
            self.new_canvas.config(image="", text="(Не удалось отрендерить модифицированную версию)")

        if not rendered_old and not rendered_new:
            self.status_label.config(text="Предупреждение: предпросмотр не удался. Можно всё равно утвердить или пропустить.")
        else:
            self.status_label.config(text="")

def build_patterns(from_colors: list[str]) -> list[re.Pattern]:
    patterns = []
    for c in from_colors:
        c = c.strip()
        if not c.startswith("#") or len(c) != 7:
            print(f"[WARN] Пропущен некорректный цвет '{c}'. Ожидается формат #RRGGBB.", file=sys.stderr)
            continue
        # точное совпадение #RRGGBB, регистр игнорируется, словоразделитель после (чтобы не задеть суффиксы)
        pat = re.compile(re.escape(c) + r"\b", flags=re.IGNORECASE)
        patterns.append(pat)
    return patterns


def apply_replacements(text: str, patterns: list[re.Pattern], to_color: str) -> str:
    for pat in patterns:
        text = pat.sub(to_color, text)
    return text


def build_review_list(root_dir: str, from_colors: list[str], to_color: str) -> list[dict]:
    patterns = build_patterns(from_colors)
    if not patterns:
        return []

    svg_paths = find_svg_files(root_dir)
    review_list = []
    for p in svg_paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(p, "r", encoding="latin-1") as f:
                    content = f.read()
            except Exception:
                print(f"[WARN] Не удалось прочитать файл (кодировка?): {p}", file=sys.stderr)
                continue
        except Exception as e:
            print(f"[WARN] Ошибка чтения {p}: {e}", file=sys.stderr)
            continue

        modified = apply_replacements(content, patterns, to_color)
        if modified != content:
            review_list.append({"path": p, "original_text": content, "modified_text": modified})

    return review_list


def main():
    parser = argparse.ArgumentParser(
        description="Интерактивная замена цвета(ов) в SVG с предпросмотром и подтверждением."
    )
    parser.add_argument("--root", default=".", help="Корневая директория проекта (по умолчанию текущая).")
    parser.add_argument("--from", dest="from_colors", action="append",
                        help="Исходный цвет #RRGGBB для замены. Можно указать несколько флагов --from.")
    parser.add_argument("--to", dest="to_color", default="#e20074",
                        help="Цвет-замена #RRGGBB (по умолчанию #e20074).")
    parser.add_argument("--no-backup", action="store_true", help="Не создавать .bak перед перезаписью.")
    parser.add_argument("--dry-run", action="store_true", help="Режим просмотра без записи изменений.")
    args = parser.parse_args()

    root_dir = os.path.abspath(args.root)

    # Значения по умолчанию для обратной совместимости (если --from не указан)
    from_colors = args.from_colors if args.from_colors else ["#305680"]
    to_color = args.to_color

    # Валидация целевого цвета
    if not (to_color.startswith("#") and len(to_color) == 7):
        print("Ошибка: --to должен быть в формате #RRGGBB", file=sys.stderr)
        sys.exit(2)

    try:
        review_list = build_review_list(root_dir, from_colors, to_color)
    except Exception:
        traceback.print_exc()
        sys.exit(1)

    if not review_list:
        print("Файлы с указанными цветами не найдены. Нечего изменять.")
        return

    root = tk.Tk()
    App(root, review_list, make_backup=(not args.no_backup), dry_run=args.dry_run)
    root.mainloop()


if __name__ == "__main__":
    main()
