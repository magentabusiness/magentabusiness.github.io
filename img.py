#!/usr/bin/env python3
import os
import argparse

OLD = "https://iothub.magenta.at"
NEW = "https://iothub.magenta.at"

TEXT_EXTS = (
    ".md", ".markdown", ".html", ".htm",
    ".yml", ".yaml", ".json",
    ".js", ".ts", ".tsx", ".jsx",
    ".css", ".scss", ".txt",
    ".py", ".xml", ".liquid"
)

EXCLUDE_DIRS = {".git", ".hg", ".svn", "node_modules", "dist", "build", ".idea", ".vscode"}


def process_file(path: str, dry_run: bool, create_backup: bool) -> bool:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"[SKIPPED] {path} ({e})")
        return False

    if OLD not in content:
        return False

    if dry_run:
        for i, line in enumerate(content.splitlines(), start=1):
            if OLD in line:
                print(f"{path}:{i}: {line.strip()}")
        return True

    new_content = content.replace(OLD, NEW)

    if create_backup:
        try:
            os.replace(path, path + ".bak")  # создаём резервную копию
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
        except Exception as e:
            print(f"[ERROR] Backup/write failed for {path}: {e}")
            if os.path.exists(path + ".bak"):
                os.replace(path + ".bak", path)  # откат
            return False
    else:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
        except Exception as e:
            print(f"[ERROR] Write failed for {path}: {e}")
            return False

    print(f"[UPDATED] {path}")
    return True


def main():
    ap = argparse.ArgumentParser(
        description=f"Replace '{OLD}' → '{NEW}' recursively in project files."
    )
    ap.add_argument("--root", default=".", help="Корневая директория (по умолчанию текущая).")
    ap.add_argument("--dry-run", action="store_true", help="Показать совпадения без записи.")
    ap.add_argument("--backup", action="store_true", help="Создавать .bak копии перед изменением.")
    ap.add_argument("--exts", nargs="*", default=list(TEXT_EXTS), help="Обрабатываемые расширения.")
    ap.add_argument("--exclude-dirs", nargs="*", default=list(EXCLUDE_DIRS),
                    help="Исключаемые каталоги.")
    args = ap.parse_args()

    ex_dirs = set(args.exclude_dirs)
    exts = tuple(args.exts)

    total_files = 0

    for subdir, dirnames, files in os.walk(args.root):
        dirnames[:] = [d for d in dirnames if d not in ex_dirs]
        for name in files:
            if not name.endswith(exts):
                continue
            path = os.path.join(subdir, name)
            if process_file(path, args.dry_run, args.backup):
                total_files += 1

    mode = "DRY-RUN" if args.dry_run else "APPLY"
    print(f"\n✅ Done [{mode}]. Files affected: {total_files}")


if __name__ == "__main__":
    main()
