import pytest

from .. import legendary_humanoids

from ..legendary_humanoids import HumanoidChampionStatBlock

@pytest.fixture
def gog_the_crusher_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.gog_the_crusher_custom_stat_block)


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

@pytest.fixture
def bruthazmus_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.bruthazmus_custom_stat_block)


def test_bruthazmus_stat_block(bruthazmus_stat_block):
    # Check if the Bruthazmus StatBlock instance is created correctly
    assert bruthazmus_stat_block.name == "Bruthazmus"
    assert bruthazmus_stat_block.hit_points == 280
    assert bruthazmus_stat_block.armor_class == 17
    assert bruthazmus_stat_block.speed == "30 ft."
    assert bruthazmus_stat_block.abilities.strength == 20
    assert bruthazmus_stat_block.saving_throws.strength == 10
    assert "Stealth +12" in bruthazmus_stat_block.skills
    assert bruthazmus_stat_block.damage_resistances == "poison"
    assert bruthazmus_stat_block.condition_immunities == "frightened"
    assert bruthazmus_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert bruthazmus_stat_block.languages == "Giant, Common, Goblin"
    assert bruthazmus_stat_block.challenge == 17
    assert (
        "Sneak Attack (5d6): Once per turn, Bruthazmus can deal an extra 5d6 damage to one creature he hits with an attack if he has advantage on the attack roll. The attack must use a finesse or a ranged weapon."
        in bruthazmus_stat_block.special_abilities
    )
    assert (
        bruthazmus_stat_block.legendary_actions["Vanish"]
        == "Bruthazmus can take the Hide action."
    )
    assert (
        bruthazmus_stat_block.actions[0]
        == "Multiattack: Bruthazmus makes two attacks with his Barbed Longbow or Poisoned Dagger."
    )
    assert (
        bruthazmus_stat_block.actions[1]
        == "Barbed Longbow: Ranged Weapon Attack: +11 to hit, range 150/600 ft., one target. Hit: 18 (2d10 + 7) piercing damage."
    )
    assert (
        bruthazmus_stat_block.bonus_actions[0]
        == "Cunning Action: Bruthazmus can use his bonus action to Dash, Disengage, or Hide."
    )
    assert (
        bruthazmus_stat_block.reactions[0]
        == "Uncanny Dodge: When an attacker that Bruthazmus can see hits him with an attack, he can use his reaction to halve the attack's damage against him."
    )

@pytest.fixture
def throgg_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.throgg_custom_stat_block)


def test_throgg_stat_block(throgg_stat_block):
    # Check if the Throgg the Troll King StatBlock instance is created correctly
    assert throgg_stat_block.name == "Throgg the Troll King"
    assert throgg_stat_block.hit_points == 400
    assert throgg_stat_block.armor_class == 18
    assert throgg_stat_block.speed == "40 ft."
    assert throgg_stat_block.abilities.strength == 24
    assert throgg_stat_block.saving_throws.strength == 13
    assert "Intimidation +10" in throgg_stat_block.skills
    assert throgg_stat_block.damage_resistances == "fire, necrotic"
    assert throgg_stat_block.condition_immunities == "frightened, charmed"
    assert throgg_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    assert throgg_stat_block.languages == "Giant, Common, Infernal"
    assert throgg_stat_block.challenge == 20
    assert (
        "Regeneration: Throgg regains 20 hit points at the start of his turn if he has at least 1 hit point remaining. If Throgg takes acid or fire damage, this trait doesn't function at the start of his next turn."
        in throgg_stat_block.special_abilities
    )
    assert (
        throgg_stat_block.legendary_actions["Fiendish Smite"]
        == "Throgg makes a melee weapon attack with his Corrupted Greataxe. On a hit, the target takes an additional 4d6 necrotic damage."
    )
    assert (
        throgg_stat_block.actions[0]
        == "Multiattack: Throgg makes two attacks with his Corrupted Greataxe or Regenerating Claws."
    )
    assert (
        throgg_stat_block.actions[1]
        == "Corrupted Greataxe: Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 27 (3d12 + 6) slashing damage plus 7 (2d6) necrotic damage."
    )
    assert (
        throgg_stat_block.bonus_actions[0]
        == "Dark Bargain: Throgg can use his bonus action to empower his attacks with necrotic energy, dealing an extra 2d6 necrotic damage on all melee attacks for 1 minute."
    )
    assert (
        throgg_stat_block.reactions[0]
        == "Unyielding Endurance: When Throgg is reduced to 0 hit points, he can use his reaction to instead be reduced to 1 hit point. He can't use this feature again until he finishes a long rest."
    )


@pytest.fixture
def skalmad_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.skalmad_custom_stat_block)


def test_skalmad_stat_block(skalmad_stat_block):
    # Check if the Skalmad the Troll Champion StatBlock instance is created correctly
    assert skalmad_stat_block.name == "Skalmad the Troll Champion"
    assert skalmad_stat_block.hit_points == 370
    assert skalmad_stat_block.armor_class == 19
    assert skalmad_stat_block.speed == "40 ft."
    assert skalmad_stat_block.abilities.strength == 26
    assert skalmad_stat_block.saving_throws.strength == 14
    assert "Athletics +14" in skalmad_stat_block.skills
    assert skalmad_stat_block.damage_resistances == "fire, bludgeoning, piercing, and slashing from nonmagical attacks"
    assert skalmad_stat_block.condition_immunities == "frightened"
    assert skalmad_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    assert skalmad_stat_block.languages == "Giant, Common, Goblin"
    assert skalmad_stat_block.challenge == 21
    assert (
        "Regeneration: Skalmad regains 20 hit points at the start of his turn if he has at least 1 hit point remaining. If Skalmad takes acid damage, this trait doesn't function at the start of his next turn."
        in skalmad_stat_block.special_abilities
    )
    assert (
        skalmad_stat_block.legendary_actions["Fiery Gaze"]
        == "Skalmad uses his Eye of Veng to shoot a beam of fire at a creature within 60 feet. The target must make a DC 18 Dexterity saving throw, taking 4d10 fire damage on a failed save, or half as much on a successful one."
    )
    assert (
        skalmad_stat_block.actions[0]
        == "Multiattack: Skalmad makes three attacks with his Eye of Veng or one with his Fiery Gaze."
    )
    assert (
        skalmad_stat_block.actions[1]
        == "Eye of Veng: Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 28 (3d12 + 8) bludgeoning damage plus 7 (2d6) fire damage."
    )
    assert (
        skalmad_stat_block.bonus_actions[0]
        == "Second Wind: Skalmad can use a bonus action to regain hit points equal to 1d10 + 18."
    )
    assert (
        skalmad_stat_block.reactions[0]
        == "Unyielding Endurance: When Skalmad is reduced to 0 hit points, he can use his reaction to instead be reduced to 1 hit point. He can't use this feature again until he finishes a long rest."
    )


@pytest.fixture
def kargath_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.kargath_custom_stat_block)


def test_kargath_stat_block(kargath_stat_block):
    # Check if the Kargath the Slayer StatBlock instance is created correctly
    assert kargath_stat_block.name == "Kargath the Slayer"
    assert kargath_stat_block.hit_points == 425
    assert kargath_stat_block.armor_class == 18
    assert kargath_stat_block.speed == "40 ft."
    assert kargath_stat_block.abilities.strength == 28
    assert kargath_stat_block.saving_throws.strength == 15
    assert "Athletics +15" in kargath_stat_block.skills
    assert kargath_stat_block.damage_resistances == "bludgeoning, piercing, and slashing from nonmagical attacks while raging"
    assert kargath_stat_block.condition_immunities == "frightened, charmed"
    assert kargath_stat_block.senses == "darkvision 60 ft., passive Perception 16"
    assert kargath_stat_block.languages == "Giant, Common"
    assert kargath_stat_block.challenge == 22
    assert (
        "Rage (6/day): Kargath can enter a rage as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage, as well as a +4 bonus to damage rolls. His rage lasts for 1 minute or until he is incapacitated."
        in kargath_stat_block.special_abilities
    )
    assert (
        kargath_stat_block.legendary_actions["Reckless Cleave"]
        == "Kargath makes a melee weapon attack with Bloodthirster. If the attack hits, it deals an additional 2d12 damage. Kargath then gains advantage on all attacks until the end of his next turn, but attacks against him also have advantage."
    )
    assert (
        kargath_stat_block.actions[0]
        == "Multiattack: Kargath makes three attacks with Bloodthirster."
    )
    assert (
        kargath_stat_block.actions[1]
        == "Bloodthirster: Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 32 (3d12 + 9) slashing damage."
    )
    assert (
        kargath_stat_block.bonus_actions[0]
        == "Frenzied Attack: While raging, Kargath can make an additional melee weapon attack as a bonus action."
    )
    assert (
        kargath_stat_block.reactions[0]
        == "Relentless Endurance: When Kargath is reduced to 0 hit points, he can use his reaction to instead be reduced to 1 hit point. He can't use this feature again until he finishes a long rest."
    )

@pytest.fixture
def hartusk_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.hartusk_custom_stat_block)


def test_hartusk_stat_block(hartusk_stat_block):
    # Check if the Hartusk the Orc Warlord StatBlock instance is created correctly
    assert hartusk_stat_block.name == "Hartusk the Orc Warlord"
    assert hartusk_stat_block.hit_points == 290
    assert hartusk_stat_block.armor_class == 20
    assert hartusk_stat_block.speed == "30 ft."
    assert hartusk_stat_block.abilities.strength == 20
    assert hartusk_stat_block.saving_throws.strength == 10
    assert "Intimidation +10" in hartusk_stat_block.skills
    assert hartusk_stat_block.damage_resistances == "bludgeoning, piercing, and slashing from nonmagical attacks while raging"
    assert hartusk_stat_block.condition_immunities == "frightened"
    assert hartusk_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert hartusk_stat_block.languages == "Orc, Common"
    assert hartusk_stat_block.challenge == 18
    assert (
        "Commander's Strike: When Hartusk takes the Attack action on his turn, he can forego one of his attacks and use a bonus action to direct one of his allies to strike. That ally can immediately use their reaction to make one weapon attack, adding Hartusk's Charisma modifier to the attack roll."
        in hartusk_stat_block.special_abilities
    )
    assert (
        hartusk_stat_block.legendary_actions["War Cry"]
        == "Hartusk lets out a powerful war cry, bolstering his allies and intimidating his enemies. All allies within 30 feet gain temporary hit points equal to 10 + Hartusk's Charisma modifier. All enemies must succeed on a DC 18 Wisdom saving throw or become frightened until the end of Hartusk's next turn."
    )
    assert (
        hartusk_stat_block.actions[0]
        == "Multiattack: Hartusk makes three attacks with his Crushing Warhammer."
    )
    assert (
        hartusk_stat_block.actions[1]
        == "Crushing Warhammer: Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 18 (2d8 + 6) bludgeoning damage."
    )
    assert (
        hartusk_stat_block.bonus_actions[0]
        == "Orcish Fury: Hartusk can use his bonus action to enter a rage, gaining advantage on Strength checks and saving throws, and dealing an extra 2d6 damage on melee weapon attacks for 1 minute."
    )
    assert (
        hartusk_stat_block.reactions[0]
        == "Parry: Hartusk adds +3 to his AC against one melee attack that would hit him. To do so, Hartusk must see the attacker and be wielding a melee weapon."
    )


@pytest.fixture
def obould_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.obould_custom_stat_block)

def test_obould_stat_block(obould_stat_block):
    # Check if the Obould Many-Arrows StatBlock instance is created correctly
    assert obould_stat_block.name == "Obould Many-Arrows"
    assert obould_stat_block.hit_points == 320
    assert obould_stat_block.armor_class == 21
    assert obould_stat_block.speed == "30 ft."
    assert obould_stat_block.abilities.strength == 22
    assert obould_stat_block.saving_throws.strength == 12
    assert "Intimidation +10" in obould_stat_block.skills
    assert obould_stat_block.damage_resistances == "bludgeoning, piercing, and slashing from nonmagical attacks"
    assert obould_stat_block.condition_immunities == "frightened"
    assert obould_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    assert obould_stat_block.languages == "Orc, Common"
    assert obould_stat_block.challenge == 20
    assert (
            "Aura of Conquest: Creatures within 10 feet of Obould that are frightened by him have their speed reduced to 0 and take psychic damage equal to his Charisma modifier at the start of each of their turns."
            in obould_stat_block.special_abilities
    )
    assert (
            obould_stat_block.legendary_actions["Conquering Strike"]
            == "Obould makes a melee weapon attack with his Flame-tongue Greatsword. If the attack hits, the target must succeed on a DC 18 Wisdom saving throw or be frightened until the end of Obould's next turn."
    )
    assert (
            obould_stat_block.actions[0]
            == "Multiattack: Obould makes three attacks with his Flame-tongue Greatsword or Orcish Longbow."
    )
    assert (
            obould_stat_block.actions[1]
            == "Flame-tongue Greatsword: Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 22 (3d6 + 8) slashing damage plus 7 (2d6) fire damage."
    )
    assert (
            obould_stat_block.bonus_actions[0]
            == "Shield of Faith: Obould can cast *Shield of Faith* as a bonus action, gaining +2 AC for 10 minutes (concentration)."
    )
    assert (
            obould_stat_block.reactions[0]
            == "Parry: Obould adds +3 to his AC against one melee attack that would hit him. To do so, Obould must see the attacker and be wielding a melee weapon."
    )


@pytest.fixture
def karzoug_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.karzoug_custom_stat_block)


def test_karzoug_stat_block(karzoug_stat_block):
    # Check if the Karzoug, the Runelord of Greed StatBlock instance is created correctly
    assert karzoug_stat_block.name == "Karzoug, the Runelord of Greed"
    assert karzoug_stat_block.hit_points == 375
    assert karzoug_stat_block.armor_class == 20
    assert karzoug_stat_block.speed == "30 ft., fly 60 ft."
    assert karzoug_stat_block.abilities.strength == 24
    assert karzoug_stat_block.saving_throws.strength == 12
    assert "Arcana +14" in karzoug_stat_block.skills
    assert karzoug_stat_block.damage_resistances == "cold, force"
    assert karzoug_stat_block.condition_immunities == "charmed, frightened"
    assert karzoug_stat_block.senses == "darkvision 60 ft., truesight 60 ft., passive Perception 20"
    assert karzoug_stat_block.languages == "Giant, Common, Draconic, Infernal, Abyssal"
    assert karzoug_stat_block.challenge == 24
    assert (
        "Transmuter's Stone: Karzoug can create a magical stone that grants a variety of benefits, such as resistance to a specific damage type, increased speed, or the ability to breathe underwater."
        in karzoug_stat_block.special_abilities
    )
    assert (
        karzoug_stat_block.legendary_actions["Arcane Ray"]
        == "Karzoug makes a ranged spell attack (+14 to hit) against one target within 120 feet. On a hit, the target takes 28 (8d6) force damage."
    )
    assert (
        karzoug_stat_block.actions[0]
        == "Multiattack: Karzoug makes two Arcane Ray attacks or one attack with his Staff of Greed and one Arcane Ray attack."
    )
    assert (
        karzoug_stat_block.actions[1]
        == "Staff of Greed: Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 22 (2d10 + 10) bludgeoning damage plus 14 (4d6) necrotic damage."
    )
    assert (
        karzoug_stat_block.bonus_actions[0]
        == "Second Wind: Karzoug can use a bonus action to regain hit points equal to 1d10 + 3."
    )
    assert (
        karzoug_stat_block.reactions[0]
        == "Arcane Deflection: When Karzoug is hit by an attack, he can use his reaction to add +4 to his AC against the attack, potentially causing it to miss."
    )


@pytest.fixture
def sharak_stat_block():
    # Fixture to provide a sample instance of HumanoidChampionStatBlock for testing
    return HumanoidChampionStatBlock(**legendary_humanoids.sharak_custom_stat_block)


def test_sharak_stat_block(sharak_stat_block):
    # Check if the Sharak the Sorcerer StatBlock instance is created correctly
    assert sharak_stat_block.name == "Sharak the Sorcerer"
    assert sharak_stat_block.hit_points == 340
    assert sharak_stat_block.armor_class == 20
    assert sharak_stat_block.speed == "30 ft., fly 60 ft."
    assert sharak_stat_block.abilities.strength == 22
    assert sharak_stat_block.saving_throws.strength == 11
    assert "Arcana +10" in sharak_stat_block.skills
    assert sharak_stat_block.damage_resistances == "necrotic, psychic"
    assert sharak_stat_block.condition_immunities == "charmed, frightened"
    assert sharak_stat_block.senses == "darkvision 120 ft., passive Perception 18"
    assert sharak_stat_block.languages == "Giant, Common, Infernal, Abyssal"
    assert sharak_stat_block.challenge == 22
    assert (
        "Eyes of the Dark: Sharak can see normally in darkness, both magical and nonmagical, up to 120 feet."
        in sharak_stat_block.special_abilities
    )
    assert (
        sharak_stat_block.legendary_actions["Arcane Blast"]
        == "Sharak makes a ranged spell attack (+14 to hit) against one target within 120 feet. On a hit, the target takes 27 (6d8) force damage."
    )
    assert (
        sharak_stat_block.actions[0]
        == "Multiattack: Sharak makes two attacks with his Shadow Blade or one with his Shadow Blade and one Arcane Blast."
    )
    assert (
        sharak_stat_block.actions[1]
        == "Shadow Blade: Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (2d8 + 10) psychic damage."
    )
    assert (
        sharak_stat_block.bonus_actions[0]
        == "Hound of Ill Omen: Sharak can use a bonus action to summon a shadowy hound to track and harry one creature he can see within 120 feet."
    )
    assert (
        sharak_stat_block.reactions[0]
        == "Uncanny Dodge: When an attacker that Sharak can see hits him with an attack, he can use his reaction to halve the attack's damage against him."
    )
