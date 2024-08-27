import pytest

from .. import journey_to_the_west_characters

from ..journey_to_the_west_characters import journeytotheWestCharacterStatBlock


@pytest.fixture
def sun_wukong_stat_block():
    # Fixture to provide a sample instance of SunWukongStatBlock for testing
    return journeytotheWestCharacterStatBlock(
        **journey_to_the_west_characters.sun_wukong_custom_stat_block
    )


def test_sun_wukong_stat_block(sun_wukong_stat_block):
    # Check if the Sun Wukong StatBlock instance is created correctly
    assert sun_wukong_stat_block.name == "Sun Wukong"
    assert sun_wukong_stat_block.hit_points == 158
    assert sun_wukong_stat_block.armor_class == 19
    assert sun_wukong_stat_block.speed == "50 ft. (Base, potentially higher with Mobile feat and Boots of Speed)"
    assert sun_wukong_stat_block.abilities.strength == 18
    assert sun_wukong_stat_block.saving_throws.strength == 8
    assert "Acrobatics +10" in sun_wukong_stat_block.skills
    assert (
        sun_wukong_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert sun_wukong_stat_block.damage_immunities == "poison"
    assert sun_wukong_stat_block.condition_immunities == "charmed, frightened, poisoned"
    assert sun_wukong_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert (
        sun_wukong_stat_block.languages
        == "All spoken languages (Tongue of the Sun and Moon)"
    )
    assert sun_wukong_stat_block.challenge == 20  # Ensure this is an integer
    assert (
        "Martial Arts: Allows use of Dexterity for attack and damage rolls with unarmed strikes and monk weapons."
        in sun_wukong_stat_block.special_abilities
    )
    assert (
        sun_wukong_stat_block.legendary_actions["Unseen Strike"]
        == "Sun Wukong uses his speed to make an additional unarmed strike with advantage."
    )
    assert (
        sun_wukong_stat_block.actions[0]
        == "Multiattack: Sun Wukong makes two attacks with his Ruyi Jingu Bang or unarmed strikes."
    )
    assert (
        sun_wukong_stat_block.actions[1]
        == "Ruyi Jingu Bang: Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 12 (1d8 + 4) bludgeoning damage plus 2d6 force damage."
    )
    assert (
        sun_wukong_stat_block.bonus_actions[0]
        == "Step of the Wind: Sun Wukong can use a bonus action to Disengage or Dash and double his jump distance."
    )
    assert (
        sun_wukong_stat_block.reactions[0]
        == "Deflect Missiles: When hit by a ranged weapon attack, he can use his reaction to reduce the damage by 1d10 + Dexterity modifier + Monk level."
    )
