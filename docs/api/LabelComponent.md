<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › LabelComponent

# LabelComponent

36 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `create` | `LabelComponent:create(...)` | SNJ | `a79e8 / 114d70 / e85b0` | Calls create. |
| `getBottomColor` | `LabelComponent:getBottomColor(): (number, number, number, number)` | SNJ | `aa644 / db49c / ea9e4` | Returns the bottom color. |
| `getCharacterSpacingOffset` | `LabelComponent:getCharacterSpacingOffset(): integer` | SNJ | `aaab4 / e06fc / eae54` | Returns the character spacing offset. |
| `getFlags` | `LabelComponent:getFlags(): number` | SNJ | `aacdc / db038 / eb07c` | Returns the flags. |
| `getFontResource` | `LabelComponent:getFontResource()` | SNJ | `aad44 / 113064 / eb0e4` | Returns the font resource. |
| `getLineHeightOffset` | `LabelComponent:getLineHeightOffset(): integer` | SNJ | `aa9d8 / e0788 / ead78` | Returns the line height offset. |
| `getPivot` | `LabelComponent:getPivot(): (number, number)` | SNJ | `aa058 / db970 / ea3f8` | Returns the pivot. |
| `getShadowColor` | `LabelComponent:getShadowColor(): (number, number, number, number)` | SNJ | `aa310 / db738 / ea6b0` | Returns the shadow color. |
| `getShadowOffset` | `LabelComponent:getShadowOffset(): (number, number)` | SNJ | `aa1d8 / db864 / ea578` | Returns the shadow offset. |
| `getText` | `LabelComponent:getText(): string` | SNJ | `ab5e0 / dad78 / eb978` | Returns the text. |
| `getTextOffset` | `LabelComponent:getTextOffset(): (number, number)` | SNJ | `aa858 / db2f8 / eabf8` | Returns the text offset. |
| `getTextScale` | `LabelComponent:getTextScale(): (number, number)` | SNJ | `aab18 / db110 / eaeb8` | Returns the text scale. |
| `getTopColor` | `LabelComponent:getTopColor(): (number, number, number, number)` | SNJ | `aa7ac / db374 / eab4c` | Returns the top color. |
| `getWrapWidth` | `LabelComponent:getWrapWidth(): integer` | SNJ | `aab94 / e0670 / eaf34` | Returns the wrap width. |
| `hasShadow` | `LabelComponent:hasShadow(): boolean` | SNJ | `aa424 / e08b0 / ea7c4` | Returns whether shadow. |
| `hasWordWrap` | `LabelComponent:hasWordWrap(): boolean` | SNJ | `aabf8 / e05d4 / eaf98` | Returns whether word wrap. |
| `isMonospaced` | `LabelComponent:isMonospaced(): boolean` | SNJ | `aa488 / e0814 / ea828` | Returns whether monospaced. |
| `refreshText` | `LabelComponent:refreshText()` | SNJ | `ab28c / 10115c / eb62c` | Calls refresh text. |
| `refreshTextAll` | `LabelComponent:refreshTextAll(...)` | SNJ | `ab2f4 / e8b24 / eb694` | Calls refresh text all. |
| `setBottomColor` | `LabelComponent:setBottomColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | `aa588 / db528 / ea928` | Sets the bottom color. |
| `setCharacterSpacingOffset` | `LabelComponent:setCharacterSpacingOffset(characterSpacingOffset: integer)` | SNJ | `aaa3c / db18c / eaddc` | Sets the character spacing offset. |
| `setFlags` | `LabelComponent:setFlags(flags: integer)` | SNJ | `aac64 / db0a0 / eb004` | Sets the flags. |
| `setFontResource` | `LabelComponent:setFontResource(fontResource: FontResource)` | SNJ | `ab0e4 / daddc / eb484` | Sets the font resource. |
| `setHasShadow` | `LabelComponent:setHasShadow(hasShadow: boolean)` | SNJ | `aa3bc / db690 / ea75c` | Sets the has shadow. |
| `setLineHeightOffset` | `LabelComponent:setLineHeightOffset(lineHeightOffset: integer)` | SNJ | `aa960 / db1fc / ead00` | Sets the line height offset. |
| `setLocalIntVariable` | `LabelComponent:setLocalIntVariable(arg1: integer, arg2: any)` | SNJ | `aae2c / d3990 / eb1cc` | Sets the local int variable. |
| `setLocalVariable` | `LabelComponent:setLocalVariable(arg1: any, arg2: any)` | SNJ | `aaf14 / d2e8c / eb2b4` | Sets the local variable. |
| `setMonospaced` | `LabelComponent:setMonospaced(monospaced: boolean)` | SNJ | `aa4f0 / db5c4 / ea890` | Sets the monospaced. |
| `setShadowColor` | `LabelComponent:setShadowColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | `aa254 / db7c8 / ea5f4` | Sets the shadow color. |
| `setShadowOffset` | `LabelComponent:setShadowOffset(arg1: number, arg2: number)` | SNJ | `aa14c / db8e0 / ea4ec` | Sets the shadow offset. |
| `setText` | `LabelComponent:setText(text: string)` | SNJ | `ab56c / dba60 / eb904` | Sets the text. |
| `setTextFromStringId` | `LabelComponent:setTextFromStringId(textFromStringId: string)` | SNJ | `ab4e8 / dbafc / eb880` | Sets the text from string id. |
| `setTextOffset` | `LabelComponent:setTextOffset(arg1: number, arg2: number)` | SNJ | `aa8d4 / db26c / eac74` | Sets the text offset. |
| `setTextScale` | `LabelComponent:setTextScale(arg1: number, arg2: number)` | SNJ | `aafe0 / dbc40 / eb380` | Sets the text scale. |
| `setTopColor` | `LabelComponent:setTopColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | `aa6f0 / db400 / eaa90` | Sets the top color. |
| `setWrapWidth` | `LabelComponent:setWrapWidth(wrapWidth: integer)` | SNJ | `ab074 / dbb88 / eb414` | Sets the wrap width. |

## How to read the tables

- **Signature**: `Class:method(...)` is an instance method (colon call); `Class.method(...)` is a static function of a
  global table. Types come from the helper the binding uses to read an argument or push a result: `number`, `integer`,
  `boolean`, `string`, or a resource class. `any` means that helper was not classified. For NES-only methods the
  signature lists only the argument count.
- **Families**: S = SNES (EUR, USA, SHVC), N = NES and HVC, J = Shonen. A dash means the family does not bind the method.
- **Binding**: address of the binding function in the SNES EUR 2.0.14, NES 1.0.7 and Shonen 3.0.1 builds.
- **Summary**: derived from the method name. A **Note** was verified in the code.
- Parameter names are not in the binary: single-argument setters use the name after `set`, the others are `argN`.


---

← [Input](Input.md) · [Index](README.md) · [Localization](Localization.md) →
