<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › MeshComponent

# MeshComponent

5 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `create` | `MeshComponent:create(...)` | SNJ | `ac534 / 1153a0 / ed9a0` | Not described (name only). |
| `getTexture` | `MeshComponent:getTexture()` | SNJ | `ad474 / 117ab4 / edf10` | Returns the texture. |
| `getTrianglesCount` | `MeshComponent:getTrianglesCount(): integer` | SNJ | `ad718 / f62b8 / eddb4` | Returns the triangles count. |
| `setTexture` | `MeshComponent:setTexture(texture: Resource)` | SNJ | `ad89c / f59ec / ede18` | Sets the texture. |
| `setTriangles` | `MeshComponent:setTriangles(...)` | SNJ | `ad4d0 / e094c / edb6c` | Sets the triangles. |

## How to read the tables

- **Signature**: `Class:method(...)` is an instance method (colon call); `Class.method(...)` is a static function of a
  global table. Types come from the helper the binding uses to read an argument or push a result: `number`, `integer`,
  `boolean`, `string`, or a resource class. `any` means that helper was not classified. For NES-only methods the
  signature lists only the argument count, except the `VideoComponent` methods, whose bindings were read by hand.
- **Families**: S = SNES (EUR, USA, SHVC), N = NES and HVC, J = Shonen. A dash means the family does not bind the method.
- **Binding**: address of the binding function in the SNES EUR 2.0.14, NES 1.0.7 and Shonen 3.0.1 builds.
- **Summary**: derived from the method name (getters and setters only); "Not described (name only)" means nothing beyond the name is known. A **Note** was verified in the code or in the stock scripts.
- Parameter names are not in the binary: single-argument setters use the name after `set`, the others are `argN`.


---

← [Localization](Localization.md) · [Index](README.md) · [Object](Object.md) →
