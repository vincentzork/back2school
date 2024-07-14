import pytest


from .. import LegendaryDragons

from ..LegendaryDragons import LegendaryDragonStatBlock

@pytest.fixture
def tiamat_stat_block():
    # Fixture to provide a sample instance of LegendaryDragons for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.tiamat_custom_stat_block)

def test_tiamat_stat_block(tiamat_stat_block):
    # Check if the Tiamat StatBlock instance is created correctly
    assert tiamat_stat_block.name == "Tiamat"
    assert tiamat_stat_block.hit_points == 615
    assert tiamat_stat_block.armor_class == 25
    assert tiamat_stat_block.speed == "60 ft, fly 120 ft"
    assert tiamat_stat_block.abilities.strength == 30
    assert tiamat_stat_block.saving_throws.strength == 17
    assert "Arcana +15" in tiamat_stat_block.skills
    assert (
        tiamat_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        tiamat_stat_block.damage_immunities
        == "acid, cold, fire, lightning, poison"
    )
    assert (
        tiamat_stat_block.condition_immunities
        == "charmed, frightened, poisoned"
    )
    assert tiamat_stat_block.senses == "darkvision 240 ft., truesight 120 ft., passive Perception 32"
    assert tiamat_stat_block.languages == "all, telepathy 120 ft."
    assert tiamat_stat_block.challenge == 30
    assert (
        "Legendary Resistance (5/Day): If Tiamat fails a saving throw, she can choose to succeed instead."
        in tiamat_stat_block.special_abilities
    )
    assert (
        tiamat_stat_block.legendary_actions["Detect"]
        == "Tiamat makes a Wisdom (Perception) check."
    )
    assert (
        tiamat_stat_block.actions["Multiattack"]
        == "Tiamat can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws."
    )
    assert (
        tiamat_stat_block.actions["Bite"]
        == "Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 32 (4d10 + 10) piercing damage plus 14 (4d6) damage of a type based on the dragon head used: acid (black), lightning (blue), fire (red), poison (green), or cold (white)."
    )
    assert tiamat_stat_block.bonus_actions[0] == "Wing Attack (Costs 2 Actions): Tiamat beats her wings. Each creature within 15 ft. of Tiamat must succeed on a DC 25 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Tiamat can then fly up to half her flying speed."
    assert (
        tiamat_stat_block.reactions[0]
        == "Multiple Heads: Tiamat can take one reaction per turn, rather than only one per round. She also has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious."
    )

@pytest.fixture
def bahamut_stat_block():
    # Fixture to provide a sample instance of LegendaryDragons for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.bahamut_custom_stat_block)

def test_bahamut_stat_block(bahamut_stat_block):
    # Check if the Bahamut StatBlock instance is created correctly
    assert bahamut_stat_block.name == "Bahamut"
    assert bahamut_stat_block.hit_points == 585
    assert bahamut_stat_block.armor_class == 24
    assert bahamut_stat_block.speed == "60 ft, fly 120 ft"
    assert bahamut_stat_block.abilities.strength == 30
    assert bahamut_stat_block.saving_throws.strength == 17
    assert "Arcana +15" in bahamut_stat_block.skills
    assert (
        bahamut_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert bahamut_stat_block.damage_immunities == "radiant, necrotic"
    assert bahamut_stat_block.condition_immunities == "charmed, frightened, poisoned"
    assert bahamut_stat_block.senses == "darkvision 240 ft., truesight 120 ft., passive Perception 36"
    assert bahamut_stat_block.languages == "all, telepathy 120 ft."
    assert bahamut_stat_block.challenge == 30
    assert (
        "Legendary Resistance (5/Day): If Bahamut fails a saving throw, he can choose to succeed instead."
        in bahamut_stat_block.special_abilities
    )
    assert (
        bahamut_stat_block.legendary_actions["Detect"]
        == "Bahamut makes a Wisdom (Perception) check."
    )
    assert (
        bahamut_stat_block.actions["Multiattack"]
        == "Bahamut can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws."
    )
    assert (
        bahamut_stat_block.actions["Bite"]
        == "Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 32 (4d10 + 10) piercing damage plus 14 (4d6) radiant damage."
    )
    assert (
        bahamut_stat_block.actions["Radiant Breath (Recharge 5-6)"]
        == "Bahamut exhales radiant energy in a 90-foot cone. Each creature in that area must make a DC 27 Dexterity saving throw, taking 91 (26d6) radiant damage on a failed save, or half as much damage on a successful one."
    )
    assert (
        bahamut_stat_block.actions["Platinum Aura"]
        == "Bahamut radiates a calming aura in a 60-foot radius. Each creature of Bahamut's choice in that area has advantage on saving throws against being charmed or frightened, and other creatures have disadvantage on attack rolls against them."
    )
    assert (
        bahamut_stat_block.reactions[0]
        == "Multiple Heads: Bahamut can take one reaction per turn, rather than only one per round. She also has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious."
    )

