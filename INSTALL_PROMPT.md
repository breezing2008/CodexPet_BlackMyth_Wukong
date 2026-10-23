# 安装提示词 / Installation prompt

将下面任一段发给自己电脑上可以访问本地文件的 Codex。它安装已有成品，不会重新生成形象。 / Send either prompt to a local Codex session with filesystem access. It installs the existing artwork without regenerating it.

## 中文

```text
请从 https://github.com/breezing2008/CodexPet_BlackMyth_Wukong 下载 v1.0.0 发布包，阅读 README.md、NOTICE.md 和 scripts/install.py，并将已有的“天命人 · 黑神话悟空”宠物安装到我这台电脑的 Codex 自定义宠物库。只用于个人、非商业用途，不要重新生成或修改形象、动画或 pet ID。

先检查发布包校验值和 pet/ 两个文件的 SHA-256，确认 spriteVersionNumber=2。使用受支持的本地 Python 运行 scripts/install.py --dry-run，确认目标目录后再正常安装；根据 CODEX_HOME 或 --pets-dir 选择正确目录。不要删除、覆盖其他宠物，不要修改当前选中项、全局配置或应用程序；如已有同名不同版本，先备份。如果需要写入权限，请按系统审批流程操作。

完成后校验安装文件与发布包一致，告诉我打开设置 → Pets → Refresh（刷新）并选择“天命人 · 黑神话悟空”。把文件安装成功、设置列表可见和实际动画播放分开报告；没有界面或用户确认时不要声称已显示。若版本不支持该 v2 格式，保留原文件并报告，不要擅自改成其他宠物。
```

## English

```text
Download the v1.0.0 release from https://github.com/breezing2008/CodexPet_BlackMyth_Wukong, read README.md, NOTICE.md and scripts/install.py, and install the existing “天命人 · 黑神话悟空” pet into the Codex custom-pet library on this computer for personal, non-commercial use. Do not regenerate or change its artwork, animations or pet ID.

Verify the release checksum and SHA-256 digests of both pet/ files, and confirm spriteVersionNumber=2. Use a supported local Python to run scripts/install.py --dry-run, confirm the destination, then install. Respect CODEX_HOME or --pets-dir. Do not delete or overwrite other pets, change my current selection or global settings, or modify the application. Back up an existing differing version. Follow the system approval flow for any required write permission.

Verify installed files match the release, then tell me to open Settings → Pets → Refresh and select “天命人 · 黑神话悟空”. Report file installation, picker visibility and actual animation playback separately; do not claim UI success without UI or user confirmation. If this build cannot read the v2 format, preserve existing files and report that limitation instead of substituting another pet.
```
