<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › CameraDevice

# CameraDevice

7 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `getTextureCoordinates` | `CameraDevice:getTextureCoordinates(0 args)` | N | `- / b44c0 / -` | Returns the texture coordinates. |
| `isStarted` | `CameraDevice:isStarted(0 args)` | N | `- / beb38 / -` | Returns whether started. |
| `setEffect` | `CameraDevice:setEffect(1 args)` | N | `- / b43e0 / -` | Sets the effect. |
| `setFramerate` | `CameraDevice:setFramerate(1 args)` | N | `- / b4300 / -` | Sets the framerate. |
| `setResolution` | `CameraDevice:setResolution(2 args)` | N | `- / b4218 / -` | Sets the resolution. |
| `start` | `CameraDevice:start(0 args)` | N | `- / b3fc8 / -` | Calls start. |
| `stop` | `CameraDevice:stop(0 args)` | N | `- / b40f0 / -` | Calls stop. |

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

← [CameraComponent](CameraComponent.md) · [Index](README.md) · [ClickableComponent](ClickableComponent.md) →
