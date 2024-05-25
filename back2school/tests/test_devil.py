import pytest


from .. import devil
from .. import abililty_scores
from .. import savings_throws


def test_behaviors():
    asmodeus = devil.Archdevil("Asmodeus")
    actual = asmodeus.common_behaviors_actions
    expected = [
        "Manipulative schemes",
        "Deals with mortals and other beings for power",
        "Strategic planning",
        "Master of manipulation and deception",
    ]

    assert actual == expected


def test_unique_weapon():
    asmodeus = devil.Archdevil("Asmodeus")
    actual = asmodeus.unique_attacks_weapons
    expected = ["Infernal Sword", "Hellfire Whip"]
    assert actual == expected


from typing import Dict, List
from pydantic import BaseModel


class ArchdevilStatBlock(BaseModel):
    unique_attacks_weapons: List[str]
    common_behaviors_actions: List[str]
    name: str
    hit_points: int
    armor_class: int
    speed: str
    abilities: abililty_scores.AbilityScores
    saving_throws: savings_throws.SavingThrows
    skills: List[str]
    damage_resistances: str
    damage_immunities: str
    condition_immunities: str
    senses: str
    languages: str
    challenge: int
    special_abilities: List[str]
    legendary_actions: Dict[str, str]


@pytest.fixture
def asmodeus_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return ArchdevilStatBlock(**devil.asmodeus_custom_stat_block)


def test_asmodeus_stat_block(asmodeus_stat_block):
    # Check if the AsmodeusStatBlock instance is created correctly
    assert asmodeus_stat_block.name == "Asmodeus"
    assert asmodeus_stat_block.hit_points == 500
    assert asmodeus_stat_block.armor_class == 25
    assert asmodeus_stat_block.speed == "40 ft, fly 60 ft"
    assert asmodeus_stat_block.abilities.strength == 24
    assert asmodeus_stat_block.saving_throws.strength == 14
    assert "Deception +19" in asmodeus_stat_block.skills
    assert (
        asmodeus_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert asmodeus_stat_block.damage_immunities == "fire, poison"
    assert (
        asmodeus_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert asmodeus_stat_block.senses == "truesight 120 ft., passive Perception 24"
    assert asmodeus_stat_block.languages == "all, telepathy 120 ft."
    assert asmodeus_stat_block.challenge == 30
    assert "Magic Resistance" in asmodeus_stat_block.special_abilities
    assert (
        asmodeus_stat_block.legendary_actions["Infernal Command"]
        == "Asmodeus commands his minions with unparalleled authority."
    )


@pytest.fixture
def baalzebul_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return ArchdevilStatBlock(**devil.baalzebul_custom_stat_block)


def test_baalzebul_stat_block(baalzebul_stat_block):
    # Check if the BaalzebulStatBlock instance is created correctly
    assert baalzebul_stat_block.name == "Baalzebul"
    assert baalzebul_stat_block.hit_points == 450
    assert baalzebul_stat_block.armor_class == 24
    assert baalzebul_stat_block.speed == "40 ft, fly 60 ft"
    assert baalzebul_stat_block.abilities.strength == 22
    assert baalzebul_stat_block.saving_throws.strength == 13
    assert "Deception +18" in baalzebul_stat_block.skills
    assert (
        baalzebul_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert baalzebul_stat_block.damage_immunities == "fire, poison"
    assert (
        baalzebul_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert baalzebul_stat_block.senses == "truesight 120 ft., passive Perception 23"
    assert baalzebul_stat_block.languages == "all, telepathy 120 ft."
    assert baalzebul_stat_block.challenge == 29
    assert "Corrupting Touch" in baalzebul_stat_block.special_abilities
    assert (
        baalzebul_stat_block.legendary_actions["Infernal Command"]
        == "Baalzebul commands his minions with unparalleled authority."
    )


@pytest.fixture
def belial_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return ArchdevilStatBlock(**devil.belial_custom_stat_block)


def test_belial_stat_block(belial_stat_block):
    # Check if the BelialStatBlock instance is created correctly
    assert belial_stat_block.name == "Belial"
    assert belial_stat_block.hit_points == 480
    assert belial_stat_block.armor_class == 25
    assert belial_stat_block.speed == "40 ft, fly 60 ft"
    assert belial_stat_block.abilities.strength == 24
    assert belial_stat_block.saving_throws.strength == 14
    assert "Deception +17" in belial_stat_block.skills
    assert (
        belial_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert belial_stat_block.damage_immunities == "fire, poison"
    assert (
        belial_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert belial_stat_block.senses == "truesight 120 ft., passive Perception 23"
    assert belial_stat_block.languages == "all, telepathy 120 ft."
    assert belial_stat_block.challenge == 28
    assert "Fire Aura" in belial_stat_block.special_abilities
    assert (
        belial_stat_block.legendary_actions["Infernal Command"]
        == "Belial commands his minions with unparalleled authority."
    )


@pytest.fixture
def dispater_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return ArchdevilStatBlock(**devil.dispater_custom_stat_block)


def test_dispater_stat_block(dispater_stat_block):
    # Check if the DispaterStatBlock instance is created correctly
    assert dispater_stat_block.name == "Dispater"
    assert dispater_stat_block.hit_points == 470
    assert dispater_stat_block.armor_class == 25
    assert dispater_stat_block.speed == "40 ft, fly 60 ft"
    assert dispater_stat_block.abilities.strength == 22
    assert dispater_stat_block.saving_throws.strength == 13
    assert "Deception +17" in dispater_stat_block.skills
    assert (
        dispater_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert dispater_stat_block.damage_immunities == "fire, poison"
    assert (
        dispater_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert dispater_stat_block.senses == "truesight 120 ft., passive Perception 23"
    assert dispater_stat_block.languages == "all, telepathy 120 ft."
    assert dispater_stat_block.challenge == 28
    assert "Lord of Dis" in dispater_stat_block.special_abilities
    assert (
        dispater_stat_block.legendary_actions["Infernal Command"]
        == "Dispater commands his minions with unparalleled authority."
    )


@pytest.fixture
def mammon_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return ArchdevilStatBlock(**devil.mammon_custom_stat_block)


def test_mammon_stat_block(mammon_stat_block):
    # Check if the MammonStatBlock instance is created correctly
    assert mammon_stat_block.name == "Mammon"
    assert mammon_stat_block.hit_points == 460
    assert mammon_stat_block.armor_class == 24
    assert mammon_stat_block.speed == "40 ft, fly 60 ft"
    assert mammon_stat_block.abilities.strength == 22
    assert mammon_stat_block.saving_throws.strength == 13
    assert "Deception +18" in mammon_stat_block.skills
    assert (
        mammon_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert mammon_stat_block.damage_immunities == "fire, poison"
    assert (
        mammon_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert mammon_stat_block.senses == "truesight 120 ft., passive Perception 23"
    assert mammon_stat_block.languages == "all, telepathy 120 ft."
    assert mammon_stat_block.challenge == 28
    assert "Golden Gaze" in mammon_stat_block.special_abilities
    assert (
        mammon_stat_block.legendary_actions["Infernal Command"]
        == "Mammon commands his minions with unparalleled authority."
    )


@pytest.fixture
def mephistopheles_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return ArchdevilStatBlock(**devil.mephistopheles_custom_stat_block)


def test_mephistopheles_stat_block(mephistopheles_stat_block):
    # Check if the MephistophelesStatBlock instance is created correctly
    assert mephistopheles_stat_block.name == "Mephistopheles"
    assert mephistopheles_stat_block.hit_points == 500
    assert mephistopheles_stat_block.armor_class == 26
    assert mephistopheles_stat_block.speed == "40 ft, fly 60 ft"
    assert mephistopheles_stat_block.abilities.strength == 24
    assert mephistopheles_stat_block.saving_throws.strength == 14
    assert "Insight +14" in mephistopheles_stat_block.skills
    assert (
        mephistopheles_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert mephistopheles_stat_block.damage_immunities == "fire, poison"
    assert (
        mephistopheles_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert (
        mephistopheles_stat_block.senses == "truesight 120 ft., passive Perception 24"
    )
    assert mephistopheles_stat_block.languages == "all, telepathy 120 ft."
    assert mephistopheles_stat_block.challenge == 30
    assert "Hellfire Aura" in mephistopheles_stat_block.special_abilities
    assert (
        mephistopheles_stat_block.legendary_actions["Infernal Command"]
        == "Mephistopheles commands his minions with unparalleled authority."
    )


@pytest.fixture
def geryon_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return ArchdevilStatBlock(**devil.geryon_custom_stat_block)


def test_geryon_stat_block(geryon_stat_block):
    # Check if the GeryonStatBlock instance is created correctly
    assert geryon_stat_block.name == "Geryon"
    assert geryon_stat_block.hit_points == 480
    assert geryon_stat_block.armor_class == 25
    assert geryon_stat_block.speed == "40 ft, fly 60 ft"
    assert geryon_stat_block.abilities.strength == 24
    assert geryon_stat_block.saving_throws.strength == 14
    assert "Insight +14" in geryon_stat_block.skills
    assert (
        geryon_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert geryon_stat_block.damage_immunities == "fire, poison"
    assert (
        geryon_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert geryon_stat_block.senses == "truesight 120 ft., passive Perception 24"
    assert geryon_stat_block.languages == "all, telepathy 120 ft."
    assert geryon_stat_block.challenge == 29
    assert "Fear Aura" in geryon_stat_block.special_abilities
    assert (
        geryon_stat_block.legendary_actions["Infernal Command"]
        == "Geryon commands his minions with unparalleled authority."
    )
