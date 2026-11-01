<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › SoundResource

# SoundResource

3 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `getLength` | `SoundResource:getLength(): number` | SNJ | `a7c50 / b2e68 / e2488` | Returns the length. |
| `getSampleCount` | `SoundResource:getSampleCount(): number` | SNJ | `a7bb8 / b30d0 / e23f0` | Returns the sample count. |
| `getSampleRate` | `SoundResource:getSampleRate(): number` | SNJ | `a7b30 / b3320 / e2368` | Returns the sample rate. |

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

← [SoundListenerComponent](SoundListenerComponent.md) · [Index](README.md) · [SpriteAnimationResource](SpriteAnimationResource.md) →
