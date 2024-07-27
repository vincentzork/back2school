import pytest


from .. import r3k_tiger_generals

from ..r3k_tiger_generals import R3KTigerGeneralStatBlock


@pytest.fixture
def zhang_fei_stat_block():
    # Fixture to provide a sample instance of R3KTigerGeneralStatBlock for testing
    return R3KTigerGeneralStatBlock(**r3k_tiger_generals.zhang_fei_custom_stat_block)


def test_zhang_fei_stat_block(zhang_fei_stat_block):
    # Check if the Zhang Fei StatBlock instance is created correctly
    assert zhang_fei_stat_block.name == "Zhang Fei"
    assert zhang_fei_stat_block.hit_points == 255
    assert zhang_fei_stat_block.armor_class == 18
    assert zhang_fei_stat_block.speed == "30 ft."
    assert zhang_fei_stat_block.abilities.strength == 20
    assert zhang_fei_stat_block.saving_throws.strength == 11
    assert "Athletics +11" in zhang_fei_stat_block.skills
    assert (
        zhang_fei_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks (while raging)"
    )
    assert zhang_fei_stat_block.condition_immunities == "frightened (while raging)"
    assert zhang_fei_stat_block.senses == "passive Perception 17"
    assert zhang_fei_stat_block.languages == "Common"
    assert zhang_fei_stat_block.challenge == 20
    assert (
        "Unyielding Presence: Zhang Fei can use his Action Surge to emit a terrifying battle cry. Enemies within 30 feet must make a DC 15 Wisdom saving throw or become frightened for 1 minute."
        in zhang_fei_stat_block.special_abilities
    )
    assert (
        zhang_fei_stat_block.legendary_actions["Indomitable"]
        == "Zhang Fei can reroll a saving throw that he fails. If he does so, he must use the new roll."
    )
    assert (
        zhang_fei_stat_block.actions[0]
        == "Multiattack: Zhang Fei makes three attacks with his Serpent Spear."
    )
    assert (
        zhang_fei_stat_block.actions[1]
        == "Serpent Spear: Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 1d10+7 (12) piercing damage (or 1d10+10 (15) while raging)."
    )
    assert zhang_fei_stat_block.bonus_actions[0] == "Rage (4 uses/day)"
    assert (
        zhang_fei_stat_block.reactions[0]
        == "Riposte: When a creature misses Zhang Fei with a melee attack, he can use his reaction to make a melee weapon attack against the creature."
    )


@pytest.fixture
def guan_yu_stat_block():
    # Fixture to provide a sample instance of R3KTigerGeneralStatBlock for testing
    return R3KTigerGeneralStatBlock(**r3k_tiger_generals.guan_yu_custom_stat_block)


def test_guan_yu_stat_block(guan_yu_stat_block):
    # Check if the Guan Yu StatBlock instance is created correctly
    assert guan_yu_stat_block.name == "Guan Yu"
    assert guan_yu_stat_block.hit_points == 190
    assert guan_yu_stat_block.armor_class == 20
    assert guan_yu_stat_block.speed == "30 ft."
    assert guan_yu_stat_block.abilities.strength == 20
    assert guan_yu_stat_block.saving_throws.strength == 8
    assert "Athletics +8" in guan_yu_stat_block.skills
    assert guan_yu_stat_block.damage_resistances == ""
    assert guan_yu_stat_block.condition_immunities == ""
    assert guan_yu_stat_block.senses == "passive Perception 12"
    assert guan_yu_stat_block.languages == "Common"
    assert guan_yu_stat_block.challenge == 20
    assert (
        "Unyielding Justice: Guan Yu can use his Action Surge to invoke a powerful aura of righteousness. Allies within 30 feet gain advantage on saving throws against fear and charm effects for 1 minute."
        in guan_yu_stat_block.special_abilities
    )
    assert (
        "Aura of Command: Allies within 10 feet of Guan Yu add his Charisma modifier (+4) to their saving throws."
        in guan_yu_stat_block.special_abilities
    )
    assert (
        guan_yu_stat_block.actions[0]
        == "Multiattack: Guan Yu makes three attacks with his Green Dragon Crescent Blade."
    )
    assert (
        guan_yu_stat_block.actions[1]
        == "Green Dragon Crescent Blade: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 1d10+5 slashing damage."
    )
    assert (
        "Sword: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d8+3 slashing damage."
        in guan_yu_stat_block.actions
    )
    assert not guan_yu_stat_block.bonus_actions
    assert (
        guan_yu_stat_block.reactions[0]
        == "Parry: When a creature hits Guan Yu with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    )


@pytest.fixture
def huang_zhong_stat_block():
    # Fixture to provide a sample instance of R3KTigerGeneralStatBlock for testing
    return R3KTigerGeneralStatBlock(**r3k_tiger_generals.huang_zhong_custom_stat_block)


def test_huang_zhong_stat_block(huang_zhong_stat_block):
    # Check if the Huang Zhong StatBlock instance is created correctly
    assert huang_zhong_stat_block.name == "Huang Zhong"
    assert huang_zhong_stat_block.hit_points == 180
    assert huang_zhong_stat_block.armor_class == 18
    assert huang_zhong_stat_block.speed == "30 ft."
    assert huang_zhong_stat_block.abilities.dexterity == 20
    assert huang_zhong_stat_block.saving_throws.dexterity == 10
    assert "Athletics +7" in huang_zhong_stat_block.skills
    assert "Perception +10" in huang_zhong_stat_block.skills
    assert huang_zhong_stat_block.damage_resistances == ""
    assert huang_zhong_stat_block.condition_immunities == ""
    assert huang_zhong_stat_block.senses == "passive Perception 20"
    assert huang_zhong_stat_block.languages == "Common"
    assert huang_zhong_stat_block.challenge == 20
    assert (
        "Precision Archer: Huang Zhong can make four attacks with his Longbow, adding his Dexterity modifier to the damage rolls."
        in huang_zhong_stat_block.special_abilities
    )
    assert (
        "Tactical Leader: Huang Zhong can use his Action Surge to grant a bonus action to an ally within 30 feet, allowing them to take an additional action."
        in huang_zhong_stat_block.special_abilities
    )
    assert (
        huang_zhong_stat_block.actions[0]
        == "Multiattack: Huang Zhong makes four attacks with his Longbow."
    )
    assert (
        huang_zhong_stat_block.actions[1]
        == "Longbow: Ranged Weapon Attack: +10 to hit, range 150/600 ft., one target. Hit: 1d8+5 piercing damage."
    )
    assert not huang_zhong_stat_block.bonus_actions
    assert (
        huang_zhong_stat_block.reactions[0]
        == "Parry: When a creature hits Huang Zhong with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    )


@pytest.fixture
def zhao_yun_stat_block():
    # Fixture to provide a sample instance of R3KTigerGeneralStatBlock for testing
    return R3KTigerGeneralStatBlock(**r3k_tiger_generals.zhao_yun_custom_stat_block)


def test_zhao_yun_stat_block(zhao_yun_stat_block):
    # Check if the Zhao Yun StatBlock instance is created correctly
    assert zhao_yun_stat_block.name == "Zhao Yun"
    assert zhao_yun_stat_block.hit_points == 168
    assert zhao_yun_stat_block.armor_class == 20
    assert zhao_yun_stat_block.speed == "30 ft., mounted 60 ft."
    assert zhao_yun_stat_block.abilities.strength == 16
    assert zhao_yun_stat_block.saving_throws.strength == 7
    assert "Athletics +7" in zhao_yun_stat_block.skills
    assert "Acrobatics +4" in zhao_yun_stat_block.skills
    assert zhao_yun_stat_block.damage_resistances == ""
    assert zhao_yun_stat_block.condition_immunities == ""
    assert zhao_yun_stat_block.senses == "passive Perception 14"
    assert zhao_yun_stat_block.languages == "Common"
    assert zhao_yun_stat_block.challenge == 18
    assert (
        "Combat Superiority: Zhao Yun has 7 superiority dice, which are d10s. He regains all expended superiority dice on a short or long rest."
        in zhao_yun_stat_block.special_abilities
    )
    assert (
        "Second Wind: Once per short rest, Zhao Yun can use a bonus action to regain hit points equal to 1d10 + his fighter level."
        in zhao_yun_stat_block.special_abilities
    )
    assert (
        "Action Surge: Once per short rest, Zhao Yun can take an additional action on his turn."
        in zhao_yun_stat_block.special_abilities
    )
    assert (
        zhao_yun_stat_block.actions[0]
        == "Multiattack: Zhao Yun makes three attacks with his sword or two attacks while mounted."
    )
    assert (
        zhao_yun_stat_block.actions[1]
        == "Sword: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d8+3 slashing damage."
    )
    assert not zhao_yun_stat_block.bonus_actions
    assert (
        zhao_yun_stat_block.reactions[0]
        == "Parry: When a creature hits Zhao Yun with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    )


@pytest.fixture
def ma_chao_stat_block():
    # Fixture to provide a sample instance of R3KTigerGeneralStatBlock for testing
    return R3KTigerGeneralStatBlock(**r3k_tiger_generals.ma_chao_custom_stat_block)


def test_ma_chao_stat_block(ma_chao_stat_block):
    # Check if the Ma Chao StatBlock instance is created correctly
    assert ma_chao_stat_block.name == "Ma Chao"
    assert ma_chao_stat_block.hit_points == 180
    assert ma_chao_stat_block.armor_class == 18
    assert ma_chao_stat_block.speed == "30 ft., mounted 60 ft."
    assert ma_chao_stat_block.abilities.dexterity == 16
    assert ma_chao_stat_block.saving_throws.dexterity == 7
    assert "Athletics +7" in ma_chao_stat_block.skills
    assert "Acrobatics +3" in ma_chao_stat_block.skills
    assert ma_chao_stat_block.damage_resistances == ""
    assert ma_chao_stat_block.condition_immunities == ""
    assert ma_chao_stat_block.senses == "passive Perception 14"
    assert ma_chao_stat_block.languages == "Common"
    assert ma_chao_stat_block.challenge == 18
    assert (
        "Combat Superiority: Ma Chao has 7 superiority dice, which are d8s. He regains all expended superiority dice on a short or long rest."
        in ma_chao_stat_block.special_abilities
    )
    assert (
        "Second Wind: Once per short rest, Ma Chao can use a bonus action to regain hit points equal to 1d10 + his fighter level."
        in ma_chao_stat_block.special_abilities
    )
    assert (
        "Primeval Awareness: As a ranger, Ma Chao can sense aberrations, celestials, dragons, elementals, fey, fiends, and undead within 1 mile."
        in ma_chao_stat_block.special_abilities
    )
    assert (
        ma_chao_stat_block.actions[0]
        == "Multiattack: Ma Chao makes three attacks with his bow or two attacks with his sword."
    )
    assert (
        ma_chao_stat_block.actions[1]
        == "Sword: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d8+3 slashing damage."
    )
    assert (
        ma_chao_stat_block.actions[2]
        == "Longbow: Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit: 1d8+3 piercing damage."
    )
    assert not ma_chao_stat_block.bonus_actions
    assert (
        ma_chao_stat_block.reactions[0]
        == "Parry: When a creature hits Ma Chao with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    )
