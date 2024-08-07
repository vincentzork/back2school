import pytest


from .. import legendary_dragons

from ..legendary_dragons import LegendaryDragonStatBlock


@pytest.fixture
def bahamut_stat_block():
    # Fixture to provide a sample instance of legendary_dragons for testing
    return LegendaryDragonStatBlock(**legendary_dragons.bahamut_custom_stat_block)


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
    assert (
        bahamut_stat_block.senses
        == "darkvision 240 ft., truesight 120 ft., passive Perception 36"
    )
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
    return LegendaryDragonStatBlock(**legendary_dragons.tiamat_custom_stat_block)

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
    assert (
        tiamat_stat_block.senses
        == "darkvision 240 ft., truesight 120 ft., passive Perception 32"
    )
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
    return LegendaryDragonStatBlock(**legendary_dragons.shimmergloom_custom_stat_block)


def test_shimmergloom_stat_block(shimmergloom_stat_block):
    # Check if the Shimmergloom StatBlock instance is created correctly
    assert shimmergloom_stat_block.name == "Shimmergloom"
    assert shimmergloom_stat_block.hit_points == 370
    assert shimmergloom_stat_block.armor_class == 21
    assert shimmergloom_stat_block.speed == "60 ft, fly 80 ft"
    assert shimmergloom_stat_block.abilities.strength == 23
    assert shimmergloom_stat_block.saving_throws.strength == 13
    assert "Perception +17" in shimmergloom_stat_block.skills
    assert (
        shimmergloom_stat_block.damage_resistances
        == "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert shimmergloom_stat_block.damage_immunities == "cold, necrotic"
    assert (
        shimmergloom_stat_block.condition_immunities
        == "charmed, exhaustion, frightened, poisoned"
    )
    assert (
        shimmergloom_stat_block.senses
        == "darkvision 240 ft., truesight 120 ft., passive Perception 27"
    )
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
    return LegendaryDragonStatBlock(**legendary_dragons.ashardalon_custom_stat_block)


def test_ashardalon_stat_block(ashardalon_stat_block):
    # Check if the Ashardalon StatBlock instance is created correctly
    assert ashardalon_stat_block.name == "Ashardalon"
    assert ashardalon_stat_block.hit_points == 500
    assert ashardalon_stat_block.armor_class == 21
    assert ashardalon_stat_block.speed == "40 ft, fly 80 ft (hover)"
    assert ashardalon_stat_block.abilities.strength == 27
    assert (
        ashardalon_stat_block.saving_throws.strength == 15
    )  # Adjusted to expect an integer
    assert ashardalon_stat_block.saving_throws.dexterity == 5  # Added for consistency
    assert "Perception +16" in ashardalon_stat_block.skills
    assert (
        ashardalon_stat_block.damage_resistances
        == "fire; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert ashardalon_stat_block.damage_immunities == "none"
    assert ashardalon_stat_block.condition_immunities == "exhausted, frightened"
    assert (
        ashardalon_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 26"
    )
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
    return LegendaryDragonStatBlock(**legendary_dragons.null_custom_stat_block)


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
    assert (
        null_stat_block.condition_immunities
        == "exhausted, frightened, paralyzed, poisoned"
    )
    assert (
        null_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 26"
    )
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
        null_stat_block.legendary_actions["tail_attack"] == "Null makes a tail attack."
    )
    assert (
        null_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Null beats his wings. Each creature within 15 feet of him must succeed on a DC 24 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. Null can then fly up to half his flying speed."
    )


@pytest.fixture
def iymrith_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**legendary_dragons.iymrith_custom_stat_block)


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
    assert iymrith_stat_block.damage_immunities == "lightning"
    assert iymrith_stat_block.condition_immunities == "exhausted, paralyzed"
    assert (
        iymrith_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 27"
    )
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
    return LegendaryDragonStatBlock(**legendary_dragons.dragotha_custom_stat_block)


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
    assert (
        dragotha_stat_block.condition_immunities
        == "charmed, exhausted, frightened, paralyzed, poisoned"
    )
    assert (
        dragotha_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 25"
    )
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


@pytest.fixture
def klauth_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**legendary_dragons.klauth_custom_stat_block)


def test_klauth_stat_block(klauth_stat_block):
    # Check if the Klauth StatBlock instance is created correctly
    assert klauth_stat_block.name == "Klauth"
    assert klauth_stat_block.hit_points == 546
    assert klauth_stat_block.armor_class == 24
    assert klauth_stat_block.speed == "40 ft, burrow 40 ft, fly 80 ft"
    assert klauth_stat_block.abilities.strength == 30
    assert klauth_stat_block.abilities.dexterity == 10
    assert klauth_stat_block.abilities.constitution == 28
    assert klauth_stat_block.abilities.intelligence == 18
    assert klauth_stat_block.abilities.wisdom == 15
    assert klauth_stat_block.abilities.charisma == 22
    assert klauth_stat_block.saving_throws.strength == 19
    assert klauth_stat_block.saving_throws.dexterity == 9
    assert klauth_stat_block.saving_throws.constitution == 18
    assert klauth_stat_block.saving_throws.intelligence == 12
    assert klauth_stat_block.saving_throws.wisdom == 11
    assert klauth_stat_block.saving_throws.charisma == 14
    assert "Perception +17" in klauth_stat_block.skills
    assert "Stealth +9" in klauth_stat_block.skills
    assert klauth_stat_block.damage_immunities == "fire"
    assert (
        klauth_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 27"
    )
    assert klauth_stat_block.languages == "Common, Draconic"
    assert klauth_stat_block.challenge == 23
    assert (
        "Legendary Resistance (3/Day): If Klauth fails a saving throw, he can choose to succeed instead."
        in klauth_stat_block.special_abilities
    )
    assert (
        "Magic Resistance: Klauth has advantage on saving throws against spells and other magical effects."
        in klauth_stat_block.special_abilities
    )
    assert (
        "Fire Breath (Recharge 5-6): Klauth exhales fire in a 90-foot cone. Each creature in that area must make a DC 26 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one."
        in klauth_stat_block.special_abilities
    )
    assert (
        "Spellcasting: Klauth is a 17th-level spellcaster. His spellcasting ability is Charisma (spell save DC 22, +14 to hit with spell attacks). He has the following spells prepared:"
        in klauth_stat_block.special_abilities
    )
    assert (
        "- Cantrips (at will): Fire Bolt, Mage Hand, Prestidigitation"
        in klauth_stat_block.special_abilities
    )
    assert (
        "- 1st level (4 slots): Burning Hands, Shield"
        in klauth_stat_block.special_abilities
    )
    assert (
        "- 2nd level (3 slots): Scorching Ray, Mirror Image"
        in klauth_stat_block.special_abilities
    )
    assert (
        "- 3rd level (3 slots): Fireball, Counterspell"
        in klauth_stat_block.special_abilities
    )
    assert (
        "- 4th level (3 slots): Wall of Fire, Greater Invisibility"
        in klauth_stat_block.special_abilities
    )
    assert (
        "- 5th level (3 slots): Immolation, Cone of Cold"
        in klauth_stat_block.special_abilities
    )
    assert (
        "- 6th level (1 slot): Chain Lightning" in klauth_stat_block.special_abilities
    )
    assert (
        klauth_stat_block.actions["multiattack"]
        == "Klauth can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws."
    )
    assert (
        klauth_stat_block.actions["bite"]
        == "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 30 (4d6 + 19) piercing damage plus 14 (4d6) fire damage."
    )
    assert (
        klauth_stat_block.actions["claw"]
        == "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 24 (3d8 + 19) slashing damage."
    )
    assert (
        klauth_stat_block.legendary_actions["detect"]
        == "Klauth makes a Wisdom (Perception) check."
    )
    assert (
        klauth_stat_block.legendary_actions["tail_attack"]
        == "Klauth makes a tail attack."
    )
    assert (
        klauth_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Klauth beats his wings. Each creature within 15 feet of him must succeed on a DC 27 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Klauth can then fly up to half his flying speed."
    )


@pytest.fixture
def ilnezhara_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**legendary_dragons.ilnezhara_custom_stat_block)


def test_ilnezhara_stat_block(ilnezhara_stat_block):
    # Check if the Ilnezhara StatBlock instance is created correctly
    assert ilnezhara_stat_block.name == "Ilnezhara"
    assert ilnezhara_stat_block.hit_points == 367
    assert ilnezhara_stat_block.armor_class == 21
    assert ilnezhara_stat_block.speed == "40 ft, fly 80 ft, swim 40 ft"
    assert ilnezhara_stat_block.abilities.strength == 23
    assert ilnezhara_stat_block.abilities.dexterity == 14
    assert ilnezhara_stat_block.abilities.constitution == 21
    assert ilnezhara_stat_block.abilities.intelligence == 18
    assert ilnezhara_stat_block.abilities.wisdom == 17
    assert ilnezhara_stat_block.abilities.charisma == 20
    assert ilnezhara_stat_block.saving_throws.strength == 12
    assert ilnezhara_stat_block.saving_throws.dexterity == 8
    assert ilnezhara_stat_block.saving_throws.constitution == 11
    assert ilnezhara_stat_block.saving_throws.intelligence == 10
    assert ilnezhara_stat_block.saving_throws.wisdom == 9
    assert ilnezhara_stat_block.saving_throws.charisma == 10
    assert "Perception +13" in ilnezhara_stat_block.skills
    assert "Stealth +8" in ilnezhara_stat_block.skills
    assert "Deception +10" in ilnezhara_stat_block.skills
    assert "Persuasion +10" in ilnezhara_stat_block.skills
    assert ilnezhara_stat_block.damage_immunities == "poison"
    assert (
        ilnezhara_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 23"
    )
    assert ilnezhara_stat_block.languages == "Common, Draconic, Elvish"
    assert ilnezhara_stat_block.challenge == 22
    assert (
        "Legendary Resistance (3/Day): If Ilnezhara fails a saving throw, she can choose to succeed instead."
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "Magic Resistance: Ilnezhara has advantage on saving throws against spells and other magical effects."
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "Poison Breath (Recharge 5-6): Ilnezhara exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 20 Constitution saving throw, taking 70 (20d6) poison damage on a failed save, or half as much damage on a successful one."
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "Spellcasting: Ilnezhara is a 16th-level spellcaster. Her spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). She has the following spells prepared:"
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "- Cantrips (at will): Druidcraft, Poison Spray, Thaumaturgy"
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "- 1st level (4 slots): Entangle, Fog Cloud, Charm Person"
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "- 2nd level (3 slots): Barkskin, Enhance Ability, Pass without Trace"
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "- 3rd level (3 slots): Plant Growth, Protection from Energy, Sleet Storm"
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "- 4th level (3 slots): Blight, Dominate Beast, Greater Invisibility"
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        "- 5th level (2 slots): Cloudkill, Insect Plague"
        in ilnezhara_stat_block.special_abilities
    )
    assert (
        ilnezhara_stat_block.actions["multiattack"]
        == "Ilnezhara can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws."
    )
    assert (
        ilnezhara_stat_block.actions["bite"]
        == "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) poison damage."
    )
    assert (
        ilnezhara_stat_block.actions["claw"]
        == "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    )
    assert (
        ilnezhara_stat_block.legendary_actions["detect"]
        == "Ilnezhara makes a Wisdom (Perception) check."
    )
    assert (
        ilnezhara_stat_block.legendary_actions["tail_attack"]
        == "Ilnezhara makes a tail attack."
    )
    assert (
        ilnezhara_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Ilnezhara beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Ilnezhara can then fly up to half her flying speed."
    )


@pytest.fixture
def tazmikella_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**legendary_dragons.tazmikella_custom_stat_block)


def test_tazmikella_stat_block(tazmikella_stat_block):
    # Check if the Tazmikella StatBlock instance is created correctly
    assert tazmikella_stat_block.name == "Tazmikella"
    assert tazmikella_stat_block.hit_points == 367
    assert tazmikella_stat_block.armor_class == 21
    assert tazmikella_stat_block.speed == "40 ft, fly 80 ft, swim 40 ft"

    # Access AbilityScores attributes individually
    assert tazmikella_stat_block.abilities.strength == 23
    assert tazmikella_stat_block.abilities.dexterity == 14
    assert tazmikella_stat_block.abilities.constitution == 21
    assert tazmikella_stat_block.abilities.intelligence == 18
    assert tazmikella_stat_block.abilities.wisdom == 17
    assert tazmikella_stat_block.abilities.charisma == 20

    # Access SavingThrows attributes individually
    assert tazmikella_stat_block.saving_throws.strength == 12
    assert tazmikella_stat_block.saving_throws.dexterity == 8
    assert tazmikella_stat_block.saving_throws.constitution == 11
    assert tazmikella_stat_block.saving_throws.intelligence == 10
    assert tazmikella_stat_block.saving_throws.wisdom == 9
    assert tazmikella_stat_block.saving_throws.charisma == 10

    # Validate skills
    assert "Perception +13" in tazmikella_stat_block.skills
    assert "Stealth +8" in tazmikella_stat_block.skills
    assert "Deception +10" in tazmikella_stat_block.skills
    assert "Persuasion +10" in tazmikella_stat_block.skills

    # Validate other attributes
    assert tazmikella_stat_block.damage_resistances == ""
    assert tazmikella_stat_block.damage_immunities == "poison"
    assert tazmikella_stat_block.condition_immunities == ""
    assert (
        tazmikella_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 23"
    )
    assert tazmikella_stat_block.languages == "Common, Draconic, Elvish"
    assert tazmikella_stat_block.challenge == 22

    # Validate special abilities
    assert (
        "Legendary Resistance (3/Day): If Tazmikella fails a saving throw, she can choose to succeed instead."
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "Magic Resistance: Tazmikella has advantage on saving throws against spells and other magical effects."
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "Poison Breath (Recharge 5-6): Tazmikella exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 20 Constitution saving throw, taking 70 (20d6) poison damage on a failed save, or half as much damage on a successful one."
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "Spellcasting: Tazmikella is a 16th-level spellcaster. Her spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). She has the following spells prepared:"
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "- Cantrips (at will): Druidcraft, Poison Spray, Thaumaturgy"
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "- 1st level (4 slots): Entangle, Fog Cloud, Charm Person"
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "- 2nd level (3 slots): Barkskin, Enhance Ability, Pass without Trace"
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "- 3rd level (3 slots): Plant Growth, Protection from Energy, Sleet Storm"
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "- 4th level (3 slots): Blight, Dominate Beast, Greater Invisibility"
        in tazmikella_stat_block.special_abilities
    )
    assert (
        "- 5th level (2 slots): Cloudkill, Insect Plague"
        in tazmikella_stat_block.special_abilities
    )

    # Validate actions
    assert (
        tazmikella_stat_block.actions["multiattack"]
        == "Tazmikella can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws."
    )
    assert (
        tazmikella_stat_block.actions["bite"]
        == "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) poison damage."
    )
    assert (
        tazmikella_stat_block.actions["claw"]
        == "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    )

    # Validate legendary actions
    assert (
        tazmikella_stat_block.legendary_actions["detect"]
        == "Tazmikella makes a Wisdom (Perception) check."
    )
    assert (
        tazmikella_stat_block.legendary_actions["tail_attack"]
        == "Tazmikella makes a tail attack."
    )
    assert (
        tazmikella_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Tazmikella beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Tazmikella can then fly up to half her flying speed."
    )


@pytest.fixture
def aurgloroasa_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**legendary_dragons.aurgloroasa_custom_stat_block)


@pytest.fixture
def aurgloroasa_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**legendary_dragons.aurgloroasa_custom_stat_block)


def test_aurgloroasa_stat_block(aurgloroasa_stat_block):
    # Check if the Aurgloroasa StatBlock instance is created correctly
    assert aurgloroasa_stat_block.name == "Aurgloroasa"
    assert aurgloroasa_stat_block.hit_points == 350
    assert aurgloroasa_stat_block.armor_class == 19
    assert aurgloroasa_stat_block.speed == "40 ft, fly 80 ft, swim 40 ft"

    # Access AbilityScores attributes individually
    assert aurgloroasa_stat_block.abilities.strength == 22
    assert aurgloroasa_stat_block.abilities.dexterity == 14
    assert aurgloroasa_stat_block.abilities.constitution == 21
    assert aurgloroasa_stat_block.abilities.intelligence == 18
    assert aurgloroasa_stat_block.abilities.wisdom == 17
    assert aurgloroasa_stat_block.abilities.charisma == 20

    # Access SavingThrows attributes individually
    assert aurgloroasa_stat_block.saving_throws.strength == 12
    assert aurgloroasa_stat_block.saving_throws.dexterity == 8
    assert aurgloroasa_stat_block.saving_throws.constitution == 11
    assert aurgloroasa_stat_block.saving_throws.intelligence == 10
    assert aurgloroasa_stat_block.saving_throws.wisdom == 9
    assert aurgloroasa_stat_block.saving_throws.charisma == 10

    # Validate skills
    assert "Perception +13" in aurgloroasa_stat_block.skills
    assert "Stealth +8" in aurgloroasa_stat_block.skills
    assert "Deception +10" in aurgloroasa_stat_block.skills
    assert "Arcana +10" in aurgloroasa_stat_block.skills

    # Validate other attributes
    assert (
        aurgloroasa_stat_block.damage_resistances
        == "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        aurgloroasa_stat_block.damage_immunities
        == "necrotic, poison; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        aurgloroasa_stat_block.condition_immunities
        == "charmed, frightened, paralyzed, poisoned"
    )
    assert (
        aurgloroasa_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 23"
    )
    assert aurgloroasa_stat_block.languages == "Common, Draconic, Abyssal"
    assert aurgloroasa_stat_block.challenge == 23

    # Validate special abilities
    assert (
        "Legendary Resistance (3/Day): If Aurgloroasa fails a saving throw, she can choose to succeed instead."
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "Magic Resistance: Aurgloroasa has advantage on saving throws against spells and other magical effects."
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "Life Drain (Recharge 5-6): Aurgloroasa targets one creature she can see within 30 feet of her. The target must succeed on a DC 20 Constitution saving throw or take 45 (10d8) necrotic damage and Aurgloroasa regains hit points equal to the necrotic damage dealt."
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "Shadow Control: Aurgloroasa can manipulate shadows within 120 feet of her, using them to obscure vision or create areas of darkness as if casting the darkness spell."
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "Spellcasting: Aurgloroasa is a 16th-level spellcaster. Her spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). She has the following spells prepared:"
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "- Cantrips (at will): Chill Touch, Mage Hand, Minor Illusion"
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "- 1st level (4 slots): Detect Magic, Ray of Sickness, Shield"
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "- 2nd level (3 slots): Blindness/Deafness, Misty Step, Ray of Enfeeblement"
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "- 3rd level (3 slots): Counterspell, Fear, Lightning Bolt"
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "- 4th level (3 slots): Blight, Greater Invisibility, Phantasmal Killer"
        in aurgloroasa_stat_block.special_abilities
    )
    assert (
        "- 5th level (2 slots): Cloudkill, Dominate Person"
        in aurgloroasa_stat_block.special_abilities
    )

    # Validate actions
    assert (
        aurgloroasa_stat_block.actions["multiattack"]
        == "Aurgloroasa can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws."
    )
    assert (
        aurgloroasa_stat_block.actions["bite"]
        == "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) necrotic damage."
    )
    assert (
        aurgloroasa_stat_block.actions["claw"]
        == "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    )

    # Validate legendary actions
    assert (
        aurgloroasa_stat_block.legendary_actions["detect"]
        == "Aurgloroasa makes a Wisdom (Perception) check."
    )
    assert (
        aurgloroasa_stat_block.legendary_actions["tail_attack"]
        == "Aurgloroasa makes a tail attack."
    )
    assert (
        aurgloroasa_stat_block.legendary_actions["wing_attack (costs 2 actions)"]
        == "Aurgloroasa beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Aurgloroasa can then fly up to half her flying speed."
    )


# Define the fixture for Niv-Mizzet's stat block
@pytest.fixture
def niv_mizzet_stat_block():
    # Fixture to provide a sample instance of LegendaryDragonStatBlock for testing
    return LegendaryDragonStatBlock(**legendary_dragons.niv_mizzet_custom_stat_block)


# Test function for Niv-Mizzet's stat block
def test_niv_mizzet_stat_block(niv_mizzet_stat_block):
    # Check if the Niv-Mizzet StatBlock instance is created correctly
    assert niv_mizzet_stat_block.name == "Niv-Mizzet, the Firemind"
    assert niv_mizzet_stat_block.hit_points == 546
    assert niv_mizzet_stat_block.armor_class == 22
    assert niv_mizzet_stat_block.speed == "40 ft, fly 80 ft"
    assert niv_mizzet_stat_block.abilities.strength == 23
    assert niv_mizzet_stat_block.abilities.dexterity == 10
    assert niv_mizzet_stat_block.abilities.constitution == 21
    assert niv_mizzet_stat_block.abilities.intelligence == 26
    assert niv_mizzet_stat_block.abilities.wisdom == 17
    assert niv_mizzet_stat_block.abilities.charisma == 24
    assert niv_mizzet_stat_block.saving_throws.strength == 13
    assert niv_mizzet_stat_block.saving_throws.dexterity == 6
    assert niv_mizzet_stat_block.saving_throws.constitution == 12
    assert niv_mizzet_stat_block.saving_throws.intelligence == 15
    assert niv_mizzet_stat_block.saving_throws.wisdom == 10
    assert niv_mizzet_stat_block.saving_throws.charisma == 14
    assert "Arcana +15" in niv_mizzet_stat_block.skills
    assert niv_mizzet_stat_block.damage_resistances == "fire"
    assert niv_mizzet_stat_block.damage_immunities == ""
    assert niv_mizzet_stat_block.condition_immunities == "charmed, frightened"
    assert (
        niv_mizzet_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 20"
    )
    assert (
        niv_mizzet_stat_block.languages
        == "Common, Draconic, Ravnican, telepathy 120 ft."
    )
    assert niv_mizzet_stat_block.challenge == 26
    assert (
        "Legendary Resistance (3/Day): If Niv-Mizzet fails a saving throw, he can choose to succeed instead."
        in niv_mizzet_stat_block.special_abilities
    )
    assert (
        niv_mizzet_stat_block.actions["Multiattack"]
        == "Niv-Mizzet can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws."
    )
    assert (
        niv_mizzet_stat_block.actions["Bite"]
        == "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage plus 14 (4d6) fire damage."
    )
    assert (
        niv_mizzet_stat_block.actions["Claw"]
        == "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage."
    )
    assert (
        niv_mizzet_stat_block.legendary_actions["Detect"]
        == "Niv-Mizzet makes a Wisdom (Perception) check."
    )
    assert (
        niv_mizzet_stat_block.legendary_actions["Tail Attack"]
        == "Niv-Mizzet makes a tail attack."
    )
    assert (
        niv_mizzet_stat_block.legendary_actions["Wing Attack (Costs 2 Actions)"]
        == "Niv-Mizzet beats his wings. Each creature within 15 feet of him must succeed on a DC 21 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Niv-Mizzet can then fly up to half his flying speed."
    )
