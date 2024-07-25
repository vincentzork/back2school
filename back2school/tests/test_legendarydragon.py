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

# Define the fixture for Tiamat's stat block
@pytest.fixture
def tiamat_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.tiamat_custom_stat_block)

    # Test function for Tiamat's stat block
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
    assert tiamat_stat_block.damage_immunities == "acid, cold, fire, lightning, poison"
    assert tiamat_stat_block.condition_immunities == "charmed, frightened, poisoned"
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
    assert (
        tiamat_stat_block.actions["Breath Weapons (Recharge 5-6)"]
        == "Tiamat uses one of the following breath weapons. She can use each breath weapon only once per recharge cycle."
    )
    assert (
        tiamat_stat_block.actions["Acid Breath (Black Dragon Head)"]
        == "Tiamat exhales acid in a 90-foot line that is 10 feet wide. Each creature in that line must make a DC 27 Dexterity saving throw, taking 88 (16d10) acid damage on a failed save, or half as much damage on a successful one."
    )
    assert (
        tiamat_stat_block.actions["Lightning Breath (Blue Dragon Head)"]
        == "Tiamat exhales lightning in a 120-foot line that is 10 feet wide. Each creature in that line must make a DC 27 Dexterity saving throw, taking 110 (20d10) lightning damage on a failed save, or half as much damage on a successful one."
    )
    assert (
        tiamat_stat_block.actions["Fire Breath (Red Dragon Head)"]
        == "Tiamat exhales fire in a 90-foot cone. Each creature in that area must make a DC 27 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one."
    )
    assert (
        tiamat_stat_block.actions["Poison Breath (Green Dragon Head)"]
        == "Tiamat exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 27 Constitution saving throw, taking 77 (22d6) poison damage on a failed save, or half as much damage on a successful one."
    )
    assert (
        tiamat_stat_block.actions["Cold Breath (White Dragon Head)"]
        == "Tiamat exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 27 Constitution saving throw, taking 72 (16d8) cold damage on a failed save, or half as much damage on a successful one."
    )

@pytest.fixture
def shimmergloom_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.shimmergloom_custom_stat_block)

def test_shimmergloom_stat_block(shimmergloom_stat_block):
    # Check if the Shimmergloom StatBlock instance is created correctly
    assert shimmergloom_stat_block.name == "Shimmergloom"
    assert shimmergloom_stat_block.hit_points == 370
    assert shimmergloom_stat_block.armor_class == 21
    assert shimmergloom_stat_block.speed == "60 ft, fly 80 ft"
    assert shimmergloom_stat_block.abilities.strength == 23
    assert shimmergloom_stat_block.saving_throws.strength == 13
    assert "Perception +17" in shimmergloom_stat_block.skills
    assert shimmergloom_stat_block.damage_resistances == "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks"
    assert shimmergloom_stat_block.damage_immunities == "cold, necrotic"
    assert shimmergloom_stat_block.condition_immunities == "charmed, exhaustion, frightened, poisoned"
    assert shimmergloom_stat_block.senses == "darkvision 240 ft., truesight 120 ft., passive Perception 27"
    assert shimmergloom_stat_block.languages == "Common, Draconic, telepathy 120 ft."
    assert shimmergloom_stat_block.challenge == 24
    assert (
        "Legendary Resistance (3/Day): If Shimmergloom fails a saving throw, it can choose to succeed instead."
        in shimmergloom_stat_block.special_abilities
    )
    assert (
        shimmergloom_stat_block.legendary_actions["Detect"]
        == "Shimmergloom makes a Wisdom (Perception) check."
    )
    assert (
        shimmergloom_stat_block.actions["Multiattack"]
        == "Shimmergloom makes three attacks: one with its bite and two with its claws."
    )
    assert (
        shimmergloom_stat_block.actions["Bite"]
        == "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 36 (4d10 + 16) piercing damage plus 14 (4d6) necrotic damage."
    )
    assert (
        shimmergloom_stat_block.actions["Shadow Breath (Recharge 5-6)"]
        == "Shimmergloom exhales shadowy energy in a 90-foot cone. Each creature in that area must make a DC 21 Dexterity saving throw, taking 63 (18d6) necrotic damage on a failed save, or half as much damage on a successful one."
    )

@pytest.fixture
def ashardalon_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.ashardalon_custom_stat_block)
def test_ashardalon_stat_block(ashardalon_stat_block):
    # Check if the Ashardalon StatBlock instance is created correctly
    assert ashardalon_stat_block.name == "Ashardalon"
    assert ashardalon_stat_block.hit_points == 500
    assert ashardalon_stat_block.armor_class == 21
    assert ashardalon_stat_block.speed == "40 ft, fly 80 ft (hover)"
    assert ashardalon_stat_block.abilities.strength == 27
    assert ashardalon_stat_block.saving_throws.strength == 15  # Adjusted to expect an integer
    assert ashardalon_stat_block.saving_throws.dexterity == 5  # Added for consistency
    assert "Perception +16" in ashardalon_stat_block.skills
    assert (
        ashardalon_stat_block.damage_resistances
        == "fire; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert ashardalon_stat_block.damage_immunities == "none"
    assert ashardalon_stat_block.condition_immunities == "exhausted, frightened"
    assert ashardalon_stat_block.senses == "blindsight 60 ft., darkvision 120 ft., passive Perception 26"
    assert ashardalon_stat_block.languages == "Common, Draconic"
    assert ashardalon_stat_block.challenge == 24
    assert (
        "Legendary Resistance (3/Day): If Ashardalon fails a saving throw, he can choose to succeed instead."
        in ashardalon_stat_block.special_abilities
    )
    assert (
        ashardalon_stat_block.legendary_actions["detect"]
        == "Ashardalon makes a Wisdom (Perception) check."
    )
    assert (
        ashardalon_stat_block.actions["multiattack"]
        == "Ashardalon can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws."
    )
    assert (
        ashardalon_stat_block.actions["bite"]
        == "Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 34 (4d10 + 13) piercing damage plus 14 (4d6) fire damage."
    )
    assert (
        ashardalon_stat_block.actions["claw"]
        == "Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 27 (4d6 + 13) slashing damage."
    )
    assert (
        ashardalon_stat_block.legendary_actions["tail_attack"]
        == "Ashardalon makes a tail attack."
    )
    assert (
        ashardalon_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Ashardalon beats his wings. Each creature within 15 feet of him must succeed on a DC 23 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Ashardalon can then fly up to half his flying speed."
    )

@pytest.fixture
def null_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.null_custom_stat_block)

def test_null_stat_block(null_stat_block):
    # Check if the Null StatBlock instance is created correctly
    assert null_stat_block.name == "Null, The Deathwyrm"
    assert null_stat_block.hit_points == 550
    assert null_stat_block.armor_class == 23
    assert null_stat_block.speed == "40 ft, fly 80 ft (hover)"
    assert null_stat_block.abilities.strength == 24
    assert null_stat_block.saving_throws.strength == 14  # Adjusted to expect an integer
    assert null_stat_block.saving_throws.dexterity == 8  # Added for consistency
    assert "Perception +16" in null_stat_block.skills
    assert (
        null_stat_block.damage_resistances
        == "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert null_stat_block.damage_immunities == "necrotic, poison"
    assert null_stat_block.condition_immunities == "exhausted, frightened, paralyzed, poisoned"
    assert null_stat_block.senses == "blindsight 60 ft., darkvision 120 ft., passive Perception 26"
    assert null_stat_block.languages == "Common, Draconic"
    assert null_stat_block.challenge == 26
    assert (
        "Legendary Resistance (3/Day): If Null fails a saving throw, he can choose to succeed instead."
        in null_stat_block.special_abilities
    )
    assert (
        null_stat_block.legendary_actions["detect"]
        == "Null makes a Wisdom (Perception) check."
    )
    assert (
        null_stat_block.actions["multiattack"]
        == "Null can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws."
    )
    assert (
        null_stat_block.actions["bite"]
        == "Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 34 (4d10 + 12) piercing damage plus 14 (4d6) necrotic damage. On a hit, Null can use Life Drain."
    )
    assert (
        null_stat_block.actions["claw"]
        == "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 27 (4d6 + 12) slashing damage."
    )
    assert (
        null_stat_block.legendary_actions["tail_attack"]
        == "Null makes a tail attack."
    )
    assert (
        null_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Null beats his wings. Each creature within 15 feet of him must succeed on a DC 24 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. Null can then fly up to half his flying speed."
    )

@pytest.fixture
def iymrith_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.iymrith_custom_stat_block)

def test_iymrith_stat_block(iymrith_stat_block):
    # Check if the Iymrith StatBlock instance is created correctly
    assert iymrith_stat_block.name == "Iymrith, the Doom of the Desert"
    assert iymrith_stat_block.hit_points == 481
    assert iymrith_stat_block.armor_class == 22
    assert iymrith_stat_block.speed == "40 ft, burrow 40 ft, fly 120 ft"
    assert iymrith_stat_block.abilities.strength == 27
    assert iymrith_stat_block.saving_throws.strength == 16
    assert iymrith_stat_block.saving_throws.dexterity == 8
    assert "Perception +17" in iymrith_stat_block.skills
    assert (
        iymrith_stat_block.damage_immunities
        == "lightning"
    )
    assert iymrith_stat_block.condition_immunities == "exhausted, paralyzed"
    assert iymrith_stat_block.senses == "blindsight 60 ft., darkvision 120 ft., passive Perception 27"
    assert iymrith_stat_block.languages == "Common, Draconic"
    assert iymrith_stat_block.challenge == 23
    assert (
        "Legendary Resistance (3/Day): If Iymrith fails a saving throw, she can choose to succeed instead."
        in iymrith_stat_block.special_abilities
    )
    assert (
        iymrith_stat_block.legendary_actions["detect"]
        == "Iymrith makes a Wisdom (Perception) check."
    )
    assert (
        iymrith_stat_block.actions["multiattack"]
        == "Iymrith can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws."
    )
    assert (
        iymrith_stat_block.actions["bite"]
        == "Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 36 (4d10 + 16) piercing damage."
    )
    assert (
        iymrith_stat_block.actions["claw"]
        == "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 28 (4d6 + 16) slashing damage."
    )
    assert (
        iymrith_stat_block.legendary_actions["tail_attack"]
        == "Iymrith makes a tail attack."
    )
    assert (
        iymrith_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Iymrith beats her wings. Each creature within 15 feet of her must succeed on a DC 24 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Iymrith can then fly up to half her flying speed."
    )

@pytest.fixture
def dragotha_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**LegendaryDragons.dragotha_custom_stat_block)

def test_dragotha_stat_block(dragotha_stat_block):
    # Check if the Dragotha StatBlock instance is created correctly
    assert dragotha_stat_block.name == "Dragotha"
    assert dragotha_stat_block.hit_points == 367
    assert dragotha_stat_block.armor_class == 20
    assert dragotha_stat_block.speed == "40 ft, fly 80 ft (hover)"
    assert dragotha_stat_block.abilities.strength == 22
    assert dragotha_stat_block.abilities.dexterity == 10
    assert dragotha_stat_block.abilities.constitution == 20
    assert dragotha_stat_block.abilities.intelligence == 18
    assert dragotha_stat_block.abilities.wisdom == 15
    assert dragotha_stat_block.abilities.charisma == 21
    assert dragotha_stat_block.saving_throws.strength == 12
    assert dragotha_stat_block.saving_throws.dexterity == 6
    assert dragotha_stat_block.saving_throws.constitution == 11
    assert dragotha_stat_block.saving_throws.intelligence == 10
    assert dragotha_stat_block.saving_throws.wisdom == 9
    assert dragotha_stat_block.saving_throws.charisma == 11
    assert "Perception +15" in dragotha_stat_block.skills
    assert (
        dragotha_stat_block.damage_resistances
        == "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert dragotha_stat_block.damage_immunities == "cold, poison"
    assert dragotha_stat_block.condition_immunities == "charmed, exhausted, frightened, paralyzed, poisoned"
    assert dragotha_stat_block.senses == "blindsight 60 ft., darkvision 120 ft., passive Perception 25"
    assert dragotha_stat_block.languages == "Common, Draconic, plus any three languages"
    assert dragotha_stat_block.challenge == 22
    assert (
        "Legendary Resistance (3/Day): If Dragotha fails a saving throw, he can choose to succeed instead."
        in dragotha_stat_block.special_abilities
    )
    assert (
        dragotha_stat_block.legendary_actions["detect"]
        == "Dragotha makes a Wisdom (Perception) check."
    )
    assert (
        dragotha_stat_block.actions["multiattack"]
        == "Dragotha can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws."
    )
    assert (
        dragotha_stat_block.actions["bite"]
        == "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 23 (3d10 + 7) piercing damage plus 14 (4d6) necrotic damage."
    )
    assert (
        dragotha_stat_block.actions["claw"]
        == "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 7) slashing damage."
    )
    assert (
        dragotha_stat_block.legendary_actions["tail_attack"]
        == "Dragotha makes a tail attack."
    )
    assert (
        dragotha_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Dragotha beats his wings. Each creature within 15 feet of him must succeed on a DC 21 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Dragotha can then fly up to half his flying speed."
    )
