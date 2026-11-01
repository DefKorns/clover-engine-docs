<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › WorldNode

# WorldNode

76 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `addChildNode` | `WorldNode:addChildNode(arg1: any): number` | SNJ | `b1730 / f6110 / eff18` | Not described (name only). |
| `addHierarchyToNode` | `WorldNode:addHierarchyToNode(arg1: any): number` | SNJ | `af458 / f5cb0 / efdb4` | Not described (name only). |
| `addHierarchyToRoot` | `WorldNode:addHierarchyToRoot(): number` | SNJ | `af4d0 / dbe50 / efe2c` | Not described (name only). |
| `attachComponent` | `WorldNode:attachComponent(arg1: any): number` | SNJ | `b13ac / f326c / f1c24` | Not described (name only). |
| `attachToWorld` | `WorldNode:attachToWorld(): number` | SNJ | `af53c / dc0d8 / efe98` | Not described (name only). |
| `create` | `WorldNode:create(...)` | SNJ | `b19c8 / 115450 / f2124` | Not described (name only). |
| `destroy` | `WorldNode:destroy()` | SNJ | `af8b8 / dc4d8 / f02a4` | Not described (name only). |
| `detachComponent` | `WorldNode:detachComponent(arg1: any): number` | SNJ | `b10ec / f6880 / f19d4` | Not described (name only). |
| `detachFromWorld` | `WorldNode:detachFromWorld(): number` | SNJ | `af3cc / dbf78 / efd2c` | Not described (name only). |
| `disable` | `WorldNode:disable()` | SNJ | `b0d90 / ddfb4 / f1678` | Not described (name only). |
| `enable` | `WorldNode:enable()` | SNJ | `b0df0 / de0a0 / f16d8` | Not described (name only). |
| `getAllComponents` | `WorldNode:getAllComponents(): array` | SNJ | `b0ec8 / 1068b4 / f17b0` | Returns the all components. |
| `getAlpha` | `WorldNode:getAlpha(): number` | SJ | `aeb88 / - / ef394` | Returns the alpha. |
| `getCategory` | `WorldNode:getCategory(): integer` | SNJ | `aee84 / dc3b0 / ef690` | Returns the category. |
| `getChildByName` | `WorldNode:getChildByName(arg1: any)` | SNJ | `b1688 / debd4 / f1ca8` | Returns the child by name. |
| `getColor` | `WorldNode:getColor(): (number, number, number, number)` | SJ | `aec94 / - / ef4a0` | Returns the color. |
| `getComponent` | `WorldNode:getComponent(arg1: any)` | SNJ | `b1024 / de8b4 / f190c` | Returns the component. |
| `getComponents` | `WorldNode:getComponents(arg1: any): array` | SNJ | `b0f28 / 106a30 / f1810` | Returns the components. |
| `getFirstChildNode` | `WorldNode:getFirstChildNode()` | SNJ | `b1550 / df2f4 / f1e70` | Returns the first child node. |
| `getLastChildNode` | `WorldNode:getLastChildNode()` | SNJ | `b14f0 / df250 / f1e10` | Returns the last child node. |
| `getLocalPosition` | `WorldNode:getLocalPosition(): (number, number)` | SNJ | `af2c4 / dd5f8 / efad0` | Returns the local position. |
| `getLocalPositionX` | `WorldNode:getLocalPositionX(): number` | SNJ | `af258 / dd590 / efa64` | Returns the local position x. |
| `getLocalPositionY` | `WorldNode:getLocalPositionY(): number` | SNJ | `af1ec / dd528 / ef9f8` | Returns the local position y. |
| `getLocalRotation` | `WorldNode:getLocalRotation(): number` | SNJ | `af180 / dd38c / ef98c` | Returns the local rotation. |
| `getLocalScale` | `WorldNode:getLocalScale(): (number, number)` | SNJ | `af100 / dd0d0 / ef90c` | Returns the local scale. |
| `getLocalScaleX` | `WorldNode:getLocalScaleX(): number` | SNJ | `af094 / dd068 / ef8a0` | Returns the local scale x. |
| `getLocalScaleY` | `WorldNode:getLocalScaleY(): number` | SNJ | `af028 / dd000 / ef834` | Returns the local scale y. |
| `getLocalTransform` | `WorldNode:getLocalTransform(): (number, number, number, number, number, number)` | SNJ | `b0b64 / ddd94 / f08c8` | Returns the local transform. |
| `getName` | `WorldNode:getName()` | SNJ | `af7e4 / dc170 / f01c4` | Returns the name. |
| `getParentNode` | `WorldNode:getParentNode()` | SNJ | `b15b0 / df398 / f1ed0` | Returns the parent node. |
| `getPreviousSiblingNode` | `WorldNode:getPreviousSiblingNode()` | SNJ | `b1430 / df108 / f1d50` | Returns the previous sibling node. |
| `getSelfAlpha` | `WorldNode:getSelfAlpha(): number` | SJ | `aeb1c / - / ef328` | Returns the self alpha. |
| `getSelfColor` | `WorldNode:getSelfColor(): (number, number, number, number)` | SJ | `aebf4 / - / ef400` | Returns the self color. |
| `getSiblingNode` | `WorldNode:getSiblingNode()` | SNJ | `b1490 / df1ac / f1db0` | Returns the sibling node. |
| `getWorldPosition` | `WorldNode:getWorldPosition(): (number, number)` | SNJ | `b05a8 / dd498 / f04f4` | Returns the world position. |
| `getWorldRotation` | `WorldNode:getWorldRotation(): number` | SNJ | `afeac / dd310 / f0b10` | Returns the world rotation. |
| `getWorldScale` | `WorldNode:getWorldScale(): (number, number)` | SNJ | `b050c / dcf24 / f12f8` | Returns the world scale. |
| `getWorldTransform` | `WorldNode:getWorldTransform(): (number, number, number, number, number, number)` | SNJ | `b0a94 / ddd00 / f0588` | Returns the world transform. |
| `getWorldZIndex` | `WorldNode:getWorldZIndex(): integer` | SNJ | `aef58 / dca08 / ef764` | Returns the world zindex. |
| `getXAxis` | `WorldNode:getXAxis(): (number, number)` | SNJ | `afe14 / dcc38 / f0a78` | Returns the xaxis. |
| `getYAxis` | `WorldNode:getYAxis(): (number, number)` | SNJ | `afd78 / dcb88 / f09dc` | Returns the yaxis. |
| `getZIndex` | `WorldNode:getZIndex(): integer` | SNJ | `aefc0 / dcafc / ef7cc` | Returns the zindex. |
| `isDestroyed` | `WorldNode:isDestroyed(): boolean` | SNJ | `aeeec / dc43c / ef6f8` | Returns whether destroyed. |
| `isEnabled` | `WorldNode:isEnabled(): boolean` | SNJ | `b0d1c / ddf10 / efbbc` | Returns whether enabled. |
| `isSelfEnabled` | `WorldNode:isSelfEnabled(): boolean` | SNJ | `b0cb0 / dde74 / efb50` | Returns whether self enabled. |
| `isSelfVisible` | `WorldNode:isSelfVisible(): boolean` | SJ | `aed34 / - / ef540` | Returns whether self visible. |
| `isVisible` | `WorldNode:isVisible(): boolean` | SJ | `aeda0 / - / ef5ac` | Returns whether visible. |
| `localToWorldDirection` | `WorldNode:localToWorldDirection(arg1: number, arg2: number): (number, number)` | SNJ | `afa10 / dc798 / f03fc` | Not described (name only). |
| `localToWorldPosition` | `WorldNode:localToWorldPosition(arg1: number, arg2: number): (number, number)` | SNJ | `afbc4 / dc88c / f0714` | Not described (name only). |
| `removeChildNode` | `WorldNode:removeChildNode(arg1: any): number` | SNJ | `b1944 / f5ec0 / efc30` | Not described (name only). |
| `removeHierarchy` | `WorldNode:removeHierarchy(): number` | SNJ | `af344 / f14c0 / efcb4` | Not described (name only). |
| `rotate` | `WorldNode:rotate(arg1: number)` | SNJ | `b0178 / dd14c / f0ddc` | Not described (name only). |
| `scale` | `WorldNode:scale(arg1: number, arg2: number)` | SNJ | `aff18 / dcce4 / f0b7c` | Not described (name only). |
| `setAlpha` | `WorldNode:setAlpha(alpha: number)` | SJ | `af5bc / - / eff9c` | Sets the alpha. |
| `setCategory` | `WorldNode:setCategory(category: integer)` | SNJ | `aee18 / dc350 / ef624` | Sets the category. |
| `setColor` | `WorldNode:setColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SJ | `af634 / - / f0014` | Sets the color. |
| `setEnabled` | `WorldNode:setEnabled(enabled: boolean)` | SNJ | `b0e54 / de434 / f173c` | Sets the enabled. |
| `setLocalPosition` | `WorldNode:setLocalPosition(arg1: number, arg2: number)` | SNJ | `b0718 / dd8a8 / f1260` | Sets the local position. |
| `setLocalPositionX` | `WorldNode:setLocalPositionX(localPositionX: number)` | SNJ | `b06a4 / dd83c / f11e8` | Sets the local position x. |
| `setLocalPositionY` | `WorldNode:setLocalPositionY(localPositionY: number)` | SNJ | `b0630 / dd7d0 / f1170` | Sets the local position y. |
| `setLocalRotation` | `WorldNode:setLocalRotation(localRotation: number)` | SNJ | `b02c0 / dd298 / f0f24` | Sets the local rotation. |
| `setLocalScale` | `WorldNode:setLocalScale(arg1: number, arg2: number)` | SNJ | `b00d4 / dce84 / f0d38` | Sets the local scale. |
| `setLocalScaleX` | `WorldNode:setLocalScaleX(localScaleX: number)` | SNJ | `b0050 / dce0c / f0cb4` | Sets the local scale x. |
| `setLocalScaleY` | `WorldNode:setLocalScaleY(localScaleY: number)` | SNJ | `affcc / dcd94 / f0c30` | Sets the local scale y. |
| `setLocalTransform` | `WorldNode:setLocalTransform(arg1: number, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number)` | SNJ | `b07b0 / ddbd4 / f1394` | Sets the local transform. |
| `setName` | `WorldNode:setName(name: any)` | SNJ | `af854 / dc1fc / f0240` | Sets the name. |
| `setNewParent` | `WorldNode:setNewParent(...)` | SNJ | `b17b4 / decfc / f1f94` | Sets the new parent. |
| `setVisible` | `WorldNode:setVisible(visible: boolean)` | SJ | `af6fc / - / f00dc` | Sets the visible. |
| `setWorldPosition` | `WorldNode:setWorldPosition(arg1: number, arg2: number)` | SNJ | `b03ec / dd674 / f1050` | Sets the world position. |
| `setWorldRotation` | `WorldNode:setWorldRotation(worldRotation: number)` | SNJ | `b0204 / dd1cc / f0e68` | Sets the world rotation. |
| `setWorldTransform` | `WorldNode:setWorldTransform(arg1: number, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number)` | SNJ | `b08bc / dd93c / f14a0` | Sets the world transform. |
| `setWorldZIndex` | `WorldNode:setWorldZIndex(worldZIndex: integer)` | SNJ | `afc80 / dc990 / f07d0` | Sets the world zindex. |
| `setZIndex` | `WorldNode:setZIndex(zIndex: integer)` | SNJ | `afd04 / dca94 / f0854` | Sets the zindex. |
| `translate` | `WorldNode:translate(arg1: number, arg2: number)` | SNJ | `b0344 / dd3f4 / f0fa8` | Not described (name only). |
| `worldToLocalDirection` | `WorldNode:worldToLocalDirection(arg1: number, arg2: number): (number, number)` | SNJ | `af914 / dc530 / f0300` | Not described (name only). |
| `worldToLocalPosition` | `WorldNode:worldToLocalPosition(arg1: number, arg2: number): (number, number)` | SNJ | `afb08 / dc64c / f0658` | Not described (name only). |

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

← [Volumes](Volumes.md) · [Index](README.md)
