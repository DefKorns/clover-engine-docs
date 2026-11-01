<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › Lua API

# Lua API reference

Every class and method the engine exposes to Lua: 40 classes, 436 methods across the SNES, NES and Shonen engines. One page per class; each lists the signature, the families that bind the method and the binding address.

| Class | Methods | S | N | J | Kind |
|---|---|---|---|---|---|
| [AnimatedImageResource](AnimatedImageResource.md) | 1 | 0 | 0 | 1 | instance |
| [AnimatedSpriteComponent](AnimatedSpriteComponent.md) | 16 | 16 | 16 | 16 | instance |
| [AnimatorComponent](AnimatorComponent.md) | 22 | 22 | 22 | 22 | instance |
| [Application](Application.md) | 18 | 13 | 10 | 18 | static |
| [CRC64](CRC64.md) | 1 | 1 | 1 | 1 | static |
| [CameraCaptureResource](CameraCaptureResource.md) | 2 | 0 | 2 | 0 | instance |
| [CameraComponent](CameraComponent.md) | 21 | 17 | 17 | 19 | instance |
| [CameraDevice](CameraDevice.md) | 7 | 0 | 7 | 0 | instance |
| [ClickableComponent](ClickableComponent.md) | 23 | 23 | 23 | 23 | instance |
| [Component](Component.md) | 8 | 8 | 8 | 8 | instance |
| [FileNameUtils](FileNameUtils.md) | 6 | 0 | 0 | 6 | instance |
| [FileUtils](FileUtils.md) | 17 | 17 | 10 | 17 | static |
| [FontResource](FontResource.md) | 3 | 3 | 3 | 3 | instance |
| [ImageResource](ImageResource.md) | 4 | 3 | 3 | 4 | instance |
| [Input](Input.md) | 8 | 7 | 7 | 8 | static |
| [LabelComponent](LabelComponent.md) | 36 | 36 | 36 | 36 | instance |
| [Localization](Localization.md) | 6 | 6 | 6 | 6 | static |
| [MeshComponent](MeshComponent.md) | 5 | 5 | 5 | 5 | instance |
| [Object](Object.md) | 2 | 2 | 2 | 2 | instance |
| [Player](Player.md) | 3 | 0 | 0 | 3 | instance |
| [RawResource](RawResource.md) | 1 | 1 | 1 | 1 | instance |
| [RenderTargetResource](RenderTargetResource.md) | 2 | 2 | 2 | 1 | instance |
| [Resource](Resource.md) | 2 | 2 | 2 | 2 | instance |
| [Scene](Scene.md) | 1 | 1 | 1 | 1 | instance |
| [SceneAnimation](SceneAnimation.md) | 1 | 1 | 1 | 1 | instance |
| [ScriptComponent](ScriptComponent.md) | 1 | 1 | 1 | 1 | instance |
| [SoundComponent](SoundComponent.md) | 36 | 36 | 35 | 36 | instance |
| [SoundListenerComponent](SoundListenerComponent.md) | 1 | 1 | 1 | 1 | instance |
| [SoundResource](SoundResource.md) | 3 | 3 | 3 | 3 | instance |
| [SpriteAnimationResource](SpriteAnimationResource.md) | 1 | 1 | 1 | 1 | instance |
| [SpriteComponent](SpriteComponent.md) | 11 | 11 | 11 | 11 | instance |
| [SpriteResource](SpriteResource.md) | 3 | 3 | 3 | 3 | instance |
| [TextVariable](TextVariable.md) | 3 | 3 | 3 | 3 | instance |
| [TextureComponent](TextureComponent.md) | 19 | 18 | 12 | 19 | instance |
| [TextureResource](TextureResource.md) | 2 | 2 | 2 | 1 | instance |
| [TilemapComponent](TilemapComponent.md) | 7 | 7 | 7 | 7 | instance |
| [VideoComponent](VideoComponent.md) | 18 | 0 | 18 | 0 | instance |
| [VisualComponent](VisualComponent.md) | 31 | 31 | 23 | 31 | instance |
| [Volumes](Volumes.md) | 8 | 0 | 0 | 8 | instance |
| [WorldNode](WorldNode.md) | 76 | 76 | 67 | 76 | instance |

## How to read the tables

- **Signature**: `Class:method(...)` is an instance method (colon call); `Class.method(...)` is a static function of a
  global table. Types come from the helper the binding uses to read an argument or push a result: `number`, `integer`,
  `boolean`, `string`, or a resource class. `any` means that helper was not classified. For NES-only methods the
  signature lists only the argument count.
- **Families**: S = SNES (EUR, USA, SHVC), N = NES and HVC, J = Shonen. A dash means the family does not bind the method.
- **Binding**: address of the binding function in the SNES EUR 2.0.14, NES 1.0.7 and Shonen 3.0.1 builds.
- **Summary**: derived from the method name (getters and setters only); "Not described (name only)" means nothing beyond the name is known. A **Note** was verified in the code or in the stock scripts.
- Parameter names are not in the binary: single-argument setters use the name after `set`, the others are `argN`.


Machine-readable data: [`../lua-api.json`](../lua-api.json).
