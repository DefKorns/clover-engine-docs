# Boot music (bgm_boot)

Evidence: `main.lua` and `sys_boot.lua` of the SNES EUR and Shonen Bases (decompiled with luajit-decompiler), and
`ReedPlayer-Clover` SNES EUR 2.0.14 (decompiled with REA/Ghidra).

## How it plays

- `defaultscene.scn` has a SoundComponent on the `Main` node, linked as `Main.bootBGM`, with the resource
  `/sounds/hvc/bgm_boot.wav`, `autoPlay: false`, `volume: 1`. The same component exists in the HVC, NES, SNES and
  Shonen Bases.
- `Main.update` (`main.lua`) waits for the main music (`resMainBGM`) to load, then when
  `not bootBGM:isPlaying()` (or the sample position went back) it calls `mainBGM:play()` and `bootBGM:disable()`.
- `sys_boot.lua` plays `bootSound` only if that link is set. It is empty in `sys_boot.scn` in both Bases, so the
  boot screen itself plays nothing.

## How the Shonen firmware silences it

Its `Main.start` calls `bootBGM:disable()` before anything else, then runs its own rotation of five tracks. The
other Bases keep the sound and disable it only once the main music starts.

## Engine behaviour that matters

- `SoundComponent:isPlaying` (SNES `FUN_000a75e4`): if the component has no native sound object it returns false,
  with no error.
- Component API: `enable`, `disable`, `setEnabled`, `isEnabled`.

- `SoundComponent:getSamplePosition` (SNES `0xa7340`, read from the disassembly): when the component has no native
  sound object it returns the constant `0.0`, with no error. It is a Lua binding lambda that Ghidra did not define as a
  function.

## Silencing without a dummy WAV

With the component disabled, `Main.update` behaves like this: the first `getSamplePosition` returns 0.0, so
`bgmSamplePosition` is stored as 0.0; `isPlaying` returns false; the condition `not bootBGM:isPlaying()` is true and
`mainBGM:play()` runs at once. Nothing in these paths raises an error. So a scene whose `bootBGM` component is
disabled gives the same result as the Shonen firmware's `bootBGM:disable()`, as far as the code shows.

## Not verified

- That a component loaded with `enabled: false` in the scene has no native sound object (that is when the engine
  creates it was not read), and that nothing re-enables it.
- Nothing was run on a console.
