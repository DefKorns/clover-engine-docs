<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › Input

# Input

8 methods (static functions of a global table).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `freeze` | `Input.freeze(...)` | SNJ | `a2988 / e8e38 / e2194` | Not described (name only). |
| `getPreviousState` | `Input.getPreviousState(arg1: integer, arg2: any): number` | SNJ | `a2d98 / b3b90 / e2b0c` | Returns the previous state. |
| `getState` | `Input.getState(arg1: integer, arg2: any): number` | SNJ | `a2e20 / b3a30 / e2b90` | Returns the state. |
| `getStateDelta` | `Input.getStateDelta(arg1: integer, arg2: any): number` | SNJ | `a2d30 / b3cf0 / e2aa4` | Returns the state delta. |
| `isConnected` | `Input.isConnected(arg1: any): boolean` | SNJ | `a2cac / bda88 / e2a20` | Returns whether connected. |
| `setPreviousState` | `Input.setPreviousState(arg1: integer, arg2: number, arg3: any)` | SNJ | `a2b7c / e7d18 / e28f0` | Sets the previous state. |
| `setState` | `Input.setState(arg1: integer, arg2: number, arg3: any)` | SNJ | `a2c14 / e7e44 / e2988` | Sets the state. |
| `touchToViewPoint` | `Input.touchToViewPoint(arg1: integer, arg2: integer, arg3: any): (integer, integer, integer)` | J | `- / - / e2850` | Not described (name only). |

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

← [ImageResource](ImageResource.md) · [Index](README.md) · [LabelComponent](LabelComponent.md) →
