<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# Boot music (bgm_boot)

Evidence: `main.lua` and `sys_boot.lua` of the SNES EUR and Shonen stock UI packages (decompiled with
luajit-decompiler), `defaultscene.scn` and `sys_boot.scn` of the SNES EUR package, and `ReedPlayer-Clover` SNES EUR
2.0.14 (decompiled with REA/Ghidra, plus disassembly).

## How the boot music plays

1. `defaultscene.scn` has several `SoundComponent`s on the `Main` node. The first one is linked as `Main.bootBGM`:
   resource `/sounds/hvc/bgm_boot.wav`, `autoPlay: false`, `volume: 1`. The second (`Main.mainBGM`) has no sound
   resource until the script sets it. The component is the same in the HVC, NES, SNES and Shonen stock UI packages.
2. `Main.start` (`main.lua`) ends by playing it: unless `debug_store.debugBGMOff` is set, it calls
   `self:getComponent(SoundComponent):play()`, which returns the first `SoundComponent` of the node, `bootBGM`.
   Nothing else in the scripts plays the boot sound. `sys_boot.lua` plays `bootSound` only if that link is set; it is
   empty in `sys_boot.scn`, which also holds an unused `SoundComponent` with the same WAV.
3. `Main.update` then waits for the main music (`resMainBGM`) to load. When the main music is loaded and
   `not bootBGM:isPlaying()` (or the sample position went back) it calls `mainBGM:play()` and `bootBGM:disable()`.

## How the Shonen firmware silences it

Its `Main.start` calls `bootBGM:disable()` before the play call of step 2, then runs its own rotation of five tracks
(its `Main.update` does not use the step 3 logic). The play call still runs, on the disabled component.

## What the engine does with a disabled component

- `SoundComponent:play()` (SNES binding `FUN_000a7790`, native `FUN_0010a8fc`): it starts playback only when the
  component has a native sound object **and** the virtual `isEnabled` method (the one `Component:isEnabled` calls)
  returns true. Otherwise it returns `0` with no error. It returns the playback handle as a number.
- `SoundComponent:isPlaying()`: false when there is no native sound object. No error.
- `SoundComponent:getSamplePosition()` (binding `0xa7340`, read from the disassembly, a lambda Ghidra did not define as a
  function): returns the constant `0.0` when there is no native sound object. No error.
- `Component:enable`, `disable`, `setEnabled`, `isEnabled` exist on every component.

## Consequence

With `bootBGM` disabled, `Main.start`'s play call does nothing, so the boot sound never plays and no error is raised;
`Main.update` sees `isPlaying()` false and `getSamplePosition()` 0.0, and starts the main music at once. This is exactly
what the Shonen firmware does at run time with `bootBGM:disable()`.

## Not verified

- That `enabled: false` in the scene reaches the same state as the run-time `disable()` call. The component
  deserializer stores `enabled` on the component, and `Component:isEnabled` is a virtual call; the link between the
  two was not read.
- That `getComponent(SoundComponent)` returns a disabled component. If it skipped it, it would return the next
  `SoundComponent` of `Main`, `mainBGM`, which has no sound resource at that time; the result is silent either way.
- Nothing was run on a console.
