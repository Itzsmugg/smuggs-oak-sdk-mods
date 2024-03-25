from mods_base.keybinds import keybind
from mods_base.options import BoolOption, SliderOption
import unrealsdk
from mods_base import  hook, get_pc
from typing import Any
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray








print_to_log_bool = BoolOption(
    "Prints details to log",
    False,
    description="Prints details to log",
)

TEXT = "NONE"

def get_text():
    return TEXT


@hook("/Script/GbxWeapon.LightProjectileData:OnImpact", Type.POST)
def OnImpact(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    if args.Hit.Actor != None and args.Projectile.GetInstigator() == get_pc().Pawn:
        global TEXT

        CLASS = args.Hit.Actor.Class.Name
        NAME = args.Hit.Actor.Name
        TEXT = f"""Last Hit Object: 
        Class: {CLASS} 
        Name: {NAME}"""

    if print_to_log_bool.value:
        print(f"Last Hit Object: Class: {CLASS} Name: {NAME}")

