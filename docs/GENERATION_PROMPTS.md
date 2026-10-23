# 天命人宠物生成提示词 / Generation prompt set

本项目使用 Codex 内置 imagegen 生成角色和每行动作，之后通过 hatch-pet 的确定性抽帧、注册、透明边缘清理与验证脚本合成。以下保留最终采用的主提示词；附图由官方宣传参考、规范布局图、已批准主形象与已完成动画依赖组成。提示词中的 run 相对路径是制作阶段依赖，临时图像在成功安装后清理。

Generated using built-in imagegen, with deterministic hatch-pet extraction, registration, transparency cleanup and validation. These are the final primary prompts, grounded in the official reference and approved visual dependencies. Run-relative paths describe production inputs; temporary files are cleaned after successful installation. No game models or animations were extracted.

Row 10 uses five files for the six original reference roles because of the generator input limit: official artwork and canonical identity are preserved without pixel alteration in one reference board; layout, standard contact sheet, approved cardinals and row 9 are attached separately.

The final row-10 repair board also includes the prior coherent candidate at the top. The generator resynthesized the whole family with a uniform size reduction and corrected up-left head yaw; no final direction cells were pasted or procedurally redrawn.

## 朝向机制 / Look mechanics

# 天命人指针朝向机制

The Destined One is an anatomical humanoid monkey, not a rigid rotating object. Keep boots, pelvis, lower armor and waist gourd anchored to the neutral stance. Attention leads through the existing realistic eyes and eyelids, then head/neck yaw and pitch; shoulders follow only slightly. Keep the facial skull, muzzle, brow spacing and swept-up fur identity fixed. Never invent large eye whites or googly eyes, warp the skull, or rotate the entire sprite.

The canonical base locks character appearance, not its three-quarter resting face angle. All directions are SCREEN / VIEWER coordinates. The one staff stays gripped by its original anatomical hand close beside the body; maintain continuous physical hand contact, stable lower end and original design. It may be modestly occluded by the turning shoulder/head, never jumps across the body or detaches. Armor/gourd/feet do not mirror or spin.

## Cardinal pose families

- 000 UP: head clearly pitches back; chin and underside of muzzle rise, existing eyes/pupils look above the brow line, neck slightly lengthens. Face aims at the top edge, not neutral/front.
- 090 SCREEN RIGHT: head/neck yaw about 55–65 degrees to screen right; muzzle/nose tip protrudes toward the right edge, rightward pupils move with physical eyeballs/eyelids, far eye is partially occluded, opposite cheek becomes visible. Shoulders follow a few degrees, pelvis and boots remain fixed.
- 180 DOWN: head pitches down and chin tucks toward upper chest; muzzle/nose points below head center, eyelids/brow and pupils look down, crown/fur top becomes more visible. Not a neutral front stare.
- 270 SCREEN LEFT: true opposite of 090; head/neck yaw about 55–65 degrees left, nose/muzzle clearly protrude toward the left edge and pupils/eyelids aim left; far eye is partly hidden and opposite cheek becomes visible. Do not mirror the whole character or leave this front/right-facing.

## Continuous family and motion budget

Keep the same lower-body anchor, body size and baseline. Each 22.5-degree step changes the same eyes/head/neck by an even small amount, with restrained shoulder follow-through. Do not use full-cell rotation, raster warping, independently repositioned faces, fixed irises with detached pupil overlays, or prop teleportation.

Row 9 is one coherent 8-pose clockwise family: up; up-right near up; up-right diagonal; up-right near right; right; down-right near right; down-right diagonal; down-right near down. Row 10 continues: down; down-left near down; down-left diagonal; down-left near left; left; up-left near left; up-left diagonal; up-left near up. The 157.5→180 and 337.5→000 boundaries must look like normal adjacent steps. Intermediates must carry BOTH axes through combined yaw/pitch/eyes, without crossing quadrants.

No new expression style, armor, staff, colors, plumes, crown, label, arrow, glow, shadow or scenery. Source poses are complete separated sprites on #FF00FF. All look cells must remain distinguishable from idle at 192×208.

## base

```text
Create one clean full-body reference sprite for Codex pet 天命人 · 黑神话悟空.

Pet identity: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible..
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..


Place a single centered pose on a perfectly flat pure user-selected #FF00FF chroma-key background. Keep the full pet visible, compact, readable at 192x208, and easy to animate. Preserve approved reference identity cues. No scenery, text, borders, checkerboard transparency, shadows, glows, detached effects, or extra props. Keep #FF00FF and close colors out of the pet, props, highlights, and effects.
```

## idle

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: REPAIR ONLY THE INERT IDLE MOTION. Six deliberately different calm vigilant poses: 0 relaxed shoulders and staff close, 1 inhale shoulders visibly lift by about 5% of body height, 2 peak breath with a small head nod and a slight lifted heel while toes stay planted, 3 shoulders settle and chin turns a few degrees with a brief eyelid blink, 4 shift weight to other boot with a tiny heel lift and soft elbow flex, 5 recover exact relaxed start. Keep pelvis/boot toes registered; body size stays constant while anatomical shoulders/elbows/knees really move. At native pet size the breathing/weight shift MUST be visible, not six copies with microscopic texture changes. Calm vigilance, no waving, walking, staff spin, jumping, work or new items. Same canonical identity, armor and staff design; equal spacing and full connected outlines.

State requirements:
- CRITICAL: idle is the low-distraction baseline state and the first frame is also used as the reduced-motion static pet.
- Use only subtle idle motion: gentle breathing, a tiny blink, a slight head or body bob, a very small material sway, or another quiet motion that fits the pet persona.
- Keep the pet essentially in the same pose, facing direction, silhouette, markings, palette, and prop state across all 6 frames.
- Idle variation must stay calm but still read as animation; do not repeat effectively identical copies across the loop.
- Do not show waving, walking, running, jumping, talking, working, reviewing, emotional reactions, large gestures, item interactions, or new props.
- Feet, base, body, or object anchor should remain planted or nearly planted.
- The first and last frames should be very close visually so the loop feels calm and does not pop.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## running-right

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `running-right`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Eight-frame staff-wielding travel cycle facing unmistakably SCREEN RIGHT: turn head and torso into right profile, alternate lead boot, passing legs, other lead boot, then recover in an even cyclic cadence. Carry the same staff diagonally close to the torso in its original handed grip, with slight armored cloth follow-through. Body travels conceptually right but stays centered in each slot. Keep the entire staff inside every slot; no rolls or detached motion effects. The base reference locks identity, not its frontal pose.

State requirements:
- Show directional drag movement to the right through body, limb, and prop movement only.
- The row must unmistakably face and travel right.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## running-left

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `running-left`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Eight-frame staff-wielding travel cycle facing unmistakably SCREEN LEFT, not a mirrored costume: turn head and torso into left profile; alternate lead boot, passing legs, other lead boot, and recover with the same timing family as running-right. Preserve the SAME anatomical staff hand, gourd side, ornate armor and lighting; the opposite side of the character becomes visible naturally. Staff remains close to body and completely inside each slot. The base reference locks identity, not its frontal pose.

State requirements:
- Show directional drag movement to the left through body, limb, and prop movement only.
- The row must unmistakably face and travel left.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## waving

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `waving`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 4 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 4 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Four-frame confident restrained greeting: original staff hand holds the same staff upright beside the body; free hand starts down, rises to shoulder/head height with an open palm, makes a small beckoning wrist gesture, and lowers to the initial stance. Use a warm knowing expression without changing the serious monkey face. No marks, circles or light effects. Base locks appearance, not exact pose.

State requirements:
- Show the greeting through paw, hand, wing, or limb pose only.
- Do not draw wave marks, motion arcs, lines, sparkles, symbols, or floating effects around the gesture.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## jumping

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `jumping`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 5 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 5 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Five-frame compact jump-smash inspired by SMASH staff stance: slight crouch and ready, rise with knees tucked and staff lifted close across upper body, airborne peak with bent limbs, descending guarded overhead smash posture, then land and return. Keep body size consistent, use actual vertical position change, and keep the whole single staff inside the slot with foreshortening. The staff remains attached to hands. No impact effect, enemy, damage, shadows, dust or trails. Base locks appearance, not exact pose.

State requirements:
- Show the jump through pose and vertical body position only: anticipation, lift, airborne peak, descent, settle.
- Do not draw ground shadows, contact shadows, drop shadows, oval shadows, landing marks, dust, smears, bounce pads, or motion marks under the pet.
- Keep the background outside the pet perfectly flat chroma key with no darker key-colored patches.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## failed

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `failed`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Eight-frame readable blocked-task reaction: slowly lean forward while resting on the held staff, lower head and shoulders, briefly close eyes, pause, then lift the head and return to composed ready stance. The waist gourd remains attached, staff stays in the same hand, and feet do not travel. No collapse, injury, tears, new effects, or extra props. Base locks appearance, not exact pose.

State requirements:
- Show failure through slumped pose, drooping ears/limbs, closed or sad eyes, and lower body position.
- Tears, small smoke puffs, or tiny stars are allowed only if attached to or overlapping the pet silhouette and kept inside the same frame slot.
- Do not draw red X marks, floating symbols, detached stars, separated smoke clouds, falling tear drops, dust, or other loose effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## waiting

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `waiting`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Six-frame conspicuous needs-user-input alert inspired by PILLAR stance: plant the same staff vertically close to the torso; crouch and rise into a compact crouching perch on its upper end, then raise and beckon with the free hand toward the viewer, lower and return. The pole and body remain one connected silhouette through hand and boot contact; use folded legs, not body shrinkage, to keep every pose inside the slot. Clear expectant eyes and a visible raised hand ask the user to intervene. All six frames form a repeatable alert, distinct from ordinary idle/work/review. No floating symbols, no clouds, no duplication. The base locks appearance, not the exact pose.

State requirements:
- Show that Codex needs approval, help, or user input through an expectant asking pose.
- Keep the motion patient and readable, without turning it into ordinary idle or review.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## running

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `running`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Six-frame stationary compact staff-flower drill (gunhua) to show focused task work: feet stay planted; rotate the ONE attached dark/gold staff through upright, compact diagonal across chest, foreshortened horizontal guard, opposite diagonal, vertical catch, and return. Hands visibly regrip the same staff and elbows articulate; torso follows subtly with focused eyes. The long staff stays within the slot through perspective and close-body handling, never changes into another weapon, and never detaches from both hands. No literal foot-running, locomotion, duplicate staff, energy trails or blur. Base locks appearance, not its exact pose.

State requirements:
- Show the pet actively working or processing, as if running a task: focused posture, busy hands or paws, purposeful bobbing, thinking motion, tool or prop motion only if already part of the pet identity, or other non-locomotion activity.
- Do not show literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, directional travel, speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## review

```text
Create one horizontal animation strip for Codex pet `black-myth-destined-one`, state `review`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure user-selected #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: The Destined One from Black Myth Wukong, grounded in the supplied official hero artwork: realistic stern brown-furred monkey warrior face with swept-up hair, intricately embossed weathered black-and-gold Chinese armor, dark burgundy cloth, boots and a small attached waist gourd. Carry one dark staff with gold end fittings, always attached to at least one hand. No phoenix plumes, crown, helmet, monkey cartoon face or extra weapons. Compact complete full-body hero silhouette, not generic Journey to the West cartoon Sun Wukong. Base stands front three-quarter facing viewer, staff kept close along body, boots visible.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Compact semi-realistic 3D game miniature; retain game face and armor, slightly simplified readable ornamental detail, serious heroic character, no chibi or googly eyes..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Six-frame composed output-review loop with a compact THRUST-stance gesture: lean forward slightly and aim the same staff a short foreshortened distance toward screen-right/front as if pointing out the completed result, pause to inspect with eyes and a slight head tilt, withdraw the staff and settle upright. This is a calm guard/pointing gesture, not combat or locomotion. Preserve same staff grip, armor and gourd; the entire staff fits each slot. No paper, UI, icons, new objects, motion effects or enemy. Base locks appearance, not exact pose.

State requirements:
- Show review through lean, blink, narrowed eyes, head tilt, or paw/hand position.
- Do not add magnifying glasses, papers, code, UI, punctuation, symbols, or other new props unless they already exist in the base pet identity.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
```

## look-cardinals

```text
Create one horizontal four-cardinal anchor strip for Codex pet `black-myth-destined-one`.

Use the attached canonical base, completed standard contact sheet, and layout guide for exact identity, style, scale, baseline, face construction, materials, palette, markings, props, and spacing. Read `qa/look-mechanics.md` and use the pet's natural gaze mechanism.

Output exactly four centered complete full-body poses in this exact left-to-right order: `000 up`, `090 screen-right`, `180 down`, `270 screen-left`. Screen-left and screen-right always mean the viewer's image edges, never the character's own left or right.

For `000`, keep the face broadly frontal and point the eyes and natural head mechanism toward the TOP edge. For `090`, put the nose tip, pupils, face surface, or natural aiming feature on the screen-right side of the head center. For `180`, keep the face broadly frontal and point toward the BOTTOM edge. For `270`, apply the inverse screen-left landmark rule. Every cardinal must be unmistakable without labels.

Place one pose in each invisible equal-width slot on a flat pure user-selected #FF00FF background with generous padding. Keep scale, feet/base, lower body, and registration consistent across all four slots.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement eyes, labels, degree text, arrows, boxes, guide marks, shadows, scenery, detached effects, or chroma-key colors inside the pet.
```

## look-row-9

```text
Create one horizontal look-direction strip for Codex pet `black-myth-destined-one`, atlas row 9.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip is authoritative for the up, screen-right, down, and screen-left pose families. Interpolate the intermediate directions as even 22.5-degree steps between those anchors.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 000, 022.5, 045, 067.5, 090, 112.5, 135, 157.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `000`: vertical UP; no horizontal requirement.
2. `022.5`: horizontal SCREEN-RIGHT and vertical UP.
3. `045`: horizontal SCREEN-RIGHT and vertical UP.
4. `067.5`: horizontal SCREEN-RIGHT and vertical UP.
5. `090`: horizontal SCREEN-RIGHT; no vertical requirement.
6. `112.5`: horizontal SCREEN-RIGHT and vertical DOWN.
7. `135`: horizontal SCREEN-RIGHT and vertical DOWN.
8. `157.5`: horizontal SCREEN-RIGHT and vertical DOWN.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-right means the viewer's right image edge, never the character's own right. The row should travel naturally through the right half of the loop. Near-vertical 022.5 and 157.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure user-selected #FF00FF. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 157.5 must be one even 22.5-degree step before 180. Match the approved 180 pose's body size, baseline, planted anchor, expression, and construction. Preserve the overall right-hand arc, but do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 157.5 does not flow evenly into 180. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.
```

## look-row-10

```text
Create one horizontal look-direction strip for Codex pet `black-myth-destined-one`, atlas row 10.

FINAL GENERATIVE REPAIR: the TOP horizontal eight-pose strip in the repair reference board is the newest front-facing LEFT-family candidate. Recreate this entire coherent family on the same roughly 2172x724 output canvas, but reduce ALL EIGHT complete character groups uniformly by ABOUT SEVEN PERCENT (0.93 times their current source size) to add magenta breathing room above the crown and below the boots. This is one unified new synthesis, not a paste or final-cell edit. Preserve the exact fixed camera, front armor, original hand/staff, gourd, identity and head/neck motions of this TOP strip except strengthen the sixth pose's UP-LEFT yaw. Official appearance and canonical full-body identity appear BELOW the top strip on the same board. Source pose maximum span must stay below 480 pixels rather than the candidate's 512. ALL character groups share the same smaller body scale and baseline. DO NOT make them larger to fill the canvas.

Special sixth-pose repair (292.5): muzzle MUST project LEFT of head center while chin tilts UP. Show a strong left-facing nose profile and lifted chin like the approved 270 LEFT anchor plus modest upward pitch. Never show a nose projecting screen-right in this sixth pose. Seventh and eighth poses retain up-left, approaching the up cardinal. Bodies remain frontal.

REPAIR THE BACK-FACING MISINTERPRETATION. Degree labels describe a two-dimensional screen gaze clock, NOT the character's 3D body yaw. 180 means look DOWN toward the ground in front of the character, NOT turn 180 degrees and show the back. 270 means turn only the HEAD to screen-left, NOT turn the body away. All eight bodies MUST show the same front armor, front burgundy sash, front knees and boot fronts as the canonical neutral and row 9. Staff remains along screen-left and gourd along screen-right in all cells. Back armor, rear head-only silhouettes, reversed pelvis, back-facing shoulders, and rear boots are forbidden. Never orbit the camera. All poses use the identical fixed camera, front-facing body, planted lower limbs and light. Only existing eyes, brow, muzzle, head and neck change. At 180 the chin visibly tucks toward the front chest and the crown is seen from above while the front torso remains unchanged. At all leftward diagonals the muzzle protrudes screen-left with the required pitch; never show an entirely rear-facing head. Match the APPROVED cardinal DOWN and LEFT rather than guessing from degree numbers.

Use the attached canonical base, completed standard contact sheet, layout guide, and approved four-cardinal strip for identity, scale, registration, spacing, direction semantics, and cross-row continuity. Read `qa/look-mechanics.md` and follow its pet-specific movement and eye/prop mechanics. The approved cardinal strip and completed coherent row 9 are authoritative. Use the cardinals for direction meaning and row 9 for cross-row identity, scale, registration, and continuity.

COHERENT SYNTHESIS LOCK: produce one unified eight-pose row. Do not paste, tile, or independently restyle individual cells. Every final cell must be drawn together with the same face construction, body proportions, line/render quality, lighting, materials, scale, baseline, and registration.

Output exactly 8 complete full-body frames in this exact left-to-right order: 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5. Degrees are clockwise: 000 is up, 090 right, 180 down, and 270 left. Neutral/front is not part of this row.

LEFT-ARC REPAIR AND SOURCE SCALE LOCK: ignore the right-looking HEADS in row 9 except for identity; row 9 is a body/scale/registration reference, not the target face direction for this second half. Use the clearly screen-LEFT head of the approved cardinal strip as the target. In cells 2 through 8 the nose/muzzle tip must visibly extend toward the LEFT IMAGE EDGE relative to the head center. In cell 5 (270), the bridge-to-nose profile extends left, the muzzle protrudes LEFT, and the far eye is hidden by that leftward yaw. A rightward nose/profile anywhere in these seven cells is forbidden. Cell 1 bows chin straight DOWN; cell 2 bows down with a small LEFT yaw; cell 3 down+LEFT; cell 4 strongly LEFT with a little chin tuck; cell 5 strongly LEFT level; cell 6 strongly LEFT with little chin lift; cell 7 up+LEFT; cell 8 mostly UP with small LEFT yaw. Do not reverse this arc. Keep the front torso fixed despite all head turns.

Match the source character height of attached row 9, not the larger body of an earlier attempt. On a 2172x724 canvas each character's complete crown/staff-top-to-boot span should be about 470–480 pixels, never 500+; keep all poses the same overall body size and baseline, with about one-third of the vertical canvas remaining chroma-only breathing room. If another output size is chosen, keep the same row 9 relative character scale. Do not enlarge any individual pose. Safe outer and inter-pose chroma gaps are mandatory. The fixed-scale final normalization must leave hair and staff inside the cell.

DIRECTION TARGETS — use these to shape the coherent row, not as pixel-level landmark gates:

1. `180`: vertical DOWN; no horizontal requirement.
2. `202.5`: horizontal SCREEN-LEFT and vertical DOWN.
3. `225`: horizontal SCREEN-LEFT and vertical DOWN.
4. `247.5`: horizontal SCREEN-LEFT and vertical DOWN.
5. `270`: horizontal SCREEN-LEFT; no vertical requirement.
6. `292.5`: horizontal SCREEN-LEFT and vertical UP.
7. `315`: horizontal SCREEN-LEFT and vertical UP.
8. `337.5`: horizontal SCREEN-LEFT and vertical UP.

Cardinals must be unmistakable. Intermediate poses should broadly occupy the intended quadrant and advance naturally through the ordered loop. Minor pupil, nose, eyelid, or aiming-feature deviations are acceptable when the overall direction, continuity, identity, and motion remain coherent. Do not deform the character merely to make every intermediate axis independently obvious.

SCREEN-COORDINATE LOCK: screen-left means the viewer's left image edge, never the character's own left. The row should travel naturally through the left half of the loop. Near-vertical 202.5 and 337.5 may have subtle horizontal cues; prioritize a coherent arc over exact pupil or nose placement.

HARD LAYOUT AND CONTINUITY CONTRACT — DETERMINISTIC REGISTRATION: draw exactly eight separated pose groups in left-to-right direction order. Keep enough chroma-only space between neighboring poses that each complete pose can be detected without cutting through foreground. Approximate the guide's equal spacing, but do not distort a pose merely to hit an exact source-canvas coordinate; deterministic assembly will crop the eight ordered groups, then apply one shared scale and baseline.

Use the same body height, head size, baseline, and planted-body position across the generated family. Never overlap neighboring poses, merge two poses into one connected group, crop foreground at the outer canvas edge, or resize one pose independently.

Keep the feet, base, or lower torso planted at the same coordinates across all eight frames. Express direction through the eyes, face, head, upper body, and physically appropriate prop movement, not by moving, rotating, or rescaling the entire sprite.

Place one centered pose in each invisible equal-width slot on flat pure user-selected #FF00FF. Change only the natural parts needed to express gaze: eyes, eyelids, head, face, neck, upper body, appendages, and constrained prop follow-through. Keep identity, silhouette, materials, palette, markings, and props consistent.

ROW-BOUNDARY LOCK: 180 must continue directly from row 9's 157.5, matching its body size, baseline, planted anchor, expression, and construction. 337.5 must be one even 22.5-degree step before 000: nearly up-facing while remaining on the overall left-hand arc. Do not distort pupils, nose, or body geometry merely to exaggerate the subtle horizontal component.

PRE-RETURN CHECK: reject this result if it does not contain eight separated pose groups in the required order; neighboring poses overlap; foreground is cropped at the outer canvas edge; any frame changes sprite scale, body or head size, baseline, or planted-body position; the row visibly reverses into the wrong half of the loop; or 180 does not continue from 157.5 or 337.5 does not flow evenly into 000. Minor intermediate pupil or nose deviations are not rejection reasons. Exact cell cropping, resizing, and recentering happen deterministically after generation.

Do not rotate, skew, or tilt the whole sprite to fake gaze. Do not add replacement/googly eyes, labels, degree text, arrows, clocks, grids, shadows, glows, scenery, detached effects, or chroma-key colors inside the pet.
```

