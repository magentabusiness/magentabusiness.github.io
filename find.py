#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import sys
from typing import Iterable

INSTALL_RE_DEFAULT = re.compile(r'/install/')
LINK_GUESS_RE = re.compile(
    r'''(?ix)
    (                              # любое из:
       href\s*=\s*["'][^"']*["']   #   HTML: href="..."`
     | \[[^\]]*\]\([^)]+\)         #   Markdown: [text](url)
     | https?://\S+                #   Явный URL http/https
     | \b(?:mailto|ftp|ws|wss|mqtt)://\S+  # другие схемы
    )
    '''
)

DEFAULT_EXCLUDE_DIRS = {
    ".git", ".hg", ".svn", ".idea", ".vscode",
    "node_modules", "dist", "build", "_site",
    ".venv", "venv", ".mypy_cache", ".cache"
}

BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svgz", ".webp", ".ico",
    ".pdf", ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar",
    ".woff", ".woff2", ".ttf", ".otf",
    ".mp3", ".mp4", ".mov", ".avi", ".mkv",
}

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
    return ext.lower() in BINARY_EXTS

def should_scan_file(path: str, strict_text_only: bool) -> bool:
    if is_binary_path(path):
        return False
    if strict_text_only:
        _, ext = os.path.splitext(path)
        return (ext.lower() in TEXT_EXTS) or (ext == "")
    return True

def read_lines(path: str) -> Iterable[str]:
    # Сначала пробуем UTF-8, затем latin-1 (чтобы не падать на экзотике)
    try:
        with open(path, "r", encoding="utf-8", errors="strict") as f:
            for line in f:
                yield line.rstrip("\n")
        return
    except UnicodeDecodeError:
        pass
    try:
        with open(path, "r", encoding="latin-1") as f:
            for line in f:
                yield line.rstrip("\n")
    except Exception:
        return

def clip(s: str, start: int, end: int, margin: int = 80) -> str:
    """Обрезает строку вокруг [start:end] с небольшими полями, чтобы вывод был читабельным."""
    left = max(0, start - margin)
    right = min(len(s), end + margin)
    prefix = "…" if left > 0 else ""
    suffix = "…" if right < len(s) else ""
    return prefix + s[left:right] + suffix

def scan_file(path: str, rx: re.Pattern, only_links: bool, print_pointer: bool):
    results = []
    for lineno, line in enumerate(read_lines(path), start=1):
        for m in rx.finditer(line):
            if only_links and not LINK_GUESS_RE.search(line):
                continue
            span = m.span()
            snippet = clip(line, span[0], span[1])
            pointer = ""
            if print_pointer:
                # Стрелочка под совпадением (с учётом обрезки)
                left = max(0, span[0] - max(0, span[0] - max(0, span[0] - 80)))
                caret_pos = span[0] - (span[0] - min(span[0], max(0, span[0] - 80)))
                pointer = " " * caret_pos + "^" * max(1, span[1] - span[0])
            results.append((lineno, span[0] + 1, snippet, pointer))
    return results

def main():
    p = argparse.ArgumentParser(
        description="Ищет ВСЕ упоминания '/install/' в проекте (в любом контексте)."
    )
    p.add_argument("root", nargs="?", default=".", help="Корень проекта (по умолчанию текущая директория)")
    p.add_argument("--ignore-case", action="store_true", help="Нечувствительный к регистру поиск")
    p.add_argument("--strict-text", action="store_true", help="Сканировать только текстовые файлы по списку расширений")
    p.add_argument("--exclude-dir", action="append", default=[], help="Доп. каталоги для исключения (можно несколько)")
    p.add_argument("--only-links", action="store_true", help="Показывать только строки, где '/install/' внутри ссылок (HTML/Markdown/URL)")
    p.add_argument("--print-pointer", action="store_true", help="Печатать указатель под совпадением (^)")
    args = p.parse_args()

    rx = INSTALL_RE_DEFAULT if not args.ignore_case else re.compile(r'/install/', re.IGNORECASE)

    exclude_dirs = set(DEFAULT_EXCLUDE_DIRS) | set(args.exclude_dir)

    total_hits = 0
    total_files = 0

    for dirpath, dirnames, filenames in os.walk(args.root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs and not d.startswith(".git")]
        for fname in filenames:
            path = os.path.join(dirpath, fname)
            if not should_scan_file(path, args.strict_text):
                continue

            matches = scan_file(path, rx, only_links=args.only_links, print_pointer=args.print_pointer)
            if not matches:
                continue

            total_files += 1
            print("—" * 90)
            print(f"Файл: {path}")
            for lineno, col, snippet, pointer in matches:
                total_hits += 1
                print(f"  [{lineno}:{col}] {snippet}")
                if args.print_pointer and pointer:
                    print(f"            {pointer}")

    print("\nИТОГО")
    print("—" * 90)
    print(f"Файлов с совпадениями: {total_files}")
    print(f"Всего совпадений: {total_hits}")

    # Если нужно, чтобы CI валился при найденных совпадениях, раскомментируй:
    # if total_hits > 0:
    #     sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
