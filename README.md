# Clover engine documentation

Reverse engineering notes on the console UI stack of the SNES Classic, NES Classic, Famicom Mini and the Shonen Jump
Famicom Mini: the supervisor `clover-mcp`, the engine `ReedPlayer-Clover`, the UI package formats and the Lua API.

Start with the [Reference](docs/clover-engine-reference.md); it links to every topic below.

## Pages

| Page | What it covers |
|---|---|
| [Reference](docs/clover-engine-reference.md) | The complete reference: architecture, supervisor, formats, components, Lua layer, subsystems. |
| [Supervisor](docs/supervisor.md) | clover-mcp: state machine, settings, game scan, splash and error screens. |
| [File formats](docs/file-formats.md) | init.json, dependencies.json, nodes, textures, animation tracks, strings. |
| [Scene components](docs/scene-components.md) | The keys each component reads from a .scn file. |
| [Lua API](docs/api/README.md) | Every Lua class and method, one page per class. |
| [Boot music](docs/boot-music.md) | How bgm_boot plays and how it can be silenced. |
| [Error C8](docs/c8-error.md) | What the C8 screen is and when it appears. |
| [Family differences](docs/family-differences.md) | SNES, NES and Shonen compared. |
| [Lua toolchain](docs/lua-toolchain.md) | Which LuaJIT reproduces the console bytecode. |
| [About](docs/about.md) | Method, tools and confidence. |

## Reference sections

1. [Architecture](docs/clover-engine-reference.md#1-architecture)
2. [Firmware and families](docs/clover-engine-reference.md#2-firmware-and-families)
3. [Boot and process lifecycle](docs/clover-engine-reference.md#3-boot-and-process-lifecycle)
4. [The supervisor (clover-mcp)](docs/clover-engine-reference.md#4-the-supervisor-clover-mcp)
5. [The UI package: files and formats](docs/clover-engine-reference.md#5-the-ui-package-files-and-formats)
6. [Scene components](docs/clover-engine-reference.md#6-scene-components)
7. [The Lua layer](docs/clover-engine-reference.md#7-the-lua-layer)
8. [Subsystems](docs/clover-engine-reference.md#8-subsystems)
9. [Family differences at a glance](docs/clover-engine-reference.md#9-family-differences-at-a-glance)
10. [Method and confidence](docs/clover-engine-reference.md#10-method-and-confidence)
11. [Open questions](docs/clover-engine-reference.md#11-open-questions)
12. [Appendices](docs/clover-engine-reference.md#12-appendices)

## Lua API classes

[AnimatedImageResource](docs/api/AnimatedImageResource.md) · [AnimatedSpriteComponent](docs/api/AnimatedSpriteComponent.md) · [AnimatorComponent](docs/api/AnimatorComponent.md) · [Application](docs/api/Application.md) · [CRC64](docs/api/CRC64.md) · [CameraCaptureResource](docs/api/CameraCaptureResource.md) · [CameraComponent](docs/api/CameraComponent.md) · [CameraDevice](docs/api/CameraDevice.md) · [ClickableComponent](docs/api/ClickableComponent.md) · [Component](docs/api/Component.md) · [FileNameUtils](docs/api/FileNameUtils.md) · [FileUtils](docs/api/FileUtils.md) · [FontResource](docs/api/FontResource.md) · [ImageResource](docs/api/ImageResource.md) · [Input](docs/api/Input.md) · [LabelComponent](docs/api/LabelComponent.md) · [Localization](docs/api/Localization.md) · [MeshComponent](docs/api/MeshComponent.md) · [Object](docs/api/Object.md) · [Player](docs/api/Player.md) · [RawResource](docs/api/RawResource.md) · [RenderTargetResource](docs/api/RenderTargetResource.md) · [Resource](docs/api/Resource.md) · [Scene](docs/api/Scene.md) · [SceneAnimation](docs/api/SceneAnimation.md) · [ScriptComponent](docs/api/ScriptComponent.md) · [SoundComponent](docs/api/SoundComponent.md) · [SoundListenerComponent](docs/api/SoundListenerComponent.md) · [SoundResource](docs/api/SoundResource.md) · [SpriteAnimationResource](docs/api/SpriteAnimationResource.md) · [SpriteComponent](docs/api/SpriteComponent.md) · [SpriteResource](docs/api/SpriteResource.md) · [TextVariable](docs/api/TextVariable.md) · [TextureComponent](docs/api/TextureComponent.md) · [TextureResource](docs/api/TextureResource.md) · [TilemapComponent](docs/api/TilemapComponent.md) · [VideoComponent](docs/api/VideoComponent.md) · [VisualComponent](docs/api/VisualComponent.md) · [Volumes](docs/api/Volumes.md) · [WorldNode](docs/api/WorldNode.md)

## Sources

The notes are based on the stock firmware images of the three families (SNES Classic, NES Classic / Famicom Mini,
Shonen Jump Famicom Mini) and on the open-source release that Nintendo publishes for the consoles:
[Nintendo Open Source Software](https://support.nintendo.com/jp/oss/index.html) (the pages for the Super NES Classic
Edition, and for the NES Classic Edition and Nintendo Classic Mini Family Computer). From that release the notes use
the exact LuaJIT source the consoles ship (see [Lua toolchain](docs/lua-toolchain.md)) and the names and versions of
the bundled libraries.

## What this repository does not contain

No firmware, no binaries, no decompiled code or pseudocode, and no extracted game or UI assets. The engine and the
firmware belong to Nintendo. The notes describe formats, interfaces and behaviour, and cite function addresses of the
analysed builds as evidence. No license is set.

Machine-readable API data: [`docs/lua-api.json`](docs/lua-api.json).
