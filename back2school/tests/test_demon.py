import pytest


from .. import demon

from ..demon import DemonLordStatBlock

@pytest.fixture
def demogorgon_stat_block():
    # Fixture to provide a sample instance of DemonLordStatBlock for testing
    return DemonLordStatBlock(**demon.demogorgon_custom_stat_block)

def test_demogorgon_stat_block(demogorgon_stat_block):
    # Check if the DemogorgonStatBlock instance is created correctly
    assert demogorgon_stat_block.name == "Demogorgon"
    assert demogorgon_stat_block.hit_points == 550
    assert demogorgon_stat_block.armor_class == 26
    assert demogorgon_stat_block.speed == "40 ft, swim 60 ft"
    assert demogorgon_stat_block.abilities.strength == 26
    assert demogorgon_stat_block.saving_throws.strength == 15
    assert "Deception +13" in demogorgon_stat_block.skills
    assert (
        demogorgon_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert demogorgon_stat_block.damage_immunities == "fire, poison"
    assert (
        demogorgon_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert demogorgon_stat_block.senses == "truesight 120 ft., passive Perception 22"
    assert demogorgon_stat_block.languages == "Abyssal, telepathy 120 ft."
    assert demogorgon_stat_block.challenge == 30
    assert "Demogorgon's Madness" in demogorgon_stat_block.special_abilities
    assert (
        demogorgon_stat_block.legendary_actions["Baleful Eye"]
        == "Demogorgon targets one creature he can see within 120 feet of him. The target must succeed on a DC 21 Wisdom saving throw or be affected by the madness of Demogorgon for 1 minute."
    )

@pytest.fixture
def orcus_stat_block():
    # Fixture to provide a sample instance of DemonLordStatBlock for testing
    return DemonLordStatBlock(**demon.orcus_custom_stat_block)

def test_orcus_stat_block(orcus_stat_block):
    # Check if the OrcusStatBlock instance is created correctly
    assert orcus_stat_block.name == "Orcus"
    assert orcus_stat_block.hit_points == 600
    assert orcus_stat_block.armor_class == 25
    assert orcus_stat_block.speed == "30 ft, fly 60 ft"
    assert orcus_stat_block.abilities.strength == 24
    assert orcus_stat_block.saving_throws.strength == 14
    assert "Deception +15" in orcus_stat_block.skills
    assert (
        orcus_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert orcus_stat_block.damage_immunities == "fire, poison"
    assert (
        orcus_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert orcus_stat_block.senses == "truesight 120 ft., passive Perception 20"
    assert orcus_stat_block.languages == "Abyssal, telepathy 120 ft."
    assert orcus_stat_block.challenge == 26
    assert "Death's Gaze" in orcus_stat_block.special_abilities
    assert (
        orcus_stat_block.legendary_actions["Teleport"]
        == "Orcus magically teleports, along with any equipment he is wearing or carrying, up to 120 feet to an unoccupied space he can see."
    )