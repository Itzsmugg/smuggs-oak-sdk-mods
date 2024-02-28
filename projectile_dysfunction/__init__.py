# ruff: noqa: D103
if True:
    assert __import__("mods_base").__version_info__ >= (1, 0), "Please update the SDK"

import unrealsdk
from mods_base import build_mod, hook, get_pc
from typing import Any
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray

__version__: str
__version_info__: tuple[int, ...]


@hook("/Script/GbxWeapon.Weapon:OnUseStarted", Type.POST)
def EnumerateOtherParts(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    print("OnUseStarted: ", str(obj))
    try:
        # Original statement
        new_proj = unrealsdk.find_object("Default__LightProjectile_JAK_Fakobs_C", "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/LightProjectile_JAK_Fakobs.Default__LightProjectile_JAK_Fakobs_C").Class
    except Exception as e:
        # Alternative statement if an exception occurs
        loadingproj = unrealsdk.find_object("TestLibrary", "/Script/GbxTest.Default__TestLibrary").LoadAsset("/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/LightProjectile_JAK_Fakobs.Default__LightProjectile_JAK_Fakobs_C", unrealsdk.find_class("Object"))
        loadingprojtuple = [item for item in loadingproj if isinstance(item, UObject)]
        new_proj = loadingprojtuple[0].Class
    get_pc().Pawn.GetActiveWeapon(0).CurrentFireComponent.LightProjectileData = new_proj


build_mod()
