<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › VideoComponent

# VideoComponent

18 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `close` | `VideoComponent:close()` | N | `- / f16c8 / -` | Not described (name only). |
| `create` | `VideoComponent:create(? args)` | N | `- / 114cc0 / -` | Not described (name only). |
| `getCurrentTime` | `VideoComponent:getCurrentTime(): number` | N | `- / fbf50 / -` | Returns the current time. |
| `getCurrentTimeAsSeconds` | `VideoComponent:getCurrentTimeAsSeconds(): number` | N | `- / fa278 / -` | Returns the current time as seconds. |
| `getLength` | `VideoComponent:getLength(): number` | N | `- / fbdc8 / -` | Returns the length. |
| `getLengthAsSeconds` | `VideoComponent:getLengthAsSeconds(): number` | N | `- / fa400 / -` | Returns the length as seconds. |
| `getState` | `VideoComponent:getState(): number` | N | `- / fd038 / -` | Returns the state. |
| `isAutoPlay` | `VideoComponent:isAutoPlay(): boolean` | N | `- / fc41c / -` | Returns whether auto play. |
| `open` | `VideoComponent:open(1 args)` | N | `- / d3f8c / -` | Not described (name only). |
| `pause` | `VideoComponent:pause()` | N | `- / fea58 / -` | Not described (name only). |
| `play` | `VideoComponent:play()` | N | `- / fe8d4 / -` | Not described (name only). |
| `resume` | `VideoComponent:resume()` | N | `- / fe5cc / -` | Not described (name only). |
| `seek` | `VideoComponent:seek(arg1: integer)` | N | `- / fbc50 / -` | Not described (name only). |
| `seekAsSeconds` | `VideoComponent:seekAsSeconds(arg1: number)` | N | `- / fb954 / -` | Not described (name only). |
| `setAutoPlay` | `VideoComponent:setAutoPlay(autoPlay: boolean)` | N | `- / fb124 / -` | Sets the auto play. |
| `setAutoresize` | `VideoComponent:setAutoresize(autoresize: boolean)` | N | `- / faf64 / -` | Sets the autoresize. |
| `setSize` | `VideoComponent:setSize(arg1: number, arg2: number)` | N | `- / f87ec / -` | Sets the size. |
| `stop` | `VideoComponent:stop()` | N | `- / fe750 / -` | Not described (name only). |

## Notes

- **`close`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`getCurrentTime`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`getCurrentTimeAsSeconds`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`getLength`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`getLengthAsSeconds`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`getState`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`isAutoPlay`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`pause`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`play`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`resume`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`seek`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`seekAsSeconds`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`setAutoPlay`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`setAutoresize`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`setSize`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.
- **`stop`**: Types read by hand from the NES binding. The NES build inlines result pushes, so the automatic matching could not type it.

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

← [TilemapComponent](TilemapComponent.md) · [Index](README.md) · [VisualComponent](VisualComponent.md) →
