<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › Application

# Application

18 methods (static functions of a global table).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `abort` | `Application.abort(...)` | J | `- / - / f3810` | Calls abort. |
| `captureScreen` | `Application.captureScreen(arg1: integer, arg2: string): number` | SNJ | `b1fe8 / c6ac0 / f2a90` | Calls capture screen. |
| `eventFdRead` | `Application.eventFdRead(arg1: integer): (integer, number)` | SJ | `b2d58 / - / f3784` | Calls event fd read. |
| `eventFdWrite` | `Application.eventFdWrite(arg1: integer, arg2: integer): integer` | SJ | `b2cdc / - / f3708` | Calls event fd write. |
| `exit` | `Application.exit(...)` | SNJ | `b2de4 / e820c / f3840` | Calls exit. |
| `getDataPath` | `Application.getDataPath(arg1: any)` | SNJ | `b2e68 / b962c / f3970` | Returns the data path. |
| `getErrorHandler` | `Application.getErrorHandler(...)` | J | `- / - / e263c` | Returns the error handler. |
| `getExitHandler` | `Application.getExitHandler(...)` | SNJ | `a2a30 / d9c28 / e26b0` | Returns the exit handler. |
| `getMaxFPS` | `Application.getMaxFPS(...): number` | SNJ | `b1efc / b4598 / f29a8` | Returns the max fps. |
| `getResourcesPath` | `Application.getResourcesPath(arg1: any)` | J | `- / - / f38c4` | Returns the resources path. |
| `pause` | `Application.pause(...)` | SNJ | `b1fa0 / e8368 / f2a4c` | Calls pause. |
| `resetErrorHandler` | `Application.resetErrorHandler(...)` | J | `- / - / e2600` | Calls reset error handler. |
| `resetExitHandler` | `Application.resetExitHandler(...)` | SNJ | `a29cc / d1334 / e2724` | Calls reset exit handler. |
| `setErrorHandler` | `Application.setErrorHandler(...)` | J | `- / - / e6f6c` | Sets the error handler. |
| `setExitHandler` | `Application.setExitHandler(arg1: any, arg2: any)` | SNJ | `a2ab4 / d1504 / e2788` | Sets the exit handler. |
| `setMaxFPS` | `Application.setMaxFPS(maxFPS: number)` | SNJ | `b1e8c / e7f70 / f2938` | Sets the max fps. |
| `skipDraw` | `Application.skipDraw(...)` | SJ | `b1e4c / - / f28f8` | Calls skip draw. |
| `unpause` | `Application.unpause(...)` | SNJ | `b1f5c / e84a0 / f2a08` | Calls unpause. |

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

← [AnimatorComponent](AnimatorComponent.md) · [Index](README.md) · [CRC64](CRC64.md) →
