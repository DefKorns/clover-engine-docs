<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › TextureComponent

# TextureComponent

19 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `create` | `TextureComponent:create(...)` | SNJ | `ac348 / 114f80 / e8700` | Calls create. |
| `getPivot` | `TextureComponent:getPivot(): (number, number)` | SNJ | `abd90 / f2f4c / ec250` | Returns the pivot. |
| `getSize` | `TextureComponent:getSize(): (number, number)` | SNJ | `abec8 / fe448 / ec518` | Returns the size. |
| `getTexture` | `TextureComponent:getTexture()` | SNJ | `ac2ec / 1178d0 / ec614` | Returns the texture. |
| `getTextureOffset` | `TextureComponent:getTextureOffset(): (number, number)` | SNJ | `abd14 / f33f4 / ec12c` | Returns the texture offset. |
| `getTextureRepeat` | `TextureComponent:getTextureRepeat(): (number, number)` | SNJ | `abad8 / f2c48 / ebef0` | Returns the texture repeat. |
| `resetSize` | `TextureComponent:resetSize()` | SNJ | `abe14 / f30c4 / ec2d4` | Calls reset size. |
| `setCurrentFrame` | `TextureComponent:setCurrentFrame(currentFrame: integer)` | J | `- / - / ebcec` | Sets the current frame. |
| `setHeight` | `TextureComponent:setHeight(height: number)` | SJ | `abffc / - / ec388` | Sets the height. |
| `setPivot` | `TextureComponent:setPivot(arg1: number, arg2: number)` | SNJ | `abf54 / f19dc / ec1a8` | Sets the pivot. |
| `setSize` | `TextureComponent:setSize(arg1: number, arg2: number)` | SNJ | `ac0ec / f1d58 / ec478` | Sets the size. |
| `setTexture` | `TextureComponent:setTexture(texture: Resource)` | SNJ | `ac18c / e0130 / ec5a4` | Sets the texture. |
| `setTextureOffset` | `TextureComponent:setTextureOffset(arg1: number, arg2: number)` | SNJ | `abc64 / f1840 / ec07c` | Sets the texture offset. |
| `setTextureOffsetX` | `TextureComponent:setTextureOffsetX(textureOffsetX: number)` | SJ | `abbe4 / - / ebffc` | Sets the texture offset x. |
| `setTextureOffsetY` | `TextureComponent:setTextureOffsetY(textureOffsetY: number)` | SJ | `abb64 / - / ebf7c` | Sets the texture offset y. |
| `setTextureRepeat` | `TextureComponent:setTextureRepeat(arg1: number, arg2: number)` | SNJ | `aba3c / f2ac0 / ebe54` | Sets the texture repeat. |
| `setTextureRepeatX` | `TextureComponent:setTextureRepeatX(textureRepeatX: number)` | SJ | `ab9c8 / - / ebde0` | Sets the texture repeat x. |
| `setTextureRepeatY` | `TextureComponent:setTextureRepeatY(textureRepeatY: number)` | SJ | `ab954 / - / ebd6c` | Sets the texture repeat y. |
| `setWidth` | `TextureComponent:setWidth(width: number)` | SJ | `ac074 / - / ec400` | Sets the width. |

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

← [TextVariable](TextVariable.md) · [Index](README.md) · [TextureResource](TextureResource.md) →
