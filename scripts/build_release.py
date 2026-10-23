#!/usr/bin/env python3
"""Build allowlisted release ZIPs / 按公开文件白名单制作发布包."""

import argparse
import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "CodexPet_BlackMyth_Wukong-v1.0.0"
TOP_FILES = (
    ".gitignore", "README.md", "NOTICE.md", "INSTALL_PROMPT.md",
    "RELEASE_NOTES.md", "requirements-dev.txt",
)
FOLDERS = {
    "pet": {".json", ".webp"},
    "previews": {".gif"},
    "docs": {".md", ".png"},
    "scripts": {".py"},
    "qa": {".md", ".json"},
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def publication_files():
    files = [ROOT / name for name in TOP_FILES]
    for folder, extensions in FOLDERS.items():
        parent = ROOT / folder
        if parent.is_symlink() or not parent.is_dir():
            raise ValueError("Unsafe/missing directory / 目录异常: " + folder)
        files.extend(path for path in parent.iterdir() if path.suffix in extensions)
    files = sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())
    for path in files:
        if path.is_symlink() or not path.is_file():
            raise ValueError("Unsafe/missing file / 文件异常: " + str(path))
    return files


def make_zip(path, entries):
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source, name in entries:
            # Fixed timestamps and permissions / 固定时间戳与文件权限。
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, "ZIP integrity failed / ZIP 校验失败"
        assert len(archive.namelist()) == len(entries)
        for source, name in entries:
            assert archive.read(name) == source.read_bytes(), name


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh-checksums", action="store_true", help="更新源文件校验清单 / Refresh source checksums")
    args = parser.parse_args()
    files = publication_files()
    manifest = "".join(digest(path) + "  " + path.relative_to(ROOT).as_posix() + "\n" for path in files)
    checksum_file = ROOT / "checksums.sha256"
    if args.refresh_checksums:
        checksum_file.write_text(manifest, encoding="utf-8")
    if checksum_file.is_symlink() or checksum_file.read_text(encoding="utf-8") != manifest:
        raise ValueError("Source checksum manifest differs / 源文件校验清单不同")
    files.append(checksum_file)
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    full_zip = output / (NAME + ".zip")
    pet_zip = output / "black-myth-destined-one-v2.zip"
    make_zip(full_zip, [(path, NAME + "/" + path.relative_to(ROOT).as_posix()) for path in files])
    make_zip(pet_zip, [(ROOT / "pet" / name, name) for name in ("pet.json", "spritesheet.webp")])
    lines = "".join(digest(path) + "  " + path.name + "\n" for path in (full_zip, pet_zip))
    (output / "SHA256SUMS.txt").write_text(lines, encoding="utf-8")
    print(lines, end="")
    print("Verified ZIPs / 已校验发布包: " + str(len(files)) + " public files / 个公开文件")


if __name__ == "__main__":
    main()
