# 资料与设计边界 / Sources and interpretation

## 外观 / Appearance

- [PlayStation 官方游戏页面 / Official PlayStation game page](https://www.playstation.com/en-us/games/black-myth-wukong/)：制作阶段的官方宣传形象参考，包括猿猴脸、束发、黑金甲胄与暗红布料。 / Production reference for the monkey face, swept-up fur, black-and-gold armor and burgundy cloth.
- [游戏科学官网 / Game Science](https://gamesci.cn/wukong/)：角色所属游戏的官方页面。 / Official site for the character's game.

采用半写实 3D 微缩表现，面向小尺寸桌宠简化纹饰。完整身体、姿势与循环均为视觉再演绎，不声称与游戏原始模型或动画逐帧一致。 / A semi-realistic 3D miniature with detail simplified for a small desktop sprite. Full-body poses and loops are visual reinterpretations, not frame-exact copies of the game's models or animations.

## 动作 / Motion

制作阶段使用 [BWIKI 招式说明 / Moves](https://wiki.biligame.com/wukong/%E6%8B%9B%E5%BC%8F) 与 [重棍说明 / Heavy attacks](https://wiki.biligame.com/wukong/%E6%8B%9B%E5%BC%8F/%E9%87%8D%E6%A3%8D) 辅助理解棍花、劈、立、戳的概念。这些是非官方社区资料，并不代表游戏科学为本项目背书。 / Community BWIKI references informed staff-flower, smash, pillar and thrust concepts during production. These are unofficial sources, not a Game Science endorsement.

工作状态以原地棍花表现；需要介入时采用立棍招手；完成检视用短程戳棍与收势；腾跃、行走和低头恢复均重新组织成短循环。实际状态触发由应用负责。 / Working uses a stationary staff drill, needs-input uses a pillar-inspired perch and beckon, and review uses a compact thrust and inspection. Leaping, gait and bow-recovery motions were adapted into short loops. The app controls when states play.

## 制作与发布 / Production and publication

原始素材于 2026-10-14 使用内置 imagegen 与当时的 hatch-pet v2 工作流完成。 [原始生成提示词 / Original prompts](GENERATION_PROMPTS.md) 保留工具使用的英文原文，开头有双语说明；其中制作阶段的相对路径不代表这些中间文件都随包发布。 / Artwork was completed on 2026-10-14 using built-in imagegen and the then-current hatch-pet v2 workflow. [Generation prompts](GENERATION_PROMPTS.md) preserve the original English tool inputs with a bilingual introduction. Production-relative paths do not imply that every intermediate input is included.

本次发布不改动角色素材。公开内容排除官方参考原图、本机内部诊断、私人绝对路径、凭据与临时制作文件。 / Publication does not change the character assets. Official reference-image downloads, internal local diagnostics, private absolute paths, credentials and temporary production files are excluded.

安装列表刷新、`/pet` 显示及减少动态效果说明依据 [OpenAI 官方 Pets 文档](https://learn.chatgpt.com/docs/pets)，发布时于 2026-10-23 查阅。该文档与本项目的本地 v2 图集校验是不同证据。 / Picker refresh, `/pet` and reduced-motion guidance follow the [official OpenAI Pets documentation](https://learn.chatgpt.com/docs/pets), consulted for publication on 2026-10-23. Product documentation and local v2 atlas validation are distinct evidence.
