#!/usr/bin/env python3
"""Exercise the installer in a temporary folder / 在临时目录验证安装脚本."""

from pathlib import Path
import subprocess
import sys
import tempfile

from install import PET_ID, ROOT, digest


def invoke(pets, *arguments):
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/install.py"), "--pets-dir", str(pets), *arguments],
        check=True, capture_output=True, text=True,
    )
    return completed.stdout


def main():
    with tempfile.TemporaryDirectory(prefix="destined-one-install-test-") as folder:
        pets = Path(folder) / "pets"
        settings = Path(folder) / "config.toml"
        settings.write_text('selected_pet = "another-pet"\n', encoding="utf-8")
        invoke(pets, "--dry-run")
        assert not pets.exists(), "Dry run changed the filesystem"
        invoke(pets)
        destination = pets / PET_ID
        for filename in ("pet.json", "spritesheet.webp"):
            assert digest(destination / filename) == digest(ROOT / "pet" / filename)
        result = invoke(pets)
        assert "Already installed" in result
        backup_root = Path(folder) / "pet-backups" / PET_ID
        assert not backup_root.exists()
        old = b'{"id":"black-myth-destined-one","old_version":true}\n'
        (destination / "pet.json").write_bytes(old)
        invoke(pets, "--dry-run")
        assert (destination / "pet.json").read_bytes() == old
        assert not backup_root.exists()
        invoke(pets)
        backups = list(backup_root.iterdir())
        assert len(backups) == 1
        assert (backups[0] / "pet.json").read_bytes() == old
        assert digest(backups[0] / "spritesheet.webp") == digest(ROOT / "pet/spritesheet.webp")
        assert digest(destination / "pet.json") == digest(ROOT / "pet/pet.json")
        unrelated = pets / "another-pet"
        unrelated.mkdir()
        marker = unrelated / "keep.txt"
        marker.write_text("keep", encoding="utf-8")
        invoke(pets)
        assert marker.read_text(encoding="utf-8") == "keep"
        assert settings.read_text(encoding="utf-8") == 'selected_pet = "another-pet"\n'
        assert sorted(path.name for path in pets.iterdir()) == ["another-pet", PET_ID]
        damaged = destination / "spritesheet.webp"
        damaged.unlink()
        damaged.mkdir()
        refused = subprocess.run(
            [sys.executable, str(ROOT / "scripts/install.py"), "--pets-dir", str(pets)],
            capture_output=True, text=True,
        )
        assert refused.returncode != 0
        damaged.rmdir()
        if sys.platform != "win32":
            external = Path(folder) / "external.webp"
            external.write_bytes(b"must remain unchanged")
            damaged.symlink_to(external)
            refused = subprocess.run(
                [sys.executable, str(ROOT / "scripts/install.py"), "--pets-dir", str(pets)],
                capture_output=True, text=True,
            )
            assert refused.returncode != 0
            assert external.read_bytes() == b"must remain unchanged"
            linked_pets = Path(folder) / "linked-pets"
            linked_pets.mkdir()
            (linked_pets / PET_ID).symlink_to(Path(folder) / "unrelated-folder", target_is_directory=True)
            refused = subprocess.run(
                [sys.executable, str(ROOT / "scripts/install.py"), "--pets-dir", str(linked_pets)],
                capture_output=True, text=True,
            )
            assert refused.returncode != 0
            assert not (Path(folder) / "unrelated-folder").exists()
    print("PASS: dry run, install, idempotence, backup outside catalog, unrelated pets/settings preserved, unsafe target refusal")
    print("通过：预览、安装、重复安装、目录外备份、其他宠物与设置保留及异常目标拒绝")
    print("Symlink refusal tested on non-Windows hosts / 非 Windows 系统额外验证符号链接拒绝")


if __name__ == "__main__":
    main()
