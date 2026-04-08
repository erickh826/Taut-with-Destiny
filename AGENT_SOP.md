# AI Film Agent SOP

Use this file as the main execution map for the `story1` project.
Each stage points to the file or folder that should be read or updated.

## Stage Map
| Stage | Status | Primary Path | What It Covers |
|------|--------|--------------|----------------|
| 01 Story Lock | ready | `content/` | Story premise, character arc, world rules |
| 02 Visual Rules | partial | `visual_bible/` | Color, light, lens, continuity rules |
| 03 Character Package | ready | `Characters/` | Character templates, reference images |
| 04 Scene Package | partial | `Scene/` | Location prompts, camera language, scene backgrounds |
| 05 Storyboard Lock | ready | `storyboard/` | Shot-by-shot storyboards and prompt execution |
| 06 Shot Tracking | missing -> created | `production/shot_tracking/` | Shot status, coverage, missing assets |
| 07 Sound Plan | missing -> created | `sound/` | Ambience, foley, music, dialogue plan |
| 08 Edit / Animatic | missing -> created | `edit/` | Rough cut, timing, transitions, missing shots |
| 09 QC / Delivery | missing -> created | `production/qc/` and `exports/` | Final checks and export targets |

## 01 Story Lock
- Read first: `content/synopsis.md`
- Check overview: `content/_index.md`
- Goal: lock the story spine before more asset generation
- Done when:
  - protagonist goal is clear
  - emotional arc is clear
  - all acts have a distinct function

## 02 Visual Rules
- Main folder: `visual_bible/`
- Existing source material:
  - `storyboard/comment_prompt.md`
  - `Scene/camera language tags/_index.md`
  - `Scene/scene_prompt/`
- Goal: centralize visual rules that are currently scattered
- Fill next:
  - `visual_bible/visual_bible.md`
- Done when:
  - color palette is fixed
  - light rules are fixed
  - lens / framing rules are fixed
  - continuity rules are documented

## 03 Character Package
- Main folder: `Characters/`
- Read first:
  - `Characters/_index.md`
  - `Characters/character_prompt/_index.md`
  - `Characters/character_prompt/character_template/_index.md`
- Key working areas:
  - `Characters/character_prompt/`
  - `Characters/夏星辰/`
  - `Characters/程子言/`
  - `Characters/霍宇翔/`
- Goal: lock official look for each character
- Watch items:
  - `Characters/character_prompt/character_template/couple.md`
  - `Characters/character_prompt/character_template/brunout_wonman.md`
- Done when:
  - each main role has an official face / half body / full body reference
  - support characters are reusable
  - clothing and expression sets are stable

## 04 Scene Package
- Main folder: `Scene/`
- Read first:
  - `Scene/_index.md`
  - `Scene/camera language tags/_index.md`
  - `Scene/scene_prompt/_index.md`
- Goal: keep environment prompts reusable and location-consistent
- Current gap:
  - `Scene/scene_prompt/` mainly covers ACT 1
- Done when:
  - each recurring location has a reusable prompt
  - each location has wide / medium / detail variants
  - Hong Kong and Taiwan spaces are both covered

## 05 Storyboard Lock
- Main folder: `storyboard/`
- Read first:
  - `storyboard/_index.md`
  - `storyboard/Summary.md`
  - `storyboard/characters.md`
  - `storyboard/comment_prompt.md`
- Execution files:
  - `storyboard/ACT1/`
  - `storyboard/ACT2/`
  - `storyboard/ACT3/`
- Goal: every shot must be shootable and editable
- Done when:
  - each shot has function, duration, framing, movement, and prompt
  - missing reverse shots / inserts / reactions are identified

## 06 Shot Tracking
- Main folder: `production/shot_tracking/`
- Fill next:
  - `production/shot_tracking/master_shot_tracker.md`
- Goal: track generation and edit readiness
- Track fields:
  - shot id
  - status
  - keyframe ready
  - motion needed
  - sound note
  - edit note

## 07 Sound Plan
- Main folder: `sound/`
- Fill next:
  - `sound/sound_plan.md`
- Pull references from:
  - sound notes inside `storyboard/ACT*/board*.md`
- Goal: define ambience, foley, dialogue, and music before final edit

## 08 Edit / Animatic
- Main folder: `edit/`
- Fill next:
  - `edit/animatic_plan.md`
- Goal: assemble rough cut before full motion work
- Order:
  - keyframes
  - rough timing
  - transition plan
  - missing shot list

## 09 QC / Delivery
- QC folder: `production/qc/`
- Export folder: `exports/`
- Fill next:
  - `production/qc/final_qc_checklist.md`
- Goal: verify continuity and prepare final renders
- Final checks:
  - face continuity
  - costume continuity
  - location continuity
  - color continuity
  - sound balance
  - subtitle / dialogue sync

## Recommended Working Order
1. Lock `ACT1` first using `storyboard/ACT1/`
2. Fill `visual_bible/visual_bible.md`
3. Finalize official character references in `Characters/`
4. Expand missing scene prompts in `Scene/`
5. Track all shots in `production/shot_tracking/master_shot_tracker.md`
6. Build animatic plan in `edit/animatic_plan.md`
7. Add sound structure in `sound/sound_plan.md`
8. Run final checks in `production/qc/final_qc_checklist.md`
