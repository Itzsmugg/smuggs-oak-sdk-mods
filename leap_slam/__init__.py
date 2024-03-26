import mods_base

from mods_base import build_mod, keybind, KeybindType, KeybindOption, keybinds, hook, SETTINGS_DIR
from ui_utils import show_hud_message
from typing import Any
import unrealsdk
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray

assert mods_base.__version_info__ >= (1, 1), "Please update the SDK"

__version__: str
__version_info__: tuple[int, ...]


slam = unrealsdk.find_object("ControlledMove_Global_GroundSlam_High_C", "/Game/PlayerCharacters/_Shared/_Design/GroundSlam/High/ControlledMove_Global_GroundSlam_High.Default__ControlledMove_Global_GroundSlam_High_C")
sprint = False
sprintjump = False
@hook("/Script/OakGame.OakCharacter:OnStartSprinting", Type.PRE)
def OnStartSprinting(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:

    global sprint
    sprint = True
@hook("/Script/OakGame.OakCharacter:OnEndSprinting", Type.PRE)
def OnEndSprinting(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    global sprint
    sprint = False
@hook("/Script/OakGame.OakPlayerController:JumpPressed", Type.PRE)
def JumpPressed(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    
    global sprintjump
    if sprint:
        sprintjump = True
        
    else:
        sprintjump = False

    if sprintjump:
        slam.HighGroundSlamThreshold = 135
        slam.bSpeedAffectedByMaxGroundSpeedScale = True
        slam.Duration.BaseValueConstant = 999
        slam.MovementType = 0
        slam.Speed.BaseValueConstant = 6000.0
        slam.Speed.BaseValueAttribute = None
        slam.Speed.BaseValueScale = 1

        sprintjump = False
    else:
        slam.HighGroundSlamThreshold = 300
        slam.bSpeedAffectedByMaxGroundSpeedScale = False
        slam.Duration.BaseValueConstant = 0.0
        slam.MovementType = 2
        slam.Speed.BaseValueConstant = 0.6499999761581421
        slam.Speed.BaseValueAttribute = unrealsdk.find_object("GbxAttributeData", "/Game/GameData/Attributes/Character/Att_Character_CurrentSpeed2D.Att_Character_CurrentSpeed2D")
        slam.Speed.BaseValueScale = 0.6499999761581421

        

build_mod()
