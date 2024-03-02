# ruff: noqa: D103
if True:
    assert __import__("mods_base").__version_info__ >= (1, 1), "Please update the SDK"

from re import T
from mods_base.options import BoolOption, SliderOption
import unrealsdk
from mods_base import build_mod, hook, get_pc
from typing import Any
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray

__version__: str
__version_info__: tuple[int, ...]



draw_text_bool = BoolOption(
    "Draw Text Details on HUD, top left",
    False,
    description="Draw Text Details on HUD, top left",
)

on_screen_size = SliderOption("HUD Display Font Size", 0, 0, 100, is_integer=True) 

print_to_log_bool = BoolOption(
    "Prints details to log",
    False,
    description="Prints details to log",
)

YELLOW = unrealsdk.make_struct("LinearColor", R=1, G=1, B=0, A=1)
FONT = unrealsdk.construct_object(unrealsdk.find_class("Font"), unrealsdk.find_class("Font").Outer, "NEWFONT", 0, unrealsdk.find_object("Font", "/Game/UI/_Shared/Fonts/OAK_BODY.OAK_BODY")) 
FONT.LegacyFontSize += 30
CLASS = "NONE"
NAME = "NONE"
TEXT = "NONE"


@hook(
    "/Script/Engine.HUD:ReceiveDrawHUD",
    Type.POST,
    auto_enable=True,
)
def draw(
    obj: UObject,
    _2: WrappedStruct,
    _3: Any,
    _4: BoundFunction,
) -> None:

        global TEXT
        TEXT = f"""Last Hit Object: 
        Class: {CLASS} 
        Name: {NAME}"""
        if draw_text_bool.value:
            obj.DrawText(TEXT, YELLOW, 10, 10, FONT, 0.5 + on_screen_size.value / 100, False)


@hook("/Script/GbxWeapon.LightProjectileData:OnImpact", Type.POST)
def OnImpact(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    if args.Hit.Actor != None and args.Projectile.GetInstigator() == get_pc().Pawn:
        global CLASS
        global NAME
        CLASS = args.Hit.Actor.Class.Name
        NAME = args.Hit.Actor.Name
        
    else:
        CLASS, NAME = "NONE", "NONE"

    if print_to_log_bool.value:
        print(f"Last Hit Object: Class: {CLASS} Name: {NAME}")




build_mod()
