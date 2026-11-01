<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › Component

# Component

8 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `disable` | `Component:disable()` | SNJ | `b1a90 / f38b4 / f21f4` | Not described (name only). |
| `enable` | `Component:enable()` | SNJ | `b1aec / f3564 / f2250` | Not described (name only). |
| `getNode` | `Component:getNode()` | SNJ | `b1628 / f4164 / f1f34` | Returns the node. |
| `getTypeName` | `Component:getTypeName(): string` | SNJ | `b1bbc / f4304 / f1bb0` | Returns the type name. |
| `isActive` | `Component:isActive(): boolean` | SNJ | `b1170 / f3f9c / f1a58` | Returns whether active. |
| `isEnabled` | `Component:isEnabled(): boolean` | SNJ | `b1254 / f370c / f1b3c` | Returns whether enabled. |
| `isSelfEnabled` | `Component:isSelfEnabled(): boolean` | SNJ | `b11e8 / f3dd8 / f1ad0` | Returns whether self enabled. |
| `setEnabled` | `Component:setEnabled(enabled: boolean)` | SNJ | `b1b48 / fd830 / f22ac` | Sets the enabled. |

## Notes

- **`disable`**: Disables the component. The boot music (Main.bootBGM) is disabled this way by main.lua and by the Shonen firmware.
- **`enable`**: Enables the component.

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

← [ClickableComponent](ClickableComponent.md) · [Index](README.md) · [FileNameUtils](FileNameUtils.md) →
