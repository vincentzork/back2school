import pytest

from .. import legendary_humanoids

from ..legendary_humanoids import LegendaryGiantStatBlock

@pytest.fixture

def test_gog_the_crusher_stat_block(gog_the_crusher_stat_block):
    # Check if the Gog the Crusher StatBlock instance is created correctly
    assert gog_the_crusher_stat_block.name == "Gog the Crusher"
    assert gog_the_crusher_stat_block.hit_points == 350
    assert gog_the_crusher_stat_block.armor_class == 19
    assert gog_the_crusher_stat_block.speed == "40 ft."
    assert gog_the_crusher_stat_block.abilities.strength == 26
    assert gog_the_crusher_stat_block.saving_throws.strength == 14
    assert "Athletics +18" in gog_the_crusher_stat_block.skills
    assert gog_the_crusher_stat_block.damage_resistances == "bludgeoning, piercing, and slashing from nonmagical attacks while raging"
    assert gog_the_crusher_stat_block.condition_immunities == "frightened while raging"
    assert gog_the_crusher_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert gog_the_crusher_stat_block.languages == "Giant, Common"
    assert gog_the_crusher_stat_block.challenge == 19
    assert (
        "Juggernaut's Fury: When Gog uses his Rage feature, he gains an additional +2 bonus to all damage rolls. His melee weapon attacks also have the chance to knock creatures prone (DC 19 Strength saving throw)."
        in gog_the_crusher_stat_block.special_abilities
    )
    assert (
        gog_the_crusher_stat_block.legendary_actions["Crushing Blow"]
        == "Gog makes a single melee weapon attack with his Crushing Maul. If the attack hits, the target must succeed on a DC 19 Constitution saving throw or be stunned until the end of Gog's next turn."
    )
    assert (
        gog_the_crusher_stat_block.actions[0]
        == "Multiattack: Gog makes three attacks with his Crushing Maul or Spiked Gauntlets."
    )
    assert (
        gog_the_crusher_stat_block.actions[1]
        == "Crushing Maul: Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 6) bludgeoning damage."
    )
    assert (
        gog_the_crusher_stat_block.bonus_actions[0]
        == "Rage: Gog can enter a rage as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage, as well as a +2 bonus to damage rolls."
    )
    assert (
        gog_the_crusher_stat_block.reactions[0]
        == "Unyielding: When Gog is subjected to an effect that allows him to make a Strength or Constitution saving throw to take only half damage, he can use his reaction to take no damage if he succeeds on the saving throw, or only half damage if he fails."
    )