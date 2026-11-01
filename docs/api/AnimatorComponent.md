<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › AnimatorComponent

# AnimatorComponent

22 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `advanceCurrentTime` | `AnimatorComponent:advanceCurrentTime(arg1: number)` | SNJ | `a84b0 / 104e40 / e8154` | Not described (name only). |
| `callEventHandlers` | `AnimatorComponent:callEventHandlers(arg1: number, arg2: number)` | SNJ | `a82a8 / 104ab0 / e7b50` | Not described (name only). |
| `create` | `AnimatorComponent:create(...)` | SNJ | `a78a0 / 1152f0 / e8460` | Not described (name only). |
| `getCurrentTime` | `AnimatorComponent:getCurrentTime(): number` | SNJ | `a808c / f966c / e7dd8` | Returns the current time. |
| `getDuration` | `AnimatorComponent:getDuration(): number` | SNJ | `a7dc8 / f9030 / e7d58` | Returns the duration. |
| `getEventListener` | `AnimatorComponent:getEventListener()` | SNJ | `a7d50 / f9350 / e4230` | Returns the event listener. |
| `getSceneAnimation` | `AnimatorComponent:getSceneAnimation()` | SNJ | `a81c0 / 113364 / e8378` | Returns the scene animation. |
| `getSpeed` | `AnimatorComponent:getSpeed(): number` | SNJ | `a80f4 / f94e8 / e7e40` | Returns the speed. |
| `isLooped` | `AnimatorComponent:isLooped(): boolean` | SNJ | `a815c / f9db8 / e80f0` | Returns whether looped. |
| `isPaused` | `AnimatorComponent:isPaused(): boolean` | SNJ | `a7f64 / f8464 / e7fc8` | Returns whether paused. |
| `isPlaying` | `AnimatorComponent:isPlaying(): boolean` | SNJ | `a7ff8 / f8290 / e805c` | Returns whether playing. |
| `isStopped` | `AnimatorComponent:isStopped(): boolean` | SNJ | `a7efc / f9bfc / e7f60` | Returns whether stopped. |
| `play` | `AnimatorComponent:play()` | SNJ | `a7ea0 / fac3c / e7c34` | Not described (name only). |
| `replay` | `AnimatorComponent:replay()` | SNJ | `a8450 / d508c / e7f00` | Not described (name only). |
| `reset` | `AnimatorComponent:reset()` | SNJ | `a83f8 / d516c / e7ea8` | Not described (name only). |
| `resolveBindings` | `AnimatorComponent:resolveBindings()` | SNJ | `a83a0 / d5244 / e7cfc` | Not described (name only). |
| `setCurrentTime` | `AnimatorComponent:setCurrentTime(currentTime: number)` | SNJ | `a8520 / d4f70 / e81c4` | Sets the current time. |
| `setEventListener` | `AnimatorComponent:setEventListener(eventListener: any)` | SNJ | `a7ce8 / f6460 / e74a8` | Sets the event listener. |
| `setLoop` | `AnimatorComponent:setLoop(loop: boolean)` | SNJ | `a8590 / f7f14 / e8234` | Sets the loop. |
| `setSceneAnimation` | `AnimatorComponent:setSceneAnimation(sceneAnimation: SceneAnimation)` | SNJ | `a85f8 / d4d2c / e829c` | Sets the scene animation. |
| `setSpeed` | `AnimatorComponent:setSpeed(speed: number)` | SNJ | `a8334 / f91d0 / e7c90` | Sets the speed. |
| `stop` | `AnimatorComponent:stop()` | SNJ | `a7e48 / fb2e4 / e7bdc` | Not described (name only). |

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

← [AnimatedSpriteComponent](AnimatedSpriteComponent.md) · [Index](README.md) · [Application](Application.md) →
