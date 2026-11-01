<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › TilemapComponent

# TilemapComponent

7 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `create` | `TilemapComponent:create(...)` | SNJ | `a7a8c / 114e20 / e8658` | Not described (name only). |
| `getTileGridSize` | `TilemapComponent:getTileGridSize(): (integer, integer)` | SNJ | `ab6d4 / f57fc / eba6c` | Returns the tile grid size. |
| `getTileSizeScreen` | `TilemapComponent:getTileSizeScreen(): (number, number)` | SNJ | `ab8d8 / f568c / ebc70` | Returns the tile size screen. |
| `getTileSizeTexture` | `TilemapComponent:getTileSizeTexture(): (number, number)` | SNJ | `ab7d0 / f551c / ebb68` | Returns the tile size texture. |
| `setTileGridSize` | `TilemapComponent:setTileGridSize(arg1: integer, arg2: integer)` | SNJ | `ab644 / e0458 / eb9dc` | Sets the tile grid size. |
| `setTileSizeScreen` | `TilemapComponent:setTileSizeScreen(arg1: number, arg2: number)` | SNJ | `ab84c / f4eec / ebbe4` | Sets the tile size screen. |
| `setTileSizeTexture` | `TilemapComponent:setTileSizeTexture(arg1: number, arg2: number)` | SNJ | `ab744 / f4d74 / ebadc` | Sets the tile size texture. |

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

← [TextureResource](TextureResource.md) · [Index](README.md) · [VideoComponent](VideoComponent.md) →
