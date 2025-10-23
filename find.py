import os
import sys
import tkinter as tk
from tkinter import scrolledtext, font, messagebox

# --- НАСТРОЙКИ ---
OLD_STRING = "$THINGSBOARD_HOST"
NEW_STRING = "iothub.magenta.at"
PROJECT_DIR = '.'
CONTEXT_LINES = 2
EXCLUDE_DIRS = {
    '.git', '__pycache__', 'node_modules', '.venv',
    'venv', 'build', 'dist', '.idea', '.vscode'
}
# --- КОНЕЦ НАСТРОЕК ---

class RefactorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Интерактивная замена текста")
        self.root.geometry("900x600")

        # --- Инициализация логики ---
        # Сначала сканируем проект, чтобы получить список файлов с совпадениями
        self.files_with_matches = self.collect_files_with_matches()
        self.total_matched_files = len(self.files_with_matches)

        self.current_file_index = 0
        self.current_file_path = None
        self.current_lines = []
        self.current_matches = []
        self.current_match_index = -1
        self.file_was_modified = False

        # --- Настройка виджетов ---

        # 1. Фрейм для заголовка и прогресса
        header_frame = tk.Frame(root, padx=10, pady=5)
        header_frame.pack(fill="x")

        # 1.1. Индикатор прогресса (НОВЫЙ ЭЛЕМЕНТ)
        self.progress_font = font.Font(family="Helvetica", size=10, weight="bold")
        self.progress_label = tk.Label(header_frame, text="Прогресс: 0/0", anchor="w", font=self.progress_font, foreground="#008000")
        self.progress_label.pack(side="left")

        # 1.2. Заголовок (путь к файлу и статус)
        self.status_font = font.Font(family="Helvetica", size=12)
        self.status_label = tk.Label(header_frame, text="Поиск файлов...", anchor="e", font=self.status_font)
        self.status_label.pack(side="right")
        self.update_progress_label() # Изначальное обновление

        # 2. Основное текстовое поле с прокруткой
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier New", 11), relief="sunken", borderwidth=2)
        self.text_area.pack(expand=True, fill="both", padx=10, pady=5)

        # 3. Настройка стилей (тегов) для подсветки
        self.text_area.tag_configure("header", font=("Helvetica", 12, "bold"), foreground="#00008B")
        self.text_area.tag_configure("context", foreground="gray")
        self.text_area.tag_configure("before", background="#FFFACD", font=("Courier New", 11, "bold"))
        self.text_area.tag_configure("after", background="#90EE90", font=("Courier New", 11, "bold"))

        # 4. Фрейм для кнопок
        button_frame = tk.Frame(root, pady=10)
        button_frame.pack(fill="x")

        # 5. Кнопки
        self.btn_approve = tk.Button(button_frame, text="Заменить (A)", command=self.approve, width=20, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
        self.btn_approve.pack(side="left", expand=True, padx=10)

        self.btn_skip = tk.Button(button_frame, text="Пропустить (S)", command=self.skip, width=20, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
        self.btn_skip.pack(side="left", expand=True, padx=10)

        self.btn_quit = tk.Button(button_frame, text="Выход (Q)", command=self.root.quit, width=15, font=("Helvetica", 10))
        self.btn_quit.pack(side="right", expand=True, padx=10)

        # Привязка клавиш (для строчных и заглавных букв)
        self.root.bind('<a>', lambda event: self.approve())
        self.root.bind('<A>', lambda event: self.approve())

        self.root.bind('<s>', lambda event: self.skip())
        self.root.bind('<S>', lambda event: self.skip())

        self.root.bind('<q>', lambda event: self.root.quit())
        self.root.bind('<Q>', lambda event: self.root.quit())

        self.load_next_file()

    def collect_files_with_matches(self):
        """
        Предварительно сканирует проект и возвращает список путей
        к файлам, где есть совпадения. Это необходимо для точного
        индикатора прогресса.
        """
        matched_files = []
        for root, dirs, files in os.walk(PROJECT_DIR, topdown=True):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for filename in files:
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        if OLD_STRING in f.read():
                            matched_files.append(filepath)
                except Exception:
                    # Пропускаем файлы с ошибками чтения/доступа
                    continue
        return matched_files

    def update_progress_label(self):
        """Обновляет текст индикатора прогресса."""
        self.progress_label.config(text=f"Прогресс: {self.current_file_index}/{self.total_matched_files} файлов")

    def load_next_file(self):
        """
        Загружает следующий файл из предварительно собранного списка.
        """
        if self.current_file_index >= self.total_matched_files:
            self.show_done()
            return

        self.current_file_path = self.files_with_matches[self.current_file_index]
        self.current_lines = []
        self.current_matches = []
        self.current_match_index = -1
        self.file_was_modified = False

        self.current_file_index += 1
        self.update_progress_label() # Обновляем прогресс, как только берем файл в работу

        try:
            # Пытаемся прочитать файл
            with open(self.current_file_path, 'r', encoding='utf-8') as f:
                self.current_lines = f.readlines()
        except (UnicodeDecodeError, IOError, PermissionError) as e:
            # Если не смогли прочитать файл, идем дальше.
            # Это не должно случиться, т.к. файл уже был проверен в collect_files_with_matches.
            print(f"[ОШИБКА ЧТЕНИЯ] {self.current_file_path}: {e}")
            self.load_next_file()
            return

        # Ищем все совпадения (в файле они гарантированно есть)
        for i, line in enumerate(self.current_lines):
            if OLD_STRING in line:
                proposed_line = line.replace(OLD_STRING, NEW_STRING)
                self.current_matches.append((i, line, proposed_line))

        # Нашли файл с совпадениями, показываем первое
        self.current_match_index = 0
        self.display_current_match()

    def display_current_match(self):
        """Отображает текущее совпадение в текстовом поле."""
        if self.current_match_index >= len(self.current_matches):
            return

        self.text_area.config(state="normal")
        self.text_area.delete(1.0, tk.END) # Очистить окно

        # 1. Обновить статус
        match_num = self.current_match_index + 1
        total_matches = len(self.current_matches)
        status_text = f"Файл: {self.current_file_path}\n"
        self.text_area.insert(tk.END, status_text, "header")

        status_text_match = f"Совпадение {match_num} из {total_matches}\n\n"
        self.text_area.insert(tk.END, status_text_match, "header")

        # 2. Получить данные о совпадении
        line_num, old_line, new_line = self.current_matches[self.current_match_index]

        # 3. Показать контекст "ДО"
        self.text_area.insert(tk.END, "--- КОНТЕКСТ (ДО) ---\n", "context")
        start = max(0, line_num - CONTEXT_LINES)
        for i in range(start, line_num):
            self.text_area.insert(tk.END, f"{i + 1: >4}: {self.current_lines[i].rstrip()}\n", "context")

        # 4. Показать "ДО"
        self.text_area.insert(tk.END, "\n" + "-"*10 + " ДО " + "-"*10 + "\n")
        self.text_area.insert(tk.END, f"->{line_num + 1: >4}: {old_line.rstrip()}\n", "before")

        # 5. Показать "ПОСЛЕ"
        self.text_area.insert(tk.END, "\n" + "-"*10 + " ПОСЛЕ " + "-"*10 + "\n")
        self.text_area.insert(tk.END, f"->{line_num + 1: >4}: {new_line.rstrip()}\n", "after")

        # 6. Показать контекст "ПОСЛЕ"
        self.text_area.insert(tk.END, "\n--- КОНТЕКСТ (ПОСЛЕ) ---\n", "context")
        end = min(len(self.current_lines), line_num + CONTEXT_LINES + 1)
        for i in range(line_num + 1, end):
            self.text_area.insert(tk.END, f"{i + 1: >4}: {self.current_lines[i].rstrip()}\n", "context")

        # Заблокировать редактирование
        self.text_area.config(state="disabled")

        # Обновить заголовок окна
        self.status_label.config(text=f"Файл: {self.current_file_path}")

    def approve(self):
        """Применяет изменение в памяти и переходит к следующему."""
        if self.current_match_index == -1: return

        # 1. Применить изменение к списку строк в памяти
        line_num, _, new_line = self.current_matches[self.current_match_index]
        self.current_lines[line_num] = new_line
        self.file_was_modified = True

        # 2. Переключиться на следующее совпадение
        self.load_next_match()

    def skip(self):
        """Пропускает изменение и переходит к следующему."""
        if self.current_match_index == -1: return
        self.load_next_match()

    def load_next_match(self):
        """Загружает следующее совпадение в ТЕКУЩЕМ файле."""
        self.current_match_index += 1

        if self.current_match_index < len(self.current_matches):
            # В этом файле еще есть совпадения
            self.display_current_match()
        else:
            # Совпадения в этом файле закончились
            self.write_current_file_if_modified()
            self.load_next_file() # Загружаем следующий файл

    def write_current_file_if_modified(self):
        """Записывает изменения в файл, если они были."""
        if self.file_was_modified:
            try:
                # Используем временный файл для безопасной записи
                temp_filepath = self.current_file_path + '.tmp'
                with open(temp_filepath, 'w', encoding='utf-8') as f:
                    f.writelines(self.current_lines)

                # Перемещаем временный файл на место оригинала
                os.replace(temp_filepath, self.current_file_path)

                print(f"[OK] Файл '{self.current_file_path}' обновлен.")
            except Exception as e:
                # Попытка удалить временный файл в случае ошибки
                if os.path.exists(temp_filepath):
                    os.remove(temp_filepath)

                print(f"[ОШИБКА] Не удалось записать в {self.current_file_path}: {e}")
                messagebox.showerror("Ошибка записи", f"Не удалось сохранить изменения в файле:\n{self.current_file_path}\n\nОшибка: {e}")

        self.file_was_modified = False

    def show_done(self):
        """Показывает сообщение о завершении."""
        self.status_label.config(text="Готово!")
        self.text_area.config(state="normal")
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"🎉\n\nСканирование и замена завершены.\n\nОбработано {self.total_matched_files} файлов с совпадениями.", "header")
        self.text_area.config(state="disabled")

        # Отключить кнопки
        self.btn_approve.config(text="Готово", state="disabled", bg="gray")
        self.btn_skip.config(text="Готово", state="disabled", bg="gray")
        self.progress_label.config(text=f"Прогресс: {self.total_matched_files}/{self.total_matched_files} файлов")


# --- Точка входа ---
if __name__ == "__main__":
    root = tk.Tk()
    app = RefactorApp(root)
    root.mainloop()