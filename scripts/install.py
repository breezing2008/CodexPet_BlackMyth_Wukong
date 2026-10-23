#!/usr/bin/env python3
"""Install the Destined One; back up differing files / 安装天命人并备份旧文件."""

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile

PET_ID = "black-myth-destined-one"
ROOT = Path(__file__).resolve().parents[1]
FILES = ("pet.json", "spritesheet.webp")


def digest(file_path):
    return hashlib.sha256(file_path.read_bytes()).hexdigest()


def verify_source():
    expected = {}
    for line in (ROOT / "checksums.sha256").read_text(encoding="utf-8").splitlines():
        if line.strip():
            value, relative = line.split(maxsplit=1)
            expected[relative.lstrip("*")] = value
    for filename in FILES:
        relative = "pet/" + filename
        if expected.get(relative) != digest(ROOT / relative):
            raise ValueError("Checksum mismatch / 校验值不一致: " + relative)
    manifest = json.loads((ROOT / "pet/pet.json").read_text(encoding="utf-8"))
    if (manifest.get("id") != PET_ID or manifest.get("spriteVersionNumber") != 2
            or manifest.get("spritesheetPath") != "spritesheet.webp"):
        raise ValueError("Unexpected pet manifest / 宠物配置不符合预期")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pets-dir", type=Path, help="Pets directory / 宠物目录")
    parser.add_argument("--dry-run", action="store_true", help="Preview only / 仅预览")
    args = parser.parse_args()
    verify_source()
    codex_root = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    pets_root = (args.pets_dir or codex_root / "pets").expanduser().resolve()
    destination = pets_root / PET_ID
    print("Destination / 安装位置: " + str(destination))
    if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
        raise ValueError("Destination must be a regular directory / 安装位置必须是普通目录")
    for filename in FILES:
        target = destination / filename
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise ValueError("Unsafe existing file / 现有文件类型不符合预期: " + str(target))
    unchanged = destination.is_dir() and all(
        (destination / filename).is_file()
        and digest(destination / filename) == digest(ROOT / "pet" / filename)
        for filename in FILES
    )
    if unchanged:
        print("Already installed and verified / 已安装且校验通过")
        return
    if args.dry_run:
        print("Files verified; no changes made / 文件校验通过，未写入文件")
        return
    pets_root.mkdir(parents=True, exist_ok=True)
    backup = None
    if destination.exists() and any((destination / filename).exists() for filename in FILES):
        backup_root = pets_root.parent / "pet-backups"
        backup_pet_root = backup_root / PET_ID
        for path in (backup_root, backup_pet_root):
            if path.is_symlink() or (path.exists() and not path.is_dir()):
                raise ValueError("Unsafe backup directory / 备份目录不安全: " + str(path))
        backup_pet_root.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-")
        backup = Path(tempfile.mkdtemp(prefix=stamp, dir=backup_pet_root))
        for filename in FILES:
            existing = destination / filename
            if existing.exists():
                shutil.copy2(existing, backup / filename)
        print("Backup / 备份: " + str(backup))
    destination.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".destined-one-install-", dir=pets_root) as staging_name:
        staging = Path(staging_name)
        for filename in FILES:
            shutil.copy2(ROOT / "pet" / filename, staging / filename)
        for filename in FILES:
            os.replace(staging / filename, destination / filename)
    for filename in FILES:
        if digest(destination / filename) != digest(ROOT / "pet" / filename):
            raise ValueError("Installed checksum mismatch / 安装后校验失败: " + filename)
    print("Installed and verified / 安装并校验完成")
    print("Open Settings → Pets → Refresh, then choose 天命人 · 黑神话悟空.")
    print("打开设置 → Pets（宠物）→ Refresh（刷新），选择天命人 · 黑神话悟空。")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        raise SystemExit(str(error))
