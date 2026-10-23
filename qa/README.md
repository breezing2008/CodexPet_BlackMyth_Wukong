# 发布验收 / Release QA

## 可复查检查 / Reproducible checks

- `python3 scripts/validate.py --json-out qa/validation.json`：验证清单与 SHA-256，1536 × 2288 RGBA WebP、8 × 11 网格、192 × 208 单元格、九类有效动画与十六朝向、空白格、透明像素 RGB，以及十个循环 GIF 的尺寸/帧数/时长。 / Manifest and SHA-256; atlas format, grid, populated and blank cells, transparent-pixel RGB; all ten GIF dimensions, frame counts, timing and looping.
- `python3 scripts/test_install.py`：临时目录内检查预览不写入、安装、重复安装、旧版本备份、其他宠物和当前设置不变、异常目标/符号链接拒绝。 / Temporary-directory tests for no-write dry run, installation, idempotence, backups, preservation of other pets and settings, and refusal of unsafe targets/symlinks.
- `python3 scripts/build_release.py`：只打包列明的公开目录与文件，拒绝符号链接，验证文件清单和 ZIP 完整性，并生成 Release 校验文件。 / Packages only the listed public files/directories, rejects symlinks, checks the file manifest and ZIP integrity, and generates Release checksums.

`validation.json` 是本次发布重新运行的结构检查，不是新一轮所有平台实机测试。 / `validation.json` is a fresh structural publication check, not a new end-to-end test on all platforms.

## 原版视觉验收 / Original visual acceptance

2026-10-14 已完成动作总览、原尺寸反应动作及方向连续性检查。四个主朝向通过；部分中间角度的另一轴线索较细微，尤其 337.5° 的左向线索；受阻动作为克制的头肩下沉，不是大幅弯腰。双腿之间的透明区域为自然轮廓。以上限制随原版素材一起保留，本次不重绘。 / Original review on 2026-10-14 covered the contact sheet, native-size blocked reaction and direction continuity. The four cardinal directions passed. Some intermediate secondary-axis cues are subtle, particularly the leftward cue at 337.5°. The blocked reaction is a restrained head-and-shoulder bow, not a deep torso bend. Transparent leg gaps are natural silhouette gaps. These original limits are retained; no artwork is regenerated here.

## 应用内验收 / App acceptance

原制作机器上的文件一致性曾通过校验；2026-10-14 用户确认 Refresh 后设置列表中可见。选择和所有实际播放状态未单独确认；其他电脑需安装后自行验证。不将 GIF 演示、结构检查或文件复制当作应用内播放成功。 / File consistency was verified on the production machine, and on 2026-10-14 the user confirmed picker visibility after Refresh. Selection and all playback states were not separately confirmed; other computers need their own installation test. GIFs, structural checks and copied files are not proof of successful in-app playback.
