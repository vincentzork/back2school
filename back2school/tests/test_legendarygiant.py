import pytest

from .. import legendary_giants

from ..legendary_giants import LegendaryGiantStatBlock

@pytest.fixture
def thane_kayalithica_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.thane_kayalithica_custom_stat_block)

def test_thane_kayalithica_stat_block(thane_kayalithica_stat_block):
    # Check if the Thane Kayalithica StatBlock instance is created correctly
    assert thane_kayalithica_stat_block.name == "Thane Kayalithica"
    assert thane_kayalithica_stat_block.hit_points == 230
    assert thane_kayalithica_stat_block.armor_class == 18
    assert thane_kayalithica_stat_block.speed == "40 ft."
    assert thane_kayalithica_stat_block.abilities.strength == 25
    assert thane_kayalithica_stat_block.saving_throws.strength == 12
    assert "Perception +9" in thane_kayalithica_stat_block.skills
    assert (
        thane_kayalithica_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert thane_kayalithica_stat_block.condition_immunities == "none"
    assert thane_kayalithica_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    assert thane_kayalithica_stat_block.languages == "Giant, Terran"
    assert thane_kayalithica_stat_block.challenge == 13
    assert (
        "Stone Camouflage: Thane Kayalithica has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
        in thane_kayalithica_stat_block.special_abilities
    )
    assert (
        thane_kayalithica_stat_block.legendary_actions["Detect"]
        == "Thane Kayalithica makes a Wisdom (Perception) check."
    )
    assert (
        thane_kayalithica_stat_block.actions[0]
        == "Multiattack: Thane Kayalithica makes two attacks with her Greatclub."
    )
    assert (
        thane_kayalithica_stat_block.actions[1]
        == "Greatclub: Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 25 (3d8 + 7) bludgeoning damage."
    )
    # No bonus actions defined, but including an empty check
    assert thane_kayalithica_stat_block.bonus_actions == []
    # No reactions defined, but including an empty check
    assert thane_kayalithica_stat_block.reactions == []

@pytest.fixture
def king_snurre_ironbelly_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.king_snurre_ironbelly_custom_stat_block)

def test_king_snurre_ironbelly_stat_block(king_snurre_ironbelly_stat_block):
    # Check if the King Snurre Ironbelly StatBlock instance is created correctly
    assert king_snurre_ironbelly_stat_block.name == "King Snurre Ironbelly"
    assert king_snurre_ironbelly_stat_block.hit_points == 345
    assert king_snurre_ironbelly_stat_block.armor_class == 21
    assert king_snurre_ironbelly_stat_block.speed == "40 ft."
    assert king_snurre_ironbelly_stat_block.abilities.strength == 28
    assert king_snurre_ironbelly_stat_block.saving_throws.strength == 14
    assert "Athletics +14" in king_snurre_ironbelly_stat_block.skills
    assert king_snurre_ironbelly_stat_block.damage_resistances == "fire"
    assert king_snurre_ironbelly_stat_block.condition_immunities == "none"
    assert king_snurre_ironbelly_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert king_snurre_ironbelly_stat_block.languages == "Giant, Common, Ignan"
    assert king_snurre_ironbelly_stat_block.challenge == 18
    assert (
        "Fire Aura: King Snurre radiates intense heat. Any creature that starts its turn within 5 feet of him takes 10 (3d6) fire damage."
        in king_snurre_ironbelly_stat_block.special_abilities
    )
    assert (
        king_snurre_ironbelly_stat_block.legendary_actions["Detect"]
        == "King Snurre makes a Wisdom (Perception) check."
    )
    assert (
        king_snurre_ironbelly_stat_block.actions[0]
        == "Multiattack: King Snurre makes three attacks with his Flaming Greatsword."
    )
    assert (
        king_snurre_ironbelly_stat_block.actions[1]
        == "Flaming Greatsword: Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 23 (4d6 + 9) slashing damage plus 14 (4d6) fire damage."
    )
    assert (
        king_snurre_ironbelly_stat_block.bonus_actions[0]
        == "Rage (4 uses/day): King Snurre can enter a rage as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage, and adding bonus damage to his melee attacks."
    )
    assert (
        king_snurre_ironbelly_stat_block.reactions[0]
        == "Parry: King Snurre adds 4 to his AC against one melee attack that would hit him. To do so, King Snurre must see the attacker and be wielding a melee weapon."
    )
