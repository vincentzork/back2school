import pytest


from .. import devil
from .. import abililty_scores
from .. import savings_throws


def test_behaviors():
    asmodeus = devil.Archdevil("Asmodeus")
    actual = asmodeus.get_common_behaviors_actions()
    expected = ['Manipulative schemes', 'Deals with mortals and other beings for power', 'Strategic planning', 'Master of manipulation and deception']

    assert actual == expected

def test_unique_weapon():
    asmodeus = devil.Archdevil("Asmodeus")
    actual = asmodeus.get_unique_attacks_weapons()
    expected = ["Infernal Sword", "Hellfire Whip"]
    assert actual == expected

from typing import Dict, List
from pydantic import BaseModel

class LegendaryActions(BaseModel):
    Infernal_Command: str

class AsmodeusStatBlock(BaseModel):
    Name: str
    Hit_Points: int
    Armor_Class: int
    Speed: str
    Abilities: abililty_scores.AbilityScores
    Saving_Throws: savings_throws.SavingThrows
    Skills: List[str]
    Damage_Resistances: str
    Damage_Immunities: str
    Condition_Immunities: str
    Senses: str
    Languages: str
    Challenge: int
    Special_Abilities: List[str]
    Legendary_Actions: LegendaryActions

@pytest.fixture
def asmodeus_stat_block():
    # Fixture to provide a sample instance of AsmodeusStatBlock for testing
    return AsmodeusStatBlock(
        Name="Asmodeus",
        Hit_Points=500,
        Armor_Class=25,
        Speed="40 ft, fly 60 ft",
        Abilities=abililty_scores.AbilityScores(
            strength=24,
            dexterity=18,
            constitution=26,
            intelligence=30,
            wisdom=24,
            charisma=32
        ),
        Saving_Throws=savings_throws.SavingThrows(
            STR="+14",
            DEX="+11",
            CON="+15",
            INT="+17",
            WIS="+14",
            CHA="+19"
        ),
        Skills=["Arcana +17", "Deception +19", "Insight +14", "Intimidation +19", "Perception +14", "Persuasion +19"],
        Damage_Resistances="cold; bludgeoning, piercing, and slashing from nonmagical attacks",
        Damage_Immunities="fire, poison",
        Condition_Immunities="charmed, exhausted, frightened, poisoned",
        Senses="truesight 120 ft., passive Perception 24",
        Languages="all, telepathy 120 ft.",
        Challenge=30,
        Special_Abilities=[
            "Innate Spellcasting",
            "Magic Resistance",
            "Infernal Pact",
            "Infernal Glare",
            "Hellish Rejuvenation",
            "Legendary Actions"
        ],
        Legendary_Actions={
            "Infernal_Command": "Asmodeus commands his minions with unparalleled authority."
        }
    )

def test_asmodeus_stat_block(asmodeus_stat_block):
    # Check if the AsmodeusStatBlock instance is created correctly
    assert asmodeus_stat_block.Name == "Asmodeus"
    assert asmodeus_stat_block.Hit_Points == 500
    assert asmodeus_stat_block.Armor_Class == 25
    assert asmodeus_stat_block.Speed == "40 ft, fly 60 ft"
    assert asmodeus_stat_block.Abilities.strength == 24
    assert asmodeus_stat_block.Saving_Throws.STR == 14
    assert "Deception +19" in asmodeus_stat_block.Skills
    assert asmodeus_stat_block.Damage_Resistances == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    assert asmodeus_stat_block.Damage_Immunities == "fire, poison"
    assert asmodeus_stat_block.Condition_Immunities == "charmed, exhausted, frightened, poisoned"
    assert asmodeus_stat_block.Senses == "truesight 120 ft., passive Perception 24"
    assert asmodeus_stat_block.Languages == "all, telepathy 120 ft."
    assert asmodeus_stat_block.Challenge == 30
    assert "Magic Resistance" in asmodeus_stat_block.Special_Abilities
    assert asmodeus_stat_block.Legendary_Actions.Infernal_Command == "Asmodeus commands his minions with unparalleled authority."
