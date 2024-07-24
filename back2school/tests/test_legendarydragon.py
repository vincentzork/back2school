"""""
import pytest

from .bahamut_stat_block import BahamutStatBlock, bahamut_custom_stat_block

@pytest.fixture
def bahamut_stat_block():
    return BahamutStatBlock(**bahamut_custom_stat_block)

def test_bahamut_stat_block(bahamut_stat_block):
    assert bahamut_stat_block.Dragon_Type == "Gold Dragon"
    assert bahamut_stat_block.Name == "Bahamut"
    assert bahamut_stat_block.Hit_Points == 585
    assert bahamut_stat_block.Armor_Class == 24
    assert bahamut_stat_block.Speed == "60 ft, fly 120 ft"
    assert bahamut_stat_block.Abilities.Strength == 30
    assert bahamut_stat_block.Abilities.Dexterity == 16
    assert bahamut_stat_block.Abilities.Constitution == 30
    assert bahamut_stat_block.Abilities.Intelligence == 26
    assert bahamut_stat_block.Abilities.Wisdom == 27
    assert bahamut_stat_block.Abilities.Charisma == 30
    assert bahamut_stat_block.Saving_Throws.STR == "+17"
    assert bahamut_stat_block.Saving_Throws.DEX == "+13"
    assert bahamut_stat_block.Saving_Throws.CON == "+17"
    assert bahamut_stat_block.Saving_Throws.INT == "+15"
    assert bahamut_stat_block.Saving_Throws.WIS == "+16"
    assert bahamut_stat_block.Saving_Throws.CHA == "+18"
    assert "Arcana +15" in bahamut_stat_block.Skills
    assert "Insight +16" in bahamut_stat_block.Skills
    assert "Perception +26" in bahamut_stat_block.Skills
    assert "Persuasion +18" in bahamut_stat_block.Skills
    assert "Religion +15" in bahamut_stat_block.Skills
    assert bahamut_stat_block.Damage_Resistances == "bludgeoning, piercing, and slashing from nonmagical attacks"
    assert bahamut_stat_block.Damage_Immunities == "radiant, necrotic"
    assert bahamut_stat_block.Condition_Immunities == "charmed, frightened, poisoned"
    assert bahamut_stat_block.Senses == "darkvision 240 ft., truesight 120 ft., passive Perception 36"
    assert bahamut_stat_block.Languages == "all, telepathy 120 ft."
    assert bahamut_stat_block.Challenge == 30
    assert (
        "Legendary Resistance (5/Day): If Bahamut fails a saving throw, he can choose to succeed instead."
        in bahamut_stat_block.Special_Abilities
    )
    assert (
        "Magic Resistance: Bahamut has advantage on saving throws against spells and other magical effects."
        in bahamut_stat_block.Special_Abilities
    )
    assert (
        "Divine Awareness: Bahamut knows if he hears a lie."
        in bahamut_stat_block.Special_Abilities
    )
    assert (
        "Regeneration: Bahamut regains 30 hit points at the start of his turn if he has at least 1 hit point."
        in bahamut_stat_block.Special_Abilities
    )
    assert (
        "Innate Spellcasting: Bahamut's spellcasting ability is Charisma (spell save DC 26). He can innately cast the following spells, requiring no material components: 3/day each: bless, cure wounds (9th level), divine word, holy aura"
        in bahamut_stat_block.Special_Abilities
    )
    assert (
        "Legendary Actions: Bahamut can take 5 legendary actions, choosing from the options below."
        in bahamut_stat_block.Special_Abilities
    )
    assert (
        bahamut_stat_block.Actions["Multiattack"]
        == "Bahamut can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws."
    )
    assert (
        bahamut_stat_block.Actions["Bite"]
        == "Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 32 (4d10 + 10) piercing damage plus 14 (4d6) radiant damage."
    )
    assert (
        bahamut_stat_block.Actions["Claw"]
        == "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 22 (4d6 + 10) slashing damage."
    )
    assert (
        bahamut_stat_block.Actions["Tail"]
        == "Melee Weapon Attack: +19 to hit, reach 25 ft., one target. Hit: 24 (4d8 + 10) bludgeoning damage."
    )
    assert (
        bahamut_stat_block.Actions["Frightful Presence"]
        == "Each creature of Bahamut's choice that is within 120 feet of him and aware of him must succeed on a DC 26 Wisdom saving throw or become frightened for 1 minute. A frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if Bahamut is within line of sight, ending the effect on itself on a success."
    )
    assert (
        bahamut_stat_block.Actions["Radiant Breath (Recharge 5-6)"]
        == "Bahamut exhales radiant energy in a 90-foot cone. Each creature in that area must make a DC 27 Dexterity saving throw, taking 91 (26d6) radiant damage on a failed save, or half as much damage on a successful one."
    )
    assert (
        bahamut_stat_block.Actions["Platinum Aura"]
        == "Bahamut radiates a calming aura in a 60-foot radius. Each creature of Bahamut's choice in that area has advantage on saving throws against being charmed or frightened, and other creatures have disadvantage on attack rolls against them."
    )
    assert bahamut_stat_block.Legendary_Actions["Detect"] == "Bahamut makes a Wisdom (Perception) check."
    assert bahamut_stat_block.Legendary_Actions["Tail Attack"] == "Bahamut makes a tail attack."
    assert (
        bahamut_stat_block.Legendary_Actions["Wing Attack (Costs 2 Actions)"]
        == "Bahamut beats his wings. Each creature within 15 ft. of Bahamut must succeed on a DC 25 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Bahamut can then fly up to half his flying speed."
    )
    assert bahamut_stat_block.Legendary_Actions["Bite Attack"] == "Bahamut makes a bite attack."
    assert bahamut_stat_block.Legendary_Actions["Claw Attack"] == "Bahamut makes a claw attack."

"""""



import pytest


from .. import LegendaryDragons

from ..LegendaryDragons import LegendaryDragonStatBlock

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


