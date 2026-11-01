<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › VideoComponent

# VideoComponent

18 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `close` | `VideoComponent:close(0 args)` | N | `- / f16c8 / -` | Not described (name only). |
| `create` | `VideoComponent:create(? args)` | N | `- / 114cc0 / -` | Not described (name only). |
| `getCurrentTime` | `VideoComponent:getCurrentTime(0 args)` | N | `- / fbf50 / -` | Returns the current time. |
| `getCurrentTimeAsSeconds` | `VideoComponent:getCurrentTimeAsSeconds(0 args)` | N | `- / fa278 / -` | Returns the current time as seconds. |
| `getLength` | `VideoComponent:getLength(0 args)` | N | `- / fbdc8 / -` | Returns the length. |
| `getLengthAsSeconds` | `VideoComponent:getLengthAsSeconds(0 args)` | N | `- / fa400 / -` | Returns the length as seconds. |
| `getState` | `VideoComponent:getState(0 args)` | N | `- / fd038 / -` | Returns the state. |
| `isAutoPlay` | `VideoComponent:isAutoPlay(0 args)` | N | `- / fc41c / -` | Returns whether auto play. |
| `open` | `VideoComponent:open(1 args)` | N | `- / d3f8c / -` | Not described (name only). |
| `pause` | `VideoComponent:pause(0 args)` | N | `- / fea58 / -` | Not described (name only). |
| `play` | `VideoComponent:play(0 args)` | N | `- / fe8d4 / -` | Not described (name only). |
| `resume` | `VideoComponent:resume(0 args)` | N | `- / fe5cc / -` | Not described (name only). |
| `seek` | `VideoComponent:seek(1 args)` | N | `- / fbc50 / -` | Not described (name only). |
| `seekAsSeconds` | `VideoComponent:seekAsSeconds(1 args)` | N | `- / fb954 / -` | Not described (name only). |
| `setAutoPlay` | `VideoComponent:setAutoPlay(1 args)` | N | `- / fb124 / -` | Sets the auto play. |
| `setAutoresize` | `VideoComponent:setAutoresize(1 args)` | N | `- / faf64 / -` | Sets the autoresize. |
| `setSize` | `VideoComponent:setSize(2 args)` | N | `- / f87ec / -` | Sets the size. |
| `stop` | `VideoComponent:stop(0 args)` | N | `- / fe750 / -` | Not described (name only). |

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

← [TilemapComponent](TilemapComponent.md) · [Index](README.md) · [VisualComponent](VisualComponent.md) →
