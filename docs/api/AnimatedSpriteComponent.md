<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › AnimatedSpriteComponent

# AnimatedSpriteComponent

16 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `animEnded` | `AnimatedSpriteComponent:animEnded(): boolean` | SNJ | `aca44 / fcc78 / ed13c` | Calls anim ended. |
| `changeAnimation` | `AnimatedSpriteComponent:changeAnimation(arg1: SpriteAnimationResource)` | SNJ | `acb98 / dfdcc / ed214` | Calls change animation. |
| `create` | `AnimatedSpriteComponent:create(...)` | SNJ | `ac3ec / 115030 / e87a8` | Calls create. |
| `getAnchor` | `AnimatedSpriteComponent:getAnchor(): (number, number)` | SNJ | `ac67c / fa920 / ecd5c` | Returns the anchor. |
| `getSpriteAnimation` | `AnimatedSpriteComponent:getSpriteAnimation()` | SNJ | `accb8 / 112e54 / ecddc` | Returns the sprite animation. |
| `increaseTime` | `AnimatedSpriteComponent:increaseTime(arg1: number)` | SNJ | `acda0 / fc298 / ed334` | Calls increase time. |
| `isAutoUpdated` | `AnimatedSpriteComponent:isAutoUpdated(): boolean` | SNJ | `ac97c / f2904 / ecf2c` | Returns whether auto updated. |
| `isFlippedHorizontal` | `AnimatedSpriteComponent:isFlippedHorizontal(): boolean` | SNJ | `ac914 / f20a0 / eccf4` | Returns whether flipped horizontal. |
| `isFlippedVertical` | `AnimatedSpriteComponent:isFlippedVertical(): boolean` | SNJ | `ac8ac / f1ee4 / ecc8c` | Returns whether flipped vertical. |
| `isLooped` | `AnimatedSpriteComponent:isLooped(): boolean` | SNJ | `ac9e0 / f2748 / ecff8` | Returns whether looped. |
| `restart` | `AnimatedSpriteComponent:restart()` | SNJ | `acab0 / f240c / ed1a8` | Calls restart. |
| `setAutoUpdate` | `AnimatedSpriteComponent:setAutoUpdate(autoUpdate: boolean)` | SNJ | `ac6fc / fc760 / ecec4` | Sets the auto update. |
| `setFlipHorizontal` | `AnimatedSpriteComponent:setFlipHorizontal(flipHorizontal: boolean)` | SNJ | `ac83c / fa754 / ed0cc` | Sets the flip horizontal. |
| `setFlipVertical` | `AnimatedSpriteComponent:setFlipVertical(flipVertical: boolean)` | SNJ | `ac7cc / fa588 / ed05c` | Sets the flip vertical. |
| `setLoop` | `AnimatedSpriteComponent:setLoop(loop: boolean)` | SNJ | `ac764 / fc920 / ecf90` | Sets the loop. |
| `setSpriteAnimation` | `AnimatedSpriteComponent:setSpriteAnimation(spriteAnimation: SpriteAnimationResource)` | SNJ | `acc48 / 10149c / ed2c4` | Sets the sprite animation. |

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

← [AnimatedImageResource](AnimatedImageResource.md) · [Index](README.md) · [AnimatorComponent](AnimatorComponent.md) →
