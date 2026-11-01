<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# Clover engine reference

The console UI stack of the SNES Classic, NES Classic, Famicom Mini and the Shonen Jump Famicom Mini: what runs, which
files it reads, which Lua it exposes, and where the three engine families differ.

Status: working reference, kept on disk. Method and confidence are in section 10; open questions in section 11.
Nothing here was run on a console.

## Contents

1. [Architecture](#1-architecture)
2. [Firmware and families](#2-firmware-and-families)
3. [Boot and process lifecycle](#3-boot-and-process-lifecycle)
4. [The supervisor (clover-mcp)](#4-the-supervisor-clover-mcp)
5. [The UI package: files and formats](#5-the-ui-package-files-and-formats)
6. [Scene components](#6-scene-components)
7. [The Lua layer](#7-the-lua-layer)
8. [Subsystems](#8-subsystems)
9. [Family differences at a glance](#9-family-differences-at-a-glance)
10. [Method and confidence](#10-method-and-confidence)
11. [Open questions](#11-open-questions)
12. [Appendices](#12-appendices)

---

## 1. Architecture

Three layers run on the console (ARM 32-bit Linux):

```
clover-mcp               supervisor: display, games, lifecycle, error screens
   |  starts / waits on
   v
ReedPlayer-Clover        the engine: scene graph, components, resources, Lua VM
   |  loads
   v
UI package (resources/)  scenes, sprites, sounds, strings, Lua scripts: the part that defines the menu
```

- **Supervisor.** Reads `clover-mcp.desktop`, scans the games and writes the title list for the menu, starts the
  menu or a game as a child process, and shows splash and error screens (section 4).
- **Engine.** `ReedPlayer-Clover`, about 1.2 MB. A node tree with components (textures, labels, sounds, animations),
  a resource manager driven by `dependencies.json`, and an embedded LuaJIT 2.0.4 that runs the UI scripts
  (sections 5 to 7). It runs the menu UI and the games' own front-ends alike.
- **UI package.** The files under `/usr/share/ui/<name>` (for example `snes-eur`, `hvc`): `init.json`, the scenes,
  `dependencies.json`, sprites, sounds, strings and the compiled Lua.

The supervisor and the engine communicate through a command file and a state file, plus eventfds for the
menu to game transitions (`Settings.CommandFile`, `Settings.StateFile`).

## 2. Firmware and families

Engine binaries analysed (`/usr/bin/ReedPlayer-Clover`), all ARM 32-bit ELF:

| Family | Firmware | Engine size | `engineFormat` | Decompiled |
|---|---|---|---|---|
| SNES EUR | sneseur 2.0.14 | 1 180 280 | 9 | yes |
| SNES USA | snesusa 2.0.14 | 1 180 280 | 9 | yes: API identical to EUR, 3053 of 3058 function bodies identical |
| SHVC (Super Famicom) | shvc 2.0.14 | 1 180 280 | 9 | yes: API identical to EUR, 3053 of 3058 function bodies identical |
| NES | nes 1.0.7 | 1 294 004 | 8 | yes |
| HVC (Famicom) | hvc 1.0.5 | 1 291 508 | 8 | yes: API identical to NES 1.0.7 (the code layout is shifted, so bodies were not compared by address) |
| Shonen (HVCJ) | hvcj 3.0.1 | 1 185 488 | 10 | yes |

The firmware images carry the matching revision ids (`/etc/clover/version/*`): for sneseur 2.0.14 the engine
(`reedplayer_revid`) is `69e60d8fbe15f5c000c06464930eb5f4f0e37ade` and the UI (`snes-eur-menu_revid`)
`e1ee74b8c5a6a8984fed227d6ce97ac7593f2033`.

Three engine generations exist, identified by `engineFormat` (section 5.1). The NES and HVC engines are format 8, the
SNES and SHVC ones format 9, the Shonen one format 10. Each engine accepts only its own number.

## 3. Boot and process lifecycle

1. The supervisor starts (`executeStartup`): reads settings, opens the framebuffer and display device, shows the
   startup splash, scans the games folder and writes `menu.titles.lua`.
2. It starts the menu: the engine runs the UI package's `init.json` default scene and its Lua. The UI's `sys_boot`
   script builds the boot screen, loads fonts and textures, and hands over to the `Main` scene.
3. In the menu, the user picks a game. The menu writes a command; the supervisor stops the menu, starts the game and
   waits. On the way back it starts the menu again.
4. In the SNES and Shonen supervisors the two transitions (menu to game, game to menu) wait up to 20 s on an eventfd.
5. Failures draw a full-screen splash and wait (section 4.5).

### UI boot sequence (Lua)

- `sys_boot.lua`: `start` sets `sys_boot.instance`, plays `bootSound` if linked, and shows the error dialogs for
  `TITLE_RETURN_CODE` (previous game crashed, suspend point unusable, rewind corrupted...); it also provides
  `loadFont`.
- `main.lua`: loads the main music (`resMainBGM`); while the boot music (`Main.bootBGM`) plays it waits, then starts
  `mainBGM` and disables `bootBGM` (section 8.1).

## 4. The supervisor (clover-mcp)

Sources: SNES EUR 2.0.14 (stripped), NES 1.0.7 (**unstripped**, 79 functions named `nerd::clover::*`) and Shonen
3.0.1 (stripped). The NES names label the SNES and Shonen code by matching their messages.

### 4.1 State machine

| Handler | Purpose |
|---|---|
| `executeStartup` | Settings, display, game scan. Failure: "UNABLE TO INITIALIZE SYSTEM". |
| `executeCheckEnableTest`, `executeCheckSelectStart`, `executeWaitForKeyCombo` | Boot key combos (test menu, reset). |
| `executeStartMenu`, `executeMenuRunning`, `executeMenuCommand`, `executeMenuShutdown`, `executeMenuFailure` | Menu lifecycle and its commands. |
| `executeStartGame`, `executeResumeGame`, `executeStartSuperPlay` | Launch a game, resume a suspend point, Super Play. |
| `executeGameRunning`, `executeGameReset`, `executeGameShutdown`, `executeGameFailure` | Game lifecycle. |
| `executeStartTestMenu`, `executeTestMenuRunning`, `executeFactoryReset` | Test menu and factory reset. |
| `executeStartupFailure`, `executeGeneralFailure`, `executeShutdown` | Error screens and power-off. |

SNES EUR addresses: startup and game scan `FUN_0001e290`, start menu `FUN_0001d948`, start game `FUN_0001ae98`, resume
game `FUN_0001b570`, menu command `FUN_0001c210`, the loop `FUN_00017860`.

### 4.2 Settings (`clover-mcp.desktop`)

| Key | SNES | NES | Shonen |
|---|---|---|---|
| `Settings.GamesFolder`, `MenuLuaFile`, `StateFile`, `CommandFile` | x | x | x |
| `Settings.SaveGameVolatilePath`, `SaveGameVolatileBackupPath` | x | x | x |
| `Settings.DefaultLangFile`, `UserLangFile` | x | x | x |
| `Settings.DefaultAutoShutdownDelay`, `UserAutoShutdownDelayFile` | x | x | x |
| `Settings.DefaultDimmingDelay`, `UserDimmingDelayFile` | x | - | x |
| `Settings.MenuDesktop`, `TestMenuDesktop`, `FactoryResetDesktop`, `MenuResetDesktop` | x | x | x |
| `Settings.FramebufferPath`, `DispDevPath`, `MenuResolution`, `GameResolution`, `SplashResolution` | x | x | x |
| `Settings.SplashStartup` | x | - | x |
| `Settings.SplashShutdown` | x | x | x |
| `Settings.DaemonMode`, `DebugMode` | x | x | x |
| `Settings.GUI` | x | - | x |
| `Settings.GamesListFile`, `GamesTitleFont`, `CopyrightFont`, `SaveGamePersistentPath`, `DebugMenuDesktop` | - | x | - |
| `Errors.Unknown`, `Errors.StartupFailed` (one per locale, e.g. `Unknown[de_EUR]`) | x | x | x |

Per game (`<game>/<game>.desktop`): `Desktop Entry.Name`, `Desktop Entry.Icon`, `Game.Players`, `Game.Simultaneous`,
`Game.ReleaseDate`, `Game.SaveCount`, `Game.Copyright`, `Game.SortRawTitle`, `Game.SortRawPublisher`, `Game.TestID`.
SNES and Shonen add `Game.Status` and `Game.MyPlayDemoTime`; Shonen adds `Game.FastTransition`.

### 4.3 The game scan

In `executeStartup`: `opendir(GamesFolder)`; for each sub-directory not starting with `.`, parse
`<dir>/<dir>.desktop` as INI, check for `pixelart/<name>.png`, `autoplay/<name>.inputs` and
`superplay/<name>.inputs`, replace `-` by `_` in the id, and emit one entry of `titles_list = { ... }` into
`MenuLuaFile` (`/var/cache/clover/menu.titles.lua`). The scan has no time limit of its own.

### 4.4 Timeouts

SNES and Shonen: the menu to game and game to menu transitions wait on an eventfd with `select()` for 20 000 000 µs
(20 s) (`FUN_0001d710(fd, 20000000)` in SNES `0x17860`, at two places; `FUN_0001dce0` in Shonen `0x17d40`). Expiry
records `MENU TO GAME TRANSITION TIMEOUT` or `GAME TO MENU TRANSITION TIMEOUT`. The NES supervisor has no such wait (its
2 000 000 000 ns values are 2 s shutdown timeouts).

### 4.5 Error screens

Every error screen is a full-screen LZ4 image, listed per locale in `[X-CLOVER Errors]`: a raw 1280x720 BGRA
framebuffer of 3 686 400 bytes after decompression.

| Image | Reads (SNES EUR) | Shown by |
|---|---|---|
| `Errors.StartupFailed` | C1 | `executeStartup`; in the SNES build also the start-menu handler |
| `Errors.Unknown` | **C8** | `executeMenuRunning`, `executeMenuShutdown`, `executeMenuCommand`, `executeGameReset`, `executeGameShutdown`, `executeTestMenuRunning`; in the SNES build also start-game and resume-game |

The assignment (`Settings.Unknown` or `Settings.StartupFailed` copied into the splash path) was read in the NES build
(Machine `+0x178` from `+0xa0` / `+0xa4`) and in the SNES start-up, start-game and resume-game handlers
(`+0xdc` / `+0xe0`). The splash source of the inlined running and shutdown states in the SNES `FUN_00017860` was not
resolved; by the NES layout it is `Errors.Unknown`.

Failure messages (stderr, `FATAL ERROR: ...`): `CLOVER GAME CRASHED` (also `DURING RESET`, `DURING SHUTDOWN`),
`CLOVER MENU CRASHED` (also `DURING SHUTDOWN`), `CLOVER TEST MENU CRASHED`, `GAME TO MENU TRANSITION TIMEOUT`,
`MENU TO GAME TRANSITION TIMEOUT`, `INVALID SETTINGS`, `UNABLE TO INITIALIZE SYSTEM`, `UNABLE TO RESUME CLOVER GAME`,
`UNABLE TO START CLOVER GAME`, `UNABLE TO START CLOVER MENU`, `UNABLE TO START CLOVER SUPER PLAY`,
`UNABLE TO START CLOVER TEST MENU`, `UNKNOWN CLOVER MENU COMMAND`, `WILD UNKNOWN ERROR APPEARED`. The NES supervisor
lacks `CLOVER GAME CRASHED` and the two `TRANSITION TIMEOUT` messages.

The other error codes belong to the Lua UI (`sys_error_*` in `strings/*/strings.lng`): C2 menu settings reset, C4
suspend point could not be stored, C6 suspend point unusable, C7 game crash, C9 rewind data corrupted. `C8` is the
supervisor's `Errors.Unknown` image; the key `sys_error_Unexcepted` is not used by any UI script.

## 5. The UI package: files and formats

### 5.1 `init.json`

| Key | Notes |
|---|---|
| `engineFormat` | Must equal the engine's number: NES/HVC 8, SNES/SHVC 9, Shonen 10. Lower is rejected with `0x80660000`, higher with `0x80660001`. Checked against the stock `init.json` files: nes and hvc 8, shvc and sneseur 9, hvcj-shonen 10. |
| `defaultScene` | Resource id of the first scene. |
| `luaScripts` | Script paths; the loader drops the first character of each (the leading `/`). |
| `exportTime`, `buildName` | Optional (default `"Unknown"` / empty). |
| `virtualPlatformRegion` | Optional. |
| `localizationRootPath`, `localizationStringFilePath`, `localePathFormats` | Strings folder, strings file (`strings.json` on NES/HVC, `strings.lng` on SNES and Shonen) and folder patterns (`<REGION>_<LANGUAGE>`, `jpn_ja`, `usa_en`). |

`worldUnitsPerMeter` and `gravity` appear in the stock `init.json` files; their reader was not located. Copying an `init.json`
between families is refused because of `engineFormat`.

### 5.2 `dependencies.json`

- `resources`: `{ id, type, path?, content?, contentType?, groupId, dependencies: [{ id, refCount }] }`.
  Types: `Resource`, `TextureResource`, `RenderTargetResource`, `CameraCaptureResource`, `FontResource`,
  `SpriteSheet`, `SpriteAnimationResource`, `Scene`, `SceneAnimation`, `SoundResource`, `SpriteResource`, `RawResource`.
- `resourceGroups`: `{ id, resourceCount, minRefCount }`. Read by the engine; empty in the stock packages checked.

### 5.3 Scene node

`{ id, components: [{ id, type }], children: [...] }` plus the node keys `name`, `transform`, `enabled`, `zIndex`,
`category`, `visible`, `color`, and for scripts `scriptType` and `properties`. A script property that links another
object is `{ linkType, linkId }` (or `scriptTypeVariable`).

### 5.4 Textures and sprite sheets (the `.json` next to a `.png`)

- Texture: `type`, `format`, `width`, `height`, `mipmapCount`, `keepOnCpuAfterUpload`, under a platform key (`Linux`).
- Sprite sheet: `texture { id, width, height }`, `sprites { <name>: { textureFrame, sourceSize, sourceOffset, pivot } }`.
- Sprite resource: `textureId`, `textureFrame`, `pivot`, `sourceSize`, `sourceOffset`.

### 5.5 Scene animation tracks

`worldNodePath`, `componentType`, `propertyId`, `scriptPropertyName`, `scriptPropertySetter`,
`keyCurves: [{ time, value, interp }]`. There is one loader per value type (eleven in SNES and Shonen).
`scriptPropertySetter` exists in the SNES and Shonen engines and **not in the NES one**: only they can animate a
script property.

### 5.6 Strings (`strings.lng`)

`strings`, `modifiers`, `groupName`, `params`, `exploded_strings`, `type`, `text`, `value`, `format`.

## 6. Scene components

Fifteen component types exist in all three engines. Keys each deserializer reads (SNES EUR; Shonen has the same key
sets; the NES has the same keys except that its nodes lack `visible` and `color`, its visual component lacks `visible`,
and it reads `enabled`, `properties` and `scriptType` inside each component instead of once in a base):

| Component | Keys |
|---|---|
| Node base | `name`, `transform`, `enabled`, `zIndex`, `category`, `visible`, `color` |
| Visual | `minFilterMode`, `magFilterMode`, `visible`, `color`, `layer`, `blendMode` |
| Texture | `textureId`, `size`, `pivot`, `uvOffset`, `uvRepeat`, `horizontalWrapMode`, `verticalWrapMode` |
| Sprite | `spriteId`, `size`, `hFlip`, `vFlip` |
| AnimatedSprite | `animation`, `looped`, `hFlip`, `vFlip` |
| Label | `text`, `fontResource`, `wordWrap`, `wrapWidth`, `horizontalAnchor`, `verticalAnchor`, `alignment`, `gradientcolortop`, `gradientcolorbottom`, `monospaced`, `has_shadow`, `shadowcolor`, `shadowoffsetx`, `shadowoffsety` |
| Tilemap | `spriteSheet`, `tileWidthScreen`, `tileHeightScreen`, `tileWidthTexture`, `tileHeightTexture`, `tileGridWidth`, `tileGridHeight`, `tiles` |
| Animator | `animation`, `looped`, `time`, `speed`, `listener` |
| Clickable | `layer`, `center`, `clickCallbackComponent`, `shape` (then `width`/`height` or `radius`) |
| Sound | `soundId`, `loop`, `volume`, `pitch`, `priority`, `pan`, `autoPlay`, `positional`, `minDistance`, `maxDistance`, `stopWhenDisabled` |
| Camera | `viewportRect`, `order`, `clearScreen`, `clearColor`, `categoryMask`, `targetScreen`, `renderTarget` |
| Mesh | `horizontalWrapMode`, `verticalWrapMode`, `textureId` (triangles set from Lua) |
| Script | `scriptType`, `properties` |
| Particle, Physics, SoundListener, Video | no keys beyond the base were found |

`colorName` on a label is not read by the engine: it is a script property resolved in `colors_*.lua`.

## 7. The Lua layer

### 7.1 Bytecode

The scripts are LuaJIT 2.0 bytecode version 1, stripped (`1b 4c 4a 01 02`). The engine reports LuaJIT 2.0.4.

| Compiler | Reproduces the console's `colors_eur.lua` |
|---|---|
| LuaJIT 2.0.2 (Windows `luajit.exe`) | yes, byte for byte (`-b` and `-bs`) |
| LuaJIT `v2.0` at `592f9e3f5...` or `2410b57fd...`, `-bs`, Linux x64 | no (1454 bytes against 1051); same output as each other |

One file was tested. Whether the larger bytecode loads on a console was not tested.

### 7.2 API exposed by the engine

40 classes and 436 methods across the three engines; the full reference, with the signature of each method and the
families that bind it, is in [Lua API](api/README.md) (one page per class). The core of it:

| Class | Role |
|---|---|
| `WorldNode` (76 methods) | Tree navigation, transform, visibility, alpha and colour, components. |
| `Component` | `enable`, `disable`, `setEnabled`, `isEnabled`, `getNode`, `getTypeName`. |
| `SoundComponent` (34) | `play`, `pause`, `stop`, `isPlaying`, `getSamplePosition`, `setSoundResource`, volume, pitch, pan, loop. |
| `LabelComponent` (36), `TextureComponent` (18), `SpriteComponent`, `AnimatedSpriteComponent`, `TilemapComponent`, `MeshComponent`, `CameraComponent`, `ClickableComponent`, `AnimatorComponent`, `VisualComponent` | The visual components. |
| `Scene`, `SceneAnimation`, `Resource`, `TextureResource`, `SpriteResource`, `SoundResource`, `FontResource`, `ImageResource`, `RawResource` | Resources. |
| `Localization`, `TextVariable` | Strings. |
| `Application`, `Input`, `FileUtils`, `CRC64`, `Object` | System. |

Calling a method on a null native object raises `Lua object pointer is NULL!`; a wrong argument count raises
`Wrong number of parameters! Got %d, expected %d.`

### 7.3 Globals

`REED_FINAL`, `REED_DEBUG`, `HOST_PLATFORM_IS_LINUX`, and the `PLATFORM_IS_*` family (3DS, Wii U, Windows, Linux,
Android, OSX, iOS) are set by the engine before the scripts run. `TITLE_RETURN_CODE` is passed by the supervisor
(its strings include `--title-code` and `TITLE_RETURN_CODE=`).

## 8. Subsystems

### 8.1 Boot music (`bgm_boot`)

- `defaultscene.scn` has a `SoundComponent` on `Main`, linked as `Main.bootBGM`: `/sounds/hvc/bgm_boot.wav`,
  `autoPlay: false`, `volume: 1`. It is identical in the HVC, NES, SNES and Shonen stock UI packages.
- `Main.update` waits for the main music to load; when `not bootBGM:isPlaying()` (or the sample position went back) it
  calls `mainBGM:play()` and `bootBGM:disable()`.
- `sys_boot.lua` plays `bootSound` only if linked; the link is empty in `sys_boot.scn` in both packages checked.
- The Shonen firmware calls `bootBGM:disable()` at the start of `Main.start`.
- Engine behaviour on a component with no native sound object (SNES): `isPlaying` returns false and
  `getSamplePosition` returns `0.0`, neither raises an error. A scene with `bootBGM` disabled therefore gives the same
  result as the Shonen `disable()` call, as far as the code shows.

### 8.2 Palettes (`colors_*.lua`)

Compiled Lua tables `colors_<region> = { <name> = { r, g, b, a }, ... }` (`eur`, `usa`, `jpn`). Scripts and labels refer
to a colour by name (`colorName`).

### 8.3 Animations

Scene animations drive node properties (position, scale, texture, visibility) with key curves. In the SNES and Shonen
engines a track may call a script property setter; the NES engine has no such track.

## 9. Family differences at a glance

| Area | NES / HVC | SNES / SHVC | Shonen |
|---|---|---|---|
| `engineFormat` | 8 | 9 | 10 |
| Strings file | `strings.json` | `strings.lng` | `strings.lng` |
| Animation tracks with script property setters | no | yes | yes |
| Component key reading | `enabled`, `properties`, `scriptType` per component | in a base | in a base |
| Node keys `visible`, `color`; visual key `visible` | no | yes | yes |
| Supervisor transition timeouts (20 s) | none | yes | yes |
| Supervisor `Game.Status`, `MyPlayDemoTime`, dimming settings | no | yes | yes |
| `Game.FastTransition` | no | no | yes |
| `Application.eventFdRead/Write`, `skipDraw` | no | yes | yes |
| `FileUtils` write, copy, create, rename directory | no | yes | yes |
| `TextureComponent.setWidth/Height/TextureOffset/Repeat` | no | yes | yes |
| `VisualComponent` / `WorldNode` visibility, self colour and alpha | no | yes | yes |
| `SoundComponent.closeNativeDevice` | no | yes | yes |
| `CameraComponent.getTargetScreen`, `setTargetScreen` | yes | yes | no |
| `VideoComponent`, `CameraDevice`, `CameraCaptureResource` classes | yes | no | no |
| `FileNameUtils`, `Player`, `Volumes`, `AnimatedImageResource` classes, `Input.touchToViewPoint` | no | no | yes |

SNES EUR and USA are the same engine: identical API, 3053 of 3058 function bodies identical.

## 10. Method and confidence

- **Binaries.** `/usr/bin/ReedPlayer-Clover` and `/usr/bin/clover-mcp` from the stock `.hsqs` images.
- **Decompilation.** REA 6.8.0 with Ghidra 12.1.4 (Docker `rea-agent-ghidra`, offline). Function names are mostly
  `FUN_xxxx`, except the NES supervisor (unstripped). Disassembly with Capstone where Ghidra did not define a function
  (the Lua binding lambdas).
- **Lua.** `luajit-decompiler-v2` on the UI scripts; they are stripped, so locals are `slotN`.
- **Matching across families.** Key sets of the deserializers and the names of Lua methods were compared as strings;
  a method name present in a binary does not prove it is bound to the same class.
- **Confidence.** Confirmed: sections 4.1 to 4.4 (NES names, SNES by message), 5.1, 5.2, 5.5, 6 (SNES), 8.1 engine
  behaviour. Inferred or partial: the splash choice in the SNES inlined states, the Shonen `id` handling, components
  without keys.

## 11. Open questions

- Which process writes the eventfds that the 20 s wait watches, and what the menu does during those 20 s.
- The splash source of the SNES inlined running and shutdown states (by the NES layout: `Errors.Unknown`).
- Whether a component loaded with `enabled: false` in the scene has no native sound object, and that nothing
  re-enables it (section 8.1); not tested on a console.
- Whether the larger bytecode of recent LuaJIT builds loads on a console; the reader of `worldUnitsPerMeter` and
  `gravity`; the component that reads the `stream` boolean.

## 12. Appendices

- [Lua API](api/README.md): every class and method with its signature and the families that bind it, one page per class.
- [scene-components.md](scene-components.md), [file-formats.md](file-formats.md), [supervisor.md](supervisor.md), [boot-music.md](boot-music.md), [c8-error.md](c8-error.md), [family-differences.md](family-differences.md),
  [lua-toolchain.md](lua-toolchain.md): the topic pages this reference condenses.
