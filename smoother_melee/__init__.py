if True:
    assert __import__("mods_base").__version_info__ >= (1, 0), "Please update the SDK"
    
from typing import Any
import unrealsdk
from mods_base import get_pc, hook, keybind, build_mod
from ui_utils import show_hud_message
from unrealsdk.hooks import Type
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct

__version__: str
__version_info__: tuple[int, ...]


@hook("/Script/OakGame.OakCharacter_Player:ShowConnectEffect", Type.POST)
def smoother_melee(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    pc = get_pc()
    MeleeStateComp = pc.pawn.PlayerMeleeState
    MeleeStateComp.MeleeSpeed.Value = 1.125
    MeleeStateComp.MeleeWeaponBoneModifyBlendTime = 0
    MeleeStateComp.MeleeHitTime = 0
    MeleeStateComp.EndMeleeDuration = 0
    MeleeStateComp.MeleeCooldownEndTime = 0

    for PlayerMeleeData in unrealsdk.find_all("PlayerMeleeData", exact=False):
        PlayerMeleeData.bUseTargetHoming = False

@hook("/Game/PlayerCharacters/_Shared/_Design/Character/BPChar_Player.BPChar_Player_C:DoMelee", Type.POST)
def smoother_melee2(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    pc = get_pc()
    MeleeStateComp = pc.pawn.PlayerMeleeState
    MeleeStateComp.MeleeCooldownEndTime = 0
    print("MeleeCooldownEndTime: ", MeleeStateComp.MeleeCooldownEndTime)
build_mod()