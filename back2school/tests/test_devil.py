import pytest


from .. import devil
from .. import abililty_scores
from .. import savings_throws


def test_behaviors():
    asmodeus = devil.Archdevil("Asmodeus")
    actual = asmodeus.get_common_behaviors_actions()
    expected = [
        "Manipulative schemes",
        "Deals with mortals and other beings for power",
        "Strategic planning",
        "Master of manipulation and deception",
    ]

    assert actual == expected


def test_unique_weapon():
    asmodeus = devil.Archdevil("Asmodeus")
    actual = asmodeus.get_unique_attacks_weapons()
    expected = ["Infernal Sword", "Hellfire Whip"]
    assert actual == expected


from typing import Dict, List
from pydantic import BaseModel


class AsmodeusStatBlock(BaseModel):
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
    # Fixture to provide a sample instance of AsmodeusStatBlock for testing
    return AsmodeusStatBlock(**devil.asmodeus_custom_stat_block)


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
