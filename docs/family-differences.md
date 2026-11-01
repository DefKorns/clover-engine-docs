<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# SNES, NES and Shonen engines compared

Binaries (all `ReedPlayer-Clover`, ARM 32-bit ELF):

| Family | Firmware | Size | Lua in the binary |
|---|---|---|---|
| SNES EUR | sneseur 2.0.14 | 1 180 280 | LuaJIT 2.0.4 string |
| SNES USA, SHVC | 2.0.14 | 1 180 280 | same size as SNES EUR, different hash |
| NES | nes 1.0.7 | 1 294 004 | |
| HVC (Famicom) | hvc 1.0.5 | 1 291 508 | |
| Shonen (HVCJ) | hvcj 3.0.1 | 1 185 488 | |

Decompiled: all six. SNES USA and SHVC match SNES EUR (identical API, 3053 of 3058 function bodies identical). HVC 1.0.5 has the same Lua API as NES 1.0.7.

## engineFormat

`init.json` must carry the engine's own `engineFormat`: NES and HVC 8, SNES 9, Shonen 10 (any other value is
rejected). The scene animation tracks of the NES engine have no `scriptPropertySetter`; the SNES and Shonen ones do.

## Shared

- The same 15 component types in all three: Animated, AnimatedSprite, Camera, Clickable, Label, Mesh, ParticleSystem,
  Physics, Script, Sound, SoundListener, Texture, Tilemap, Video, Visual.
- The same Lua classes for scenes, nodes and resources (`WorldNode`, `Scene`, `SceneAnimation`, `TextureResource`,
  `SpriteResource`, `SoundResource`, `FontResource`...).
- Same deserializers for the common components (SNES and Shonen: identical key sets).

## Lua API differences

From the binding tables of each engine ([Lua API](api/README.md), 40 classes and 436 methods in total). SNES, SNES USA and SHVC share the
same API, as do NES and HVC.

| Bound in | Count | Methods |
|---|---|---|
| SNES and Shonen | 34 | `Application`: `eventFdRead`, `eventFdWrite`, `skipDraw`; `FileUtils`: `copyDirectory`, `copyDirectoryAsync`, `copyFileAsync`, `createDirectory`, `directoryExists`, `renameDirectory`, `writeFile`; `SoundComponent`: `closeNativeDevice`; `TextureComponent`: `setHeight`, `setTextureOffsetX`, `setTextureOffsetY`, `setTextureRepeatX`, `setTextureRepeatY`, `setWidth`; `VisualComponent`: `getSelfAlpha`, `getSelfColor`, `getSelfColorB`, `getSelfColorG`, `getSelfColorR`, `isSelfVisible`, `isVisible`, `setVisible`; `WorldNode`: `getAlpha`, `getColor`, `getSelfAlpha`, `getSelfColor`, `isSelfVisible`, `isVisible`, `setAlpha`, `setColor`, `setVisible` |
| Shonen only | 30 | `AnimatedImageResource`: `getFrameCount`; `Application`: `abort`, `getErrorHandler`, `getResourcesPath`, `resetErrorHandler`, `setErrorHandler`; `CameraComponent`: `getFrontCameraRenderingAtViewPoint`, `getTargetSize`, `getTargetView`, `setTargetView`; `FileNameUtils`: `concat`, `getBasename`, `getPath`, `getPrefix`, `getPrefixLength`, `normalize`; `ImageResource`: `readPixel`; `Input`: `touchToViewPoint`; `Player`: `getLastLoadResult`, `getListeningPort`, `hasLoadError`; `TextureComponent`: `setCurrentFrame`; `Volumes`: `getBootApplicationPath`, `getPath`, `getSyncApplicationPath`, `getSystemPath`, `getTempPath`, `getUserPath`, `isVolumeMounted`, `mountDataVolume` |
| NES only | 27 | `CameraCaptureResource`: `getCameraSource`, `getPixel`; `CameraDevice`: `getTextureCoordinates`, `isStarted`, `setEffect`, `setFramerate`, `setResolution`, `start`, `stop`; `VideoComponent`: `close`, `create`, `getCurrentTime`, `getCurrentTimeAsSeconds`, `getLength`, `getLengthAsSeconds`, `getState`, `isAutoPlay`, `open`, `pause`, `play`, `resume`, `seek`, `seekAsSeconds`, `setAutoPlay`, `setAutoresize`, `setSize`, `stop` |
| SNES and NES | 4 | `CameraComponent`: `getTargetScreen`, `setTargetScreen`; `RenderTargetResource`: `getPixel`; `TextureResource`: `getPixel` |

Whole classes: `VideoComponent` (18 methods), `CameraDevice` (7) and `CameraCaptureResource` (2) exist only in the NES engine;
`FileNameUtils` (6), `Player` (3), `Volumes` (8) and `AnimatedImageResource` (1) only in the Shonen engine.

## Component keys (deserializers)

Compared function by function (the best-matching deserializer of each engine for every SNES one):

- **Shonen: identical to the SNES** in every component (node base, visual, texture, sprite, animated sprite, label,
  tilemap, animator, clickable, sound, camera, mesh).
- **NES: the same keys, with three differences.**
  - Each NES deserializer reads `scriptType`, `properties` and `enabled` itself and then its visual keys; the SNES and
    Shonen read them once in a base.
  - The NES node base has `transform`, `enabled`, `zIndex` and `category`, but **no `visible` and no `color`**.
  - The NES visual keys have no `visible` (`minFilterMode`, `magFilterMode`, `color`, `layer`, `blendMode` only).
- Label enumerations: `horizontalAnchor` Left, Center, Right; `verticalAnchor` Top, Center, Bottom, Baseline;
  `alignment` Left, Center, Right, Justify (strings in the NES and Shonen engines).

## Supervisor

All three supervisors were decompiled (NES unstripped). Differences, from [supervisor.md](supervisor.md): the NES one has no 20 s
transition timeouts and no `CLOVER GAME CRASHED` message; the SNES and Shonen ones share the timeouts; Shonen adds
`Game.FastTransition`.
