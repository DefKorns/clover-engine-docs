<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# File formats read by the engine

Source: the loaders of `ReedPlayer-Clover` (SNES EUR 2.0.14 decompiled with REA/Ghidra; NES 1.0.7 and Shonen 3.0.1
compared by key sets). Keys are the JSON names each loader reads. "Optional" means the loader accepts the key being
absent; keys without that note were read without a fallback, which does not prove they are mandatory.

## init.json

| Key | Notes |
|---|---|
| `engineFormat` | **Must equal the number the engine was built for**: NES/HVC = 8, SNES = 9, Shonen = 10. A lower value is rejected with error `0x80660000`, a higher one with `0x80660001`. Checked against the stock `init.json` files: nes/hvc 8, shvc/sneseur 9, hvcj-shonen 10. |
| `defaultScene` | Resource id of the first scene. |
| `luaScripts` | List of script paths. The loader drops the first character of each (the leading `/`). |
| `exportTime`, `buildName` | Optional (fall back to `"Unknown"` / empty). |
| `virtualPlatformRegion` | Optional. |
| `localizationRootPath`, `localizationStringFilePath`, `localePathFormats` | Strings folder, strings file (`strings.json` on NES/HVC, `strings.lng` on SNES and Shonen) and the folder patterns (`<REGION>_<LANGUAGE>`, `jpn_ja`, `usa_en`). |

`worldUnitsPerMeter` and `gravity` are present in the stock `init.json` files; their reader was not located.

An `init.json` from one family is refused by the engine of another: the `engineFormat` does not match.

## dependencies.json

- `resources`: list of `{ id, type, path?, content?, contentType?, groupId, dependencies: [{ id, refCount }] }`.
  Resource types the loader knows: `Resource`, `TextureResource`, `RenderTargetResource`, `CameraCaptureResource`,
  `FontResource`, `SpriteSheet`, `SpriteAnimationResource`, `Scene`, `SceneAnimation`, `SoundResource`,
  `SpriteResource`, `RawResource`.
- `resourceGroups`: list of `{ id, resourceCount, minRefCount }`. The loader reads it; the stock packages ship it empty.
  Not found in the SNES manifest of the packages checked.

## Scene node

`{ id, components: [{ id, type }, ...], children: [...] }`, plus the node base keys `name`, `transform`, `enabled`,
`zIndex`, `category`, `visible`, `color`, and `scriptType` / `properties` for scripts. A script property that links to
another object is `{ scriptTypeVariable | linkType, linkId }`.

## Texture and sprite sheet (the `.json` next to a `.png`)

- Texture: `type`, `format`, `width`, `height`, `mipmapCount`, `keepOnCpuAfterUpload`, under a platform key (`Linux`).
- Sprite sheet: `texture { id, width, height }` and `sprites { <name>: { textureFrame, sourceSize, sourceOffset, pivot } }`.
- A sprite resource: `textureId`, `textureFrame`, `pivot`, `sourceSize`, `sourceOffset`.

## Scene animation tracks

Each track: `worldNodePath`, `componentType`, `propertyId`, `scriptPropertyName`, `scriptPropertySetter`,
`keyCurves: [{ time, value, interp }]`.

- Eleven track loaders exist in the SNES and Shonen engines, one per value type.
- `scriptPropertySetter` exists in the SNES and Shonen engines and **not in the NES one**: only they can drive a
  script property from an animation.

## Strings (`strings.lng`)

`strings`, `modifiers`, `groupName`, `params`, `exploded_strings`, `type`, `text`, `value`, `format`.

## Components

See [scene-components.md](scene-components.md) for the keys per component. The Camera deserializer reads `viewportRect`, `order`,
`clearScreen`, `clearColor`, `categoryMask`, `targetScreen`, `renderTarget`; the Clickable one reads `layer`,
`center`, `clickCallbackComponent`, `shape` and, per shape, `width`, `height` or `radius`.

## Differences between families

- The NES deserializers read `enabled`, `properties` and `scriptType` inside each component; the SNES and Shonen read
  them once in a base.
- The NES node has no `visible` and no `color` key; the NES visual component has no `visible` key.
- Shonen: identical key sets to the SNES for every component.
- Not confirmed: whether the Shonen loaders of nodes, components, sprite sheets and manifest entries read `id` (the
  extraction found it in the SNES one only; it may be an extraction miss).
