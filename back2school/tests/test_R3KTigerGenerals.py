import pytest


from .. import R3KTigerGenerals

from ..R3KTigerGenerals import R3KTigerGeneralStatBlock

@pytest.fixture
def zhang_fei_stat_block():
    # Fixture to provide a sample instance of R3KTigerGeneralStatBlock for testing
    return R3KTigerGeneralStatBlock(**R3KTigerGenerals.zhang_fei_custom_stat_block)

def test_zhang_fei_stat_block(zhang_fei_stat_block):
    # Check if the Zhang Fei StatBlock instance is created correctly
    assert zhang_fei_stat_block.name == "Zhang Fei"
    assert zhang_fei_stat_block.hit_points == 255
    assert zhang_fei_stat_block.armor_class == 18
    assert zhang_fei_stat_block.speed == "30 ft."
    assert zhang_fei_stat_block.abilities.strength == 20
    assert zhang_fei_stat_block.saving_throws.strength == "+11"
    assert "Athletics +11" in zhang_fei_stat_block.skills
    assert zhang_fei_stat_block.damage_resistances == "bludgeoning, piercing, and slashing from nonmagical attacks (while raging)"
    assert zhang_fei_stat_block.condition_immunities == "frightened (while raging)"
    assert zhang_fei_stat_block.senses == "passive Perception 17"
    assert zhang_fei_stat_block.languages == "Common"
    assert zhang_fei_stat_block.challenge == 20
    assert "Unyielding Presence" in zhang_fei_stat_block.special_abilities
    assert zhang_fei_stat_block.legendary_actions["Indomitable"] == "Zhang Fei can reroll a saving throw that he fails. If he does so, he must use the new roll."
    assert zhang_fei_stat_block.actions[0] == "Multiattack: Zhang Fei makes three attacks with his Serpent Spear."
    assert zhang_fei_stat_block.actions[1] == "Serpent Spear: Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 1d10+7 (12) piercing damage (or 1d10+10 (15) while raging)."
    assert zhang_fei_stat_block.bonus_actions[0] == "Rage (4 uses/day)"
    assert zhang_fei_stat_block.reactions[0] == "Riposte: When a creature misses Zhang Fei with a melee attack, he can use his reaction to make a melee weapon attack against the creature."
}
