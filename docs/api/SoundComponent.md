<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › SoundComponent

# SoundComponent

36 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `closeNativeDevice` | `SoundComponent:closeNativeDevice(...)` | SJ | `b3174 / - / f3bf4` | Not described (name only). |
| `create` | `SoundComponent:create(...)` | SNJ | `a77fc / 114c10 / e70d8` | Not described (name only). |
| `getMasterVolume` | `SoundComponent:getMasterVolume(...): number` | SNJ | `b3110 / b3e68 / f3b90` | Returns the master volume. |
| `getMaxDistance` | `SoundComponent:getMaxDistance(): number` | SNJ | `a3c10 / 102e6c / e3434` | Returns the max distance. |
| `getMinDistance` | `SoundComponent:getMinDistance(): number` | SNJ | `a3c78 / 102b64 / e349c` | Returns the min distance. |
| `getPan` | `SoundComponent:getPan(): number` | SNJ | `a3edc / 102ff0 / e3700` | Returns the pan. |
| `getPitch` | `SoundComponent:getPitch(): number` | SNJ | `a3e74 / 102ce8 / e3698` | Returns the pitch. |
| `getPriority` | `SoundComponent:getPriority(): integer` | SNJ | `a3e10 / 103a00 / e3634` | Returns the priority. |
| `getSamplePosition` | `SoundComponent:getSamplePosition(): number` | SNJ | `a7340 / d5650 / e3e08` | Returns the sample position. |
| `getSoundResource` | `SoundComponent:getSoundResource()` | SNJ | `a7258 / 113574 / e3834` | Returns the sound resource. |
| `getTimePosition` | `SoundComponent:getTimePosition(): number` | SNJ | `a7440 / d54d0 / e3f08` | Returns the time position. |
| `getVolume` | `SoundComponent:getVolume(): number` | SNJ | `a3f44 / 1029e0 / e3768` | Returns the volume. |
| `isAutoPlay` | `SoundComponent:isAutoPlay(): boolean` | SNJ | `a3dac / 1034cc / e35d0` | Returns whether auto play. |
| `isLooped` | `SoundComponent:isLooped(): boolean` | SNJ | `a3fac / 103688 / e37d0` | Returns whether looped. |
| `isMuted` | `SoundComponent:isMuted(...): boolean` | SNJ | `b2f9c / be9c8 / f3a1c` | Returns whether muted. |
| `isPaused` | `SoundComponent:isPaused(): boolean` | SNJ | `a7550 / 1025ec / e391c` | Returns whether paused. |
| `isPlaying` | `SoundComponent:isPlaying(): boolean` | SNJ | `a75e4 / 1019ac / e4018` | Returns whether playing. |
| `isPositional` | `SoundComponent:isPositional(): boolean` | SNJ | `a3ce0 / 103310 / e3504` | Returns whether positional. |
| `isStoppedWhenDisabled` | `SoundComponent:isStoppedWhenDisabled(): boolean` | SNJ | `a3b44 / 103844 / e3368` | Returns whether stopped when disabled. |
| `pause` | `SoundComponent:pause()` | SNJ | `a76ec / 1027b4 / e4120` | Not described (name only). |
| `play` | `SoundComponent:play(): number` | SNJ | `a7790 / d5428 / e41c4` | Not described (name only). |
| `playOneShot` | `SoundComponent:playOneShot(arg1: number, arg2: number, arg3: number)` | SNJ | `a5f70 / e7a7c / e3270` | Not described (name only). |
| `setAutoPlay` | `SoundComponent:setAutoPlay(autoPlay: boolean)` | SNJ | `a3d44 / 101d94 / e3568` | Sets the auto play. |
| `setLoop` | `SoundComponent:setLoop(loop: boolean)` | SNJ | `a4384 / d5a70 / e3d24` | Sets the loop. |
| `setMasterVolume` | `SoundComponent:setMasterVolume()` | SNJ | `b3098 / e8718 / f3b18` | Sets the master volume. |
| `setMaxDistance` | `SoundComponent:setMaxDistance(maxDistance: number)` | SNJ | `a4010 / 1017f8 / e39b0` | Sets the max distance. |
| `setMinDistance` | `SoundComponent:setMinDistance(minDistance: number)` | SNJ | `a4090 / 1012e8 / e3a30` | Sets the min distance. |
| `setMute` | `SoundComponent:setMute()` | SNJ | `b2fe4 / e8884 / f3a64` | Sets the mute. |
| `setPan` | `SoundComponent:setPan(pan: number)` | SNJ | `a4264 / d5d4c / e3c04` | Sets the pan. |
| `setPitch` | `SoundComponent:setPitch(pitch: number)` | SNJ | `a41f0 / d5ebc / e3b90` | Sets the pitch. |
| `setPositional` | `SoundComponent:setPositional(positional: boolean)` | SNJ | `a4110 / d6150 / e3ab0` | Sets the positional. |
| `setPriority` | `SoundComponent:setPriority(priority: integer)` | SNJ | `a4180 / d6008 / e3b20` | Sets the priority. |
| `setSoundResource` | `SoundComponent:setSoundResource(soundResource: SoundResource)` | SNJ | `a6068 / d57c0 / e3d94` | Sets the sound resource. |
| `setStopWhenDisabled` | `SoundComponent:setStopWhenDisabled(stopWhenDisabled: boolean)` | SNJ | `a3ba8 / 101bd4 / e33cc` | Sets the stop when disabled. |
| `setVolume` | `SoundComponent:setVolume(volume: number)` | SNJ | `a4310 / d5c00 / e3cb0` | Sets the volume. |
| `stop` | `SoundComponent:stop()` | SNJ | `a7688 / 103174 / e40bc` | Not described (name only). |

## Notes

- **`getSamplePosition`**: Returns 0.0 when the component has no native sound object; it does not raise an error.
- **`isPlaying`**: Returns false when the component has no native sound object (for example a disabled one); it does not raise an error.
- **`play`**: Plays only when the component has a native sound object and is enabled (the virtual isEnabled returns true); otherwise it returns 0 and does nothing, without an error. Returns the playback handle as a number.
- **`setSoundResource`**: The argument must be a loaded SoundResource; otherwise the engine raises 'resource (SoundResource) is not loaded'.

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

← [ScriptComponent](ScriptComponent.md) · [Index](README.md) · [SoundListenerComponent](SoundListenerComponent.md) →
