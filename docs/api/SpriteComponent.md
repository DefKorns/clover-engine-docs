<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › SpriteComponent

# SpriteComponent

11 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `create` | `SpriteComponent:create(...)` | SNJ | `ac490 / 114ed0 / ed8f8` | Not described (name only). |
| `getPivot` | `SpriteComponent:getPivot(): (number, number)` | SNJ | `acfc0 / f1b70 / ed558` | Returns the pivot. |
| `getSize` | `SpriteComponent:getSize(): (number, number)` | SNJ | `ad0c0 / f2dc8 / ed658` | Returns the size. |
| `getSprite` | `SpriteComponent:getSprite()` | SNJ | `ad418 / 112c70 / ed89c` | Returns the sprite. |
| `isFlippedHorizontal` | `SpriteComponent:isFlippedHorizontal(): boolean` | SNJ | `acf58 / f4654 / ed4ec` | Returns whether flipped horizontal. |
| `isFlippedVertical` | `SpriteComponent:isFlippedVertical(): boolean` | SNJ | `acef0 / f4498 / ed484` | Returns whether flipped vertical. |
| `resetSize` | `SpriteComponent:resetSize()` | SNJ | `ad14c / f225c / ed6e4` | Not described (name only). |
| `setFlipHorizontal` | `SpriteComponent:setFlipHorizontal(flipHorizontal: boolean)` | SNJ | `ace80 / f3c0c / ed414` | Sets the flip horizontal. |
| `setFlipVertical` | `SpriteComponent:setFlipVertical(flipVertical: boolean)` | SNJ | `ace10 / f3a40 / ed3a4` | Sets the flip vertical. |
| `setSize` | `SpriteComponent:setSize(arg1: number, arg2: number)` | SNJ | `ad200 / fd69c / ed798` | Sets the size. |
| `setSprite` | `SpriteComponent:setSprite(sprite: SpriteResource)` | SNJ | `ad294 / dfad4 / ed82c` | Sets the sprite. |

## How to read the tables

- **Signature**: `Class:method(...)` is an instance method (colon call); `Class.method(...)` is a static function of a
  global table. Types come from the helper the binding uses to read an argument or push a result: `number`, `integer`,
  `boolean`, `string`, or a resource class. `any` means that helper was not classified. For NES-only methods the
  signature lists only the argument count.
- **Families**: S = SNES (EUR, USA, SHVC), N = NES and HVC, J = Shonen. A dash means the family does not bind the method.
- **Binding**: address of the binding function in the SNES EUR 2.0.14, NES 1.0.7 and Shonen 3.0.1 builds.
- **Summary**: derived from the method name (getters and setters only); "Not described (name only)" means nothing beyond the name is known. A **Note** was verified in the code or in the stock scripts.
- Parameter names are not in the binary: single-argument setters use the name after `set`, the others are `argN`.


---

← [SpriteAnimationResource](SpriteAnimationResource.md) · [Index](README.md) · [SpriteResource](SpriteResource.md) →
