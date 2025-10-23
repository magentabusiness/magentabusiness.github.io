#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import sys

URL_HOSTS = ("YOUR_HOST", "THINGSBOARD_HOST")
TARGET_HOST = "iothub.magenta.at"

# Подходит под http/https/ws/wss/mqtt и прочие схемы с // ; сохраняем схему/порт/путь
URL_PATTERN = re.compile(
    r'(?P<scheme>[A-Za-z][A-Za-z0-9+\-.]*:)?//'
    r'(?P<host>YOUR_HOST|THINGSBOARD_HOST)'
    r'(?P<port>:\d+)?'
    r'(?P<path>[^\s"\'\)\],<>\u00A0]*)'  # до пробела/закрывающих скобок/кавычек/знаков пункт.
)

# Для подсветки/поиска «голых» вхождений вне URL (предупреждение)
BARE_TOKEN_PATTERN = re.compile(r'\b(?:YOUR_HOST|THINGSBOARD_HOST)\b')

DEFAULT_EXCLUDE_DIRS = {
    ".git", ".hg", ".svn", ".idea", ".vscode", "node_modules", "dist", "build", "_site", ".venv", "venv", ".mypy_cache"
}

# Файлы, которые заведомо бинарные — пропускаем
BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svgz",
    ".webp", ".ico",
    ".pdf", ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar",
    ".woff", ".woff2", ".ttf", ".otf",
    ".mp3", ".mp4", ".mov", ".avi", ".mkv",
}

# Текстовые расширения, если хотите ужесточить охват
TEXT_EXTS = {
    ".md", ".markdown", ".html", ".htm", ".liquid",
    ".yml", ".yaml", ".json", ".csv", ".xml",
    ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx",
    ".css", ".scss", ".sass", ".less",
    ".py", ".rb", ".php", ".java", ".kt", ".go", ".rs", ".c", ".h", ".cpp", ".hpp",
    ".sh", ".bash", ".zsh", ".ps1",
    ".conf", ".ini", ".env", ".txt", ".rst",
}

def is_binary_path(path: str) -> bool:
    _, ext = os.path.splitext(path)
    if ext.lower() in BINARY_EXTS:
        return True
    # Простая эвристика: если нет расширения, считаем текстовым
    return False

def should_scan_file(path: str, strict_text_only: bool) -> bool:
    if is_binary_path(path):
        return False
    if strict_text_only:
        _, ext = os.path.splitext(path)
        return ext.lower() in TEXT_EXTS or ext == ""
    return True

def replace_urls(content: str):
    """Возвращает (new_content, replacements, url_hits, bare_hits)"""
    replacements = []

    def _sub(match: re.Match):
        scheme = match.group("scheme") or ""
        port = match.group("port") or ""
        path = match.group("path") or ""
        old_full = match.group(0)
        new_full = f"{scheme}//{TARGET_HOST}{port}{path}"
        if old_full != new_full:
            # Сохраним небольшой контекст для лога
            start = max(match.start() - 60, 0)
            end = min(match.end() + 60, len(content))
            context_before = content[start:match.start()]
            context_after = content[match.end():end]
            replacements.append({
                "old": old_full,
                "new": new_full,
                "context": f"...{context_before}>>>{old_full}<<<{context_after}..."
            })
        return new_full

    new_content, url_hits = URL_PATTERN.subn(_sub, content)

    # «Голые» вхождения — предупредим, но не меняем, чтобы не ломать переменные/текст
    bare_hits = len(BARE_TOKEN_PATTERN.findall(new_content))

    return new_content, replacements, url_hits, bare_hits

def process_file(path: str, apply: bool, encoding="utf-8"):
    try:
        with open(path, "r", encoding=encoding, errors="strict") as f:
            original = f.read()
    except UnicodeDecodeError:
        # Попробуем как latin-1, чтобы хотя бы просканировать
        try:
            with open(path, "r", encoding="latin-1") as f:
                original = f.read()
        except Exception:
            return None

    new_content, replacements, url_hits, bare_hits = replace_urls(original)

    wrote = False
    if apply and url_hits > 0 and new_content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        wrote = True

    return {
        "path": path,
        "url_hits": url_hits,
        "bare_hits": bare_hits,
        "wrote": wrote,
        "replacements": replacements
    }

def main():
    parser = argparse.ArgumentParser(
        description="Заменяет в URL хосты YOUR_HOST/THINGSBOARD_HOST на iothub.magenta.at (с сохранением схемы/порта/пути). По умолчанию — dry-run."
    )
    parser.add_argument("root", nargs="?", default=".", help="Корень проекта (по умолчанию текущая директория)")
    parser.add_argument("--apply", action="store_true", help="Применить изменения (по умолчанию только отчёт)")
    parser.add_argument("--strict-text", action="store_true",
                        help="Сканировать только текстовые файлы по списку расширений")
    parser.add_argument("--exclude-dir", action="append", default=[],
                        help="Доп. каталоги для исключения (можно указывать несколько)")
    parser.add_argument("--print-context", action="store_true",
                        help="Печатать контекст для каждого найденного URL")
    args = parser.parse_args()

    exclude_dirs = set(DEFAULT_EXCLUDE_DIRS) | set(args.exclude_dir)

    total_files = 0
    total_url_hits = 0
    total_bare_hits = 0
    total_written = 0
    any_changes = False

    for dirpath, dirnames, filenames in os.walk(args.root):
        # Фильтруем каталоги
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs and not d.startswith(".git")]
        for fname in filenames:
            path = os.path.join(dirpath, fname)
            if not should_scan_file(path, args.strict_text):
                continue
            total_files += 1
            result = process_file(path, apply=args.apply)
            if not result:
                continue

            if result["url_hits"] or result["bare_hits"]:
                any_changes = True
                total_url_hits += result["url_hits"]
                total_bare_hits += result["bare_hits"]
                if result["wrote"]:
                    total_written += 1

                print("─" * 80)
                print(f"Файл: {result['path']}")
                if result["url_hits"]:
                    print(f"  URL-совпадений: {result['url_hits']}"
                          f"{'  (записано)' if result['wrote'] else '  (dry-run)'}")
                    if args.print_context:
                        for rep in result["replacements"]:
                            print("  - OLD:", rep["old"])
                            print("    NEW:", rep["new"])
                            print("    CTX:", rep["context"])
                if result["bare_hits"]:
                    print(f"  Предупреждение: найдено {result['bare_hits']} «голых» упоминаний "
                          f"{URL_HOSTS} вне URL. Они не изменялись.")

    print("\nИТОГО")
    print("─" * 80)
    print(f"Просканировано файлов: {total_files}")
    print(f"Найдено URL-совпадений: {total_url_hits}")
    print(f"Найдено «голых» упоминаний вне URL: {total_bare_hits}")
    if args.apply:
        print(f"Файлов изменено: {total_written}")
    else:
        print("Режим: dry-run (изменения не записывались). Добавьте --apply для записи.")

    if not any_changes:
        print("Совпадений не найдено.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
