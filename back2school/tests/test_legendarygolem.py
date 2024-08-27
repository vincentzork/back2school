import pytest

from .. import legendary_golems

from ..legendary_golems import LegendaryGolemStatBlock


@pytest.fixture
def iron_golem_of_acererak_stat_block():
    # Fixture to provide a sample instance of GolemChampionStatBlock for testing
    return LegendaryGolemStatBlock(
        **legendary_golems.iron_golem_of_acererak_custom_stat_block
    )


def test_iron_golem_of_acererak_stat_block(iron_golem_of_acererak_stat_block):
    # Check if the Iron Golem of Acererak StatBlock instance is created correctly
    assert iron_golem_of_acererak_stat_block.name == "Iron Golem of Acererak"
    assert iron_golem_of_acererak_stat_block.hit_points == 350
    assert iron_golem_of_acererak_stat_block.armor_class == 23
    assert iron_golem_of_acererak_stat_block.speed == "30 ft."
    assert iron_golem_of_acererak_stat_block.abilities.strength == 28
    assert iron_golem_of_acererak_stat_block.saving_throws.strength == 16
    assert "Athletics +18" in iron_golem_of_acererak_stat_block.skills
    assert (
        iron_golem_of_acererak_stat_block.damage_resistances == "fire, cold, necrotic"
    )
    assert (
        iron_golem_of_acererak_stat_block.damage_immunities
        == "poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        iron_golem_of_acererak_stat_block.condition_immunities
        == "charmed, exhaustion, frightened, paralyzed, petrified, poisoned"
    )
    assert (
        iron_golem_of_acererak_stat_block.senses
        == "darkvision 120 ft., passive Perception 22"
    )
    assert (
        iron_golem_of_acererak_stat_block.languages
        == "Understands Common, Infernal, and the languages of its creator but cannot speak"
    )
    assert iron_golem_of_acererak_stat_block.challenge == 22
    assert (
        "Magic Resistance: The golem has advantage on saving throws against spells and other magical effects."
        in iron_golem_of_acererak_stat_block.special_abilities
    )
    assert (
        iron_golem_of_acererak_stat_block.legendary_actions["Adamantine Slam"]
        == "The golem makes a single slam attack. If the attack hits, it deals an additional 3d8 force damage."
    )
    assert (
        iron_golem_of_acererak_stat_block.actions[0]
        == "Multiattack: The golem makes two attacks with its Adamantine Fist."
    )
    assert (
        iron_golem_of_acererak_stat_block.actions[1]
        == "Adamantine Fist: Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 25 (3d10 + 10) bludgeoning damage plus 2d6 necrotic damage."
    )
    assert (
        iron_golem_of_acererak_stat_block.bonus_actions[0]
        == "Fiendish Smite: The golem can use a bonus action to expend a Warlock spell slot, adding 4d8 necrotic damage to its next attack."
    )
    assert (
        iron_golem_of_acererak_stat_block.reactions[0]
        == "Dark Vengeance: When the golem is hit by a melee attack, it can use its reaction to deal 3d10 necrotic damage to the attacker."
    )


@pytest.fixture
def aegis_fang_golem_stat_block():
    # Fixture to provide a sample instance of GolemChampionStatBlock for testing
    return LegendaryGolemStatBlock(
        **legendary_golems.aegis_fang_golem_custom_stat_block
    )


def test_aegis_fang_golem_stat_block(aegis_fang_golem_stat_block):
    # Check if the Aegis-Fang Golem StatBlock instance is created correctly
    assert aegis_fang_golem_stat_block.name == "Aegis-Fang Golem"
    assert aegis_fang_golem_stat_block.hit_points == 400
    assert aegis_fang_golem_stat_block.armor_class == 24
    assert aegis_fang_golem_stat_block.speed == "30 ft."
    assert aegis_fang_golem_stat_block.abilities.strength == 30
    assert aegis_fang_golem_stat_block.saving_throws.strength == 17
    assert "Athletics +20" in aegis_fang_golem_stat_block.skills
    assert aegis_fang_golem_stat_block.damage_resistances == "fire, cold, force"
    assert (
        aegis_fang_golem_stat_block.damage_immunities
        == "poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        aegis_fang_golem_stat_block.condition_immunities
        == "charmed, exhaustion, frightened, paralyzed, petrified, poisoned"
    )
    assert (
        aegis_fang_golem_stat_block.senses
        == "darkvision 120 ft., passive Perception 22"
    )
    assert (
        aegis_fang_golem_stat_block.languages
        == "Understands Common, Dwarvish, and the languages of its creator but cannot speak"
    )
    assert aegis_fang_golem_stat_block.challenge == 23
    assert (
        "Magic Resistance: The golem has advantage on saving throws against spells and other magical effects."
        in aegis_fang_golem_stat_block.special_abilities
    )
    assert (
        aegis_fang_golem_stat_block.legendary_actions["Arcane Blast"]
        == "The golem releases a burst of arcane energy in a 20-foot radius. Each creature in the area must make a DC 22 Dexterity saving throw, taking 8d6 force damage on a failed save, or half as much damage on a successful one."
    )
    assert (
        aegis_fang_golem_stat_block.actions[0]
        == "Multiattack: The golem makes two attacks with its Arcane-Infused Slam."
    )
    assert (
        aegis_fang_golem_stat_block.actions[1]
        == "Arcane-Infused Slam: Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 32 (4d10 + 10) bludgeoning damage plus 3d8 force damage."
    )
    assert (
        aegis_fang_golem_stat_block.bonus_actions[0]
        == "Arcane Charge: The golem can use a bonus action to teleport up to 30 feet to an unoccupied space it can see. The next attack it makes before the end of its turn deals an additional 2d8 force damage."
    )
    assert (
        aegis_fang_golem_stat_block.reactions[0]
        == "Arcane Parry: When the golem is hit by a spell attack, it can use its reaction to halve the damage and reflect a portion of the spell's energy back at the caster. The caster must make a DC 22 Intelligence saving throw or take 4d6 force damage."
    )


@pytest.fixture
def mithral_golem_of_myth_drannor_stat_block():
    # Fixture to provide a sample instance of GolemChampionStatBlock for testing
    return LegendaryGolemStatBlock(
        **legendary_golems.mithral_golem_of_myth_drannor_custom_stat_block
    )


def test_mithral_golem_of_myth_drannor_stat_block(
    mithral_golem_of_myth_drannor_stat_block,
):
    # Check if the Mithral Golem StatBlock instance is created correctly
    assert (
        mithral_golem_of_myth_drannor_stat_block.name == "Mithral Golem of Myth Drannor"
    )
    assert mithral_golem_of_myth_drannor_stat_block.hit_points == 300
    assert mithral_golem_of_myth_drannor_stat_block.armor_class == 22
    assert mithral_golem_of_myth_drannor_stat_block.speed == "50 ft."
    assert mithral_golem_of_myth_drannor_stat_block.abilities.strength == 20
    assert mithral_golem_of_myth_drannor_stat_block.saving_throws.dexterity == 14
    assert "Acrobatics +16" in mithral_golem_of_myth_drannor_stat_block.skills
    assert (
        mithral_golem_of_myth_drannor_stat_block.damage_resistances
        == "radiant, cold, force"
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.damage_immunities
        == "poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.condition_immunities
        == "charmed, exhaustion, frightened, paralyzed, petrified, poisoned"
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.senses
        == "darkvision 120 ft., passive Perception 22"
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.languages
        == "Understands Common, Elvish, and the languages of its creator but cannot speak"
    )
    assert mithral_golem_of_myth_drannor_stat_block.challenge == 24
    assert (
        "Magic Resistance: The golem has advantage on saving throws against spells and other magical effects."
        in mithral_golem_of_myth_drannor_stat_block.special_abilities
    )
    assert (
        "Unarmored Defense: The golem's AC includes its Dexterity and Wisdom modifiers, reflecting its agility and martial prowess."
        in mithral_golem_of_myth_drannor_stat_block.special_abilities
    )
    assert (
        "Deflect Missiles: The golem can use its reaction to deflect or catch a ranged weapon attack it is hit by. When it does so, the damage it takes is reduced by 1d10 + its Dexterity modifier + its Monk level."
        in mithral_golem_of_myth_drannor_stat_block.special_abilities
    )
    assert (
        "Arcane Regeneration: At the start of each of its turns, the golem regains 15 hit points. This regeneration is suppressed if the golem takes fire or force damage in the previous round."
        in mithral_golem_of_myth_drannor_stat_block.special_abilities
    )
    assert (
        "Immutable Form: The golem is immune to any spell or effect that would alter its form."
        in mithral_golem_of_myth_drannor_stat_block.special_abilities
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.legendary_actions["Arcane Flurry"]
        == "The golem makes a flurry of strikes, making three attacks with its Mithral Strike. If all three attacks hit the same target, the target must succeed on a DC 20 Constitution saving throw or be stunned until the end of the golem's next turn."
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.actions[0]
        == "Multiattack: The golem makes two attacks with its Mithral Strike or Arcane Blade Dance."
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.actions[1]
        == "Mithral Strike: Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 18 (2d8 + 9) slashing damage plus 2d6 force damage."
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.bonus_actions[0]
        == "Step of the Wind: The golem can use a bonus action to dash or disengage, doubling its jump distance for the turn."
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.reactions[0]
        == "Deflect Missiles: The golem can use its reaction to deflect or catch a ranged weapon attack it is hit by. When it does so, the damage it takes is reduced by 1d10 + its Dexterity modifier + its Monk level. If it reduces the damage to 0, it can catch the missile and make a ranged attack with it as part of the same reaction."
    )
    assert (
        mithral_golem_of_myth_drannor_stat_block.reactions[1]
        == "Arcane Shield: When the golem is targeted by a spell, it can use its reaction to cast Shield, increasing its AC by +5 until the start of its next turn."
    )


@pytest.fixture
def adamantine_golem_of_undermountain_stat_block():
    # Fixture to provide a sample instance of GolemChampionStatBlock for testing
    return LegendaryGolemStatBlock(
        **legendary_golems.adamantine_golem_of_undermountain_custom_stat_block
    )


def test_adamantine_golem_of_undermountain_stat_block(
    adamantine_golem_of_undermountain_stat_block,
):
    # Check if the Adamantine Golem StatBlock instance is created correctly
    assert (
        adamantine_golem_of_undermountain_stat_block.name
        == "Adamantine Golem of Undermountain"
    )
    assert adamantine_golem_of_undermountain_stat_block.hit_points == 400
    assert adamantine_golem_of_undermountain_stat_block.armor_class == 24
    assert adamantine_golem_of_undermountain_stat_block.speed == "30 ft."
    assert adamantine_golem_of_undermountain_stat_block.abilities.strength == 30
    assert adamantine_golem_of_undermountain_stat_block.saving_throws.constitution == 16
    assert "Athletics +18" in adamantine_golem_of_undermountain_stat_block.skills
    assert (
        adamantine_golem_of_undermountain_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from magical attacks"
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.damage_immunities
        == "fire, poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.condition_immunities
        == "charmed, exhaustion, frightened, paralyzed, petrified, poisoned"
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.senses
        == "darkvision 120 ft., passive Perception 20"
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.languages
        == "Understands Common, Infernal, and the languages of its creator but cannot speak"
    )
    assert adamantine_golem_of_undermountain_stat_block.challenge == 23
    assert (
        "Arcane Ward: The golem has an additional pool of hit points equal to its Constitution modifier x 10 (50 hit points) that regenerates at the start of its turn. These hit points are depleted before the golem’s actual hit points are reduced."
        in adamantine_golem_of_undermountain_stat_block.special_abilities
    )
    assert (
        "Spell Reflection: When the golem is targeted by a spell that requires a saving throw, and it succeeds, the spell is reflected back at the caster as if the golem had cast it."
        in adamantine_golem_of_undermountain_stat_block.special_abilities
    )
    assert (
        "Arcane Might: The golem’s melee attacks deal an additional 2d6 force damage, representing the magical power imbued in its strikes."
        in adamantine_golem_of_undermountain_stat_block.special_abilities
    )
    assert (
        "Teleportation Anchor: The golem projects a 60-foot-radius aura that prevents creatures from teleporting or using planar travel spells. Any attempt to do so automatically fails."
        in adamantine_golem_of_undermountain_stat_block.special_abilities
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.legendary_actions[
            "Juggernaut Charge"
        ]
        == "The golem moves up to its speed in a straight line and can make a Juggernaut Slam attack against any creature in its path. If it hits, the target must make a DC 24 Strength saving throw or be knocked prone and take an additional 2d6 bludgeoning damage."
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.actions[0]
        == "Multiattack: The golem makes two attacks with its Juggernaut Slam or Arcane-Enhanced Fist."
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.actions[1]
        == "Juggernaut Slam: Melee Weapon Attack: +18 to hit, reach 10 ft., one target. Hit: 28 (3d10 + 8) bludgeoning damage plus 2d6 force damage."
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.bonus_actions[0]
        == "Shield Bash: The golem can use a bonus action to bash a target with its shield, dealing 1d8 bludgeoning damage and forcing the target to make a DC 24 Strength saving throw or be knocked prone."
    )
    assert (
        adamantine_golem_of_undermountain_stat_block.reactions[0]
        == "Arcane Shield: When the golem is targeted by a spell, it can use its reaction to cast Shield, increasing its AC by +5 until the start of its next turn."
    )
