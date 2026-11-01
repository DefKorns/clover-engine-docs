<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › ClickableComponent

# ClickableComponent

23 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `create` | `ClickableComponent:create(...)` | SNJ | `a8cd8 / 115190 / e9040` | Not described (name only). |
| `getAutoRaycastMask` | `ClickableComponent:getAutoRaycastMask(...): number` | SNJ | `a891c / b46f0 / e8c84` | Returns the auto raycast mask. |
| `getBoxShapeSize` | `ClickableComponent:getBoxShapeSize(): (number, number)` | SNJ | `a9050 / f9f74 / e9354` | Returns the box shape size. |
| `getCenter` | `ClickableComponent:getCenter(): (number, number)` | SNJ | `a91ec / fa110 / e94f0` | Returns the center. |
| `getCircleShapeRadius` | `ClickableComponent:getCircleShapeRadius(): number` | SNJ | `a8f74 / fd1e0 / e9278` | Returns the circle shape radius. |
| `getClickListener` | `ClickableComponent:getClickListener()` | SNJ | `a8efc / fcae0 / e9200` | Returns the click listener. |
| `getLayer` | `ClickableComponent:getLayer(): integer` | SNJ | `a9534 / fdf50 / e98a0` | Returns the layer. |
| `getShapeType` | `ClickableComponent:getShapeType(): integer` | SNJ | `a9408 / fe0f8 / e9774` | Returns the shape type. |
| `getWorldZIndex` | `ClickableComponent:getWorldZIndex(): integer` | SNJ | `a946c / fe2a0 / e97d8` | Returns the world zindex. |
| `getZIndex` | `ClickableComponent:getZIndex(): integer` | SNJ | `a94d0 / fdda8 / e983c` | Returns the zindex. |
| `hitTest` | `ClickableComponent:hitTest(arg1: number, arg2: number): boolean` | SNJ | `a8df4 / d49fc / e9160` | Not described (name only). |
| `raycastAll` | `ClickableComponent:raycastAll(arg1: number): array` | SNJ | `a8ab8 / 10657c / e8e20` | Not described (name only). |
| `raycastAllInCategories` | `ClickableComponent:raycastAllInCategories(arg1: number, arg2: number): array` | SNJ | `a8964 / 106dd8 / e8ccc` | Not described (name only). |
| `raycastNearest` | `ClickableComponent:raycastNearest(arg1: number)` | SNJ | `a8be4 / c309c / e8f4c` | Not described (name only). |
| `raycastNearestInCategories` | `ClickableComponent:raycastNearestInCategories(arg1: number, arg2: number)` | SNJ | `a8d5c / c2ee0 / e90c8` | Not described (name only). |
| `setAutoRaycastMask` | `ClickableComponent:setAutoRaycastMask()` | SNJ | `a88c8 / e85d8 / e8c30` | Sets the auto raycast mask. |
| `setBoxShape` | `ClickableComponent:setBoxShape(arg1: number, arg2: number)` | SNJ | `a90cc / faa94 / e93d0` | Sets the box shape. |
| `setCenter` | `ClickableComponent:setCenter(arg1: number, arg2: number)` | SNJ | `a9160 / f97f0 / e9464` | Sets the center. |
| `setCircleShape` | `ClickableComponent:setCircleShape(circleShape: number)` | SNJ | `a8fdc / fc5d8 / e92e0` | Sets the circle shape. |
| `setClickListener` | `ClickableComponent:setClickListener(clickListener: any)` | SNJ | `a8e94 / f9994 / e970c` | Sets the click listener. |
| `setLayer` | `ClickableComponent:setLayer(layer: integer)` | SNJ | `a9380 / fb45c / e9684` | Sets the layer. |
| `setWorldZIndex` | `ClickableComponent:setWorldZIndex(worldZIndex: integer)` | SNJ | `a9260 / fadb8 / e9564` | Sets the world zindex. |
| `setZIndex` | `ClickableComponent:setZIndex(zIndex: integer)` | SNJ | `a92f8 / fb7b8 / e95fc` | Sets the zindex. |

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

← [CameraDevice](CameraDevice.md) · [Index](README.md) · [Component](Component.md) →
