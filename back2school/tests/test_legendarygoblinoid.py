import pytest

from .. import legendary_goblinoids

from ..legendary_goblinoids import GoblinoidChampionStatBlock


@pytest.fixture
def kharza_the_ravager_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.kharza_the_ravager_custom_stat_block
    )
def test_kharza_the_ravager_stat_block(kharza_the_ravager_stat_block):
    # Check if the Kharza the Ravager StatBlock instance is created correctly
    assert kharza_the_ravager_stat_block.name == "Kharza the Ravager"
    assert kharza_the_ravager_stat_block.hit_points == 290
    assert kharza_the_ravager_stat_block.armor_class == 17
    assert kharza_the_ravager_stat_block.speed == "40 ft."
    assert kharza_the_ravager_stat_block.abilities.strength == 22
    assert kharza_the_ravager_stat_block.saving_throws.strength == 10
    assert "Athletics +12" in kharza_the_ravager_stat_block.skills
    assert (
        kharza_the_ravager_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks while raging"
    )
    assert kharza_the_ravager_stat_block.condition_immunities == "charmed, frightened while raging"
    assert (
        kharza_the_ravager_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    )
    assert kharza_the_ravager_stat_block.languages == "Gnoll, Common"
    assert kharza_the_ravager_stat_block.challenge == 17
    assert (
        "Savage Bloodlust: When Kharza reduces a creature to 0 hit points, he can make an additional melee attack as part of the same action. This attack deals an extra 1d8 damage."
        in kharza_the_ravager_stat_block.special_abilities
    )
    assert (
        kharza_the_ravager_stat_block.legendary_actions["Ravager's Strike"]
        == "Kharza makes a single melee weapon attack with his Ravager's Axe. If the attack hits, the target must succeed on a DC 18 Constitution saving throw or be stunned until the end of Kharza's next turn."
    )
    assert (
        kharza_the_ravager_stat_block.actions[0]
        == "Multiattack: Kharza makes three attacks with his Ravager's Axe or Gnashing Bite."
    )
    assert (
        kharza_the_ravager_stat_block.actions[1]
        == "Ravager's Axe: Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 20 (2d12 + 6) slashing damage."
    )
    assert (
        kharza_the_ravager_stat_block.bonus_actions[0]
        == "Rage: Kharza can enter a rage as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage, as well as a +2 bonus to damage rolls."
    )
    assert (
        kharza_the_ravager_stat_block.reactions[0]
        == "Savage Instinct: When Kharza is hit by a melee attack, he can use his reaction to make a single melee weapon attack against the attacker."
    )

@pytest.fixture
def vorgath_the_bloodhowler_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.vorgath_the_bloodhowler_custom_stat_block
    )
def test_vorgath_the_bloodhowler_stat_block(vorgath_the_bloodhowler_stat_block):
    # Check if the Vorgath the Bloodhowler StatBlock instance is created correctly
    assert vorgath_the_bloodhowler_stat_block.name == "Vorgath the Bloodhowler"
    assert vorgath_the_bloodhowler_stat_block.hit_points == 240
    assert vorgath_the_bloodhowler_stat_block.armor_class == 16
    assert vorgath_the_bloodhowler_stat_block.speed == "30 ft."
    assert vorgath_the_bloodhowler_stat_block.abilities.wisdom == 20
    assert vorgath_the_bloodhowler_stat_block.saving_throws.wisdom == 10
    assert "Arcana +10" in vorgath_the_bloodhowler_stat_block.skills
    assert (
        vorgath_the_bloodhowler_stat_block.damage_resistances
        == "necrotic, psychic"
    )
    assert vorgath_the_bloodhowler_stat_block.condition_immunities == "frightened, charmed"
    assert (
        vorgath_the_bloodhowler_stat_block.senses == "darkvision 60 ft., passive Perception 20"
    )
    assert vorgath_the_bloodhowler_stat_block.languages == "Gnoll, Abyssal, Common"
    assert vorgath_the_bloodhowler_stat_block.challenge == 16
    assert (
        "Blood Magic: Vorgath can sacrifice his own hit points to empower his spells, dealing an extra 2d8 necrotic damage. For each 5 hit points sacrificed, the damage increases by 1d8 (max 5d8)."
        in vorgath_the_bloodhowler_stat_block.special_abilities
    )
    assert (
        vorgath_the_bloodhowler_stat_block.legendary_actions["Bloodhowl"]
        == "Vorgath makes a single melee weapon attack with his Bloodhowl Staff. If the attack hits, the target must succeed on a DC 18 Constitution saving throw or take an additional 2d8 necrotic damage and be frightened until the end of Vorgath's next turn."
    )
    assert (
        vorgath_the_bloodhowler_stat_block.actions[0]
        == "Multiattack: Vorgath makes two attacks with his Bloodhowl Staff or Necrotic Claw."
    )
    assert (
        vorgath_the_bloodhowler_stat_block.actions[1]
        == "Bloodhowl Staff: Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage plus 2d8 necrotic damage."
    )
    assert (
        vorgath_the_bloodhowler_stat_block.bonus_actions[0]
        == "Dark Pact: Vorgath can use a bonus action to regain 1d10 + 5 hit points. This can be used once per short or long rest."
    )
    assert (
        vorgath_the_bloodhowler_stat_block.reactions[0]
        == "Blood Shield: When Vorgath is hit by a melee attack, he can use his reaction to cast a shield of blood, granting him +4 AC until the end of his next turn. If the attack misses, the attacker takes 2d6 necrotic damage."
    )


@pytest.fixture
def general_kazrak_ironblood_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.general_kazrak_ironblood_custom_stat_block
    )
def test_general_kazrak_ironblood_stat_block(general_kazrak_ironblood_stat_block):
    # Check if the General Kazrak Ironblood StatBlock instance is created correctly
    assert general_kazrak_ironblood_stat_block.name == "General Kazrak Ironblood"
    assert general_kazrak_ironblood_stat_block.hit_points == 250
    assert general_kazrak_ironblood_stat_block.armor_class == 20
    assert general_kazrak_ironblood_stat_block.speed == "30 ft."
    assert general_kazrak_ironblood_stat_block.abilities.strength == 18
    assert general_kazrak_ironblood_stat_block.saving_throws.strength == 8
    assert "Athletics +10" in general_kazrak_ironblood_stat_block.skills
    assert (
        general_kazrak_ironblood_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert general_kazrak_ironblood_stat_block.condition_immunities == "charmed, frightened"
    assert (
        general_kazrak_ironblood_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    )
    assert general_kazrak_ironblood_stat_block.languages == "Goblin, Common, Infernal"
    assert general_kazrak_ironblood_stat_block.challenge == 18
    assert (
        "Battlefield Commander: General Kazrak can use a bonus action to grant an ally within 60 feet an additional melee attack on their next turn."
        in general_kazrak_ironblood_stat_block.special_abilities
    )
    assert (
        general_kazrak_ironblood_stat_block.legendary_actions["Ironblood Strike"]
        == "General Kazrak makes a single melee weapon attack with his Ironblood Glaive. If the attack hits, the target must succeed on a DC 18 Constitution saving throw or be stunned until the end of General Kazrak's next turn."
    )
    assert (
        general_kazrak_ironblood_stat_block.actions[0]
        == "Multiattack: General Kazrak makes three attacks with his Ironblood Glaive or uses his Commanding Strike."
    )
    assert (
        general_kazrak_ironblood_stat_block.actions[1]
        == "Ironblood Glaive: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 20 (2d12 + 6) slashing damage."
    )
    assert (
        general_kazrak_ironblood_stat_block.bonus_actions[0]
        == "Tactical Positioning: General Kazrak can use a bonus action to move up to half his speed without provoking opportunity attacks."
    )
    assert (
        general_kazrak_ironblood_stat_block.reactions[0]
        == "Parry: When General Kazrak is hit by a melee attack, he can use his reaction to add +4 to his AC for that attack, potentially causing the attack to miss."
    )

@pytest.fixture
def thalrak_the_unyielding_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.thalrak_the_unyielding_custom_stat_block
    )
def test_thalrak_the_unyielding_stat_block(thalrak_the_unyielding_stat_block):
    # Check if the Thalrak the Unyielding StatBlock instance is created correctly
    assert thalrak_the_unyielding_stat_block.name == "Thalrak the Unyielding"
    assert thalrak_the_unyielding_stat_block.hit_points == 300
    assert thalrak_the_unyielding_stat_block.armor_class == 22
    assert thalrak_the_unyielding_stat_block.speed == "30 ft."
    assert thalrak_the_unyielding_stat_block.abilities.strength == 20
    assert thalrak_the_unyielding_stat_block.saving_throws.strength == 10
    assert "Athletics +12" in thalrak_the_unyielding_stat_block.skills
    assert (
        thalrak_the_unyielding_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert thalrak_the_unyielding_stat_block.condition_immunities == "frightened, paralyzed"
    assert (
        thalrak_the_unyielding_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    )
    assert thalrak_the_unyielding_stat_block.languages == "Goblin, Common"
    assert thalrak_the_unyielding_stat_block.challenge == 19
    assert (
        "Unyielding Endurance: Thalrak can reduce damage from a single attack by half as a reaction. This ability recharges after a short or long rest."
        in thalrak_the_unyielding_stat_block.special_abilities
    )
    assert (
        thalrak_the_unyielding_stat_block.legendary_actions["Unyielding Strike"]
        == "Thalrak makes a single melee weapon attack with his Colossal Warhammer. If the attack hits, the target must succeed on a DC 19 Constitution saving throw or be knocked prone and take an additional 2d8 bludgeoning damage."
    )
    assert (
        thalrak_the_unyielding_stat_block.actions[0]
        == "Multiattack: Thalrak makes three attacks with his Colossal Warhammer."
    )
    assert (
        thalrak_the_unyielding_stat_block.actions[1]
        == "Colossal Warhammer: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 24 (3d10 + 6) bludgeoning damage."
    )
    assert (
        thalrak_the_unyielding_stat_block.bonus_actions[0]
        == "Rallying Cry: Thalrak can use a bonus action to inspire his allies. All allies within 30 feet gain temporary hit points equal to Thalrak's Charisma modifier + 1d10."
    )
    assert (
        thalrak_the_unyielding_stat_block.reactions[0]
        == "Unyielding Endurance: Thalrak can reduce damage from a single attack by half as a reaction. This ability recharges after a short or long rest."
    )


@pytest.fixture
def morgath_the_red_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.morgath_the_red_custom_stat_block
    )

def test_morgath_the_red_stat_block(morgath_the_red_stat_block):
    # Check if the Morgath the Red StatBlock instance is created correctly
    assert morgath_the_red_stat_block.name == "Morgath the Red"
    assert morgath_the_red_stat_block.hit_points == 240
    assert morgath_the_red_stat_block.armor_class == 18
    assert morgath_the_red_stat_block.speed == "30 ft."
    assert morgath_the_red_stat_block.abilities.intelligence == 20
    assert morgath_the_red_stat_block.saving_throws.intelligence == 10
    assert "Arcana +12" in morgath_the_red_stat_block.skills
    assert (
        morgath_the_red_stat_block.damage_resistances
        == "fire, lightning"
    )
    assert morgath_the_red_stat_block.condition_immunities == "charmed, frightened"
    assert (
        morgath_the_red_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    )
    assert morgath_the_red_stat_block.languages == "Goblin, Common, Draconic"
    assert morgath_the_red_stat_block.challenge == 18
    assert (
        "Arcane Ward: Morgath can create a magical barrier around himself that absorbs 20 damage from incoming attacks. This ward recharges after a short or long rest."
        in morgath_the_red_stat_block.special_abilities
    )
    assert (
        morgath_the_red_stat_block.legendary_actions["Arcane Blast"]
        == "Morgath makes a ranged spell attack with Arcane Bolt. If the attack hits, it deals 4d8 force damage, and the target must succeed on a DC 18 Strength saving throw or be pushed back 10 feet."
    )
    assert (
        morgath_the_red_stat_block.actions[0]
        == "Multiattack: Morgath makes two attacks with his Enchanted Longsword or casts two cantrips."
    )
    assert (
        morgath_the_red_stat_block.actions[1]
        == "Enchanted Longsword: Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) slashing damage plus 1d8 fire damage."
    )
    assert (
        morgath_the_red_stat_block.bonus_actions[0]
        == "War Magic: When Morgath uses his action to cast a cantrip, he can make one weapon attack as a bonus action."
    )
    assert (
        morgath_the_red_stat_block.reactions[0]
        == "Shield: When Morgath is hit by an attack, he can use his reaction to cast Shield, increasing his AC by +5 until the start of his next turn."
    )


@pytest.fixture
def rikard_the_shadowblade_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.rikard_the_shadowblade_custom_stat_block
    )

def test_rikard_the_shadowblade_stat_block(rikard_the_shadowblade_stat_block):
    # Check if the Rikard the Shadowblade StatBlock instance is created correctly
    assert rikard_the_shadowblade_stat_block.name == "Rikard the Shadowblade"
    assert rikard_the_shadowblade_stat_block.hit_points == 200
    assert rikard_the_shadowblade_stat_block.armor_class == 17
    assert rikard_the_shadowblade_stat_block.speed == "40 ft."
    assert rikard_the_shadowblade_stat_block.abilities.dexterity == 22
    assert rikard_the_shadowblade_stat_block.saving_throws.dexterity == 11
    assert "Stealth +17" in rikard_the_shadowblade_stat_block.skills
    assert (
        rikard_the_shadowblade_stat_block.damage_resistances
        == "poison, psychic"
    )
    assert rikard_the_shadowblade_stat_block.condition_immunities == "charmed, frightened"
    assert (
        rikard_the_shadowblade_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    )
    assert rikard_the_shadowblade_stat_block.languages == "Goblin, Common, Thieves' Cant"
    assert rikard_the_shadowblade_stat_block.challenge == 19
    assert (
        "Assassinate: Rikard has advantage on attack rolls against any creature that hasn’t taken a turn in the combat yet. In addition, any hit Rikard scores against a surprised creature is a critical hit."
        in rikard_the_shadowblade_stat_block.special_abilities
    )
    assert (
        rikard_the_shadowblade_stat_block.legendary_actions["Shadow Step"]
        == "Rikard teleports up to 30 feet to an unoccupied space he can see. He becomes invisible until the start of his next turn."
    )
    assert (
        rikard_the_shadowblade_stat_block.actions[0]
        == "Multiattack: Rikard makes three attacks with his Shadow Dagger or Life-Sapping Blade."
    )
    assert (
        rikard_the_shadowblade_stat_block.actions[1]
        == "Shadow Dagger: Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) piercing damage plus 2d6 poison damage."
    )
    assert (
        rikard_the_shadowblade_stat_block.bonus_actions[0]
        == "Cloak of Shadows: Rikard can use a bonus action to become invisible until the start of his next turn, or until he attacks, makes a damage roll, or forces someone to make a saving throw."
    )
    assert (
        rikard_the_shadowblade_stat_block.reactions[0]
        == "Uncanny Dodge: When an attacker that Rikard can see hits him with an attack, he can use his reaction to halve the attack’s damage against him."
    )


@pytest.fixture
def skragg_the_warcaller_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.skragg_the_warcaller_custom_stat_block
    )

def test_skragg_the_warcaller_stat_block(skragg_the_warcaller_stat_block):
    # Check if the Skragg the Warcaller StatBlock instance is created correctly
    assert skragg_the_warcaller_stat_block.name == "Skragg the Warcaller"
    assert skragg_the_warcaller_stat_block.hit_points == 220
    assert skragg_the_warcaller_stat_block.armor_class == 19
    assert skragg_the_warcaller_stat_block.speed == "40 ft."
    assert skragg_the_warcaller_stat_block.abilities.strength == 18
    assert skragg_the_warcaller_stat_block.saving_throws.strength == 10
    assert "Athletics +12" in skragg_the_warcaller_stat_block.skills
    assert (
        skragg_the_warcaller_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert skragg_the_warcaller_stat_block.condition_immunities == "frightened, charmed"
    assert (
        skragg_the_warcaller_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    )
    assert skragg_the_warcaller_stat_block.languages == "Goblin, Common"
    assert skragg_the_warcaller_stat_block.challenge == 18
    assert (
        "Warcaller’s Command: Skragg can use a bonus action to give a command to one allied creature within 60 feet. The creature can immediately use its reaction to move up to its speed or make one weapon attack."
        in skragg_the_warcaller_stat_block.special_abilities
    )
    assert (
        skragg_the_warcaller_stat_block.legendary_actions["War Horn Blast"]
        == "Skragg blows his war horn, causing all enemies within 30 feet to make a DC 18 Wisdom saving throw or be frightened until the end of Skragg's next turn."
    )
    assert (
        skragg_the_warcaller_stat_block.actions[0]
        == "Multiattack: Skragg makes three attacks with his Gutripper Axe."
    )
    assert (
        skragg_the_warcaller_stat_block.actions[1]
        == "Gutripper Axe: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 18 (2d8 + 8) slashing damage."
    )
    assert (
        skragg_the_warcaller_stat_block.bonus_actions[0]
        == "Warcaller’s Command: Skragg can use a bonus action to give a command to one allied creature within 60 feet. The creature can immediately use its reaction to move up to its speed or make one weapon attack."
    )
    assert (
        skragg_the_warcaller_stat_block.reactions[0]
        == "Parry: When Skragg is hit by a melee attack, he can use his reaction to add +3 to his AC for that attack, potentially causing the attack to miss."
    )


@pytest.fixture
def grishna_the_firestarter_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.grishna_the_firestarter_custom_stat_block
    )

def test_grishna_the_firestarter_stat_block(grishna_the_firestarter_stat_block):
    # Check if the Grishna the Firestarter StatBlock instance is created correctly
    assert grishna_the_firestarter_stat_block.name == "Grishna the Firestarter"
    assert grishna_the_firestarter_stat_block.hit_points == 190
    assert grishna_the_firestarter_stat_block.armor_class == 17
    assert grishna_the_firestarter_stat_block.speed == "30 ft."
    assert grishna_the_firestarter_stat_block.abilities.charisma == 20
    assert grishna_the_firestarter_stat_block.saving_throws.charisma == 10
    assert "Arcana +12" in grishna_the_firestarter_stat_block.skills
    assert (
        grishna_the_firestarter_stat_block.damage_resistances
        == "fire"
    )
    assert grishna_the_firestarter_stat_block.condition_immunities == "frightened, charmed"
    assert (
        grishna_the_firestarter_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    )
    assert grishna_the_firestarter_stat_block.languages == "Goblin, Common, Infernal"
    assert grishna_the_firestarter_stat_block.challenge == 18
    assert (
        "Fiery Presence: Grishna can use a bonus action to cause flames to erupt around her. All creatures within 10 feet must succeed on a DC 18 Dexterity saving throw or take 3d6 fire damage."
        in grishna_the_firestarter_stat_block.special_abilities
    )
    assert (
        grishna_the_firestarter_stat_block.legendary_actions["Flame Wave"]
        == "Grishna unleashes a wave of fire in a 30-foot cone. Each creature in the area must make a DC 18 Dexterity saving throw, taking 8d6 fire damage on a failed save, or half as much on a successful one."
    )
    assert (
        grishna_the_firestarter_stat_block.actions[0]
        == "Multiattack: Grishna makes two attacks with her Inferno Staff or casts two cantrips."
    )
    assert (
        grishna_the_firestarter_stat_block.actions[1]
        == "Inferno Staff: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 12 (1d8 + 6) bludgeoning damage plus 2d8 fire damage."
    )
    assert (
        grishna_the_firestarter_stat_block.bonus_actions[0]
        == "Fiery Presence: Grishna can use a bonus action to cause flames to erupt around her. All creatures within 10 feet must succeed on a DC 18 Dexterity saving throw or take 3d6 fire damage."
    )
    assert (
        grishna_the_firestarter_stat_block.reactions[0]
        == "Hellish Rebuke: When Grishna is hit by an attack, she can use her reaction to cast Hellish Rebuke at 4th level, dealing 4d10 fire damage to the attacker on a failed DC 18 Dexterity saving throw, or half as much on a successful save."
    )


@pytest.fixture
def thorgar_the_silent_hunter_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.thorgar_the_silent_hunter_custom_stat_block
    )

def test_thorgar_the_silent_hunter_stat_block(thorgar_the_silent_hunter_stat_block):
    # Check if the Thorgar the Silent Hunter StatBlock instance is created correctly
    assert thorgar_the_silent_hunter_stat_block.name == "Thorgar the Silent Hunter"
    assert thorgar_the_silent_hunter_stat_block.hit_points == 210
    assert thorgar_the_silent_hunter_stat_block.armor_class == 18
    assert thorgar_the_silent_hunter_stat_block.speed == "40 ft."
    assert thorgar_the_silent_hunter_stat_block.abilities.dexterity == 22
    assert thorgar_the_silent_hunter_stat_block.saving_throws.dexterity == 11
    assert "Stealth +17" in thorgar_the_silent_hunter_stat_block.skills
    assert (
        thorgar_the_silent_hunter_stat_block.damage_resistances
        == "poison, psychic"
    )
    assert thorgar_the_silent_hunter_stat_block.condition_immunities == "charmed, frightened"
    assert (
        thorgar_the_silent_hunter_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    )
    assert thorgar_the_silent_hunter_stat_block.languages == "Goblin, Common, Undercommon"
    assert thorgar_the_silent_hunter_stat_block.challenge == 18
    assert (
        "Assassinate: Thorgar has advantage on attack rolls against any creature that hasn’t taken a turn in the combat yet. In addition, any hit Thorgar scores against a surprised creature is a critical hit."
        in thorgar_the_silent_hunter_stat_block.special_abilities
    )
    assert (
        thorgar_the_silent_hunter_stat_block.legendary_actions["Shadow Step"]
        == "Thorgar teleports up to 30 feet to an unoccupied space he can see. He becomes invisible until the start of his next turn."
    )
    assert (
        thorgar_the_silent_hunter_stat_block.actions[0]
        == "Multiattack: Thorgar makes three attacks with his Silencing Dagger or Shadowstrike Dagger."
    )
    assert (
        thorgar_the_silent_hunter_stat_block.actions[1]
        == "Silencing Dagger: Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 16 (2d8 + 6) piercing damage plus 2d6 poison damage."
    )
    assert (
        thorgar_the_silent_hunter_stat_block.bonus_actions[0]
        == "Cunning Action: Thorgar can use a bonus action to Dash, Disengage, or Hide."
    )
    assert (
        thorgar_the_silent_hunter_stat_block.reactions[0]
        == "Uncanny Dodge: When an attacker that Thorgar can see hits him with an attack, he can use his reaction to halve the attack’s damage against him."
    )

@pytest.fixture
def gorruk_the_bonebreaker_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.gorruk_the_bonebreaker_custom_stat_block
    )
def test_gorruk_the_bonebreaker_stat_block(gorruk_the_bonebreaker_stat_block):
    # Check if the Gorruk the Bonebreaker StatBlock instance is created correctly
    assert gorruk_the_bonebreaker_stat_block.name == "Gorruk the Bonebreaker"
    assert gorruk_the_bonebreaker_stat_block.hit_points == 250
    assert gorruk_the_bonebreaker_stat_block.armor_class == 17
    assert gorruk_the_bonebreaker_stat_block.speed == "40 ft."
    assert gorruk_the_bonebreaker_stat_block.abilities.strength == 24
    assert gorruk_the_bonebreaker_stat_block.saving_throws.strength == 12
    assert "Athletics +14" in gorruk_the_bonebreaker_stat_block.skills
    assert (
        gorruk_the_bonebreaker_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks while raging"
    )
    assert gorruk_the_bonebreaker_stat_block.condition_immunities == "frightened while raging"
    assert (
        gorruk_the_bonebreaker_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    )
    assert gorruk_the_bonebreaker_stat_block.languages == "Goblin, Common"
    assert gorruk_the_bonebreaker_stat_block.challenge == 19
    assert (
        "Rage: Gorruk can enter a rage as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage, as well as a +2 bonus to damage rolls."
        in gorruk_the_bonebreaker_stat_block.special_abilities
    )
    assert (
        gorruk_the_bonebreaker_stat_block.legendary_actions["Crushing Blow"]
        == "Gorruk makes a melee weapon attack with his Spiked Club. If the attack hits, the target must succeed on a DC 19 Constitution saving throw or be stunned until the end of Gorruk's next turn."
    )
    assert (
        gorruk_the_bonebreaker_stat_block.actions[0]
        == "Multiattack: Gorruk makes three attacks with his Spiked Club or Bonecrusher Fists."
    )
    assert (
        gorruk_the_bonebreaker_stat_block.actions[1]
        == "Spiked Club: Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 25 (3d10 + 8) bludgeoning damage."
    )
    assert (
        gorruk_the_bonebreaker_stat_block.bonus_actions[0]
        == "Frenzy: While raging, Gorruk can make a single melee weapon attack as a bonus action on each of his turns."
    )
    assert (
        gorruk_the_bonebreaker_stat_block.reactions[0]
        == "Unyielding: When Gorruk is subjected to an effect that allows him to make a Strength or Constitution saving throw to take only half damage, he can use his reaction to take no damage if he succeeds on the saving throw, or only half damage if he fails."
    )


@pytest.fixture
def kragga_the_huntmaster_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.kragga_the_huntmaster_custom_stat_block
    )
def test_kragga_the_huntmaster_stat_block(kragga_the_huntmaster_stat_block):
    # Check if the Kragga the Huntmaster StatBlock instance is created correctly
    assert kragga_the_huntmaster_stat_block.name == "Kragga the Huntmaster"
    assert kragga_the_huntmaster_stat_block.hit_points == 200
    assert kragga_the_huntmaster_stat_block.armor_class == 18
    assert kragga_the_huntmaster_stat_block.speed == "40 ft."
    assert kragga_the_huntmaster_stat_block.abilities.dexterity == 20
    assert kragga_the_huntmaster_stat_block.saving_throws.dexterity == 11
    assert "Stealth +15" in kragga_the_huntmaster_stat_block.skills
    assert (
        kragga_the_huntmaster_stat_block.damage_resistances
        == "poison, bludgeoning from nonmagical attacks"
    )
    assert kragga_the_huntmaster_stat_block.condition_immunities == "charmed, frightened"
    assert (
        kragga_the_huntmaster_stat_block.senses == "darkvision 60 ft., passive Perception 20"
    )
    assert kragga_the_huntmaster_stat_block.languages == "Goblin, Common, Sylvan"
    assert kragga_the_huntmaster_stat_block.challenge == 18
    assert (
        "Beast Command: Kragga can use a bonus action to command one of his beasts to make a melee attack, Dash, Disengage, or use the Help action."
        in kragga_the_huntmaster_stat_block.special_abilities
    )
    assert (
        kragga_the_huntmaster_stat_block.legendary_actions["Coordinated Strike"]
        == "Kragga commands all his beasts to attack simultaneously. Each beast within 30 feet of Kragga can make one melee attack."
    )
    assert (
        kragga_the_huntmaster_stat_block.actions[0]
        == "Multiattack: Kragga makes two attacks with his Longbow of the Hunt or Beastmaster's Whip."
    )
    assert (
        kragga_the_huntmaster_stat_block.actions[1]
        == "Longbow of the Hunt: Ranged Weapon Attack: +11 to hit, range 150/600 ft., one target. Hit: 15 (2d8 + 6) piercing damage plus 1d8 poison damage."
    )
    assert (
        kragga_the_huntmaster_stat_block.bonus_actions[0]
        == "Beast Command: Kragga can use a bonus action to command one of his beasts to make a melee attack, Dash, Disengage, or use the Help action."
    )
    assert (
        kragga_the_huntmaster_stat_block.reactions[0]
        == "Counterattack: When a beast under Kragga's command is attacked, Kragga can use his reaction to make a ranged attack with his Longbow of the Hunt against the attacker."
    )


@pytest.fixture
def mazrak_the_darkshadow_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.mazrak_the_darkshadow_custom_stat_block
    )

def test_mazrak_the_darkshadow_stat_block(mazrak_the_darkshadow_stat_block):
    # Check if the Mazrak the Darkshadow StatBlock instance is created correctly
    assert mazrak_the_darkshadow_stat_block.name == "Mazrak the Darkshadow"
    assert mazrak_the_darkshadow_stat_block.hit_points == 240
    assert mazrak_the_darkshadow_stat_block.armor_class == 19
    assert mazrak_the_darkshadow_stat_block.speed == "30 ft."
    assert mazrak_the_darkshadow_stat_block.abilities.strength == 20
    assert mazrak_the_darkshadow_stat_block.saving_throws.strength == 10
    assert "Athletics +12" in mazrak_the_darkshadow_stat_block.skills
    assert (
        mazrak_the_darkshadow_stat_block.damage_resistances
        == "necrotic, bludgeoning from nonmagical attacks"
    )
    assert mazrak_the_darkshadow_stat_block.condition_immunities == "frightened, charmed"
    assert (
        mazrak_the_darkshadow_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    )
    assert mazrak_the_darkshadow_stat_block.languages == "Goblin, Common, Infernal"
    assert mazrak_the_darkshadow_stat_block.challenge == 19
    assert (
        "Dark Command: Mazrak can use a bonus action to command one of his allies within 60 feet to move up to its speed or make a single weapon attack."
        in mazrak_the_darkshadow_stat_block.special_abilities
    )
    assert (
        mazrak_the_darkshadow_stat_block.legendary_actions["Gloomstrike"]
        == "Mazrak makes a melee weapon attack with his Darkshadow Warhammer. If the attack hits, the target must succeed on a DC 18 Constitution saving throw or take an additional 4d6 necrotic damage and be blinded until the end of Mazrak's next turn."
    )
    assert (
        mazrak_the_darkshadow_stat_block.actions[0]
        == "Multiattack: Mazrak makes three attacks with his Darkshadow Warhammer or Gloomstrike."
    )
    assert (
        mazrak_the_darkshadow_stat_block.actions[1]
        == "Darkshadow Warhammer: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 22 (3d8 + 6) bludgeoning damage plus 2d6 necrotic damage."
    )
    assert (
        mazrak_the_darkshadow_stat_block.bonus_actions[0]
        == "Dark Command: Mazrak can use a bonus action to command one of his allies within 60 feet to move up to its speed or make a single weapon attack."
    )
    assert (
        mazrak_the_darkshadow_stat_block.reactions[0]
        == "Parry: When Mazrak is hit by a melee attack, he can use his reaction to add +3 to his AC for that attack, potentially causing the attack to miss."
    )



@pytest.fixture
def vorgeth_the_soulflayer_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.vorgeth_the_soulflayer_custom_stat_block
    )

def test_vorgeth_the_soulflayer_stat_block(vorgeth_the_soulflayer_stat_block):
    # Check if the Vorgeth the Soulflayer StatBlock instance is created correctly
    assert vorgeth_the_soulflayer_stat_block.name == "Vorgeth the Soulflayer"
    assert vorgeth_the_soulflayer_stat_block.hit_points == 180
    assert vorgeth_the_soulflayer_stat_block.armor_class == 17
    assert vorgeth_the_soulflayer_stat_block.speed == "30 ft."
    assert vorgeth_the_soulflayer_stat_block.abilities.intelligence == 20
    assert vorgeth_the_soulflayer_stat_block.saving_throws.intelligence == 10
    assert "Arcana +12" in vorgeth_the_soulflayer_stat_block.skills
    assert (
            vorgeth_the_soulflayer_stat_block.damage_resistances
            == "necrotic, cold"
    )
    assert vorgeth_the_soulflayer_stat_block.condition_immunities == "frightened, charmed"
    assert (
            vorgeth_the_soulflayer_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    )
    assert vorgeth_the_soulflayer_stat_block.languages == "Goblin, Common, Abyssal"
    assert vorgeth_the_soulflayer_stat_block.challenge == 18

    # Check for each special ability separately
    expected_special_abilities = [
        "Undead Mastery: Vorgeth can control up to twice the usual number of undead using his necromancy spells. Additionally, undead under his control have advantage on attack rolls and saving throws while within 60 feet of him.",
        "Life Drain: When Vorgeth reduces a creature to 0 hit points, he regains hit points equal to the damage dealt. This ability can only be used once per turn.",
        "Aura of Dread: Any creature that starts its turn within 10 feet of Vorgeth must succeed on a DC 18 Wisdom saving throw or be frightened until the end of its next turn."
    ]

    for ability in expected_special_abilities:
        assert ability in vorgeth_the_soulflayer_stat_block.special_abilities

    assert (
            vorgeth_the_soulflayer_stat_block.legendary_actions["Necrotic Bolt"]
            == "Vorgeth makes a ranged spell attack with Necrotic Touch. If the attack hits, it deals 4d8 necrotic damage, and the target must succeed on a DC 18 Constitution saving throw or have its hit point maximum reduced by the damage taken."
    )
    assert (
            vorgeth_the_soulflayer_stat_block.actions[0]
            == "Multiattack: Vorgeth makes two attacks with his Staff of Bones or casts two cantrips."
    )
    assert (
            vorgeth_the_soulflayer_stat_block.actions[1]
            == "Staff of Bones: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage plus 2d6 necrotic damage."
    )
    assert (
            vorgeth_the_soulflayer_stat_block.bonus_actions[0]
            == "Life Drain: When Vorgeth reduces a creature to 0 hit points, he regains hit points equal to the damage dealt."
    )
    assert (
            vorgeth_the_soulflayer_stat_block.reactions[0]
            == "Shield: When Vorgeth is hit by an attack, he can use his reaction to cast Shield, increasing his AC by +5 until the start of his next turn."
    )



@pytest.fixture
def zorgath_the_bloodhound_stat_block():
    # Fixture to provide a sample instance of GoblinoidChampionStatBlock for testing
    return GoblinoidChampionStatBlock(
        **legendary_goblinoids.zorgath_the_bloodhound_custom_stat_block
    )

def test_zorgath_the_bloodhound_stat_block(zorgath_the_bloodhound_stat_block):
    # Check if the Zorgath the Bloodhound StatBlock instance is created correctly
    assert zorgath_the_bloodhound_stat_block.name == "Zorgath the Bloodhound"
    assert zorgath_the_bloodhound_stat_block.hit_points == 280
    assert zorgath_the_bloodhound_stat_block.armor_class == 18
    assert zorgath_the_bloodhound_stat_block.speed == "40 ft."
    assert zorgath_the_bloodhound_stat_block.abilities.strength == 22
    assert zorgath_the_bloodhound_stat_block.saving_throws.strength == 12
    assert "Athletics +14" in zorgath_the_bloodhound_stat_block.skills
    assert (
            zorgath_the_bloodhound_stat_block.damage_resistances
            == "bludgeoning, piercing, and slashing from nonmagical attacks while raging"
    )
    assert zorgath_the_bloodhound_stat_block.condition_immunities == "charmed, frightened"
    assert (
            zorgath_the_bloodhound_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    )
    assert zorgath_the_bloodhound_stat_block.languages == "Goblin, Common"
    assert zorgath_the_bloodhound_stat_block.challenge == 19

    # Check for each special ability separately
    expected_special_abilities = [
        "Blood Frenzy: Zorgath has advantage on melee attack rolls against any creature that doesn't have all its hit points.",
        "Blood Magic: Zorgath can use a bonus action to drain the life force of a creature he has hit with a melee attack, healing himself for 1d10 hit points per level of the creature.",
        "Relentless Rage: If Zorgath drops to 0 hit points while raging and doesn't die outright, he can make a DC 10 Constitution saving throw. If he succeeds, he drops to 1 hit point instead."
    ]

    for ability in expected_special_abilities:
        assert ability in zorgath_the_bloodhound_stat_block.special_abilities

    # Check legendary actions
    assert (
            zorgath_the_bloodhound_stat_block.legendary_actions["Bloodrage Strike"]
            == "Zorgath makes a single melee weapon attack with his Bloodthirsty Greatsword. If the attack hits, it deals an additional 4d6 necrotic damage, and Zorgath regains hit points equal to the necrotic damage dealt."
    )
    assert (
            zorgath_the_bloodhound_stat_block.legendary_actions["Terrifying Roar (Costs 2 Actions)"]
            == "Zorgath lets out a bloodcurdling roar. All enemies within 30 feet must succeed on a DC 18 Wisdom saving throw or be frightened until the end of Zorgath's next turn."
    )

    # Check actions
    assert (
            zorgath_the_bloodhound_stat_block.actions[0]
            == "Multiattack: Zorgath makes three attacks with his Bloodthirsty Greatsword or Bloodletting Claws."
    )
    assert (
            zorgath_the_bloodhound_stat_block.actions[1]
            == "Bloodthirsty Greatsword: Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 24 (3d10 + 6) slashing damage plus 2d6 necrotic damage."
    )

    # Check bonus actions
    assert (
            zorgath_the_bloodhound_stat_block.bonus_actions[0]
            == "Blood Magic: Zorgath can use a bonus action to drain the life force of a creature he has hit with a melee attack, healing himself for 1d10 hit points per level of the creature."
    )

    # Check reactions
    assert (
            zorgath_the_bloodhound_stat_block.reactions[0]
            == "Unyielding Rage: When Zorgath is hit by a melee attack, he can use his reaction to reduce the damage by half."
    )
