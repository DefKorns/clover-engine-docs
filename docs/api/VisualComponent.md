<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › VisualComponent

# VisualComponent

31 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `getAlpha` | `VisualComponent:getAlpha(): number` | SNJ | `adac8 / f7908 / ee128` | Returns the alpha. |
| `getBlendPreset` | `VisualComponent:getBlendPreset(): integer` | SNJ | `ad970 / f8e88 / edfd0` | Returns the blend preset. |
| `getColor` | `VisualComponent:getColor(): (number, number, number, number)` | SNJ | `ae108 / df83c / ee49c` | Returns the color. |
| `getColorB` | `VisualComponent:getColorB(): number` | SNJ | `adce8 / f7784 / ee2c8` | Returns the color b. |
| `getColorG` | `VisualComponent:getColorG(): number` | SNJ | `add50 / f7a8c / ee330` | Returns the color g. |
| `getColorR` | `VisualComponent:getColorR(): number` | SNJ | `addb8 / f7d90 / ee398` | Returns the color r. |
| `getLayer` | `VisualComponent:getLayer(): integer` | SNJ | `ae26c / f8ce0 / ee600` | Returns the layer. |
| `getSelfAlpha` | `VisualComponent:getSelfAlpha(): number` | SJ | `ada60 / - / ee0c0` | Returns the self alpha. |
| `getSelfColor` | `VisualComponent:getSelfColor(): (number, number, number, number)` | SJ | `ae06c / - / ee400` | Returns the self color. |
| `getSelfColorB` | `VisualComponent:getSelfColorB(): number` | SJ | `adbb0 / - / ee190` | Returns the self color b. |
| `getSelfColorG` | `VisualComponent:getSelfColorG(): number` | SJ | `adc18 / - / ee1f8` | Returns the self color g. |
| `getSelfColorR` | `VisualComponent:getSelfColorR(): number` | SJ | `adc80 / - / ee260` | Returns the self color r. |
| `getSize` | `VisualComponent:getSize(): (number, number)` | SNJ | `ad9d4 / df958 / ee034` | Returns the size. |
| `getWorldZIndex` | `VisualComponent:getWorldZIndex(): integer` | SNJ | `ae1a4 / f8b38 / ee538` | Returns the world zindex. |
| `getZIndex` | `VisualComponent:getZIndex(): integer` | SNJ | `ae208 / f8990 / ee59c` | Returns the zindex. |
| `isCulled` | `VisualComponent:isCulled(): boolean` | SNJ | `ad90c / f80d4 / edf6c` | Returns whether culled. |
| `isSelfVisible` | `VisualComponent:isSelfVisible(): boolean` | SJ | `ae2d0 / - / ee664` | Returns whether self visible. |
| `isVisible` | `VisualComponent:isVisible(): boolean` | SJ | `ae334 / - / ee6c8` | Returns whether visible. |
| `setAlpha` | `VisualComponent:setAlpha(alpha: number)` | SNJ | `adb30 / f7484 / eea04` | Sets the alpha. |
| `setBlendPreset` | `VisualComponent:setBlendPreset(blendPreset: integer)` | SNJ | `ae434 / f7c10 / ee760` | Sets the blend preset. |
| `setColor` | `VisualComponent:setColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | `adfa0 / df8bc / eec04` | Sets the color. |
| `setColorB` | `VisualComponent:setColorB(colorB: number)` | SNJ | `ade20 / f7184 / eea84` | Sets the color b. |
| `setColorG` | `VisualComponent:setColorG(colorG: number)` | SNJ | `adea0 / f7604 / eeb04` | Sets the color g. |
| `setColorR` | `VisualComponent:setColorR(colorR: number)` | SNJ | `adf20 / f7304 / eeb84` | Sets the color r. |
| `setFilters` | `VisualComponent:setFilters(arg1: integer, arg2: integer)` | SNJ | `ae560 / 102260 / ee88c` | Sets the filters. |
| `setLayer` | `VisualComponent:setLayer(layer: integer)` | SNJ | `ae7ec / f6b00 / eede4` | Sets the layer. |
| `setSamplerSettings` | `VisualComponent:setSamplerSettings(arg1: integer, arg2: integer, arg3: integer, arg4: integer)` | SNJ | `ae624 / df9e4 / ee950` | Sets the sampler settings. |
| `setVisible` | `VisualComponent:setVisible(visible: boolean)` | SJ | `ae3cc / - / eee60` | Sets the visible. |
| `setWorldZIndex` | `VisualComponent:setWorldZIndex(worldZIndex: integer)` | SNJ | `ae6d8 / f6e38 / eecd0` | Sets the world zindex. |
| `setWrapModes` | `VisualComponent:setWrapModes(arg1: integer, arg2: integer)` | SNJ | `ae49c / 102424 / ee7c8` | Sets the wrap modes. |
| `setZIndex` | `VisualComponent:setZIndex(zIndex: integer)` | SNJ | `ae770 / f6c9c / eed68` | Sets the zindex. |

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

← [VideoComponent](VideoComponent.md) · [Index](README.md) · [Volumes](Volumes.md) →
