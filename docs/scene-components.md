<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# Scene components (.scn)

Source: the component deserializers of `ReedPlayer-Clover` (SNES EUR 2.0.14, decompiled with REA/Ghidra). Each one reads
JSON keys into fields of the component. Types come from the helper each call uses (bool, float, int, resource id).
The key names were read from the strings in the data section.

The same 15 component types exist in the SNES, NES and Shonen engines; see [family-differences.md](family-differences.md).

| Component | Keys read by the engine |
|---|---|
| Node base (shared by nodes) | `name`, `transform`, `enabled`, `zIndex`, `category`, `visible`, `color` |
| VisualComponent | `minFilterMode`, `magFilterMode`, `visible`, `layer`, `blendMode` |
| TextureComponent | `textureId`, `size`, `pivot`, `uvOffset`, `uvRepeat`, `horizontalWrapMode`, `verticalWrapMode` (plus the visual keys) |
| SpriteComponent | `spriteId`, `size`, `hFlip`, `vFlip` |
| AnimatedSpriteComponent | `animation`, `looped`, `hFlip`, `vFlip` |
| LabelComponent | `text`, `fontResource`, `wordWrap`, `wrapWidth`, `horizontalAnchor`, `verticalAnchor`, `alignment`, `gradientcolortop`, `gradientcolorbottom`, `monospaced`, `has_shadow`, `shadowcolor`, `shadowoffsetx`, `shadowoffsety` (`colorName` lives in the node `properties`, read by Lua) |
| TilemapComponent | `spriteSheet`, `tileWidthScreen`, `tileHeightScreen`, `tileWidthTexture`, `tileHeightTexture`, `tileGridWidth`, `tileGridHeight`, `tiles` |
| AnimatorComponent | `animation`, `looped`, `time`, `speed`, `listener` |
| ClickableComponent | `layer`, `center`, `clickCallbackComponent`, `shape` (then `width`/`height` or `radius`) |
| SoundComponent | `soundId`, `loop`, `volume`, `pitch`, `priority`, `pan`, `autoPlay`, `positional`, `minDistance`, `maxDistance`, `stopWhenDisabled` |
| MeshComponent | `horizontalWrapMode`, `verticalWrapMode`, `textureId` (the triangles are set from Lua with `setTriangles`) |
| CameraComponent | `viewportRect`, `order`, `clearScreen`, `clearColor`, `categoryMask`, `targetScreen`, `renderTarget` |

Component base: `enabled`. `ScriptComponent` reads `scriptType` and `properties`. `ParticleSystemComponent`,
`PhysicsComponent`, `SoundListenerComponent` and `VideoComponent` have no deserializer keys of their own beyond the base
(a `stream` boolean is read by one more component whose type was not identified).

## Notes

- `colorName` on a label is not read by the engine: it is a property the Lua scripts look up in the palette
  (`colors_*.lua`).
- The engine does not mention `needs_overlay` as a string. It is not part of the engine or of the firmware: it is a
  marker file read by the theme selector (an hmod), which uses it to know that a theme must be applied with an
  overlay filesystem instead of a bind mount of its `resources`.
- A SoundComponent that is disabled has no native sound object: `isPlaying` returns false instead of raising an
  error (see [boot-music.md](boot-music.md)).
