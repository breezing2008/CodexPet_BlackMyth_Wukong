#!/usr/bin/env python3
"""Validate the Destined One publication / 校验天命人发布包."""

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image
from install import verify_source

ROOT = Path(__file__).resolve().parents[1]
STATES = [
    ("idle", 6), ("running-right", 8), ("running-left", 8),
    ("waving", 4), ("jumping", 5), ("failed", 8),
    ("waiting", 6), ("running", 6), ("review", 6),
    ("look-000-to-157.5", 8), ("look-180-to-337.5", 8),
]


def validate():
    errors = []
    try:
        verify_source()
    except (OSError, ValueError) as error:
        errors.append(str(error))
    atlas_path = ROOT / "pet/spritesheet.webp"
    cells = []
    previews = []
    with Image.open(atlas_path) as atlas:
        if atlas.format != "WEBP" or atlas.mode != "RGBA" or atlas.size != (1536, 2288):
            errors.append("Expected 1536 × 2288 RGBA WebP / 需要符合尺寸的 RGBA WebP")
        rgba = atlas.convert("RGBA")
        pixels = rgba.tobytes()
        residue = sum(
            1 for r, g, b, a in zip(pixels[0::4], pixels[1::4], pixels[2::4], pixels[3::4])
            if a == 0 and (r or g or b)
        )
        if residue:
            errors.append("Nonzero RGB in transparent pixels / 透明像素存在非零 RGB")
        for row, (state, frames) in enumerate(STATES):
            for column in range(8):
                cell = rgba.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208))
                count = sum(cell.getchannel("A").histogram()[1:])
                used = column < frames or (row == 0 and column == 6)
                if used and count < 50:
                    errors.append("Missing frame / 缺少帧: " + state + ":" + str(column))
                if not used and count:
                    errors.append("Unexpected populated cell / 空白格含有图像: " + state + ":" + str(column))
                cells.append({"state": state, "column": column, "used": used, "visible_pixels": count})
        for state, frames in STATES[:9] + [("look", 16)]:
            relative = "previews/" + state + ".gif"
            with Image.open(ROOT / relative) as gif:
                if gif.format != "GIF" or gif.n_frames != frames or gif.info.get("loop") != 0:
                    errors.append("Invalid looping GIF / GIF 循环配置不符合预期: " + relative)
                durations = []
                for index in range(gif.n_frames):
                    gif.seek(index)
                    durations.append(gif.info.get("duration", 0))
                    if gif.size != (192, 208) or gif.info.get("duration", 0) <= 0:
                        errors.append("Invalid GIF frame / GIF 帧配置不符合预期: " + relative)
                previews.append({"file": relative, "frames": gif.n_frames, "loop": 0, "duration_ms": durations})
    return {
        "ok": not errors,
        "file": "pet/spritesheet.webp",
        "format": "WEBP", "mode": "RGBA", "spriteVersionNumber": 2,
        "width": 1536, "height": 2288, "columns": 8, "rows": 11,
        "cell_width": 192, "cell_height": 208,
        "sha256": hashlib.sha256(atlas_path.read_bytes()).hexdigest(),
        "transparent_rgb_residue_pixels": residue,
        "errors": errors, "cells": cells, "previews": previews,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, help="Report output / 报告输出位置")
    args = parser.parse_args()
    result = validate()
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": result["ok"], "errors": result["errors"], "sha256": result["sha256"]}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
