#!/usr/bin/env python3
import os
import re
import argparse

# Ищем "IoT" + пробелы + "Hub" + пробелы + "CE" как отдельные слова (без учета регистра)
PATTERN = re.compile(r"\bIoT\s+Hub\s+CE\b", re.IGNORECASE)
REPLACEMENT = "IoT Hub"

DEFAULT_EXTS = (
    ".md", ".markdown", ".html", ".htm",
    ".yml", ".yaml", ".json",
    ".js", ".ts", ".tsx", ".jsx",
    ".css", ".scss", ".txt",
    ".py", ".xml", ".liquid"
)

DEFAULT_EXCLUDE_DIRS = {".git", ".hg", ".svn", "node_modules", "dist", "build", ".idea", ".vscode"}

def process_file(path: str, dry_run: bool, create_backup: bool) -> int:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"[SKIPPED] {path} ({e})")
        return 0

    matches = list(PATTERN.finditer(content))
    if not matches:
        return 0

    if dry_run:
        for m in matches:
            line_no = content.count("\n", 0, m.start()) + 1
            left  = content[max(0, m.start()-40):m.start()]
            mid   = content[m.start():m.end()]
            right = content[m.end():m.end()+40]
            print(f"{path}:{line_no}: …{left}{mid}{right}…")
        return len(matches)

    new_content = PATTERN.sub(REPLACEMENT, content)

    if create_backup:
        try:
            os.replace(path, path + ".bak")  # быстрый бэкап
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
        except Exception as e:
            print(f"[ERROR] Backup/write failed for {path}: {e}")
            if os.path.exists(path + ".bak"):
                os.replace(path + ".bak", path)  # откат
            return 0
    else:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
        except Exception as e:
            print(f"[ERROR] Write failed for {path}: {e}")
            return 0

    print(f"[UPDATED] {path} ({len(matches)} replacement(s))")
    return len(matches)

def main():
    ap = argparse.ArgumentParser(
        description="Replace 'IoT Hub' (case-insensitive, whole words) with 'IoT Hub' across a project."
    )
    ap.add_argument("--root", default=".", help="Корневая директория (по умолчанию текущая).")
    ap.add_argument("--exts", nargs="*", default=list(DEFAULT_EXTS), help="Список расширений для обработки.")
    ap.add_argument("--dry-run", action="store_true", help="Показать совпадения без записи изменений.")
    ap.add_argument("--backup", action="store_true", help="Создавать .bak рядом с изменёнными файлами.")
    ap.add_argument("--exclude-dirs", nargs="*", default=list(DEFAULT_EXCLUDE_DIRS),
                    help="Каталоги, которые нужно пропустить.")
    args = ap.parse_args()

    total_files = 0
    total_replacements = 0

    ex_dirs = set(args.exclude_dirs)
    exts = tuple(args.exts)

    for subdir, dirnames, files in os.walk(args.root):
        dirnames[:] = [d for d in dirnames if d not in ex_dirs]
        for name in files:
            if not name.endswith(exts):
                continue
            path = os.path.join(subdir, name)
            reps = process_file(path, args.dry_run, args.backup)
            if reps > 0:
                total_files += 1
                total_replacements += reps

    mode = "DRY-RUN" if args.dry_run else "APPLY"
    print(f"\n✅ Done [{mode}]. Files changed: {total_files}, replacements: {total_replacements}")

if __name__ == "__main__":
    main()
