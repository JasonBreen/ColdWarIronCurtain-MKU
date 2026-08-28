"# Paradox Scripting (PDX Script) Rules

## General Syntax
- Use curly braces `{ }` for blocks and nested structures.
- Key-value pairs use an equals sign `=` (e.g., `name = "Example"`).
- Strings should be enclosed in double quotes `"..."`.
- Use `#` for comments.

## Character Definitions
- Characters are defined in `common/characters/` files.
- Standard structure includes `name`, `portraits`, and roles (e.g., `corps_commander`, `field_marshal`).
- Skill values are typically integers.
- Traits are lists of identifiers.

## Localization
- Text intended for the game UI should use localization keys (e.g., `name = "CHARACTER_NAME_KEY"`).
- The actual text is stored in `.yml` files (usually in `localisation/`).

## AI and Strategy
- AI templates and strategy plans are defined in `common/ai_templates/` and `common/ai_strategy_plans/`.
- Files often follow a pattern of `[COUNTRY]_strategy_plan.txt`.

## Mod Structure
- This is a Hearts of Iron IV (HOI4) mod.
- Always respect the directory structure of a Paradox mod.
- Use `common/` for data, `events/` for events, `localisation/` for text, and `gfx/` for graphics (though we don't edit gfx directly).
"