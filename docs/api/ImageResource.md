<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › ImageResource

# ImageResource

4 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `getPixel` | `ImageResource:getPixel(arg1: number, arg2: number): (number, number, number, number)` | SNJ | `a3504 / b3570 / ecba8` | Returns the pixel. |
| `getSize` | `ImageResource:getSize(): (integer, integer)` | SNJ | `a35f0 / bdfdc / ec670` | Returns the size. |
| `readPixel` | `ImageResource:readPixel(arg1: integer, arg2: integer): (number, number, number, number)` | J | `- / - / ecad8` | Not described (name only). |
| `reloadFromFile` | `ImageResource:reloadFromFile(...): number` | SNJ | `a3678 / b8a70 / ec6f8` | Not described (name only). |

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

← [FontResource](FontResource.md) · [Index](README.md) · [Input](Input.md) →
