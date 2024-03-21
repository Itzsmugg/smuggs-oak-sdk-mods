from typing import Any
from mods_base import hook, options
from mods_base.options import ButtonOption
import unrealsdk
from mods_base import Mod, NestedOption, GroupedOption, keybind, KeybindType, KeybindOption, keybinds, BoolOption, build_mod
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray

def apply_anointments(part_data_list, anointments):
    anointments_map = {anoint.identifier: anoint.value for anoint in anointments}

    for part_data in part_data_list:
        part = part_data.PartData
        if not part or not part.Name:
            continue

        part_name = part.Name
        if part_name in anointments_map:
            anoint_value = anointments_map[part_name]
            weight = 1 if anoint_value else 0
        else:
            weight = 0

        part_data.Weight.BaseValueScale = weight
        part_data.Weight.BaseValueConstant = weight

        if part_data.Weight.BaseValueAttribute is not None:
            part_data.Weight.BaseValueAttribute = None
        if part_data.Weight.AttributeInitializer is not None:
            part_data.Weight.AttributeInitializer = None




def anoint_chance_base(inventory_balance_data, anointments):
    if inventory_balance_data is None:
        return

    anointments_map = {anoint.identifier: anoint.value for anoint in anointments}

    if inventory_balance_data.RuntimeGenericPartList and inventory_balance_data.RuntimeGenericPartList.PartList:
        apply_anointments(inventory_balance_data.RuntimeGenericPartList.PartList, anointments)

    if inventory_balance_data.PartSetData and inventory_balance_data.PartSetData.GenericParts and inventory_balance_data.PartSetData.GenericParts.Parts:
        apply_anointments(inventory_balance_data.PartSetData.GenericParts.Parts, anointments)

def change_all_anoints():
    for inv in anoint_inv:
        try:
            inventory = unrealsdk.find_object("InventoryBalanceData", inv)
            anoint_chance_base(inventory, anointments)
        except Exception as e:
            print(f"change_all_anoints anoint chance fail: {inv}, error: {e}")

    for expanse in unrealsdk.find_all("InventoryGenericPartExpansionData", exact=False):
        try:
            if expanse.GenericParts and expanse.GenericParts.Parts:
                apply_anointments(expanse.GenericParts.Parts, anointments)
        except Exception as e:
            print(f"EXPANSE anoint chance fail: {expanse}, error: {e}")


GPart_All_SkillEnd_WeaponDamage = BoolOption(identifier="GPart_All_SkillEnd_WeaponDamage", display_name="ASE Weapon Damage", description="On Action Skill End, Weapon Damage is increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_WeaponDamage", value=True)
GPart_All_SkillEnd_UniqueEnemyDamage = BoolOption(identifier="GPart_All_SkillEnd_UniqueEnemyDamage", display_name="ASE Weapon Damage to Badass, Named, and Bosses", description="On Action Skill End, Deal $VALUE$ more Weapon Damage to Badass, Named, and Boss enemies for a short time.", description_title="GPart_All_SkillEnd_UniqueEnemyDamage", value=True)
GPart_All_SkillEnd_SplashDamage = BoolOption(identifier="GPart_All_SkillEnd_SplashDamage", display_name="ASE Splash Damage", description="On Action Skill End, Splash Damage is increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_SplashDamage", value=True)
GPart_All_SkillEnd_NextMagBonusDamageShock = BoolOption(identifier="GPart_All_SkillEnd_NextMagBonusDamageShock", display_name="Next 2 mags Shock", description="On Action Skill End, the next $VALUE$ magazines will have", description_title="GPart_All_SkillEnd_NextMagBonusDamageShock", value=True)
GPart_All_SkillEnd_NextMagBonusDamageRadiation = BoolOption(identifier="GPart_All_SkillEnd_NextMagBonusDamageRadiation", display_name="Next 2 mags rad", description="On Action Skill End, the next $VALUE$ magazines will have", description_title="GPart_All_SkillEnd_NextMagBonusDamageRadiation", value=True)
GPart_All_SkillEnd_NextMagBonusDamageFire = BoolOption(identifier="GPart_All_SkillEnd_NextMagBonusDamageFire", display_name="Next 2 mags fire", description="On Action Skill End, the next $VALUE$ magazines will have", description_title="GPart_All_SkillEnd_NextMagBonusDamageFire", value=True)
GPart_All_SkillEnd_NextMagBonusDamageCryo = BoolOption(identifier="GPart_All_SkillEnd_NextMagBonusDamageCryo", display_name="Next 2 mags cryo", description="On Action Skill End, the next $VALUE$ magazines will have", description_title="GPart_All_SkillEnd_NextMagBonusDamageCryo", value=True)
GPart_All_SkillEnd_NextMagBonusDamageCorrosive = BoolOption(identifier="GPart_All_SkillEnd_NextMagBonusDamageCorrosive", display_name="Next 2 mags corrosive", description="On Action Skill End, the next $VALUE$ magazines will have", description_title="GPart_All_SkillEnd_NextMagBonusDamageCorrosive", value=True)
GPart_All_SkillEnd_LifeSteal = BoolOption(identifier="GPart_All_SkillEnd_LifeSteal", display_name="ASE Life Steal", description="ASE Life Steal", description_title="GPart_All_SkillEnd_LifeSteal", value=True)
GPart_All_SkillEnd_FireRateReload = BoolOption(identifier="GPart_All_SkillEnd_FireRateReload", display_name="ASE FireRate Reload", description="On Action Skill End, fire rate is increased by $VALUE$, and", description_title="GPart_All_SkillEnd_FireRateReload", value=True)
GPart_All_SkillEnd_EleChanceDamage = BoolOption(identifier="GPart_All_SkillEnd_EleChanceDamage", display_name="Ase Status effect chance, damage", description="On Action Skill End, Weapon Status Effect Damage and Chance are increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_EleChanceDamage", value=True)
GPart_All_SkillEnd_CritDamage = BoolOption(identifier="GPart_All_SkillEnd_CritDamage", display_name="ASE Crit Dmg", description="On Action Skill End, Critical Damage is increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_CritDamage", value=True)
GPart_All_SkillEnd_AccuracyHandling = BoolOption(identifier="GPart_All_SkillEnd_AccuracyHandling", display_name="ASE Accuracy Handling", description="On Action Skill End, Weapon Accuracy and Handling are greatly increased for a short time.", description_title="GPart_All_SkillEnd_AccuracyHandling", value=True)
GPart_All_SkillEnd_MoveSpeed = BoolOption(identifier="GPart_All_SkillEnd_MoveSpeed", display_name="ASE move speed", description="On Action Skill End, Movement Speed is increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_MoveSpeed", value=True)
GPart_All_SkillEnd_MeleeDamage = BoolOption(identifier="GPart_All_SkillEnd_MeleeDamage", display_name="ASE Melee Damage", description="On Action Skill End, Melee Damage is increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_MeleeDamage", value=True)
GPart_All_SkillEnd_HealthRegen = BoolOption(identifier="GPart_All_SkillEnd_HealthRegen", display_name="ASE Health Regen", description="On Action Skill End, regenerate $VALUE$ max health per second for a short time.", description_title="GPart_All_SkillEnd_HealthRegen", value=True)
GPart_All_SkillEnd_DamageReduction = BoolOption(identifier="GPart_All_SkillEnd_DamageReduction", display_name="ASE Damage Reduction", description="On Action Skill End, damage taken is reduced by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_DamageReduction", value=True)
GPart_All_SkillEnd_CooldownRate = BoolOption(identifier="GPart_All_SkillEnd_CooldownRate", display_name="ASE Cooldown", description="On Action Skill End, action skill cooldown rate is increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_CooldownRate", value=True)
GPart_Siren_Grasp_TerrorSkulls = BoolOption(identifier="GPart_Siren_Grasp_TerrorSkulls", display_name="PhaseGrasp Terror Skulls", description="After Phasegrasping an enemy, Amara fires Terror skulls at the grasped target dealing $VALUE$ damage.", description_title="GPart_Siren_Grasp_TerrorSkulls", value=True)
GPart_Operative_DroneActiveTerrorLifesteal = BoolOption(identifier="GPart_Operative_DroneActiveTerrorLifesteal", display_name="Terror SNTNL LifeSteal", description="While SNTNL is active, SNTNL gains $VALUE$ lifesteal while you are affected by Terror.", description_title="GPart_Operative_DroneActiveTerrorLifesteal", value=True)
GPart_Gunner_Reload_TerrorNova = BoolOption(identifier="GPart_Gunner_Reload_TerrorNova", display_name="Terror Reload Cryo Nova", description="After Reloading, consume all Terror and create a nova that deals cryo damage.", description_title="GPart_Gunner_Reload_TerrorNova", value=True)
GPart_Beast_AttackCmd_TerrorFireDMG = BoolOption(identifier="GPart_Beast_AttackCmd_TerrorFireDMG", display_name="Terror Attack Cmd Fire dmg", description="After using Attack Command, consume all Terror and FL4K's pet gains $VALUE$ bonus incendiary damage for a short time.", description_title="GPart_Beast_AttackCmd_TerrorFireDMG", value=True)
GPart_All_Passive_TerrorProjectilesPerShot = BoolOption(identifier="GPart_All_Passive_TerrorProjectilesPerShot", display_name="Terror bonus projectiles", description="While Terrified, you have a chance to fire an extra projectile per shot. The more Terror you have, the higher the bonus.", description_title="GPart_All_Passive_TerrorProjectilesPerShot", value=True)
GPart_All_Passive_TerrorHealthRegen = BoolOption(identifier="GPart_All_Passive_TerrorHealthRegen", display_name="Terror health regen", description="While Terrified, gain health regeneration. The more Terror you have, the higher the bonus.", description_title="GPart_All_Passive_TerrorHealthRegen", value=True)
GPart_All_Passive_TerrorDamageMitigation = BoolOption(identifier="GPart_All_Passive_TerrorDamageMitigation", display_name="Terror Damage Reduction", description="While Terrified, reduce all incoming damage by a small amount. The more Terror you have, the higher the bonus.", description_title="GPart_All_Passive_TerrorDamageMitigation", value=True)
GPart_All_Passive_TerrorCritDamage = BoolOption(identifier="GPart_All_Passive_TerrorCritDamage", display_name="Terror Crit dmg", description="While Terrified, gain increased Crit Damage. The more Terror you have, the higher the bonus.", description_title="GPart_All_Passive_TerrorCritDamage", value=True)
GPart_All_Passive_TerrorBulletReflect = BoolOption(identifier="GPart_All_Passive_TerrorBulletReflect", display_name="Terror Reflect", description="While Terrified, enemy bullets have a chance to reflect off of you. The more Terror you have, the higher the bonus.", description_title="GPart_All_Passive_TerrorBulletReflect", value=True)
GPart_All_Passive_TerrorBonus_CryoDamage = BoolOption(identifier="GPart_All_Passive_TerrorBonus_CryoDamage", display_name="Terror Cryo", description="While Terrified, deal $VALUE$ bonus Cryo damage.", description_title="GPart_All_Passive_TerrorBonus_CryoDamage", value=True)
GPart_All_Passive_TerrorAmmoRegen = BoolOption(identifier="GPart_All_Passive_TerrorAmmoRegen", display_name="Terror Ammo Regen", description="While Terrified, gain ammo regeneration. The more Terror you have, the higher the bonus.", description_title="GPart_All_Passive_TerrorAmmoRegen", value=True)
GPart_All_Passive_TerrorDamageFireRate = BoolOption(identifier="GPart_All_Passive_TerrorDamageFireRate", display_name="Terror FireRate", description="While Terrified, gain increased damage and fire rate. The more Terror you have, the higher the bonus.", description_title="GPart_All_Passive_TerrorDamageFireRate", value=True)
GPart_All_SkillEnd_TerrorHeal = BoolOption(identifier="GPart_All_SkillEnd_TerrorHeal", display_name="ASE Terror Heal", description="On Action Skill End, heal for $VALUE$ of max health. Effect is increased by 15% per Terror stack. Consumes all Terror.", description_title="GPart_All_SkillEnd_TerrorHeal", value=True)
GPart_All_SkillEnd_GenerateTerror = BoolOption(identifier="GPart_All_SkillEnd_GenerateTerror", display_name="ASE Generate Terror", description="On Action Skill End, apply Terror to yourself every 3 seconds for the next $VALUE$ seconds.", description_title="GPart_All_SkillEnd_GenerateTerror", value=True)
GPart_All_Passive_GenerateTerror_Melee = BoolOption(identifier="GPart_All_Passive_GenerateTerror_Melee", display_name="Melee Generate Terror", description="Melee attacks have a $VALUE$ chance to apply Terror to yourself.", description_title="GPart_All_Passive_GenerateTerror_Melee", value=True)
GPart_All_GrenadeDamage = BoolOption(identifier="GPart_All_GrenadeDamage", display_name="ASA Grenade dmg", description="While an Action Skill is Active, Grenade Damage is increased by $VALUE$.", description_title="GPart_All_GrenadeDamage", value=True)
GPart_All_ShockFeedback = BoolOption(identifier="GPart_All_ShockFeedback", display_name="ASA shock reflect", description="While an Action Skill is Active, $VALUE$ of health damage taken is returned to the attacker as shock damage.", description_title="GPart_All_ShockFeedback", value=True)
GPart_All_SlideRegenShields = BoolOption(identifier="GPart_All_SlideRegenShields", display_name="Slide recharge shield", description="While Sliding, build up energy that refills a portion of your shields.", description_title="GPart_All_SlideRegenShields", value=True)
GPart_All_ShieldBreakAmp = BoolOption(identifier="GPart_All_ShieldBreakAmp", display_name="Shield Break Amp", description="On shield break, the next shot deals $VALUE$ shield capacity as bonus Amp Damage.", description_title="GPart_All_ShieldBreakAmp", value=True)
GPart_All_SkillStart_OverchargeShield = BoolOption(identifier="GPart_All_SkillStart_OverchargeShield", display_name="ASS Shield Break", description="On Action Skill Start, activate any effects that trigger on shield break or fill.", description_title="GPart_All_SkillStart_OverchargeShield", value=True)
GPart_All_HealingPool = BoolOption(identifier="GPart_All_HealingPool", display_name="ASE Healing Pool", description="On Action Skill End, spawn a healing pool for several seconds.", description_title="GPart_All_HealingPool", value=True)
GPart_All_WeaponDamage = BoolOption(identifier="GPart_All_WeaponDamage", display_name="ASA Weapon DMG", description="While an Action Skill is Active, Weapon Damage is increased by $VALUE$.", description_title="GPart_All_WeaponDamage", value=True)
GPart_All_UniqueEnemyDamage = BoolOption(identifier="GPart_All_UniqueEnemyDamage", display_name="ASA Bonus gun dmg to named enemies", description="While an Action Skill is Active, Deal $VALUE$ more Weapon Damage to Badass, Named, and Boss enemies.", description_title="GPart_All_UniqueEnemyDamage", value=True)
GPart_EG_Gen_SkillActive_PulseFireNova = BoolOption(identifier="GPart_EG_Gen_SkillActive_PulseFireNova", display_name="ASA Novas", description="While an Action Skill is Active, constantly trigger novas that deal $VALUE$ damage.", description_title="GPart_EG_Gen_SkillActive_PulseFireNova", value=True)
GPart_All_DamageMitigation = BoolOption(identifier="GPart_All_DamageMitigation", display_name="ASA Damage Reduction", description="While an Action Skill is Active, reduce all incoming damage by a small amount.", description_title="GPart_All_DamageMitigation", value=True)
GPart_EG_Gen_SkillEnd_CyberSpike = BoolOption(identifier="GPart_EG_Gen_SkillEnd_CyberSpike", display_name="ASE Cyber Spike", description="On Action Skill End, create a cyber spike that damages nearby enemies.", description_title="GPart_EG_Gen_SkillEnd_CyberSpike", value=True)
GPart_All_HighHealthBreaker = BoolOption(identifier="GPart_All_HighHealthBreaker", display_name="Gain extra dmg against enemies over 90% HP", description="Gain $VALUE$ increased Weapon Damage against enemies above", description_title="GPart_All_HighHealthBreaker", value=True)
GPart_All_UnhealthyRadDamage = BoolOption(identifier="GPart_All_UnhealthyRadDamage", display_name="URAD.", description="While under 50% health, deal $VALUE$ bonus radiation damage.", description_title="GPart_All_UnhealthyRadDamage", value=True)
GPart_Passive_All_CritStatusEffect = BoolOption(identifier="GPart_Passive_All_CritStatusEffect", display_name="Elemental crit novas", description="Elemental critical hits can cause status effects of that element to explode, creating a nova that deals $VALUE$ of the status effect's damage.", description_title="GPart_Passive_All_CritStatusEffect", value=True)
GPart_EG_GrenadeThrow_GlobalDamage = BoolOption(identifier="GPart_EG_GrenadeThrow_GlobalDamage", display_name="Grenade Thrown, Weapon, Grenade, and Action Skill Dmg", description="On Grenade Thrown, Weapon, Grenade, and Action Skill Damage are increased by $VALUE$ for 6 seconds.", description_title="GPart_EG_GrenadeThrow_GlobalDamage", value=True)
GPart_EG_SkillEndBonusEleDamage_Shock = BoolOption(identifier="GPart_EG_SkillEndBonusEleDamage_Shock", display_name="ASE Shock", description="On Action Skill End, gain 50% bonus Shock damage with weapons for 10 seconds.", description_title="GPart_EG_SkillEndBonusEleDamage_Shock", value=True)
GPart_EG_SkillEndBonusEleDamage_Radiation = BoolOption(identifier="GPart_EG_SkillEndBonusEleDamage_Radiation", display_name="ASE Rad", description="On Action Skill End, gain 50% bonus Radiation Damage with weapons for 10 seconds.", description_title="GPart_EG_SkillEndBonusEleDamage_Radiation", value=True)
GPart_EG_SkillEndBonusEleDamage_Fire = BoolOption(identifier="GPart_EG_SkillEndBonusEleDamage_Fire", display_name="ASE Fire", description="On Action Skill End, gain 50% bonus Incendiary Damage with weapons for 10 seconds.", description_title="GPart_EG_SkillEndBonusEleDamage_Fire", value=True)
GPart_EG_SkillEndBonusEleDamage_Cryo = BoolOption(identifier="GPart_EG_SkillEndBonusEleDamage_Cryo", display_name="ASE Cryo", description="On Action Skill End, gain 50% bonus Cryo damage with weapons for 10 seconds.", description_title="GPart_EG_SkillEndBonusEleDamage_Cryo", value=True)
GPart_EG_SkillEndBonusEleDamage_Corrosive = BoolOption(identifier="GPart_EG_SkillEndBonusEleDamage_Corrosive", display_name="ASE Corrosive", description="On Action Skill End, gain $VALUE$ bonus Corrosive damage with weapons for 10 seconds.", description_title="GPart_EG_SkillEndBonusEleDamage_Corrosive", value=True)
GPart_EG_WhileSliding_FireRate = BoolOption(identifier="GPart_EG_WhileSliding_FireRate", display_name="Sliding FireRate", description="While sliding, Fire Rate is increased by $VALUE$", description_title="GPart_EG_WhileSliding_FireRate", value=True)
GPart_EG_WhileSliding_Damage = BoolOption(identifier="GPart_EG_WhileSliding_Damage", display_name="Sliding Dmg", description="While sliding, damage is increased by $VALUE$.", description_title="GPart_EG_WhileSliding_Damage", value=True)
GPart_EG_WhileSliding_AccuracyHandling = BoolOption(identifier="GPart_EG_WhileSliding_AccuracyHandling", display_name="sliding accuracy handling", description="While sliding, Accuracy and Handling are increased by $VALUE$", description_title="GPart_EG_WhileSliding_AccuracyHandling", value=True)
GPart_EG_WhileAirborn_FireRate = BoolOption(identifier="GPart_EG_WhileAirborn_FireRate", display_name="airborne, Fire Rate", description="While airborne, Fire Rate is increased by $VALUE$", description_title="GPart_EG_WhileAirborn_FireRate", value=True)
GPart_EG_WhileAirborn_Damage = BoolOption(identifier="GPart_EG_WhileAirborn_Damage", display_name="airborne damage", description="While airborne, damage is increased by $VALUE$.", description_title="GPart_EG_WhileAirborn_Damage", value=True)
GPart_EG_WhileAirborn_CritDamage = BoolOption(identifier="GPart_EG_WhileAirborn_CritDamage", display_name="airborne, Crit dmg", description="While airborne, Critical Damage is increased by $VALUE$.", description_title="GPart_EG_WhileAirborn_CritDamage", value=True)
GPart_EG_WhileAirborn_AccuracyHandling = BoolOption(identifier="GPart_EG_WhileAirborn_AccuracyHandling", display_name="airborne Accuracy and Handling", description="While airborne, Accuracy and Handling are increased by $VALUE$", description_title="GPart_EG_WhileAirborn_AccuracyHandling", value=True)
GPart_EG_Generic_LowHealthExecutor = BoolOption(identifier="GPart_EG_Generic_LowHealthExecutor", display_name="enemies below 25% Health recieve more Weapon Damage.", description="While enemies are below 25% Health, gain $VALUE$ increased Weapon Damage.", description_title="GPart_EG_Generic_LowHealthExecutor", value=True)
GPart_EG_Generic_KillStackReloadDamage = BoolOption(identifier="GPart_EG_Generic_KillStackReloadDamage", display_name="Killstack Reload and Damage.", description="Killing an enemy grants $VALUE$ Weapon Damage and Reload Speed for 25 seconds. This effect stacks.", description_title="GPart_EG_Generic_KillStackReloadDamage", value=True)
GPart_EG_Generic_ConsecutiveHitsDmgStack = BoolOption(identifier="GPart_EG_Generic_ConsecutiveHitsDmgStack", display_name="Consecutive Hits", description="Consecutive Hits increase Weapon Damage by $VALUE$ per hit. Misses remove all bonuses.", description_title="GPart_EG_Generic_ConsecutiveHitsDmgStack", value=True)
GPart_Siren_PhaseslamDamage = BoolOption(identifier="GPart_Siren_PhaseslamDamage", display_name="Phaseslam dmg", description="Slam damage is increased by $VALUE$ for Phaseslam and related action skills.", description_title="GPart_Siren_PhaseslamDamage", value=True)
GPart_Siren_GraspActiveDamage = BoolOption(identifier="GPart_Siren_GraspActiveDamage", display_name="phasegrasp weapon dmg", description="While Grasp is active, Weapon Damage is increased by $VALUE$.", description_title="GPart_Siren_GraspActiveDamage", value=True)
GPart_Siren_PhaseflareDamage = BoolOption(identifier="GPart_Siren_PhaseflareDamage", display_name="phaseflare dmg", description="Orb damage is increased by $VALUE$ for Phaseflare and related action skills.", description_title="GPart_Siren_PhaseflareDamage", value=True)
GPart_Siren_PhasecastDamage = BoolOption(identifier="GPart_Siren_PhasecastDamage", display_name="Phasecast damage", description="Astral Projection damage is increased by $VALUE$ for Phasecast and related action skills.", description_title="GPart_Siren_PhasecastDamage", value=True)
GPart_Operative_MNTISDamage = BoolOption(identifier="GPart_Operative_MNTISDamage", display_name="MNTIS damage", description="MNTIS Shoulder Cannon damage is increased by $VALUE$.", description_title="GPart_Operative_MNTISDamage", value=True)
GPart_Gunner_VanquisherDamage = BoolOption(identifier="GPart_Gunner_VanquisherDamage", display_name="Vanquisher Rocket Pod damage", description="While Iron Bear is active, Vanquisher Rocket Pod damage is increased by $VALUE$.", description_title="GPart_Gunner_VanquisherDamage", value=True)
GPart_Gunner_V35LauncherDamage = BoolOption(identifier="GPart_Gunner_V35LauncherDamage", display_name="V-35 Grenade Launcher damage ", description="While Iron Bear is active, V-35 Grenade Launcher damage is increased by $VALUE$.", description_title="GPart_Gunner_V35LauncherDamage", value=True)
GPart_Gunner_SalamanderDamage = BoolOption(identifier="GPart_Gunner_SalamanderDamage", display_name="Salamander damage", description="While Iron Bear is active, Salamander damage is increased by $VALUE$.", description_title="GPart_Gunner_SalamanderDamage", value=True)
GPart_Gunner_RailgunDamage = BoolOption(identifier="GPart_Gunner_RailgunDamage", display_name="Railgun Damage", description="While Iron Bear is active, Railgun Damage is increased by $VALUE$.", description_title="GPart_Gunner_RailgunDamage", value=True)
GPart_Gunner_MinigunDamage = BoolOption(identifier="GPart_Gunner_MinigunDamage", display_name="Minigun damage", description="While Iron Bear is active, Minigun damage is increased by $VALUE$.", description_title="GPart_Gunner_MinigunDamage", value=True)
GPart_Gunner_IronCubActiveDamage = BoolOption(identifier="GPart_Gunner_IronCubActiveDamage", display_name="Iron Cub Weapon Damage", description="While Iron Cub is active, Weapon Damage is increased by $VALUE$.", description_title="GPart_Gunner_IronCubActiveDamage", value=True)
GPart_Gunner_BearFistDamage = BoolOption(identifier="GPart_Gunner_BearFistDamage", display_name="Bear Fist damage", description="While Iron Bear is active, Bear Fist damage is increased by $VALUE$.", description_title="GPart_Gunner_BearFistDamage", value=True)
GPart_Beast_GravitySnareActiveDamage = BoolOption(identifier="GPart_Beast_GravitySnareActiveDamage", display_name="Gravity Snare Weapon Damage.", description="While Gravity Snare is active, Weapon Damage is increased by $VALUE$.", description_title="GPart_Beast_GravitySnareActiveDamage", value=True)
GPart_Beast_FadeActiveDamage = BoolOption(identifier="GPart_Beast_FadeActiveDamage", display_name="Fade Away Weapon Damage", description="While Fade Away is active, Weapon Damage is increased by $VALUE$.", description_title="GPart_Beast_FadeActiveDamage", value=True)
GPart_Gunner_IBGrenadeChance = BoolOption(identifier="GPart_Gunner_IBGrenadeChance", display_name="Iron bear Grenade spawn", description="While Iron Bear is active, taking damage has a $VALUE$ chance to spawn a grenade.", description_title="GPart_Gunner_IBGrenadeChance", value=True)
GPart_All_SkillEnd_AddGrenade = BoolOption(identifier="GPart_All_SkillEnd_AddGrenade", display_name="ASS, Regenerate grenade.", description="On Action Skill Start, Regenerate $VALUE$ grenade.", description_title="GPart_All_SkillEnd_AddGrenade", value=True)
GPart_Siren_Grasp_ChargeSpeed = BoolOption(identifier="GPart_Siren_Grasp_ChargeSpeed", display_name="PhaseGrasp Weapon Charge", description="While Phasegrasp is active, Weapon charge time is decreased by $VALUE$", description_title="GPart_Siren_Grasp_ChargeSpeed", value=True)
GPart_All_SkillEnd_ProjectileSpeed = BoolOption(identifier="GPart_All_SkillEnd_ProjectileSpeed", display_name="ASE Projectile Speed", description="On Action Skill End, Projectile Speed is increased by $VALUE$ for a short time.", description_title="GPart_All_SkillEnd_ProjectileSpeed", value=True)
GPart_Siren_Slam_WeaponDamage = BoolOption(identifier="GPart_Siren_Slam_WeaponDamage", display_name="Phaseslam Weapon Damage", description="After using Phaseslam, Weapon Damage is increased by $VALUE$ for a short time.", description_title="GPart_Siren_Slam_WeaponDamage", value=True)
GPart_Siren_SkillEnd_AttunedSkillDamage = BoolOption(identifier="GPart_Siren_SkillEnd_AttunedSkillDamage", display_name="Siren Radiation Damage", description="On Action Skill End, deal $VALUE$ bonus radiation damage for a short time.", description_title="GPart_Siren_SkillEnd_AttunedSkillDamage", value=True)
GPart_Siren_Grasp_AccuracyCrit = BoolOption(identifier="GPart_Siren_Grasp_AccuracyCrit", display_name="Phasegrasping Accuracy and Handling", description="After Phasegrasping an enemy, Weapon Accuracy and Handling are greatly increased.", description_title="GPart_Siren_Grasp_AccuracyCrit", value=True)
GPart_Siren_Cast_WeaponDamage = BoolOption(identifier="GPart_Siren_Cast_WeaponDamage", display_name="Phasecast Weapon Damage", description="After using Phasecast, Weapon Damage is increased by $VALUE$ for a short time.", description_title="GPart_Siren_Cast_WeaponDamage", value=True)
GPart_Siren_Cast_ElementalChance = BoolOption(identifier="GPart_Siren_Cast_ElementalChance", display_name="Phasecast Status Effect Chance", description="After using Phasecast, Status Effect Chance is increased by $VALUE$ for a short time.", description_title="GPart_Siren_Cast_ElementalChance", value=True)
GPart_Siren_Slam_ReturnDamage = BoolOption(identifier="GPart_Siren_Slam_ReturnDamage", display_name="Phaseslam Dmg Reflect", description="On Action Skill End, $VALUE$ of all damage taken is returned to the attacker for a short time.", description_title="GPart_Siren_Slam_ReturnDamage", value=True)
GPart_Siren_Slam_MeleeDamage = BoolOption(identifier="GPart_Siren_Slam_MeleeDamage", display_name="PhaseSlam Melee Dmg", description="After using Phaseslam, Melee Damage is increased by $VALUE$ for a short time.", description_title="GPart_Siren_Slam_MeleeDamage", value=True)
GPart_Siren_Slam_DamageReduction = BoolOption(identifier="GPart_Siren_Slam_DamageReduction", display_name="PhaseSlam Dmg Reduction", description="After using Phaseslam, damage taken is reduced by $VALUE$ and", description_title="GPart_Siren_Slam_DamageReduction", value=True)
GPart_Siren_Grasp_ConstantNova = BoolOption(identifier="GPart_Siren_Grasp_ConstantNova", display_name="PhaseGrasp Nova", description="While Phasegrasp is active, Amara constantly triggers novas that deal $VALUE$ damage.", description_title="GPart_Siren_Grasp_ConstantNova", value=True)
GPart_Operative_DroneActive_FireRateReload = BoolOption(identifier="GPart_Operative_DroneActive_FireRateReload", display_name="SNTNL Fire Rate, Reload Speed", description="While SNTNL is active, Fire Rate is increased by $VALUE$, and Reload Speed by", description_title="GPart_Operative_DroneActive_FireRateReload", value=True)
GPart_Operative_DroneActiveBonusDamage = BoolOption(identifier="GPart_Operative_DroneActiveBonusDamage", display_name=" SNTNL Cryo damage.", description="While SNTNL is active, gain $VALUE$ of damage as bonus Cryo damage.", description_title="GPart_Operative_DroneActiveBonusDamage", value=True)
GPart_Operative_CloneSwapInstaReload = BoolOption(identifier="GPart_Operative_CloneSwapInstaReload", display_name="Digi-Clone swap reloaded.", description="After swapping places with your Digi-Clone, your weapon is reloaded.", description_title="GPart_Operative_CloneSwapInstaReload", value=True)
GPart_CloneSwap_WeaponDamage = BoolOption(identifier="GPart_CloneSwap_WeaponDamage", display_name="Digi-Clone swap Weapon Damage", description="After swapping places with your Digi-Clone, Weapon Damage is increased by $VALUE$ for a short time.", description_title="GPart_CloneSwap_WeaponDamage", value=True)
GPart_Operative_CloneActive_AmmoRegen = BoolOption(identifier="GPart_Operative_CloneActive_AmmoRegen", display_name="Digi-Clone active regenerate ammo", description="While Digi-Clone is active, regenerate $VALUE$ of magazine ammo per second.", description_title="GPart_Operative_CloneActive_AmmoRegen", value=True)
GPart_Operative_BarrierActive_AccuracyCrit = BoolOption(identifier="GPart_Operative_BarrierActive_AccuracyCrit", display_name="Barrier Accuracy", description="While Barrier is active, Accuracy is increased by $VALUE$, and", description_title="GPart_Operative_BarrierActive_AccuracyCrit", value=True)
GPart_Operative_BarrierActive_StatusEffectChance = BoolOption(identifier="GPart_Operative_BarrierActive_StatusEffectChance", display_name="Barrier Status Effect Chance", description="While Barrier is active, Status Effect Chance is increased by $VALUE$.", description_title="GPart_Operative_BarrierActive_StatusEffectChance", value=True)
GPart_Operative_DroneActiveMovespeed = BoolOption(identifier="GPart_Operative_DroneActiveMovespeed", display_name="SNTNL MoveSpeed", description="While SNTNL is active, Movement Speed is increased by $VALUE$.", description_title="GPart_Operative_DroneActiveMovespeed", value=True)
GPart_Operative_CloneActive_HealthRegen = BoolOption(identifier="GPart_Operative_CloneActive_HealthRegen", display_name="Digi-Clone Health Regen", description="While Digi-Clone is active, regenerate $VALUE$ max health per second.", description_title="GPart_Operative_CloneActive_HealthRegen", value=True)
GPart_Operative_BarrierDeploy_ShieldRecharge = BoolOption(identifier="GPart_Operative_BarrierDeploy_ShieldRecharge", display_name="Barrier Start, shield Recharge", description="When Barrier is Deployed, instantly start recharging your shields.", description_title="GPart_Operative_BarrierDeploy_ShieldRecharge", value=True)
GPart_Gunner_ShieldHealthMax = BoolOption(identifier="GPart_Gunner_ShieldHealthMax", display_name="IronBear Exit. Max Shield and Health", description="After exiting Iron Bear, gain $VALUE$ increased shields and health for", description_title="GPart_Gunner_ShieldHealthMax", value=True)
GPart_Gunner_KillsLowerCooldown = BoolOption(identifier="GPart_Gunner_KillsLowerCooldown", display_name="Exit Ironbear killstack cooldown", description="After exiting Iron Bear, kills increase Iron Bear's cooldown rate by $VALUE$.", description_title="GPart_Gunner_KillsLowerCooldown", value=True)
GPart_Gunner_EnterExit_Nova = BoolOption(identifier="GPart_Gunner_EnterExit_Nova", display_name="Exit IronBear Nova", description="When entering and exiting Iron Bear, create a nova that deals $VALUE$ damage.", description_title="GPart_Gunner_EnterExit_Nova", value=True)
GPart_Gunner_SplashDamageIncrease = BoolOption(identifier="GPart_Gunner_SplashDamageIncrease", display_name="exit Iron Bear, Splash damage", description="After exiting Iron Bear, gain $VALUE$ increased Splash damage for", description_title="GPart_Gunner_SplashDamageIncrease", value=True)
GPart_Gunner_NoAmmoConsumption = BoolOption(identifier="GPart_Gunner_NoAmmoConsumption", display_name="exit Iron Bear infinite ammo", description="After exiting Iron Bear, do not consume ammo for $VALUE$ seconds.", description_title="GPart_Gunner_NoAmmoConsumption", value=True)
GPart_Gunner_NextMagReloadHandling = BoolOption(identifier="GPart_Gunner_NextMagReloadHandling", display_name="exit Iron Bear  next mag reload speed and handling", description="After exiting Iron Bear, the next $VALUE$ magazines will have", description_title="GPart_Gunner_NextMagReloadHandling", value=True)
GPart_Gunner_NextMagFirerateCrit = BoolOption(identifier="GPart_Gunner_NextMagFirerateCrit", display_name="exit Iron Bear next mag firerate crit", description="After exiting Iron Bear, the next $VALUE$ magazines will have", description_title="GPart_Gunner_NextMagFirerateCrit", value=True)
GPart_Gunner_NextMagFireDamage = BoolOption(identifier="GPart_Gunner_NextMagFireDamage", display_name="exit Iron Bear next mag fire damage", description="After exiting Iron Bear, the next $VALUE$ magazines will have", description_title="GPart_Gunner_NextMagFireDamage", value=True)
GPart_Gunner_AutoBear_FireDamage = BoolOption(identifier="GPart_Gunner_AutoBear_FireDamage", display_name="Auto Bear fire damage.", description="While Auto Bear is active, deals $VALUE$ bonus Incendiary damage.", description_title="GPart_Gunner_AutoBear_FireDamage", value=True)
GPart_Gunner_AutoBear_AmmoRegen = BoolOption(identifier="GPart_Gunner_AutoBear_AmmoRegen", display_name="Auto Bear regen ammo", description="While Auto Bear is active, constantly regenerate $VALUE$ of magazine size per second.", description_title="GPart_Gunner_AutoBear_AmmoRegen", value=True)
GPart_Beast_Stealth_AccuracyHandling = BoolOption(identifier="GPart_Beast_Stealth_AccuracyHandling", display_name="Fade Away Accuracy Handling.", description="While Fade Away is active, gain greatly increased Accuracy and Handling.", description_title="GPart_Beast_Stealth_AccuracyHandling", value=True)
GPart_Beast_RakkCrit = BoolOption(identifier="GPart_Beast_RakkCrit", display_name="Rakk Attack Crit Damage", description="After using Rakk Attack!, gain $VALUE$ Critical Hit Damage for a short time.", description_title="GPart_Beast_RakkCrit", value=True)
GPart_Beast_RakkSlag = BoolOption(identifier="GPart_Beast_RakkSlag", display_name="Rakk Slag (Broken anoint)", description="Enemies damaged by Rakk Attack! take $VALUE$ increased damage for a short time.", description_title="GPart_Beast_RakkSlag", value=True)
GPart_BonusRadiationDamage = BoolOption(identifier="GPart_BonusRadiationDamage", display_name="Gamma Burstradiation damage.", description="While Gamma Burst is active, gain $VALUE$ bonus radiation damage.", description_title="GPart_BonusRadiationDamage", value=True)
GPart_Beast_AttackCmd_Lifesteal = BoolOption(identifier="GPart_Beast_AttackCmd_Lifesteal", display_name="Attack Command lifesteal", description="After using Attack Command, gain $VALUE$ lifesteal for a short time.", description_title="GPart_Beast_AttackCmd_Lifesteal", value=True)
GPart_Beast_ExitStealthNova = BoolOption(identifier="GPart_Beast_ExitStealthNova", display_name="FadeAway End Nova", description="When exiting Fade Away, create a nova that deals $VALUE$ damage.", description_title="GPart_Beast_ExitStealthNova", value=True)
GPart_Beast_RakkCharge = BoolOption(identifier="GPart_Beast_RakkCharge", display_name="Rakk charge", description="Grants an extra charge of Rakk Attack!", description_title="GPart_Beast_RakkCharge", value=True)
GPart_Beast_AttackCmd_Movespeed = BoolOption(identifier="GPart_Beast_AttackCmd_Movespeed", display_name="Attack command move speed", description="After issuing an Attack Command, gain $VALUE$ Movement Speed for a short time.", description_title="GPart_Beast_AttackCmd_Movespeed", value=True)


shield_nest = NestedOption(
    "Shields",
    [GPart_All_ShieldBreakAmp, GPart_All_ShockFeedback, GPart_All_SkillEnd_CooldownRate, GPart_All_SkillEnd_DamageReduction, GPart_All_SkillEnd_HealthRegen, GPart_All_SkillEnd_MeleeDamage, GPart_All_SkillEnd_MoveSpeed, GPart_All_SkillStart_OverchargeShield, GPart_All_SlideRegenShields]
)

def options_enable(nest):
    for option in nest:
        option.value = True

def options_disable(nest):
    for option in nest:
        option.value = False
        
shield_on_button = ButtonOption(
                "Enable All Shield Anoints",
                on_press=lambda _: options_enable(shield_nest.children),
            )

shield_off_button = ButtonOption(
    "Disable All Shield Anoints",
    on_press=lambda _: options_disable(shield_nest.children),
)

shield_group = GroupedOption(
    "Shield Anoints",
    [shield_on_button, shield_off_button, shield_nest]
)

gun_nest = NestedOption(
    "Guns",
    [GPart_All_SkillEnd_AccuracyHandling, GPart_All_SkillEnd_CritDamage, GPart_All_DamageMitigation, GPart_All_HealingPool, GPart_All_HighHealthBreaker, GPart_All_SkillEnd_EleChanceDamage, GPart_All_SkillEnd_FireRateReload, GPart_All_SkillEnd_LifeSteal, GPart_All_SkillEnd_NextMagBonusDamageCorrosive, GPart_All_SkillEnd_NextMagBonusDamageCryo, GPart_All_SkillEnd_NextMagBonusDamageFire, GPart_All_SkillEnd_NextMagBonusDamageRadiation, GPart_All_SkillEnd_NextMagBonusDamageShock, GPart_All_SkillEnd_ProjectileSpeed, GPart_All_SkillEnd_SplashDamage, GPart_All_SkillEnd_UniqueEnemyDamage, GPart_All_SkillEnd_WeaponDamage, GPart_All_UnhealthyRadDamage, GPart_All_UniqueEnemyDamage, GPart_All_WeaponDamage, GPart_EG_Gen_SkillActive_PulseFireNova, GPart_EG_Gen_SkillEnd_CyberSpike, GPart_EG_Generic_ConsecutiveHitsDmgStack, GPart_EG_Generic_KillStackReloadDamage, GPart_EG_Generic_LowHealthExecutor, GPart_EG_WhileAirborn_AccuracyHandling, GPart_EG_WhileAirborn_CritDamage, GPart_EG_WhileAirborn_Damage, GPart_EG_WhileAirborn_FireRate, GPart_EG_WhileSliding_AccuracyHandling, GPart_EG_WhileSliding_Damage, GPart_EG_WhileSliding_FireRate, GPart_Passive_All_CritStatusEffect]
)

gun_on_button = ButtonOption(
    "Enable All Gun Anoints",
    on_press=lambda _: options_enable(gun_nest.children),
)

gun_off_button = ButtonOption(
    "Disable All Gun Anoints",
    on_press=lambda _: options_disable(gun_nest.children),
)
gun_group = GroupedOption(
    "Gun Anoints",
    [gun_on_button, gun_off_button, gun_nest]
)


nade_nest = NestedOption(
    "Nades",
    [GPart_All_GrenadeDamage, GPart_All_SkillEnd_AddGrenade, GPart_EG_GrenadeThrow_GlobalDamage]
)

nade_on_button = ButtonOption(
    "Enable All Nade Anoints",
    on_press=lambda _: options_enable(nade_nest.children),
)

nade_off_button = ButtonOption(
    "Disable All Nade Anoints",
    on_press=lambda _: options_disable(nade_nest.children),
)

nade_group = GroupedOption(
    "Nade Anoints",
    [nade_on_button, nade_off_button, nade_nest]
)


nade_shield_nest = NestedOption(
    "Nades and Shields",
    [GPart_EG_SkillEndBonusEleDamage_Corrosive, GPart_EG_SkillEndBonusEleDamage_Cryo, GPart_EG_SkillEndBonusEleDamage_Fire, GPart_EG_SkillEndBonusEleDamage_Radiation, GPart_EG_SkillEndBonusEleDamage_Shock]
)

nade_shield_on_button = ButtonOption(
    "Enable All Nade and Shield Anoints",
    on_press=lambda _: options_enable(nade_shield_nest.children),
)

nade_shield_off_button = ButtonOption(
    "Disable All Nade and Shield Anoints",
    on_press=lambda _: options_disable(nade_shield_nest.children),
)

nade_shield_group = GroupedOption(
    "Nade and Shield Anoints",
    [nade_shield_on_button, nade_shield_off_button, nade_shield_nest]
)

terror_universal = GroupedOption(
    "Universal",
    [GPart_All_Passive_GenerateTerror_Melee, GPart_All_Passive_TerrorDamageMitigation, GPart_All_Passive_TerrorHealthRegen, GPart_All_SkillEnd_GenerateTerror, GPart_All_SkillEnd_TerrorHeal, GPart_Gunner_Reload_TerrorNova, GPart_Siren_Grasp_TerrorSkulls],
)

terror_shield_gun	= GroupedOption(
    "Shield/Gun",
	[GPart_All_Passive_TerrorAmmoRegen, GPart_All_Passive_TerrorBulletReflect, GPart_Beast_AttackCmd_TerrorFireDMG, GPart_Operative_DroneActiveTerrorLifesteal]
)

terror_grenade_gun = GroupedOption(
    "Grenade/Gun",
	[GPart_All_Passive_TerrorDamageFireRate]
)

terror_gun = GroupedOption(
    "Gun",
	[GPart_All_Passive_TerrorBonus_CryoDamage, GPart_All_Passive_TerrorCritDamage, GPart_All_Passive_TerrorProjectilesPerShot]
)

terror_nest = NestedOption(
    "Terror",
    [terror_universal, terror_shield_gun, terror_grenade_gun, terror_gun]
)

def options_enable_terror():
    options_enable(terror_universal.children)
    options_enable(terror_shield_gun.children)
    options_enable(terror_grenade_gun.children)
    options_enable(terror_gun.children)
    

def options_disable_terror():
    options_disable(terror_universal.children)
    options_disable(terror_shield_gun.children)
    options_disable(terror_grenade_gun.children)
    options_disable(terror_gun.children)
            
terror_on_button = ButtonOption(
    "Enable All Terror Anoints",
    on_press=lambda _: options_enable_terror(),
)

terror_off_button = ButtonOption(
    "Disable All Terror Anoints",
    on_press=lambda _: options_disable_terror(),
)

terror_group = GroupedOption(
    "Terror Anoints",
    [terror_on_button, terror_off_button, terror_nest]
)

gunner_gun = GroupedOption(
	"Guns",
	[GPart_Gunner_NoAmmoConsumption, GPart_Gunner_NextMagFirerateCrit, GPart_Gunner_NextMagReloadHandling, GPart_Gunner_AutoBear_AmmoRegen, GPart_Gunner_AutoBear_FireDamage, GPart_Gunner_BearFistDamage, GPart_Gunner_IronCubActiveDamage, GPart_Gunner_MinigunDamage, GPart_Gunner_NextMagFireDamage, GPart_Gunner_RailgunDamage, GPart_Gunner_SalamanderDamage, GPart_Gunner_SplashDamageIncrease, GPart_Gunner_V35LauncherDamage, GPart_Gunner_VanquisherDamage]
)
gunner_shield = GroupedOption(
	"Shield",
	[ GPart_Gunner_EnterExit_Nova, GPart_Gunner_ShieldHealthMax]
)
gunner_nade = GroupedOption(
	"Nade",
	[GPart_Gunner_IBGrenadeChance]
)
gunner_shield_gun = GroupedOption(
	"gun and Shield",
	[GPart_Gunner_KillsLowerCooldown]
)

gunner_nest = NestedOption(
    "Gunner",
    [gunner_gun, gunner_shield, gunner_nade, gunner_shield_gun]
)

def options_enable_gunner():
    options_enable(gunner_gun.children)
    options_enable(gunner_shield.children)
    options_enable(gunner_nade.children)
    options_enable(gunner_shield_gun.children)
    
def options_disable_gunner():
    options_disable(gunner_gun.children)
    options_disable(gunner_shield.children)
    options_disable(gunner_nade.children)
    options_disable(gunner_shield_gun.children)
    
gunner_on_button = ButtonOption(
    "Enable All Gunner Anoints",
    on_press=lambda _: options_enable_gunner(),
)

gunner_off_button = ButtonOption(
    "Disable All Gunner Anoints",
    on_press=lambda _: options_disable_gunner(),
)

gunner_group = GroupedOption(
    "Gunner Anoints",
    [gunner_on_button, gunner_off_button, gunner_nest]
)


bsm_gun = GroupedOption(
	"Guns",
	[GPart_Beast_RakkCrit, GPart_Beast_Stealth_AccuracyHandling, GPart_Beast_AttackCmd_Lifesteal, GPart_Beast_FadeActiveDamage, GPart_Beast_GravitySnareActiveDamage, GPart_Beast_RakkSlag]
)
bsm_shield = GroupedOption(
	"Shield",
	[GPart_Beast_AttackCmd_Movespeed, GPart_Beast_ExitStealthNova]
)
bsm_shield_gun = GroupedOption(
	"Guns and Shield",
	[GPart_Beast_RakkCharge]
)

bsm_nest = NestedOption(
    "Beast",
    [bsm_gun, bsm_shield, bsm_shield_gun]
)

def options_enable_bsm():
    options_enable(bsm_gun.children)
    options_enable(bsm_shield.children)
    options_enable(bsm_shield_gun.children)
    
def options_disable_bsm():
    options_disable(bsm_gun.children)
    options_disable(bsm_shield.children)
    options_disable(bsm_shield_gun.children)
    
bsm_on_button = ButtonOption(
    "Enable All Beast Anoints",
    on_press=lambda _: options_enable_bsm(),
)

bsm_off_button = ButtonOption(
    "Disable All Beast Anoints",
    on_press=lambda _: options_disable_bsm(),
)

bsm_group = GroupedOption(
    "Beast Anoints",
    [bsm_on_button, bsm_off_button, bsm_nest]
)

siren_gun = GroupedOption(
	"guns",
	[GPart_Siren_Cast_ElementalChance, GPart_Siren_Grasp_ChargeSpeed, GPart_Siren_Cast_WeaponDamage, GPart_Siren_GraspActiveDamage, GPart_Siren_PhasecastDamage, GPart_Siren_PhaseflareDamage, GPart_Siren_PhaseslamDamage, GPart_Siren_SkillEnd_AttunedSkillDamage, GPart_Siren_Slam_WeaponDamage,  GPart_BonusRadiationDamage]
)
siren_shield = GroupedOption(
	"Shield",
	[GPart_Siren_Grasp_AccuracyCrit, GPart_Siren_Grasp_ConstantNova, GPart_Siren_Slam_DamageReduction, GPart_Siren_Slam_MeleeDamage, GPart_Siren_Slam_ReturnDamage]
)

siren_nest = NestedOption(
    "Siren",
    [siren_gun, siren_shield]
)

def options_enable_siren():
    options_enable(siren_gun.children)
    options_enable(siren_shield.children)
    
def options_disable_siren():
    options_disable(siren_gun.children)
    options_disable(siren_shield.children)
    
siren_on_button = ButtonOption(
    "Enable All Siren Anoints",
    on_press=lambda _: options_enable_siren(),
)

siren_off_button = ButtonOption(
    "Disable All Siren Anoints",
    on_press=lambda _: options_disable_siren(),
)

siren_group = GroupedOption(
    "Siren Anoints",
    [siren_on_button, siren_off_button, siren_nest]
)



ope_gun = GroupedOption(
	"Gun",
	[GPart_Operative_BarrierActive_AccuracyCrit, GPart_Operative_CloneActive_AmmoRegen, GPart_Operative_CloneSwapInstaReload, GPart_Operative_DroneActive_FireRateReload, GPart_CloneSwap_WeaponDamage, GPart_Operative_BarrierActive_StatusEffectChance, GPart_Operative_DroneActiveBonusDamage, GPart_Operative_MNTISDamage]
)

ope_shield = GroupedOption(
	"Shield",
	[GPart_Operative_BarrierDeploy_ShieldRecharge, GPart_Operative_CloneActive_HealthRegen, GPart_Operative_DroneActiveMovespeed]
)

ope_nest = NestedOption(
    "Operative",
    [ope_gun, ope_shield]
)

def options_enable_ope():
    options_enable(ope_gun.children)
    options_enable(ope_shield.children)
    
def options_disable_ope():
    options_disable(ope_gun.children)
    options_disable(ope_shield.children)
    
ope_on_button = ButtonOption(
    "Enable All Operative Anoints",
    on_press=lambda _: options_enable_ope(),
)

ope_off_button = ButtonOption(
    "Disable All Operative Anoints",
    on_press=lambda _: options_disable_ope(),
)

ope_group = GroupedOption(
    "Operative Anoints",
    [ope_on_button, ope_off_button, ope_nest]
)

vh_nest = NestedOption(
    "Vault Hunter Anoints",
    [ope_group, bsm_group, gunner_group, siren_group]
)

def options_enable_vh():
	options_enable_ope()
	options_enable_bsm()
	options_enable_gunner()
	options_enable_siren()
    
def options_disable_vh():
    options_disable_ope()
    options_disable_bsm()
    options_disable_gunner()
    options_disable_siren()
    
vh_on_button = ButtonOption(
    "Enable All Vault Hunter Anoints",
    on_press=lambda _: options_enable_vh(),
)

vh_off_button = ButtonOption(
    "Disable All Vault Hunter Anoints",
    on_press=lambda _: options_disable_vh(),
)

vh_group = GroupedOption(
    "Vault Hunter Anoints",
    [vh_on_button, vh_off_button, vh_nest]
)

apply_button = ButtonOption(
      "Apply Anoints (May take a few seconds)",
      on_press=lambda _: change_all_anoints(),
)




anointments = [
GPart_Gunner_IBGrenadeChance,
GPart_All_SkillEnd_AddGrenade,
GPart_Siren_Grasp_ChargeSpeed,
GPart_All_SkillEnd_ProjectileSpeed,
GPart_Siren_Slam_WeaponDamage,
GPart_Siren_SkillEnd_AttunedSkillDamage,
GPart_Siren_Grasp_AccuracyCrit,
GPart_Siren_Cast_WeaponDamage,
GPart_Siren_Cast_ElementalChance,
GPart_Operative_DroneActive_FireRateReload,
GPart_Operative_DroneActiveBonusDamage,
GPart_Operative_CloneSwapInstaReload,
GPart_CloneSwap_WeaponDamage,
GPart_Operative_CloneActive_AmmoRegen,
GPart_Operative_BarrierActive_AccuracyCrit,
GPart_Operative_BarrierActive_StatusEffectChance,
GPart_Gunner_SplashDamageIncrease,
GPart_Gunner_NoAmmoConsumption,
GPart_Gunner_NextMagReloadHandling,
GPart_Gunner_NextMagFirerateCrit,
GPart_Gunner_NextMagFireDamage,
GPart_Gunner_AutoBear_FireDamage,
GPart_Gunner_AutoBear_AmmoRegen,
GPart_Beast_Stealth_AccuracyHandling,
GPart_Beast_RakkCrit,
GPart_Beast_RakkSlag,
GPart_BonusRadiationDamage,
GPart_Beast_AttackCmd_Lifesteal,
GPart_All_SkillEnd_WeaponDamage,
GPart_All_SkillEnd_UniqueEnemyDamage,
GPart_All_SkillEnd_SplashDamage,
GPart_All_SkillEnd_NextMagBonusDamageShock,
GPart_All_SkillEnd_NextMagBonusDamageRadiation,
GPart_All_SkillEnd_NextMagBonusDamageFire,
GPart_All_SkillEnd_NextMagBonusDamageCryo,
GPart_All_SkillEnd_NextMagBonusDamageCorrosive,
GPart_All_SkillEnd_LifeSteal,
GPart_All_SkillEnd_FireRateReload,
GPart_All_SkillEnd_EleChanceDamage,
GPart_All_SkillEnd_CritDamage,
GPart_All_SkillEnd_AccuracyHandling,
GPart_Siren_Slam_ReturnDamage,
GPart_Siren_Slam_MeleeDamage,
GPart_Siren_Slam_DamageReduction,
GPart_Siren_Grasp_ConstantNova,
GPart_Operative_DroneActiveMovespeed,
GPart_Operative_CloneActive_HealthRegen,
GPart_Operative_BarrierDeploy_ShieldRecharge,
GPart_Gunner_ShieldHealthMax,
GPart_Gunner_KillsLowerCooldown,
GPart_Gunner_EnterExit_Nova,
GPart_Beast_ExitStealthNova,
GPart_Beast_RakkCharge,
GPart_Beast_AttackCmd_Movespeed,
GPart_All_SkillEnd_MoveSpeed,
GPart_All_SkillEnd_MeleeDamage,
GPart_All_SkillEnd_HealthRegen,
GPart_All_SkillEnd_DamageReduction,
GPart_All_SkillEnd_CooldownRate,
GPart_Siren_Grasp_TerrorSkulls,
GPart_Operative_DroneActiveTerrorLifesteal,
GPart_Gunner_Reload_TerrorNova,
GPart_Beast_AttackCmd_TerrorFireDMG,
GPart_All_Passive_TerrorProjectilesPerShot,
GPart_All_Passive_TerrorHealthRegen,
GPart_All_Passive_TerrorDamageMitigation,
GPart_All_Passive_TerrorCritDamage,
GPart_All_Passive_TerrorBulletReflect,
GPart_All_Passive_TerrorBonus_CryoDamage,
GPart_All_Passive_TerrorAmmoRegen,
GPart_All_Passive_TerrorDamageFireRate,
GPart_All_SkillEnd_TerrorHeal,
GPart_All_SkillEnd_GenerateTerror,
GPart_All_Passive_GenerateTerror_Melee,
GPart_All_GrenadeDamage,
GPart_All_ShockFeedback,
GPart_All_SlideRegenShields,
GPart_All_ShieldBreakAmp,
GPart_All_SkillStart_OverchargeShield,
GPart_All_HealingPool,
GPart_All_WeaponDamage,
GPart_All_UniqueEnemyDamage,
GPart_EG_Gen_SkillActive_PulseFireNova,
GPart_All_DamageMitigation,
GPart_EG_Gen_SkillEnd_CyberSpike,
GPart_All_HighHealthBreaker,
GPart_All_UnhealthyRadDamage,
GPart_Passive_All_CritStatusEffect,
GPart_EG_GrenadeThrow_GlobalDamage,
GPart_EG_SkillEndBonusEleDamage_Shock,
GPart_EG_SkillEndBonusEleDamage_Radiation,
GPart_EG_SkillEndBonusEleDamage_Fire,
GPart_EG_SkillEndBonusEleDamage_Cryo,
GPart_EG_SkillEndBonusEleDamage_Corrosive,
GPart_EG_WhileSliding_FireRate,
GPart_EG_WhileSliding_Damage,
GPart_EG_WhileSliding_AccuracyHandling,
GPart_EG_WhileAirborn_FireRate,
GPart_EG_WhileAirborn_Damage,
GPart_EG_WhileAirborn_CritDamage,
GPart_EG_WhileAirborn_AccuracyHandling,
GPart_EG_Generic_LowHealthExecutor,
GPart_EG_Generic_KillStackReloadDamage,
GPart_EG_Generic_ConsecutiveHitsDmgStack,
GPart_Siren_PhaseslamDamage,
GPart_Siren_GraspActiveDamage,
GPart_Siren_PhaseflareDamage,
GPart_Siren_PhasecastDamage,
GPart_Operative_MNTISDamage,
GPart_Gunner_VanquisherDamage,
GPart_Gunner_V35LauncherDamage,
GPart_Gunner_SalamanderDamage,
GPart_Gunner_RailgunDamage,
GPart_Gunner_MinigunDamage,
GPart_Gunner_IronCubActiveDamage,
GPart_Gunner_BearFistDamage,
GPart_Beast_GravitySnareActiveDamage,
GPart_Beast_FadeActiveDamage,
]

anoint_inv = [
    "/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_01_Common.InvBalD_GrenadeMod_01_Common",
	"/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/InvBal_GrenadeBehavior_Money_3.InvBal_GrenadeBehavior_Money_3",
	"/Game/Gear/GrenadeMods/_Design/PartSets/Part_Behavior/Money/InvBal_GrenadeBehavior_Money_1.InvBal_GrenadeBehavior_Money_1",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod.InvBalD_GrenadeMod",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_04_VeryRare.InvBalD_GrenadeMod_04_VeryRare",
	"/Game/Gear/GrenadeMods/_Design/_Unique/WidowMaker/Balance/InvBalD_GM_WidowMaker.InvBalD_GM_WidowMaker",
	"/Game/Gear/GrenadeMods/_Design/_Unique/TranFusion/Balance/InvBalD_GM_TranFusion.InvBalD_GM_TranFusion",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Surge/Balance/InvBalD_GM_Surge.InvBalD_GM_Surge",
	"/Game/Gear/GrenadeMods/_Design/_Unique/StormFront/Balance/InvBalD_GM_StormFront.InvBalD_GM_StormFront",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Seeker/Balance/InvBalD_GM_Seeker.InvBalD_GM_Seeker",
	"/Game/Gear/GrenadeMods/_Design/_Unique/RedQueen/Balance/InvBalD_GM_RedQueen.InvBalD_GM_RedQueen",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Quasar/Balance/InvBalD_GM_Quasar.InvBalD_GM_Quasar",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Nagate/Balance/InvBalD_GM_Nagate.InvBalD_GM_Nagate",
	"/Game/Gear/GrenadeMods/_Design/_Unique/MoxiesBosom/Balance/InvBalD_GM_PAN_MoxiesBosom.InvBalD_GM_PAN_MoxiesBosom",
	"/Game/Gear/GrenadeMods/_Design/_Unique/HunterSeeker/Balance/InvBalD_GM_HunterSeeker.InvBalD_GM_HunterSeeker",
	"/Game/Gear/GrenadeMods/_Design/_Unique/HipHop/Balance/InvBalD_GM_TOR_HipHop.InvBalD_GM_TOR_HipHop",
	"/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm.InvBalD_GM_VLA_FireStorm",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Fastball/Balance/InvBalD_GM_TED_Fastball.InvBalD_GM_TED_Fastball",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Epicenter/Balance/InvBalD_GM_Epicenter.InvBalD_GM_Epicenter",
	"/Game/Gear/GrenadeMods/_Design/_Unique/EchoV2/Balance/InvBalD_GM_EchoV2.InvBalD_GM_EchoV2",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Shredifier/Balance/Balance_AR_VLA_Sherdifier.Balance_AR_VLA_Sherdifier",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Ogre/Balance/Balance_AR_VLA_Ogre.Balance_AR_VLA_Ogre",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/LuciansCall/Balance/Balance_AR_VLA_LuciansCall.Balance_AR_VLA_LuciansCall",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Faisor/Balance/Balance_AR_VLA_Faisor.Balance_AR_VLA_Faisor",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Dictator/Balance/Balance_AR_VLA_Dictator.Balance_AR_VLA_Dictator",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Damn/Balance/Balance_AR_VLA_Damn.Balance_AR_VLA_Damn",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/TryBolt/Balance/Balance_AR_TOR_TryBolt.Balance_AR_TOR_TryBolt",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/LaserSploder/Balance/Balance_AR_TOR_LaserSploder.Balance_AR_TOR_LaserSploder",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Bearcat/Balance/Balance_AR_TOR_Bearcat.Balance_AR_TOR_Bearcat",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/Alchemist/Balance/Balance_AR_TOR_Alchemist.Balance_AR_TOR_Alchemist",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/RowansCall/Balance/Balance_AR_JAK_RowansCall.Balance_AR_JAK_RowansCall",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/LeadSprinkler/Balance/Balance_AR_JAK_LeadSprinkler.Balance_AR_JAK_LeadSprinkler",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/GatlingGun/Balance/Balance_AR_JAK_04_GatlingGun.Balance_AR_JAK_04_GatlingGun",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Warlord/Balance/Balance_DAL_AR_Warlord.Balance_DAL_AR_Warlord",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/StarHelix/Balance/Balance_DAL_AR_StarHelix.Balance_DAL_AR_StarHelix",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Kaos/Balance/Balance_DAL_AR_Kaos.Balance_DAL_AR_Kaos",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/BOTD/Balance/Balance_DAL_AR_BOTD.Balance_DAL_AR_BOTD",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Barrage/Balance/Balance_DAL_AR_Barrage.Balance_DAL_AR_Barrage",
	"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/Sawbar/Balance/Balance_AR_COV_Sawbar.Balance_AR_COV_Sawbar",
	"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/_Unique/KriegAR/Balance/Balance_AR_COV_KriegAR.Balance_AR_COV_KriegAR",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/RebellYell/Balance/Balance_ATL_AR_RebelYell.Balance_ATL_AR_RebelYell",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Carrier/Balance/Balance_ATL_AR_Carrier.Balance_ATL_AR_Carrier",
	"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/CloudBurst/Balance/Balance_HW_VLA_CloudBurst.Balance_HW_VLA_CloudBurst",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Tunguska/Balance/Balance_HW_TOR_Tunguska.Balance_HW_TOR_Tunguska",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Swarm/Balance/Balance_HW_TOR_Swarm.Balance_HW_TOR_Swarm",
	"/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/RubysWrath/Balance/Balance_HW_ATL_RubysWrath.Balance_HW_ATL_RubysWrath",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Magnificent/Balance/Balance_PS_VLA_Magnificent.Balance_PS_VLA_Magnificent",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/Infiniti/Balance/Balance_PS_VLA_Infiniti.Balance_PS_VLA_Infiniti",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/RoisensThorns/Balance/Balance_PS_TOR_RoisensThorns.Balance_PS_TOR_RoisensThorns",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Foursum/Balance/Balance_PS_TOR_4SUM.Balance_PS_TOR_4SUM",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Echo/Balance/Balance_PS_TOR_Echo.Balance_PS_TOR_Echo",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Devestator/Balance/Balance_PS_TOR_Devestator.Balance_PS_TOR_Devestator",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Gunerang/Balance/Balance_PS_TED_Gunerang.Balance_PS_TED_Gunerang",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Balance_PS_Tediore_BabyMaker.Balance_PS_Tediore_BabyMaker",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/_Bangarang/Balance/Balance_PS_TED_Bangerang.Balance_PS_TED_Bangerang",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/ThunderballFist/Balance/Balance_PS_MAL_ThunderballFists.Balance_PS_MAL_ThunderballFists",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Plumber/Balance/Balance_PS_MAL_Plumber.Balance_PS_MAL_Plumber",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Hellshock/Balance/Balance_PS_MAL_Hellshock.Balance_PS_MAL_Hellshock",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/WagonWheel/Balance/Balance_PS_JAK_WagonWheel.Balance_PS_JAK_WagonWheel",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Unforgiven/Balance/Balance_PS_JAK_Unforgiven.Balance_PS_JAK_Unforgiven",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TheDuc/Balance/Balance_PS_JAK_TheDuc.Balance_PS_JAK_TheDuc",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/MelsCompanion/Balance/Balance_PS_JAK_MelsCompanion.Balance_PS_JAK_MelsCompanion",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Doc/Balance/Balance_PS_JAK_Doc.Balance_PS_JAK_Doc",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Nemesis/Balance/Balance_DAL_PS_Nemesis.Balance_DAL_PS_Nemesis",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Hornet/Balance/Balance_DAL_PS_Hornet.Balance_DAL_PS_Hornet",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/AAA/Balance/Balance_DAL_PS_AAA.Balance_DAL_PS_AAA",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Legion/Balance/Balance_PS_COV_Legion.Balance_PS_COV_Legion",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheBoringGun/Balance/Balance_SG_TOR_Boring.Balance_SG_TOR_Boring",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Flakker/Balance/Balance_SG_Torgue_Flakker.Balance_SG_Torgue_Flakker",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Polybius/Balance/Balance_SG_TED_Polybius.Balance_SG_TED_Polybius",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Wisp/Balance/Balance_SG_MAL_Wisp.Balance_SG_MAL_Wisp",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Trev/Balance/Balance_SG_MAL_Trev.Balance_SG_MAL_Trev",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Recursion/Balance/Balance_SG_MAL_Recursion.Balance_SG_MAL_Recursion",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/TheWave/Balance/Balance_SG_JAK_Unique_Wave.Balance_SG_JAK_Unique_Wave",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Hellwalker/Balance/Balance_SG_JAK_Hellwalker.Balance_SG_JAK_Hellwalker",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/TheButcher/Balance/Balance_SG_HYP_TheButcher.Balance_SG_HYP_TheButcher",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Redistributor/Balance/Balance_SG_HYP_Redistributor.Balance_SG_HYP_Redistributor",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/ConferenceCall/Balance/Balance_SG_HYP_ConferenceCall.Balance_SG_HYP_ConferenceCall",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Brick/Balance/Balance_SG_HYP_Brick.Balance_SG_HYP_Brick",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/TenGallon/Balance/Balance_SM_TED_TenGallon.Balance_SM_TED_TenGallon",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/NotAFlamethrower/Balance/Balance_SM_TED_NotAFlamethrower.Balance_SM_TED_NotAFlamethrower",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Devoted/Balance/Balance_SM_MAL_Devoted.Balance_SM_MAL_Devoted",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/DestructoSpin/Balance/Balance_SM_MAL_DestructoSpin.Balance_SM_MAL_DestructoSpin",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Cutsman/Balance/Balance_SM_MAL_Cutsman.Balance_SM_MAL_Cutsman",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/XZ/Balance/Balance_SM_HYP_XZ.Balance_SM_HYP_XZ",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Handsome/Balance/Balance_SM_HYP_Handsome.Balance_SM_HYP_Handsome",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Crossroad/Balance/Balance_SM_HYP_Crossroad.Balance_SM_HYP_Crossroad",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Bitch/Balance/Balance_SM_HYP_Bitch.Balance_SM_HYP_Bitch",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Vanquisher/Balance/Balance_SM_DAHL_Vanquisher.Balance_SM_DAHL_Vanquisher",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/SleepingGiant/Balance/Balance_SM_DAL_SleepingGiant.Balance_SM_DAL_SleepingGiant",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Ripper/Balance/Balance_SM_DAL_Ripper.Balance_SM_DAL_Ripper",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/Demoskag/Balance/Balance_SM_DAL_Demoskag.Balance_SM_DAL_Demoskag",
	"/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Lyuda/Balance/Balance_VLA_SR_Lyuda.Balance_VLA_SR_Lyuda",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Storm/Balance/Balance_MAL_SR_LGD_Storm.Balance_MAL_SR_LGD_Storm",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Krakatoa/Balance/Balance_MAL_SR_Krakatoa.Balance_MAL_SR_Krakatoa",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/ASMD/Balance/Balance_MAL_SR_ASMD.Balance_MAL_SR_ASMD",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Hunted/Balance/Balance_SR_JAK_Hunted.Balance_SR_JAK_Hunted",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Monocle/Balance/Balance_SR_JAK_Monocle.Balance_SR_JAK_Monocle",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/Woodblocks/Balance/Balance_SR_HYP_Woodblocks.Balance_SR_HYP_Woodblocks",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/MalaksBane/Balance/Balance_SR_DAL_ETech_MalaksBane.Balance_SR_DAL_ETech_MalaksBane",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin.InvBalD_Shield_Pangolin",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion.InvBalD_Shield_Hyperion",
	"/Game/Gear/Shields/_Design/_Uniques/BigBoomBlaster/BigBoomBlaster_Pickup/InvBal_BigBoomBlaster.InvBal_BigBoomBlaster",
	"/Game/Gear/Shields/_Design/_Uniques/Dispensary/Booster/Upper/InvBal_Pills_Upper.InvBal_Pills_Upper",
	"/Game/Gear/Shields/_Design/_Uniques/Dispensary/Booster/Downer/InvBal_Pills_Downer.InvBal_Pills_Downer",
	"/Game/Gear/Shields/_Design/PartSets/Part_Augment/Charges/Booster/BoosterPickup/InvBal_ShieldBooster.InvBal_ShieldBooster",
	"/Game/Gear/Shields/_Design/PartSets/Part_Augment/Charges/FortifyCharge/FortifyCharge_Pickup/InvBal_FortifyCharge.InvBal_FortifyCharge",
	"/Game/Gear/Shields/_Design/PartSets/Part_Augment/Charges/HealthCharge/HealthChargePickup/InvBal_HealthCharge.InvBal_HealthCharge",
	"/Game/Gear/Shields/_Design/PartSets/Part_Augment/Charges/PowerCharge/PowerCharge_Pickup/InvBal_PowerCharge.InvBal_PowerCharge",
	"/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/ActionSkill/Defs/InvBal_Beastmaster_Mod5ShieldBooster.InvBal_Beastmaster_Mod5ShieldBooster",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_01_Common.Balance_AR_VLA_01_Common",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_01_Common.Balance_AR_TOR_01_Common",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_01_Common.Balance_AR_JAK_01_Common",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_01_Common.Balance_DAL_AR_01_Common",
	"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_01_Common.Balance_AR_COV_01_Common",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_01_Common.Balance_ATL_AR_01_Common",
	"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_01_Common.Balance_HW_VLA_01_Common",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_01_Common.Balance_HW_TOR_01_Common",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_01_Common.Balance_HW_COV_01_Common",
	"/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_01_Common.Balance_HW_ATL_01_Common",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_01_Common.Balance_PS_VLA_01_Common",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_01_Common.Balance_PS_TOR_01_Common",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_01_Common.Balance_PS_Tediore_01_Common",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_01_Common.Balance_PS_MAL_01_Common",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_01_Common.Balance_PS_JAK_01_Common",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_01_Common.Balance_DAL_PS_01_Common",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_01_Common.Balance_PS_COV_01_Common",
	"/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_01_Common.Balance_PS_ATL_01_Common",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_01_Common.Balance_SG_Torgue_01_Common",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_01_Common.Balance_SG_TED_01_Common",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_01_Common.Balance_SG_MAL_01_Common",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_01_Common.Balance_SG_JAK_01_Common",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_01_Common.Balance_SG_HYP_01_Common",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_01_Common.Balance_SM_TED_01_Common",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_01_Common.Balance_SM_MAL_01_Common",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_01_Common.Balance_SM_HYP_01_Common",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_01_Common.Balance_SM_DAHL_01_Common",
	"/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_01_Common.Balance_VLA_SR_01_Common",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_01_Common.Balance_MAL_SR_01_Common",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_01_Common.Balance_SR_JAK_01_Common",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_01_Common.Balance_SR_HYP_01_Common",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_01_Common.Balance_SR_DAL_01_Common",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_02_UnCommon.Balance_AR_VLA_02_UnCommon",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_02_UnCommon.Balance_AR_TOR_02_UnCommon",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_02_UnCommon.Balance_AR_JAK_02_UnCommon",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_02_Uncommon.Balance_DAL_AR_02_Uncommon",
	"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_02_UnCommon.Balance_AR_COV_02_UnCommon",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_02_UnCommon.Balance_ATL_AR_02_UnCommon",
	"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_02_Uncommon.Balance_HW_VLA_02_Uncommon",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_02_Uncommon.Balance_HW_TOR_02_Uncommon",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_02_UnCommon.Balance_HW_COV_02_UnCommon",
	"/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_02_UnCommon.Balance_HW_ATL_02_UnCommon",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_02_UnCommon.Balance_PS_VLA_02_UnCommon",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_02_Uncommon.Balance_PS_TOR_02_Uncommon",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_02_UnCommon.Balance_PS_Tediore_02_UnCommon",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_02_UnCommon.Balance_PS_MAL_02_UnCommon",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_02_UnCommon.Balance_PS_JAK_02_UnCommon",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_02_UnCommon.Balance_DAL_PS_02_UnCommon",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_02_Uncommon.Balance_PS_COV_02_Uncommon",
	"/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_02_UnCommon.Balance_PS_ATL_02_UnCommon",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_02_UnCommon.Balance_SG_Torgue_02_UnCommon",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_02_Uncommon.Balance_SG_TED_02_Uncommon",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_02_Uncommon.Balance_SG_MAL_02_Uncommon",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_02_UnCommon.Balance_SG_JAK_02_UnCommon",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_02_Uncommon.Balance_SG_HYP_02_Uncommon",
	"/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_02_UnCommon.Balance_VLA_SR_02_UnCommon",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_02_UnCommon.Balance_MAL_SR_02_UnCommon",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_02_Uncommon.Balance_SR_JAK_02_Uncommon",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_02_Uncommon.Balance_SR_HYP_02_Uncommon",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_02_UnCommon.Balance_SR_DAL_02_UnCommon",
	"/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/Weapons/Balance_SG_HYP_PetLoaderWeapon.Balance_SG_HYP_PetLoaderWeapon",
	"/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/Weapons/Balance_SR_HYP_PetLoaderWeapon.Balance_SR_HYP_PetLoaderWeapon",
	"/Game/PlayerCharacters/Beastmaster/_DLC/Ixora/Pet/Loader/_Design/Weapons/Balance_SG_HYP_PetLoaderWeapon_Fire.Balance_SG_HYP_PetLoaderWeapon_Fire",
	"/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Weapons/JabberWeaponBase/Balance_PS_JAK_JabberWeaponBase.Balance_PS_JAK_JabberWeaponBase",
	"/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Weapons/JabberWeaponBeefcake/Balance_SG_JAK_JabberBeefcake.Balance_SG_JAK_JabberBeefcake",
	"/Game/PlayerCharacters/Beastmaster/Pet/Monkey/_Design/Weapons/JabberWeaponGunslinger/Balance_SM_DAHL_JabberWeaponGunslinger.Balance_SM_DAHL_JabberWeaponGunslinger",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_02_UnCommon.Balance_SM_TED_02_UnCommon",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_02_Uncommon.Balance_SM_MAL_02_Uncommon",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_02_UnCommon.Balance_SM_HYP_02_UnCommon",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_02_UnCommon.Balance_SM_DAHL_02_UnCommon",
	"/Game/PlayerCharacters/Operative/DigiClone/_Design/Weapon/Balance_HYP_SM_DigiClone_Backup.Balance_HYP_SM_DigiClone_Backup",
	"/Game/PlayerCharacters/Operative/DigiClone/_Design/Weapon/Balance_DAL_AR_DigiClone.Balance_DAL_AR_DigiClone",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/OperativeSkillSCreen/Balance_DAL_PS_OperativeSkillScreen.Balance_DAL_PS_OperativeSkillScreen",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin.InvBalD_Shield_Anshin",
	"/Game/Gear/Shields/_Design/_Uniques/WhiskeyTangoFoxtrot/Balance/InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot.InvBalD_Shield_Legendary_WhiskeyTangoFoxtrot",
	"/Game/Gear/Shields/_Design/_Uniques/Vamp/Balance/InvBalD_Shield_Legendary_Vamp.InvBalD_Shield_Legendary_Vamp",
	"/Game/Gear/Shields/_Design/_Uniques/Transformer/Balance/InvBalD_Shield_LGD_Transformer.InvBalD_Shield_LGD_Transformer",
	"/Game/Gear/Shields/_Design/_Uniques/StopGap/Balance/InvBalD_Shield_LGD_StopGap.InvBalD_Shield_LGD_StopGap",
	"/Game/Gear/Shields/_Design/_Uniques/SlideKick/Balance/InvBalD_Shield_LGD_SlideKick.InvBalD_Shield_LGD_SlideKick",
	"/Game/Gear/Shields/_Design/_Uniques/RoughRider/Balance/InvBalD_Shield_LGD_RoughRider.InvBalD_Shield_LGD_RoughRider",
	"/Game/Gear/Shields/_Design/_Uniques/Revengenader/Balance/InvBalD_Shield_LGD_Revengenader.InvBalD_Shield_LGD_Revengenader",
	"/Game/Gear/Shields/_Design/_Uniques/Rectifier/Balance/InvBalD_Shield_LGD_Rectifier.InvBalD_Shield_LGD_Rectifier",
	"/Game/Gear/Shields/_Design/_Uniques/Re-Charger/Balance/InvBalD_Shield_LGD_ReCharger.InvBalD_Shield_LGD_ReCharger",
	"/Game/Gear/Shields/_Design/_Uniques/NovaBurner/Balance/InvBalD_Shield_LGD_NovaBurner.InvBalD_Shield_LGD_NovaBurner",
	"/Game/Gear/Shields/_Design/_Uniques/Impaler/Balance/InvBalD_Shield_LGD_Impaler.InvBalD_Shield_LGD_Impaler",
	"/Game/Gear/Shields/_Design/_Uniques/FrontLoader/Balance/InvBalD_Shield_LGD_FrontLoader.InvBalD_Shield_LGD_FrontLoader",
	"/Game/Gear/Shields/_Design/_Uniques/BlackHole/Balance/InvBalD_Shield_LGD_BlackHole.InvBalD_Shield_LGD_BlackHole",
	"/Game/Gear/Shields/_Design/_Uniques/BigBoomBlaster/Balance/InvBalD_Shield_LGD_BigBoomBlaster.InvBalD_Shield_LGD_BigBoomBlaster",
	"/Game/Gear/Shields/_Design/_Uniques/BackHam/Balance/InvBalD_Shield_BackHam.InvBalD_Shield_BackHam",
	"/Game/PlayerCharacters/Gunner/_DLC/Ixora/HardPoints/Weapon/Balance_IronCub_AR_VLA.Balance_IronCub_AR_VLA",
	"/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Replay/Balance/Balance_PS_ATL_Replay.Balance_PS_ATL_Replay",
	"/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Redeye/Balance/Balance_HW_VLA_Redeye.Balance_HW_VLA_Redeye",
	"/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Disruptor/Balance/Balance_SR_JAK_Disruptor.Balance_SR_JAK_Disruptor",
	"/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Deatomizer/Balance/Balance_PS_MAL_Deatomizer.Balance_PS_MAL_Deatomizer",
	"/Game/PatchDLC/Ixora2/Gear/Shields/_Unique/Re-Volter/Balance/InvBalD_Shield_Revolter.InvBalD_Shield_Revolter",
	"/Game/PatchDLC/Ixora2/Gear/GrenadeMods/_Unique/Ringer/Balance/InvBalD_GM_Ringer.InvBalD_GM_Ringer",
	"/Game/PatchDLC/Ixora2/Gear/GrenadeMods/_Unique/Mesmer/Balance/InvBalD_GM_Mesmer.InvBalD_GM_Mesmer",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Trickshot/Balance/Balance_PS_JAK_Trickshot.Balance_PS_JAK_Trickshot",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Torrent/Balance/Balance_SM_DAL_Torrent.Balance_SM_DAL_Torrent",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Tizzy/Balance/Balance_PS_COV_Tizzy.Balance_PS_COV_Tizzy",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/SpiritOfMaya/Balance/Balance_PS_ATL_SpiritOfMaya.Balance_PS_ATL_SpiritOfMaya",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/PlasmaCoil/Balance/Balance_SM_MAL_PlasmaCoil.Balance_SM_MAL_PlasmaCoil",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Kickcharger/Balance/Balance_HW_VLA_ETech_Kickcharger.Balance_HW_VLA_ETech_Kickcharger",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/IceAge/Balance/Balance_HW_TOR_IceAge.Balance_HW_TOR_IceAge",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/HotfootTeddy/Balance/Balance_AR_TOR_Hotfoot.Balance_AR_TOR_Hotfoot",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Firefly/Balance/Balance_PS_VLA_Firefly.Balance_PS_VLA_Firefly",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/DarkArmy/Balance/Balance_SM_TED_DarkArmy.Balance_SM_TED_DarkArmy",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/CriticalThug/Balance/Balance_SG_Torgue_CriticalThug.Balance_SG_Torgue_CriticalThug",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Boogeyman/Balance/Balance_VLA_SR_Boogeyman.Balance_VLA_SR_Boogeyman",
	"/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/BinaryOperator/Balance/Balance_MAL_SR_BinaryOperator.Balance_MAL_SR_BinaryOperator",
	"/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Ventilator/Balance/InvBalD_Shield_Ventilator.InvBalD_Shield_Ventilator",
	"/Game/PatchDLC/Ixora/Gear/Shields/_Unique/MadCap/Balance/InvBalD_Shield_LGD_Madcap.InvBalD_Shield_LGD_Madcap",
	"/Game/PatchDLC/Ixora/Gear/Shields/_Unique/InfernalWish/Balance/InvBalD_Shield_InfernalWish.InvBalD_Shield_InfernalWish",
	"/Game/PatchDLC/Ixora/Gear/Shields/_Unique/Beskar/Balance/InvBalD_Shield_Beskar.InvBalD_Shield_Beskar",
	"/Game/PatchDLC/Ixora/Gear/GrenadeMods/HOTSpring/Balance/InvBalD_GM_HOTSpring.InvBalD_GM_HOTSpring",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Voice/Balance/Balance_PS_TOR_Voice_Epic.Balance_PS_TOR_Voice_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Voice/Balance/Balance_PS_TOR_Voice.Balance_PS_TOR_Voice",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Septimator/Balance/Balance_VLA_SR_Septimator_Epic.Balance_VLA_SR_Septimator_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Septimator/Balance/Balance_VLA_SR_Septimator.Balance_VLA_SR_Septimator",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Sawhorse/Balance/Balance_AR_COV_Sawhorse_Epic.Balance_AR_COV_Sawhorse_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Sawhorse/Balance/Balance_AR_COV_Sawhorse.Balance_AR_COV_Sawhorse",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3_Parent.Balance_SM_TED_PatMk3_Parent",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3_Epic.Balance_SM_TED_PatMk3_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/PAT_Mk3/Balance/Balance_SM_TED_PatMk3.Balance_SM_TED_PatMk3",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/LovableRogue/Balance/Balance_AR_TOR_LovableRogue_Epic.Balance_AR_TOR_LovableRogue_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/LovableRogue/Balance/Balance_AR_TOR_LovableRogue.Balance_AR_TOR_LovableRogue",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence_Epic.Balance_SG_HYP_Convergence_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence.Balance_SG_HYP_Convergence",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit_Epic.Balance_SG_MAL_BlindBandit_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BlindBandit/Balance/Balance_SG_MAL_BlindBandit.Balance_SG_MAL_BlindBandit",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BanditLauncher/Balance/Balance_HW_COV_BanditLauncher_Epic.Balance_HW_COV_BanditLauncher_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/BanditLauncher/Balance/Balance_HW_COV_BanditLauncher.Balance_HW_COV_BanditLauncher",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/AshenBeast/Balance/Balance_SM_DAL_ETech_AshenBeast_Epic.Balance_SM_DAL_ETech_AshenBeast_Epic",
	"/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/AshenBeast/Balance/Balance_SM_DAL_ETech_AshenBeast.Balance_SM_DAL_ETech_AshenBeast",
	"/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/PlusUltra/Balance/InvBalD_Shield_Legendary_PlusUltra_Epic.InvBalD_Shield_Legendary_PlusUltra_Epic",
	"/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/PlusUltra/Balance/InvBalD_Shield_Legendary_PlusUltra.InvBalD_Shield_Legendary_PlusUltra",
	"/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/FaultyStar/Balance/InvBalD_Shield_Legendary_FaultyStar_Epic.InvBalD_Shield_Legendary_FaultyStar_Epic",
	"/Game/PatchDLC/Alisma/Gear/Shields/_Uniques/FaultyStar/Balance/InvBalD_Shield_Legendary_FaultyStar.InvBalD_Shield_Legendary_FaultyStar",
	"/Game/PatchDLC/Takedown2/Gear/Weapons/WebSlinger/Balance/Balance_AR_VLA_WebSlinger.Balance_AR_VLA_WebSlinger",
	"/Game/PatchDLC/Takedown2/Gear/Weapons/Smog/Balance/Balance_SM_HYP_Smog.Balance_SM_HYP_Smog",
	"/Game/PatchDLC/Takedown2/Gear/Weapons/Globetrotter/Balance/Balance_HW_COV_Globetrotter.Balance_HW_COV_Globetrotter",
	"/Game/PatchDLC/Takedown2/Gear/Shields/Stinger/Balance/InvBalD_Shield_LGD_Stinger.InvBalD_Shield_LGD_Stinger",
	"/Game/PatchDLC/Takedown2/Gear/Shields/Aesclepius/Balance/InvBalD_Shield_LGD_Aesclepius.InvBalD_Shield_LGD_Aesclepius",
	"/Game/PatchDLC/Takedown2/Gear/GrenadeMods/Lightspeed/Balance/InvBalD_GM_HYP_Lightspeed.InvBalD_GM_HYP_Lightspeed",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/ZheitsevEruption/Balance/Balance_AR_COV_Zheitsev.Balance_AR_COV_Zheitsev",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Tankman/Balance/Balance_SR_HYP_Tankman.Balance_SR_HYP_Tankman",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/PurpleSMG/Balance_SM_DAHL_LowLvlReturningGift.Balance_SM_DAHL_LowLvlReturningGift",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet.Balance_AR_TOR_Juliet",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juju/Balance/Balance_DAL_AR_ETech_Juju.Balance_DAL_AR_ETech_Juju",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Execute/Balance/Balance_PS_TED_Execute.Balance_PS_TED_Execute",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/DeathGrip/Balance/Balance_SG_MAL_DeathGrip.Balance_SG_MAL_DeathGrip",
	"/Game/PatchDLC/Raid1/Re-Engagement/Weapons/CraderMP5/Balance/Balance_SM_DAHL_CraderMP5.Balance_SM_DAHL_CraderMP5",
	"/Game/PatchDLC/Raid1/Gear/Weapons/TiggsBoom/Balance/Balance_SG_Torgue_TiggsBoom.Balance_SG_Torgue_TiggsBoom",
	"/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link",
	"/Game/PatchDLC/Raid1/Gear/Weapons/KybsWorth/Balance/Balance_SM_MAL_KybsWorth.Balance_SM_MAL_KybsWorth",
	"/Game/PatchDLC/Raid1/Gear/Weapons/HandCannon/Balance/Balance_PS_TOR_HandCannon.Balance_PS_TOR_HandCannon",
	"/Game/PatchDLC/Raid1/Gear/Weapons/Fork2/Balance/Balance_SM_HYP_Fork2.Balance_SM_HYP_Fork2",
	"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger",
	"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart",
	"/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner",
	"/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/SandHawk/Balance/Balance_SR_DAL_SandHawk.Balance_SR_DAL_SandHawk",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Reflux/Balance/Balance_SG_HYP_Reflux.Balance_SG_HYP_Reflux",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Plague/Balance/Balance_HW_TOR_Plague.Balance_HW_TOR_Plague",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch.Balance_AR_VLA_Monarch",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson.Balance_SM_DAHL_Kaoson",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DoubleTap/Balance/Balance_PS_ATL_DoubleTap.Balance_PS_ATL_DoubleTap",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/DNA/Balance/Balance_SM_MAL_DNA.Balance_SM_MAL_DNA",
	"/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner.Balance_HW_VLA_ETech_BackBurner",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/UnseenThreat/Balance/Balance_SR_JAK_UnseenThreat.Balance_SR_JAK_UnseenThreat",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense_MissionWeapon.Balance_PS_JAK_TheSeventhSense_MissionWeapon",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheSeventhSense/Balance/Balance_PS_JAK_TheSeventhSense.Balance_PS_JAK_TheSeventhSense",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheNothing/Balance/Balance_SG_MAL_TheNothing.Balance_SG_MAL_TheNothing",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/TheCure/Balance/Balance_SG_JAK_TheCure.Balance_SG_JAK_TheCure",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SparkyBoom/Balance/Balance_AR_COV_SparkyBoom.Balance_AR_COV_SparkyBoom",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender.Balance_DAL_AR_Soulrender",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher.Balance_SR_JAK_Skullmasher",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Shocker/Balance/Balance_SG_Torgue_ETech_Shocker.Balance_SG_Torgue_ETech_Shocker",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SFForce/Balance/Balance_SM_MAL_SFForce.Balance_SM_MAL_SFForce",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SS_L.Balance_PS_JAK_SS_L",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SeventhSense/Balance/Balance_PS_JAK_SeventhSense.Balance_PS_JAK_SeventhSense",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/SacrificalLamb/Balance/Balance_SG_TED_SacrificialLamb.Balance_SG_TED_SacrificialLamb",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Mutant/Balance/Balance_AR_JAK_Mutant.Balance_AR_JAK_Mutant",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill_Legendary.Balance_PS_JAK_LoveDrill_Legendary",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LoveDrill/Balance/Balance_PS_JAK_LoveDrill.Balance_PS_JAK_LoveDrill",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/LittleYeeti/Balance/Balance_PS_JAK_LittleYeeti.Balance_PS_JAK_LittleYeeti",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Kaleidoscope/Balance/Balance_DAL_PS_Kaleidoscope.Balance_DAL_PS_Kaleidoscope",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Hydrafrost/Balance/Balance_PS_COV_Hydrafrost.Balance_PS_COV_Hydrafrost",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/FrozenDevil/Balance/Balance_PS_MAL_FrozenDevil.Balance_PS_MAL_FrozenDevil",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Firecracker/Balance/Balance_SG_HYP_Firecracker.Balance_SG_HYP_Firecracker",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/CockyBastard/Balance/Balance_SR_JAK_CockyBastard.Balance_SR_JAK_CockyBastard",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Clairvoyance/Balance/Balance_AR_JAK_Clairvoyance.Balance_AR_JAK_Clairvoyance",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/BiteSize/Balance/Balance_PS_JAK_BiteSize.Balance_PS_JAK_BiteSize",
	"/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy.Balance_SG_TED_Anarchy",
	"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/VoidRift/Balance/InvBalD_Shield_LGD_VoidRift.InvBalD_Shield_LGD_VoidRift",
	"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch.InvBalD_Shield_Legendary_Torch",
	"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod.InvBalD_Shield_OldGod",
	"/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Initiative/Balance/InvBalD_Shield_Initiative.InvBalD_Shield_Initiative",
	"/Game/PatchDLC/Hibiscus/Gear/NPC_Weapons/Private_Eye/Balance_PS_JAK_Private_Eye.Balance_PS_JAK_Private_Eye",
	"/Game/PatchDLC/Hibiscus/Gear/NPC_Weapons/Hammerlock/Balance_AR_JAK_Hammerlock_Hib.Balance_AR_JAK_Hammerlock_Hib",
	"/Game/PatchDLC/Hibiscus/Gear/NPC_Weapons/Gaige/Balance_AR_VLA_Gaige_Hib.Balance_AR_VLA_Gaige_Hib",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/UnkemptHarold/Balance/Balance_PS_TOR_UnkemptHarold.Balance_PS_TOR_UnkemptHarold",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/StoneThrow/Balance/Balance_AR_JAK_Stonethrow.Balance_AR_JAK_Stonethrow",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Splinter/Balance/Balance_SG_JAK_Splinter.Balance_SG_JAK_Splinter",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/SpeakEasy/Balance/Balance_SG_JAK_SpeakEasy.Balance_SG_JAK_SpeakEasy",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Shoveler/Balance/Balance_SG_Torgue_Shoveler.Balance_SG_Torgue_Shoveler",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Sheriff/Balance/Balance_PS_JAK_Sheriff.Balance_PS_JAK_Sheriff",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Satisfaction/Balance/Balance_HW_TOR_Satisfaction.Balance_HW_TOR_Satisfaction",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Rose/Balance/Balance_PS_JAK_Rose.Balance_PS_JAK_Rose",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/QuickDraw/Balance/Balance_PS_JAK_QuickDraw.Balance_PS_JAK_QuickDraw",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/PrivateInvestigator/Balance/Balance_DAL_PS_PrivateInvestigator.Balance_DAL_PS_PrivateInvestigator",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Plumage/Balance/Balance_HW_ATL_Plumage.Balance_HW_ATL_Plumage",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Peashooter/Balance/Balance_PS_JAK_Peashooter.Balance_PS_JAK_Peashooter",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Narp/Balance/Balance_SR_HYP_Narp.Balance_SR_HYP_Narp",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Miscreant/Balance/Balance_PS_VLA_Miscreant.Balance_PS_VLA_Miscreant",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/McSmugger/Balance/Balance_AR_JAK_McSmugger.Balance_AR_JAK_McSmugger",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Lasocannon/Balance/Balance_PS_VLA_Lasocannon.Balance_PS_VLA_Lasocannon",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ImaginaryNumber/Balance/Balance_MAL_SR_ImaginaryNumber.Balance_MAL_SR_ImaginaryNumber",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Gargoyle/Balance/Balance_PS_COV_Gargoyle.Balance_PS_COV_Gargoyle",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Frequency/Balance/Balance_SG_MAL_Frequency.Balance_SG_MAL_Frequency",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper.Balance_SM_MAL_Flipper",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/Balance/Balance_SG_JAK_Fakobs.Balance_SG_JAK_Fakobs",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Earthbound/Balance/Balance_SM_TED_Earthbound.Balance_SM_TED_Earthbound",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/DowsingRod/Balance/Balance_AR_VLA_Dowsing.Balance_AR_VLA_Dowsing",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Decoupler/Balance/Balance_PS_MAL_Decoupler.Balance_PS_MAL_Decoupler",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Dakota/Balance/Balance_SG_JAK_Dakota.Balance_SG_JAK_Dakota",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Copybeast/Balance/Balance_SM_HYP_Copybeast.Balance_SM_HYP_Copybeast",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/CoolBeans/Balance/Balance_AR_JAK_CoolBeans.Balance_AR_JAK_CoolBeans",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/ContainedExplosion/Balance/Balance_AR_TOR_Contained.Balance_AR_TOR_Contained",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BubbleBlaster/Balance/Balance_PS_MAL_BubbleBlaster.Balance_PS_MAL_BubbleBlaster",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Brightside/Balance/Balance_SG_TED_Brightside.Balance_SG_TED_Brightside",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Shock.Balance_AR_COV_BioBetsy_Shock",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/BioBetsy/Balance/Balance_AR_COV_BioBetsy_Rad.Balance_AR_COV_BioBetsy_Rad",
	"/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Antler/Balance/Balance_SG_MAL_ETech_Antler.Balance_SG_MAL_ETech_Antler",
	"/Game/PatchDLC/Geranium/Gear/Grenade/SkagOil/Balance/InvBalD_GM_SkagOil.InvBalD_GM_SkagOil",
	"/Game/PatchDLC/Geranium/Gear/Grenade/CoreBurst/Balance/InvBalD_GM_CoreBurst.InvBalD_GM_CoreBurst",
	"/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/WeddingInvitation/Balance/Balance_SR_JAK_WeddingInvite.Balance_SR_JAK_WeddingInvite",
	"/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/TwitchPrime/Balance/Balance_SG_TED_Twitch.Balance_SG_TED_Twitch",
	"/Game/PatchDLC/EventVDay/Gear/Weapon/_Unique/PolyAim/Balance/Balance_SM_MAL_PolyAim.Balance_SM_MAL_PolyAim",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/YellowCake/Balance/Balance_HW_COV_ETech_YellowCake.Balance_HW_COV_ETech_YellowCake",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/Pricker/Balance/Balance_SM_HYP_Pricker.Balance_SM_HYP_Pricker",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/PewPew/Balance/Balance_AR_COV_PewPew.Balance_AR_COV_PewPew",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/OPQ/Balance/Balance_ATL_AR_OPQ.Balance_ATL_AR_OPQ",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/NeedleGun/Balance/Balance_SM_TED_NeedleGun.Balance_SM_TED_NeedleGun",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IcePick/Balance/Balance_PS_MAL_IcePick.Balance_PS_MAL_IcePick",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/IceBurger/Balance/Balance_SG_HYP_IceBurger.Balance_SG_HYP_IceBurger",
	"/Game/PatchDLC/Event2/Gear/Weapon/_Unique/GreaseTrap/Balance/Balance_PS_MAL_GreaseTrap.Balance_PS_MAL_GreaseTrap",
	"/Game/PatchDLC/Event2/Gear/Shield/_Unique/Wattson/Balance/InvBalD_Shield_Legendary_Wattson.InvBalD_Shield_Legendary_Wattson",
	"/Game/PatchDLC/Event2/Gear/Shield/_Unique/MEAT/Balance/InvBalD_Shield_Legendary_MEAT.InvBalD_Shield_Legendary_MEAT",
	"/Game/PatchDLC/Event2/Gear/Shield/_Unique/MEAT/InvBal_MEAT_Booster.InvBal_MEAT_Booster",
	"/Game/PatchDLC/Event2/Gear/Shield/_Unique/Firewall/Balance/InvBalD_Shield_Legendary_Firewall.InvBalD_Shield_Legendary_Firewall",
	"/Game/PatchDLC/Event2/Gear/GrenadeMods/FishSlap/Balance/InvBalD_GM_FishSlap.InvBalD_GM_FishSlap",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Varlope/Balance/Balance_AR_TOR_Varlope.Balance_AR_TOR_Varlope",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Trash/Balance/Balance_AR_COV_Trash.Balance_AR_COV_Trash",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/SlowHand/Balance/Balance_SG_HYP_SlowHand.Balance_SG_HYP_SlowHand",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Scoville/Balance/Balance_PS_TOR_Scoville.Balance_PS_TOR_Scoville",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/RoboMasher/Balance/Balance_PS_JAK_RoboMasher.Balance_PS_JAK_RoboMasher",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Nukem/Balance/Balance_HW_TOR_Nukem.Balance_HW_TOR_Nukem",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/MeltFacer/Balance/Balance_SG_HYP_MeltFacer.Balance_SG_HYP_MeltFacer",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7.Balance_PS_JAK_Lucky7",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic.Balance_SM_HYP_JustCaustic",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonLaser/Balance/Balance_SM_MAL_IonLaser.Balance_SM_MAL_IonLaser",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/IonCannon/Balance/Balance_HW_VLA_IonCannon.Balance_HW_VLA_IonCannon",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/HeartBreaker/Balance/Balance_SG_HYP_HeartBreaker.Balance_SG_HYP_HeartBreaker",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/EmbersPurge/Balance/Balance_SM_MAL_EmbersPurge.Balance_SM_MAL_EmbersPurge",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Digby/Balance/Balance_DAL_AR_Digby.Balance_DAL_AR_Digby",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Creamer/Balance/Balance_HW_TOR_Creamer.Balance_HW_TOR_Creamer",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Craps/Balance/Balance_PS_TOR_Craps.Balance_PS_TOR_Craps",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/Balance/Balance_SM_HYP_CheapTips.Balance_SM_HYP_CheapTips",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/CheapTips/InvBal_Pickup_CheapTips.InvBal_Pickup_CheapTips",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Boomer/Balance/Balance_SM_DAL_Boomer.Balance_SM_DAL_Boomer",
	"/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/AutoAime/Balance/Balance_SR_DAL_AutoAime.Balance_SR_DAL_AutoAime",
	"/Game/PatchDLC/Dandelion/Gear/Shield/Rico/Balance/InvBalD_Shield_Rico.InvBalD_Shield_Rico",
	"/Game/PatchDLC/Dandelion/Gear/Shield/Ember/Balance/InvBalD_Shield_Ember.InvBalD_Shield_Ember",
	"/Game/PatchDLC/Dandelion/Gear/Shield/DoubleDowner/Balance/InvBalD_Shield_DoubleDowner.InvBalD_Shield_DoubleDowner",
	"/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Booster/Luck/InvBal_Clover_Luck.InvBal_Clover_Luck",
	"/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Booster/ActionSkillCooldown/InvBal_Clover_ActionSkillCooldown.InvBal_Clover_ActionSkillCooldown",
	"/Game/PatchDLC/Dandelion/Gear/Shield/Clover/Balance/InvBalD_Shield_Clover.InvBalD_Shield_Clover",
	"/Game/PatchDLC/Dandelion/Gear/Grenade/Slider/Balance/InvBalD_GM_TED_Slider.InvBalD_GM_TED_Slider",
	"/Game/PatchDLC/Dandelion/Gear/Grenade/AcidBurn/Balance/InvBalD_GM_AcidBurn.InvBalD_GM_AcidBurn",
	"/Game/PatchDLC/BloodyHarvest/Gear/Weapons/SniperRifles/Dahl/_Design/_Unique/Frostbolt/Balance/Balance_SR_DAL_ETech_Frostbolt.Balance_SR_DAL_ETech_Frostbolt",
	"/Game/PatchDLC/BloodyHarvest/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Fearmonger/Balance/Balance_SG_HYP_ETech_Fearmonger.Balance_SG_HYP_ETech_Fearmonger",
	"/Game/PatchDLC/BloodyHarvest/Gear/Shields/_Design/_Unique/ScreamOfPain/Balance/InvBalD_Shield_ScreamOfTerror.InvBalD_Shield_ScreamOfTerror",
	"/Game/PatchDLC/BloodyHarvest/Gear/GrenadeMods/_Design/_Unique/FontOfDarkness/Balance/InvBalD_GM_TOR_FontOfDarkness.InvBalD_GM_TOR_FontOfDarkness",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Vladof/Balance/Balance_SR_VLA_ETech_VeryRare.Balance_SR_VLA_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Vladof/Balance/Balance_SR_VLA_ETech_Rare.Balance_SR_VLA_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_VeryRare.Balance_SR_MAL_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Maliwan/Balance/Balance_SR_MAL_ETech_Rare.Balance_SR_MAL_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Hyperion/Balance/Balance_SR_HYP_ETech_VeryRare.Balance_SR_HYP_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Hyperion/Balance/Balance_SR_HYP_ETech_Rare.Balance_SR_HYP_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Dahl/Balance/Balance_SR_DAL_ETech_VeryRare.Balance_SR_DAL_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SniperRifles/Dahl/Balance/Balance_SR_DAL_ETech_Rare.Balance_SR_DAL_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Tediore/Balance/Balance_SM_TED_ETech_VeryRare.Balance_SM_TED_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Tediore/Balance/Balance_SM_TED_ETech_Rare.Balance_SM_TED_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_VeryRare.Balance_SM_MAL_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Maliwan/Balance/Balance_SM_MAL_ETech_Rare.Balance_SM_MAL_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Hyperion/Balance/Balance_SM_HYP_ETech_VeryRare.Balance_SM_HYP_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Hyperion/Balance/Balance_SM_HYP_ETech_Rare.Balance_SM_HYP_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Dahl/Balance/Balance_SM_DAL_ETech_VeryRare.Balance_SM_DAL_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/SMGs/Dahl/Balance/Balance_SM_DAL_ETech_Rare.Balance_SM_DAL_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_VeryRare.Balance_SG_Torgue_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Torgue/Balance/Balance_SG_Torgue_ETech_Rare.Balance_SG_Torgue_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Tediore/Balance/Balance_SG_TED_ETech_VeryRare.Balance_SG_TED_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Tediore/Balance/Balance_SG_TED_ETech_Rare.Balance_SG_TED_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_VeryRare.Balance_SG_MAL_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Maliwan/Balance/Balance_SG_MAL_ETech_Rare.Balance_SG_MAL_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Hyperion/Balance/Balance_SG_HYP_ETech_VeryRare.Balance_SG_HYP_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Shotgun/Hyperion/Balance/Balance_SG_HYP_ETech_Rare.Balance_SG_HYP_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_VeryRare.Balance_PS_VLA_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Vladof/Balance/Balance_PS_VLA_ETech_Rare.Balance_PS_VLA_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_VeryRare.Balance_PS_TOR_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TOR/Balance/Balance_PS_TOR_ETech_Rare.Balance_PS_TOR_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_VeryRare.Balance_PS_Tediore_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/TED/Balance/Balance_PS_Tediore_ETech_Rare.Balance_PS_Tediore_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_VeryRare.Balance_PS_MAL_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/MAL/Balance/Balance_PS_MAL_ETech_Rare.Balance_PS_MAL_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_VeryRare.Balance_DAL_PS_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/Dahl/Balance/Balance_DAL_PS_ETech_Rare.Balance_DAL_PS_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_VeryRare.Balance_PS_COV_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/Pistol/COV/Balance/Balance_PS_COV_ETech_Rare.Balance_PS_COV_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/VLA/Balance/Balance_HW_VLA_ETech_VeryRare.Balance_HW_VLA_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/VLA/Balance/Balance_HW_VLA_ETech_Rare.Balance_HW_VLA_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/TOR/Balance/Balance_HW_TOR_ETech_VeryRare.Balance_HW_TOR_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/TOR/Balance/Balance_HW_TOR_ETech_Rare.Balance_HW_TOR_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/COV/Balance/Balance_HW_COV_ETech_VeryRare.Balance_HW_COV_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/HW/COV/Balance/Balance_HW_COV_ETech_Rare.Balance_HW_COV_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/VLA/Balance/Balance_AR_VLA_ETech_VeryRare.Balance_AR_VLA_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/VLA/Balance/Balance_AR_VLA_ETech_Rare.Balance_AR_VLA_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/TOR/Balance/Balance_AR_TOR_ETech_VeryRare.Balance_AR_TOR_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/TOR/Balance/Balance_AR_TOR_ETech_Rare.Balance_AR_TOR_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/Dahl/Balance/Balance_DAL_AR_ETech_VeryRare.Balance_DAL_AR_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/Dahl/Balance/Balance_DAL_AR_ETech_Rare.Balance_DAL_AR_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/COV/Balance/Balance_AR_COV_ETech_VeryRare.Balance_AR_COV_ETech_VeryRare",
	"/Game/Gear/Weapons/_Shared/_Design/_Manufacturers/_ETech/_Design/AssaultRifle/COV/Balance/Balance_AR_COV_ETech_Rare.Balance_AR_COV_ETech_Rare",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer.Balance_SR_HYP_ZeroForPlayer",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/Balance_SR_HYP_Zero.Balance_SR_HYP_Zero",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Typhon/Balance_SG_JAK_Typhon.Balance_SG_JAK_Typhon",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/TinyTina/Balance_PS_TOR_TinyTina.Balance_PS_TOR_TinyTina",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Mordecai/Balance_SR_VLA_Mordecai.Balance_SR_VLA_Mordecai",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Maya/Balance_SM_MAL_Maya.Balance_SM_MAL_Maya",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Marcus/Balance_HW_TOR_Marcus.Balance_HW_TOR_Marcus",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Lorelei/Balance_AR_VLA_Lorelei.Balance_AR_VLA_Lorelei",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Lilith/Balance_SM_HYP_Lilith.Balance_SM_HYP_Lilith",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Hammerlock/Balance_SR_JAK_Hammerlock.Balance_SR_JAK_Hammerlock",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Gaige/Balance_DAL_AR_Gaige.Balance_DAL_AR_Gaige",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Clay/Balance_PS_JAK_Clay.Balance_PS_JAK_Clay",
	"/Game/Gear/Weapons/_Shared/NPC_Weapons/Ava/Balance_PS_TED_Ava.Balance_PS_TED_Ava",
	"/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/_Unique/Prison/Balance/Balance_VLA_SR_Prison.Balance_VLA_SR_Prison",
	"/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_04_VeryRare.Balance_VLA_SR_04_VeryRare",
	"/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/Balance/Balance_VLA_SR_03_Rare.Balance_VLA_SR_03_Rare",
	"/Game/Gear/Weapons/SniperRifles/Vladof/_Shared/_Design/AI/Balance_VLA_SR_AI.Balance_VLA_SR_AI",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/_Unique/_Legendary/Soleki/Balance/Balance_MAL_SR_Soleki.Balance_MAL_SR_Soleki",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_04_VeryRare.Balance_MAL_SR_04_VeryRare",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/Balance/Balance_MAL_SR_03_Rare.Balance_MAL_SR_03_Rare",
	"/Game/Gear/Weapons/SniperRifles/Maliwan/Shared/_Design/AI/Balance_MAL_SR_AI.Balance_MAL_SR_AI",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Huntress/Balance/Balance_SR_JAK_Huntress.Balance_SR_JAK_Huntress",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/TheHunter/Balance/Balance_SR_JAK_Hunter.Balance_SR_JAK_Hunter",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/IceQueen/Balance/Balance_SR_JAK_IceQueen.Balance_SR_JAK_IceQueen",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/_Unique/Headsplosion/Balance/Balance_SR_JAK_Headsplosion.Balance_SR_JAK_Headsplosion",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_04_VeryRare.Balance_SR_JAK_04_VeryRare",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/Balance/Balance_SR_JAK_03_Rare.Balance_SR_JAK_03_Rare",
	"/Game/Gear/Weapons/SniperRifles/Jakobs/_Shared/_Design/AI/Balance_SR_JAK_AI.Balance_SR_JAK_AI",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/TwoTime/Balance/Balance_SR_HYP_TwoTime.Balance_SR_HYP_TwoTime",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/_Unique/MasterworkCrossbow/Balance/Balance_SR_HYP_Masterwork.Balance_SR_HYP_Masterwork",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_04_VeryRare.Balance_SR_HYP_04_VeryRare",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/Balance/Balance_SR_HYP_03_Rare.Balance_SR_HYP_03_Rare",
	"/Game/Gear/Weapons/SniperRifles/Hyperion/_Shared/_Design/AI/Balance_SR_HYP_AI.Balance_SR_HYP_AI",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/WorldDestroyer/Balance/Balance_SR_DAL_WorldDestroyer.Balance_SR_DAL_WorldDestroyer",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/_Unique/BrashisDedication/Balance/Balance_SR_DAL_BrashisDedication.Balance_SR_DAL_BrashisDedication",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_04_VeryRare.Balance_SR_DAL_04_VeryRare",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/Balance/Balance_SR_DAL_03_Rare.Balance_SR_DAL_03_Rare",
	"/Game/Gear/Weapons/SniperRifles/Dahl/_Shared/_Design/AI/Balance_SR_DAL_AI.Balance_SR_DAL_AI",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/SpiderMind/Balance/Balance_SM_TED_SpiderMind.Balance_SM_TED_SpiderMind",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans.Balance_SM_TED_Beans",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_04_VeryRare.Balance_SM_TED_04_VeryRare",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/Balance/Balance_SM_TED_03_Rare.Balance_SM_TED_03_Rare",
	"/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/AI/Balance_SM_TED_AI.Balance_SM_TED_AI",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/westergun/Balance/Balance_SM_MAL_westergun.Balance_SM_MAL_westergun",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/VibraPulse/Balance/Balance_SM_MAL_VibraPulse.Balance_SM_MAL_VibraPulse",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Tsunami/Balance/Balance_SM_MAL_Tsunami.Balance_SM_MAL_Tsunami",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Kevins/Balance/Balance_SM_MAL_Kevins.Balance_SM_MAL_Kevins",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Emporer/Balance/Balance_SM_MAL_Emporer.Balance_SM_MAL_Emporer",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Egon/Balance/Balance_SM_MAL_Egon.Balance_SM_MAL_Egon",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/E3/Balance_SM_MAL_E3.Balance_SM_MAL_E3",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/Crit/Balance/Balance_SM_MAL_Crit.Balance_SM_MAL_Crit",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/_Unique/CloudKill/Balance/Balance_SM_MAL_CloudKill.Balance_SM_MAL_CloudKill",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_04_VeryRare.Balance_SM_MAL_04_VeryRare",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/BalanceState/Balance_SM_MAL_03_Rare.Balance_SM_MAL_03_Rare",
	"/Game/Gear/Weapons/SMGs/Maliwan/_Shared/_Design/AI/Balance_SM_MAL_AI.Balance_SM_MAL_AI",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/PredatoryLending/Balance/Balance_SM_HYP_PredatoryLending.Balance_SM_HYP_PredatoryLending",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/L0V3M4CH1N3/Balance/Balance_SM_HYP_L0V3M4CH1N3.Balance_SM_HYP_L0V3M4CH1N3",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/_Unique/Fork/Balance/Balance_SM_HYP_Fork.Balance_SM_HYP_Fork",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_04_VeryRare.Balance_SM_HYP_04_VeryRare",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/BalanceState/Balance_SM_HYP_03_Rare.Balance_SM_HYP_03_Rare",
	"/Game/Gear/Weapons/SMGs/Hyperion/_Shared/_Design/AI/Balance_SM_HYP_AI.Balance_SM_HYP_AI",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/RockNRoll_Intro/Balance_SM_DAL_PlayableIntroOnly.Balance_SM_DAL_PlayableIntroOnly",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/NineVolt/Balance/Balance_SM_DAHL_NineVolt.Balance_SM_DAHL_NineVolt",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/_Unique/HellFire/Balance/Balance_SM_DAHL_HellFire.Balance_SM_DAHL_HellFire",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/EndGameTest/Balance_SM_DAHL_TEST_ENDGAME.Balance_SM_DAHL_TEST_ENDGAME",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_04_VeryRare.Balance_SM_DAHL_04_VeryRare",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_03_Rare.Balance_SM_DAHL_03_Rare",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/BalanceState/Balance_SM_DAHL_01_Common_No_Elemental.Balance_SM_DAHL_01_Common_No_Elemental",
	"/Game/Gear/Weapons/SMGs/Dahl/_Shared/_Design/AI/Balance_SM_DAHL_AI.Balance_SM_DAHL_AI",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Thumper/Balance/Balance_SG_Torgue_Thumper.Balance_SG_Torgue_Thumper",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/RedLiner/Balance/Balance_SG_Torgue_RedLine.Balance_SG_Torgue_RedLine",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Brew/Balance/Balance_SG_TOR_Brewha.Balance_SG_TOR_Brewha",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/Balrog/Balance/Balance_SG_Torgue_Balrog.Balance_SG_Torgue_Balrog",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_04_VeryRare.Balance_SG_Torgue_04_VeryRare",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/BalanceState/Balance_SG_Torgue_03_Rare.Balance_SG_Torgue_03_Rare",
	"/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/AI/Balance_SG_Torgue_AI.Balance_SG_Torgue_AI",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Sludge/Balance/Balance_SG_TED_Sludge.Balance_SG_TED_Sludge",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/Horizon/Balance/Balance_SG_TED_Horizon.Balance_SG_TED_Horizon",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/_Unique/FriendZone/Balance/Balance_SG_TED_FriendZone.Balance_SG_TED_FriendZone",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_04_VeryRare.Balance_SG_TED_04_VeryRare",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/Balance/Balance_SG_TED_03_Rare.Balance_SG_TED_03_Rare",
	"/Game/Gear/Weapons/Shotguns/Tediore/_Shared/_Design/AI/Balance_SG_TED_AI.Balance_SG_TED_AI",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/Shriek/Balance/Balance_SG_MAL_Shriek.Balance_SG_MAL_Shriek",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/_Unique/MouthPiece2/Balance/Balance_SG_MAL_Mouthpiece2.Balance_SG_MAL_Mouthpiece2",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_04_VeryRare.Balance_SG_MAL_04_VeryRare",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/BalanceState/Balance_SG_MAL_03_Rare.Balance_SG_MAL_03_Rare",
	"/Game/Gear/Weapons/Shotguns/Maliwan/_Shared/_Design/AI/Balance_SG_MAL_AI.Balance_SG_MAL_AI",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Sledge/Balance/Balance_SG_JAK_LGD_Sledge.Balance_SG_JAK_LGD_Sledge",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/OnePunch/Balance/Balance_SG_JAK_OnePunch.Balance_SG_JAK_OnePunch",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/NimbleJack/Balance/Balance_SG_JAK_Nimble.Balance_SG_JAK_Nimble",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/_Legendary/Garcia/Balance/Balance_SG_JAK_Garcia.Balance_SG_JAK_Garcia",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/_Unique/Fingerbiter/Balance/Balance_SG_JAK_Fingerbiter.Balance_SG_JAK_Fingerbiter",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_04_VeryRare.Balance_SG_JAK_04_VeryRare",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/BalanceState/Balance_SG_JAK_03_Rare.Balance_SG_JAK_03_Rare",
	"/Game/Gear/Weapons/Shotguns/Jakobs/_Shared/_Design/AI/Balance_SG_JAK_AI.Balance_SG_JAK_AI",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/_Unique/Phebert/Balance/Balance_SG_HYP_Phebert.Balance_SG_HYP_Phebert",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_04_VeryRare.Balance_SG_HYP_04_VeryRare",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/BalanceStates/Balance_SG_HYP_03_Rare.Balance_SG_HYP_03_Rare",
	"/Game/Gear/Weapons/Shotguns/Hyperion/_Shared/_Design/AI/Balance_SG_HYP_AI.Balance_SG_HYP_AI",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/TheLeech/Balance/Balance_PS_VLA_TheLeech.Balance_PS_VLA_TheLeech",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/_Unique/BoneShredder/Balance/Balance_PS_VLA_BoneShredder.Balance_PS_VLA_BoneShredder",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/FirstGun/Balance_PS_VLA_FirstGun_A.Balance_PS_VLA_FirstGun_A",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_04_VeryRare.Balance_PS_VLA_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/BalanceState/Balance_PS_VLA_03_Rare.Balance_PS_VLA_03_Rare",
	"/Game/Gear/Weapons/Pistols/Vladof/_Shared/_Design/AI/Balance_PS_VLA_AI.Balance_PS_VLA_AI",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Troy/Balance/Balance_PS_TOR_Troy.Balance_PS_TOR_Troy",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf.Balance_PS_TOR_Nurf",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Hyde/Balance/Balance_PS_TOR_Hyde.Balance_PS_TOR_Hyde",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/HeckelAndHyde/Heckle/Balance/Balance_PS_TOR_Heckle.Balance_PS_TOR_Heckle",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_04_VeryRare.Balance_PS_TOR_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/Balance/Balance_PS_TOR_03_Rare.Balance_PS_TOR_03_Rare",
	"/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/AI/Balance_PS_TOR_AI.Balance_PS_TOR_AI",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/Sabre/Balance/Balance_PS_Tediore_Sabre.Balance_PS_Tediore_Sabre",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/_Unique/BabyMaker/Balance/Salvage/Balance_PS_Tediore_BabyMaker_Salvage.Balance_PS_Tediore_BabyMaker_Salvage",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_04_VeryRare.Balance_PS_Tediore_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/BalanceState/Balance_PS_Tediore_03_Rare.Balance_PS_Tediore_03_Rare",
	"/Game/Gear/Weapons/Pistols/Tediore/Shared/_Design/AI/Balance_PS_Tediore_AI.Balance_PS_Tediore_AI",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/_AI/TrooperBadass/Balance_PS_MAL_AI_TrooperBadass.Balance_PS_MAL_AI_TrooperBadass",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/SuckerPunch/Balance/Balance_PS_MAL_SuckerPunch.Balance_PS_MAL_SuckerPunch",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/Starkiller/Balance/Balance_PS_MAL_Starkiller.Balance_PS_MAL_Starkiller",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator.Balance_PS_MAL_HyperHydrator",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_04_VeryRare.Balance_PS_MAL_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/BalanceState/Balance_PS_MAL_03_Rare.Balance_PS_MAL_03_Rare",
	"/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/AI/Balance_PS_MAL_AI.Balance_PS_MAL_AI",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/TortureTruck/Balance_PS_JAK_TortureTruck.Balance_PS_JAK_TortureTruck",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/SpyRevolver/Balance_PS_JAK_SpyRevolver.Balance_PS_JAK_SpyRevolver",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Malevolent/Balance/Balance_PS_JAK_Malevolent.Balance_PS_JAK_Malevolent",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/GodMother/Balance/Balance_PS_JAK_GodMother.Balance_PS_JAK_GodMother",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Buttplug/Balance/Balance_PS_JAK_Buttplug.Balance_PS_JAK_Buttplug",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AureliaBackup/Balance/Balance_PS_JAK_AureliaPistol.Balance_PS_JAK_AureliaPistol",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/AmazingGrace/Balance/Balance_PS_JAK_AmazingGrace.Balance_PS_JAK_AmazingGrace",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/FirstGun/Balance_PS_JAK_FirstGun_C.Balance_PS_JAK_FirstGun_C",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/FirstGun/Balance_PS_JAK_FirstGun_B.Balance_PS_JAK_FirstGun_B",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_04_VeryRare.Balance_PS_JAK_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/BalanceState/Balance_PS_JAK_03_Rare.Balance_PS_JAK_03_Rare",
	"/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/AI/Balance_PS_JAK_AI.Balance_PS_JAK_AI",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Rakkman/Balance/Balance_DAL_PS_Rakkman.Balance_DAL_PS_Rakkman",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/_Unique/Omniloader/Balance/Balance_DAL_PS_Omniloader.Balance_DAL_PS_Omniloader",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_04_VeryRare.Balance_DAL_PS_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_03_Rare.Balance_DAL_PS_03_Rare",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_01_FirstGunB.Balance_DAL_PS_01_FirstGunB",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/BalanceState/Balance_DAL_PS_01_FirstGunA.Balance_DAL_PS_01_FirstGunA",
	"/Game/Gear/Weapons/Pistols/Dahl/_Shared/_Design/AI/Balance_DAL_PS_AI.Balance_DAL_PS_AI",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Skeksis/Balance/Balance_PS_COV_Skeksis.Balance_PS_COV_Skeksis",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/PsychoStabber/Balance/Balance_PS_COV_PsychoStabber.Balance_PS_COV_PsychoStabber",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Mouthpiece/Balance/Balance_PS_COV_Mouthpiece.Balance_PS_COV_Mouthpiece",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Contagion/Balance/Balance_PS_COV_Contagion.Balance_PS_COV_Contagion",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/_Unique/Chad/Balance/Balance_PS_COV_Chad.Balance_PS_COV_Chad",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_04_VeryRare.Balance_PS_COV_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_PS_COV_03_Rare.Balance_PS_COV_03_Rare",
	"/Game/Gear/Weapons/Pistols/ChildrenOfTheVault/_Shared/_Design/AI/Balance_PS_COV_AI.Balance_PS_COV_AI",
	"/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Warmonger/Balance/Balance_PS_ATL_Warmonger.Balance_PS_ATL_Warmonger",
	"/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/_Unique/Drill/Balance/Balance_PS_ATL_Drill.Balance_PS_ATL_Drill",
	"/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_04_VeryRare.Balance_PS_ATL_04_VeryRare",
	"/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/Balance/Balance_PS_ATL_03_Rare.Balance_PS_ATL_03_Rare",
	"/Game/Gear/Weapons/Pistols/Atlas/_Shared/_Design/AI/Balance_PS_ATL_AI.Balance_PS_ATL_AI",
	"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol",
	"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_ForAI/Balance_HW_VLA_AI_UseONLY.Balance_HW_VLA_AI_UseONLY",
	"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_04_VeryRare.Balance_HW_VLA_04_VeryRare",
	"/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/Balance/Balance_HW_VLA_03_Rare.Balance_HW_VLA_03_Rare",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO.Balance_HW_TOR_RYNO",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Rampager/Balance/Balance_HW_TOR_Rampager.Balance_HW_TOR_Rampager",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/Hive/Balance/Balance_HW_TOR_Hive.Balance_HW_TOR_Hive",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/BurgerCannon/Balance/Balance_HW_TOR_BurgerCannon.Balance_HW_TOR_BurgerCannon",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_ForAI/Balance_HW_TOR_AI_UseONLY.Balance_HW_TOR_AI_UseONLY",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_04_VeryRare.Balance_HW_TOR_04_VeryRare",
	"/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/Balance/Balance_HW_TOR_03_Rare.Balance_HW_TOR_03_Rare",
	"/Game/Gear/Weapons/HeavyWeapons/Eridian/_Shared/_Design/Balance/Balance_Eridian_Fabricator.Balance_Eridian_Fabricator",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/Terror/Balance/Balance_HW_COV_Terror.Balance_HW_COV_Terror",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/PortaPooper/Balance/Balance_HW_COV_PortaPooper.Balance_HW_COV_PortaPooper",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_Unique/HotDrop/Balance/Balance_HW_COV_HotDrop.Balance_HW_COV_HotDrop",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/_ForAI/Balance_HW_COV_AI_UseONLY.Balance_HW_COV_AI_UseONLY",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_04_VeryRare.Balance_HW_COV_04_VeryRare",
	"/Game/Gear/Weapons/HeavyWeapons/ChildrenOfTheVault/_Shared/_Design/Balance/Balance_HW_COV_03_rare.Balance_HW_COV_03_Rare",
	"/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/_Unique/Freeman/Balance/Balance_HW_ATL_Freeman.Balance_HW_ATL_Freeman",
	"/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_04_VeryRare.Balance_HW_ATL_04_VeryRare",
	"/Game/Gear/Weapons/HeavyWeapons/ATL/_Shared/_Design/BalanceState/Balance_HW_ATL_03_Rare.Balance_HW_ATL_03_Rare",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/BigSucc/Balance_AR_VLA_BigSucc.Balance_AR_VLA_BigSucc",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_04_VeryRare.Balance_AR_VLA_04_VeryRare",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/BalanceState/Balance_AR_VLA_03_Rare.Balance_AR_VLA_03_Rare",
	"/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/AI/Balance_AR_VLA_AI.Balance_AR_VLA_AI",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/WardenWeapon/Balance_AR_TOR_Warden.Balance_AR_TOR_Warden",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/_Unique/AmberManagement/Balance/Balance_AR_TOR_AmberManagement.Balance_AR_TOR_AmberManagement",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_04_VeryRare.Balance_AR_TOR_04_VeryRare",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/Balance/Balance_AR_TOR_03_Rare.Balance_AR_TOR_03_Rare",
	"/Game/Gear/Weapons/AssaultRifles/Torgue/_Shared/_Design/AI/Balance_AR_TOR_AI.Balance_AR_TOR_AI",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/TraitorsDeath/Balance/Balance_AR_JAK_TraitorsDeath.Balance_AR_JAK_TraitorsDeath",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/PasRifle/Balance/Balance_AR_JAK_PasRifle.Balance_AR_JAK_PasRifle",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/HandOfGlory/Balance/Balance_AR_JAK_HandOfGlory.Balance_AR_JAK_HandOfGlory",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/_Unique/Bekah/Balance/Balance_AR_JAK_Bekah.Balance_AR_JAK_Bekah",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_04_VeryRare.Balance_AR_JAK_04_VeryRare",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/Balance/Balance_AR_JAK_03_Rare.Balance_AR_JAK_03_Rare",
	"/Game/Gear/Weapons/AssaultRifles/Jakobs/_Shared/_Design/AI/Balance_AR_JAK_AI.Balance_AR_JAK_AI",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Hail/Balance/Balance_DAL_AR_Hail.Balance_DAL_AR_Hail",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/Earworm/Balance/Balance_DAL_AR_Earworm.Balance_DAL_AR_Earworm",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/_Unique/CrazyEarlDefault/Balance_DAL_AR_CrazyEarlDefault.Balance_DAL_AR_CrazyEarlDefault",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_04_VeryRare.Balance_DAL_AR_04_VeryRare",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/BalanceState/Balance_DAL_AR_03_Rare.Balance_DAL_AR_03_Rare",
	"/Game/Gear/Weapons/AssaultRifles/Dahl/_Shared/_Design/AI/Balance_DAL_AR_AI.Balance_DAL_AR_AI",
	"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_04_VeryRare.Balance_AR_COV_04_VeryRare",
	"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/BalanceState/Balance_AR_COV_03_Rare.Balance_AR_COV_03_Rare",
	"/Game/Gear/Weapons/AssaultRifles/ChildrenOfTheVault/_Shared/_Design/AI/Balance_AR_COV_AI.Balance_AR_COV_AI",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/_Unique/Portal/Balance/Balance_ATL_AR_Portals.Balance_ATL_AR_Portals",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_04_VeryRare.Balance_ATL_AR_04_VeryRare",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/Balance/Balance_ATL_AR_03_Rare.Balance_ATL_AR_03_Rare",
	"/Game/Gear/Weapons/AssaultRifles/Atlas/_Shared/_Design/AI/Balance_ATL_AR_AI.Balance_ATL_AR_AI",
	"/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Balance/InvBalD_Shield_XPLootBooster.InvBalD_Shield_XPLootBooster",
	"/Game/Gear/Shields/_Design/_Uniques/Ward/Balance/InvBalD_Shield_Ward.InvBalD_Shield_Ward",
	"/Game/Gear/Shields/_Design/_Uniques/Unpaler/Balance/InvBalD_Shield_LGD_Unpaler.InvBalD_Shield_LGD_Unpaler",
	"/Game/Gear/Shields/_Design/_Uniques/ShootingStar/Balance/InvBalD_Shield_LGD_ShootingStar.InvBalD_Shield_LGD_ShootingStar",
	"/Game/Gear/Shields/_Design/_Uniques/Radiate/Balance/InvBalD_Shield_LGD_Radiate.InvBalD_Shield_LGD_Radiate",
	"/Game/Gear/Shields/_Design/_Uniques/MrCaffeine/Balance/InvBalD_Shield_PAN_MrCaffeine.InvBalD_Shield_PAN_MrCaffeine",
	"/Game/Gear/Shields/_Design/_Uniques/MoxxisEmbrace/Balance/InvBalD_Shield_MoxxisEmbrace.InvBalD_Shield_MoxxisEmbrace",
	"/Game/Gear/Shields/_Design/_Uniques/MessyBreakup/bALANCE/InvBalD_Shield_MessyBreakup.InvBalD_Shield_MessyBreakup",
	"/Game/Gear/Shields/_Design/_Uniques/LoopOf4N631/Balance/InvBalD_Shield_HYP_LoopOf4N631.InvBalD_Shield_HYP_LoopOf4N631",
	"/Game/Gear/Shields/_Design/_Uniques/GoldenTouch/Balance/InvBalD_Shield_GoldenTouch.InvBalD_Shield_GoldenTouch",
	"/Game/Gear/Shields/_Design/_Uniques/Dispensary/Balance/InvBalD_Shield_LGD_Dispensary.InvBalD_Shield_LGD_Dispensary",
	"/Game/Gear/Shields/_Design/_Uniques/Cyttorak/bALANCE/InvBalD_Shield_Cyttorak.InvBalD_Shield_Cyttorak",
	"/Game/Gear/Shields/_Design/_Uniques/BuriedAlive/Balance/InvBalD_Shield_BuriedAlive.InvBalD_Shield_BuriedAlive",
	"/Game/Gear/Shields/_Design/_Uniques/Aurelia/Balance/InvBalD_Shield_LGD_Aurelia.InvBalD_Shield_LGD_Aurelia",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_04_VeryRare.InvBalD_Shield_Pangolin_04_VeryRare",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_03_Rare.InvBalD_Shield_Pangolin_03_Rare",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_02_Uncommon.InvBalD_Shield_Pangolin_02_Uncommon",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Pangolin_01_Common.InvBalD_Shield_Pangolin_01_Common",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_04_VeryRare.InvBalD_Shield_Hyperion_04_VeryRare",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_03_Rare.InvBalD_Shield_Hyperion_03_Rare",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_02_Uncommon.InvBalD_Shield_Hyperion_02_Uncommon",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Hyperion_01_Common.InvBalD_Shield_Hyperion_01_Common",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_04_VeryRare.InvBalD_Shield_Anshin_04_VeryRare",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_03_Rare.InvBalD_Shield_Anshin_03_Rare",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_02_Uncommon.InvBalD_Shield_Anshin_02_Uncommon",
	"/Game/Gear/Shields/_Design/InvBalance/InvBalD_Shield_Anshin_01_Common.InvBalD_Shield_Anshin_01_Common",
	"/Game/Gear/GrenadeMods/_Design/_Unique/WizardOfNOG/Balance/InvBalD_GM_WizardOfNOG.InvBalD_GM_WizardOfNOG",
	"/Game/Gear/GrenadeMods/_Design/_Unique/ToyGrenade/Balance/InvBalD_GM_ToyGrenade.InvBalD_GM_ToyGrenade",
	"/Game/Gear/GrenadeMods/_Design/_Unique/ToiletBombs/Balance/InvBalD_GM_TOR_ToiletBombs.InvBalD_GM_TOR_ToiletBombs",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Summit/Balance/InvBalD_GM_Summit.InvBalD_GM_Summit",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Piss/Balance/InvBalD_GM_Piss.InvBalD_GM_Piss",
	"/Game/Gear/GrenadeMods/_Design/_Unique/ObviousTrap/Balance/InvBalD_GM_ObviousTrap.InvBalD_GM_ObviousTrap",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Mushroom/Balance/InvBalD_GM_Shroom.InvBalD_GM_Shroom",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Mogwai/Balance/InvBalD_GM_Mogwai.InvBalD_GM_Mogwai",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Kryll/Balance/InvBalD_GM_Kryll.InvBalD_GM_Kryll",
	"/Game/Gear/GrenadeMods/_Design/_Unique/JustDeserts/Balance/InvBalD_GM_JustDeserts.InvBalD_GM_JustDeserts",
	"/Game/Gear/GrenadeMods/_Design/_Unique/EMP/Balance/InvBalD_GM_EMP.InvBalD_GM_EMP",
	"/Game/Gear/GrenadeMods/_Design/_Unique/Chupa/Balance/InvBalD_GM_Chupa.InvBalD_GM_Chupa",
	"/Game/Gear/GrenadeMods/_Design/_Unique/CashMoneyPreorder/Balance/InvBalD_GM_CashMoneyPreorder.InvBalD_GM_CashMoneyPreorder",
	"/Game/Gear/GrenadeMods/_Design/_Unique/ButtStallion/Balance/InvBalD_GM_ButtStallion.InvBalD_GM_ButtStallion",
	"/Game/Gear/GrenadeMods/_Design/_Unique/BirthdaySuprise/Balance/InvBalD_GM_BirthdaySuprise.InvBalD_GM_BirthdaySuprise",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_04_VeryRare.InvBalD_GrenadeMod_Vladof_04_VeryRare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_03_Rare.InvBalD_GrenadeMod_Vladof_03_Rare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_02_Uncommon.InvBalD_GrenadeMod_Vladof_02_Uncommon",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Vladof_01_Common.InvBalD_GrenadeMod_Vladof_01_Common",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_04_VeryRare.InvBalD_GrenadeMod_Torgue_04_VeryRare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_03_Rare.InvBalD_GrenadeMod_Torgue_03_Rare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_02_Uncommon.InvBalD_GrenadeMod_Torgue_02_Uncommon",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Torgue_01_Common.InvBalD_GrenadeMod_Torgue_01_Common",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_04_VeryRare.InvBalD_GrenadeMod_Tediore_04_VeryRare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_03_Rare.InvBalD_GrenadeMod_Tediore_03_Rare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_02_Uncommon.InvBalD_GrenadeMod_Tediore_02_Uncommon",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Tediore_01_Common.InvBalD_GrenadeMod_Tediore_01_Common",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_04_VeryRare.InvBalD_GrenadeMod_Pangolin_04_VeryRare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_03_Rare.InvBalD_GrenadeMod_Pangolin_03_Rare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_02_Uncommon.InvBalD_GrenadeMod_Pangolin_02_Uncommon",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Pangolin_01_Common.InvBalD_GrenadeMod_Pangolin_01_Common",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_04_VeryRare.InvBalD_GrenadeMod_Hyperion_04_VeryRare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_03_Rare.InvBalD_GrenadeMod_Hyperion_03_Rare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_02_Uncommon.InvBalD_GrenadeMod_Hyperion_02_Uncommon",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Hyperion_01_Common.InvBalD_GrenadeMod_Hyperion_01_Common",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_04_VeryRare.InvBalD_GrenadeMod_Atlas_04_VeryRare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_03_Rare.InvBalD_GrenadeMod_Atlas_03_Rare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_02_Uncommon.InvBalD_GrenadeMod_Atlas_02_Uncommon",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_Atlas_01_Common.InvBalD_GrenadeMod_Atlas_01_Common",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_03_Rare.InvBalD_GrenadeMod_03_Rare",
	"/Game/Gear/GrenadeMods/_Design/InvBalance/InvBalD_GrenadeMod_02_Uncommon.InvBalD_GrenadeMod_02_Uncommon",
]


@hook("/Script/Engine.PlayerController:ServerNotifyLoadedWorld", Type.POST)
def ServerNotifyLoadedWorld(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    change_all_anoints()



build_mod(
    options=[apply_button, shield_group, gun_group, nade_group, nade_shield_group, terror_group, vh_group]
)

