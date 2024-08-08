import pytest

from .. import legendary_giants

from ..legendary_giants import LegendaryGiantStatBlock

@pytest.fixture
def thane_kayalithica_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.thane_kayalithica_custom_stat_block)

def test_thane_kayalithica_stat_block(thane_kayalithica_stat_block):
    # Check if the Thane Kayalithica StatBlock instance is created correctly
    assert thane_kayalithica_stat_block.name == "Thane Kayalithica"
    assert thane_kayalithica_stat_block.hit_points == 230
    assert thane_kayalithica_stat_block.armor_class == 18
    assert thane_kayalithica_stat_block.speed == "40 ft."
    assert thane_kayalithica_stat_block.abilities.strength == 25
    assert thane_kayalithica_stat_block.saving_throws.strength == 12
    assert "Perception +9" in thane_kayalithica_stat_block.skills
    assert (
        thane_kayalithica_stat_block.damage_resistances
        == "bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert thane_kayalithica_stat_block.condition_immunities == "none"
    assert thane_kayalithica_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    assert thane_kayalithica_stat_block.languages == "Giant, Terran"
    assert thane_kayalithica_stat_block.challenge == 13
    assert (
        "Stone Camouflage: Thane Kayalithica has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
        in thane_kayalithica_stat_block.special_abilities
    )
    assert (
        thane_kayalithica_stat_block.legendary_actions["Detect"]
        == "Thane Kayalithica makes a Wisdom (Perception) check."
    )
    assert (
        thane_kayalithica_stat_block.actions[0]
        == "Multiattack: Thane Kayalithica makes two attacks with her Greatclub."
    )
    assert (
        thane_kayalithica_stat_block.actions[1]
        == "Greatclub: Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 25 (3d8 + 7) bludgeoning damage."
    )
    # No bonus actions defined, but including an empty check
    assert thane_kayalithica_stat_block.bonus_actions == []
    # No reactions defined, but including an empty check
    assert thane_kayalithica_stat_block.reactions == []

@pytest.fixture
def king_snurre_ironbelly_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.king_snurre_ironbelly_custom_stat_block)

def test_king_snurre_ironbelly_stat_block(king_snurre_ironbelly_stat_block):
    # Check if the King Snurre Ironbelly StatBlock instance is created correctly
    assert king_snurre_ironbelly_stat_block.name == "King Snurre Ironbelly"
    assert king_snurre_ironbelly_stat_block.hit_points == 345
    assert king_snurre_ironbelly_stat_block.armor_class == 21
    assert king_snurre_ironbelly_stat_block.speed == "40 ft."
    assert king_snurre_ironbelly_stat_block.abilities.strength == 28
    assert king_snurre_ironbelly_stat_block.saving_throws.strength == 14
    assert "Athletics +14" in king_snurre_ironbelly_stat_block.skills
    assert king_snurre_ironbelly_stat_block.damage_resistances == "fire"
    assert king_snurre_ironbelly_stat_block.condition_immunities == "none"
    assert king_snurre_ironbelly_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert king_snurre_ironbelly_stat_block.languages == "Giant, Common, Ignan"
    assert king_snurre_ironbelly_stat_block.challenge == 18
    assert (
        "Fire Aura: King Snurre radiates intense heat. Any creature that starts its turn within 5 feet of him takes 10 (3d6) fire damage."
        in king_snurre_ironbelly_stat_block.special_abilities
    )
    assert (
        king_snurre_ironbelly_stat_block.legendary_actions["Detect"]
        == "King Snurre makes a Wisdom (Perception) check."
    )
    assert (
        king_snurre_ironbelly_stat_block.actions[0]
        == "Multiattack: King Snurre makes three attacks with his Flaming Greatsword."
    )
    assert (
        king_snurre_ironbelly_stat_block.actions[1]
        == "Flaming Greatsword: Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 23 (4d6 + 9) slashing damage plus 14 (4d6) fire damage."
    )
    assert (
        king_snurre_ironbelly_stat_block.bonus_actions[0]
        == "Rage (4 uses/day): King Snurre can enter a rage as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage, and adding bonus damage to his melee attacks."
    )
    assert (
        king_snurre_ironbelly_stat_block.reactions[0]
        == "Parry: King Snurre adds 4 to his AC against one melee attack that would hit him. To do so, King Snurre must see the attacker and be wielding a melee weapon."
    )

@pytest.fixture
def queen_neri_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.queen_neri_custom_stat_block)

def test_queen_neri_stat_block(queen_neri_stat_block):
    # Check if the Queen Neri StatBlock instance is created correctly
    assert queen_neri_stat_block.name == "Queen Neri"
    assert queen_neri_stat_block.hit_points == 310
    assert queen_neri_stat_block.armor_class == 20
    assert queen_neri_stat_block.speed == "50 ft., swim 100 ft."
    assert queen_neri_stat_block.abilities.strength == 26
    assert queen_neri_stat_block.saving_throws.strength == 13
    assert "Insight +10" in queen_neri_stat_block.skills
    assert queen_neri_stat_block.damage_resistances == "lightning, thunder"
    assert queen_neri_stat_block.condition_immunities == "none"
    assert queen_neri_stat_block.senses == "darkvision 60 ft., passive Perception 20"
    assert queen_neri_stat_block.languages == "Giant, Common, Aquan"
    assert queen_neri_stat_block.challenge == 17
    assert (
        "Storm Aura: Queen Neri is surrounded by a swirling storm. Any creature that starts its turn within 10 feet of her takes 10 (3d6) lightning damage."
        in queen_neri_stat_block.special_abilities
    )
    assert (
        queen_neri_stat_block.legendary_actions["Detect"]
        == "Queen Neri makes a Wisdom (Perception) check."
    )
    assert (
        queen_neri_stat_block.actions[0]
        == "Multiattack: Queen Neri makes three attacks with her Trident."
    )
    assert (
        queen_neri_stat_block.actions[1]
        == "Trident: Melee or Ranged Weapon Attack: +13 to hit, reach 10 ft. or range 20/60 ft., one target. Hit: 21 (3d8 + 8) piercing damage."
    )
    # No bonus actions defined, but including an empty check
    assert queen_neri_stat_block.bonus_actions == []
    assert (
        queen_neri_stat_block.reactions[0]
        == "Shield: Queen Neri adds 5 to her AC against one attack that would hit her. To do so, she must see the attacker."
    )

@pytest.fixture
def king_hekaton_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.king_hekaton_custom_stat_block)

def test_king_hekaton_stat_block(king_hekaton_stat_block):
    # Check if the King Hekaton StatBlock instance is created correctly
    assert king_hekaton_stat_block.name == "King Hekaton"
    assert king_hekaton_stat_block.hit_points == 350
    assert king_hekaton_stat_block.armor_class == 22
    assert king_hekaton_stat_block.speed == "50 ft., swim 50 ft."
    assert king_hekaton_stat_block.abilities.strength == 29
    assert king_hekaton_stat_block.saving_throws.strength == 15
    assert "Athletics +15" in king_hekaton_stat_block.skills
    assert king_hekaton_stat_block.damage_resistances == "lightning, thunder"
    assert king_hekaton_stat_block.condition_immunities == "none"
    assert king_hekaton_stat_block.senses == "darkvision 60 ft., passive Perception 20"
    assert king_hekaton_stat_block.languages == "Giant, Common, Primordial"
    assert king_hekaton_stat_block.challenge == 19
    assert (
        "Storm Aura: King Hekaton is surrounded by a raging storm. Any creature that starts its turn within 10 feet of him takes 10 (3d6) lightning damage."
        in king_hekaton_stat_block.special_abilities
    )
    assert (
        king_hekaton_stat_block.legendary_actions["Detect"]
        == "King Hekaton makes a Wisdom (Perception) check."
    )
    assert (
        king_hekaton_stat_block.actions[0]
        == "Multiattack: King Hekaton makes three attacks with his Thunderous Greatsword."
    )
    assert (
        king_hekaton_stat_block.actions[1]
        == "Thunderous Greatsword: Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 24 (4d6 + 10) slashing damage plus 14 (4d6) thunder damage."
    )
    # No bonus actions defined, but including an empty check
    assert king_hekaton_stat_block.bonus_actions == []
    assert (
        king_hekaton_stat_block.reactions[0]
        == "Parry: King Hekaton adds 4 to his AC against one melee attack that would hit him. To do so, he must see the attacker and be wielding a melee weapon."
    )


@pytest.fixture
def chief_nosnra_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.chief_nosnra_custom_stat_block)

def test_chief_nosnra_stat_block(chief_nosnra_stat_block):
    # Check if the Chief Nosnra StatBlock instance is created correctly
    assert chief_nosnra_stat_block.name == "Chief Nosnra"
    assert chief_nosnra_stat_block.hit_points == 340
    assert chief_nosnra_stat_block.armor_class == 19
    assert chief_nosnra_stat_block.speed == "40 ft."
    assert chief_nosnra_stat_block.abilities.strength == 27
    assert chief_nosnra_stat_block.saving_throws.strength == 14
    assert "Athletics +14" in chief_nosnra_stat_block.skills
    assert chief_nosnra_stat_block.damage_resistances == "bludgeoning, piercing, and slashing from nonmagical attacks"
    assert chief_nosnra_stat_block.condition_immunities == "none"
    assert chief_nosnra_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert chief_nosnra_stat_block.languages == "Giant, Common"
    assert chief_nosnra_stat_block.challenge == 18
    assert (
        "Rallying Cry: Chief Nosnra can use a bonus action to bolster his allies, granting them advantage on their next attack roll or saving throw."
        in chief_nosnra_stat_block.special_abilities
    )
    assert (
        chief_nosnra_stat_block.legendary_actions["Detect"]
        == "Chief Nosnra makes a Wisdom (Perception) check."
    )
    assert (
        chief_nosnra_stat_block.actions[0]
        == "Multiattack: Chief Nosnra makes three attacks with his Greatclub."
    )
    assert (
        chief_nosnra_stat_block.actions[1]
        == "Greatclub: Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 23 (3d8 + 10) bludgeoning damage."
    )
    # No bonus actions defined, but including an empty check
    assert chief_nosnra_stat_block.bonus_actions == []
    assert (
        chief_nosnra_stat_block.reactions[0]
        == "Parry: Chief Nosnra adds 4 to his AC against one melee attack that would hit him. To do so, he must see the attacker and be wielding a melee weapon."
    )


@pytest.fixture
def harshnag_the_grim_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.harshnag_the_grim_custom_stat_block)

def test_harshnag_the_grim_stat_block(harshnag_the_grim_stat_block):
    # Check if the Harshnag the Grim StatBlock instance is created correctly
    assert harshnag_the_grim_stat_block.name == "Harshnag the Grim"
    assert harshnag_the_grim_stat_block.hit_points == 450
    assert harshnag_the_grim_stat_block.armor_class == 22
    assert harshnag_the_grim_stat_block.speed == "40 ft."
    assert harshnag_the_grim_stat_block.abilities.strength == 28
    assert harshnag_the_grim_stat_block.saving_throws.strength == 15
    assert "Athletics +15" in harshnag_the_grim_stat_block.skills
    assert harshnag_the_grim_stat_block.damage_resistances == "cold"
    assert harshnag_the_grim_stat_block.condition_immunities == "none"
    assert harshnag_the_grim_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    assert harshnag_the_grim_stat_block.languages == "Giant, Common"
    assert harshnag_the_grim_stat_block.challenge == 20
    assert (
        "Great Weapon Fighting: When Harshnag rolls a 1 or 2 on a damage die for an attack he makes with a melee weapon that he is wielding with two hands, he can reroll the die and must use the new roll."
        in harshnag_the_grim_stat_block.special_abilities
    )
    assert (
        harshnag_the_grim_stat_block.legendary_actions["Detect"]
        == "Harshnag makes a Wisdom (Perception) check."
    )
    assert (
        harshnag_the_grim_stat_block.actions[0]
        == "Multiattack: Harshnag makes three attacks with his Greataxe."
    )
    assert (
        harshnag_the_grim_stat_block.actions[1]
        == "Greataxe: Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 8) slashing damage."
    )
    # No bonus actions defined, but including an empty check
    assert harshnag_the_grim_stat_block.bonus_actions == []
    assert (
        harshnag_the_grim_stat_block.reactions[0]
        == "Parry: Harshnag adds 4 to his AC against one melee attack that would hit him. To do so, he must see the attacker and be wielding a melee weapon."
    )


@pytest.fixture
def jarl_grugnur_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.jarl_grugnur_custom_stat_block)

def test_jarl_grugnur_stat_block(jarl_grugnur_stat_block):
    # Check if the Jarl Grugnur StatBlock instance is created correctly
    assert jarl_grugnur_stat_block.name == "Jarl Grugnur"
    assert jarl_grugnur_stat_block.hit_points == 480
    assert jarl_grugnur_stat_block.armor_class == 21
    assert jarl_grugnur_stat_block.speed == "40 ft."
    assert jarl_grugnur_stat_block.abilities.strength == 29
    assert jarl_grugnur_stat_block.saving_throws.strength == 15
    assert "Athletics +15" in jarl_grugnur_stat_block.skills
    assert jarl_grugnur_stat_block.damage_resistances == "cold"
    assert jarl_grugnur_stat_block.condition_immunities == "none"
    assert jarl_grugnur_stat_block.senses == "darkvision 60 ft., passive Perception 18"
    assert jarl_grugnur_stat_block.languages == "Giant, Common"
    assert jarl_grugnur_stat_block.challenge == 21
    assert (
        "Unstoppable Rage: While raging, Jarl Grugnur has advantage on all Strength checks and saving throws."
        in jarl_grugnur_stat_block.special_abilities
    )
    assert (
        jarl_grugnur_stat_block.legendary_actions["Detect"]
        == "Jarl Grugnur makes a Wisdom (Perception) check."
    )
    assert (
        jarl_grugnur_stat_block.actions[0]
        == "Multiattack: Jarl Grugnur makes three attacks with his Greatclub."
    )
    assert (
        jarl_grugnur_stat_block.actions[1]
        == "Greatclub: Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 31 (6d8 + 10) bludgeoning damage."
    )
    # No bonus actions defined, but including an empty check
    assert jarl_grugnur_stat_block.bonus_actions == []
    assert (
        jarl_grugnur_stat_block.reactions[0]
        == "Parry: Jarl Grugnur adds 4 to his AC against one melee attack that would hit him. To do so, he must see the attacker and be wielding a melee weapon."
    )


@pytest.fixture
def sylara_leafweaver_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.sylara_leafweaver_custom_stat_block)

def test_sylara_leafweaver_stat_block(sylara_leafweaver_stat_block):
    # Check if the Sylara Leafweaver StatBlock instance is created correctly
    assert sylara_leafweaver_stat_block.name == "Sylara Leafweaver"
    assert sylara_leafweaver_stat_block.hit_points == 380
    assert sylara_leafweaver_stat_block.armor_class == 20
    assert sylara_leafweaver_stat_block.speed == "40 ft."
    assert sylara_leafweaver_stat_block.abilities.strength == 22
    assert sylara_leafweaver_stat_block.saving_throws.strength == 11
    assert "Performance +18" in sylara_leafweaver_stat_block.skills
    assert sylara_leafweaver_stat_block.damage_resistances == "thunder"
    assert sylara_leafweaver_stat_block.condition_immunities == "none"
    assert sylara_leafweaver_stat_block.senses == "darkvision 60 ft., passive Perception 19"
    assert sylara_leafweaver_stat_block.languages == "Giant, Common, Elvish"
    assert sylara_leafweaver_stat_block.challenge == 20
    assert (
        "Bardic Inspiration (d12, 5/Day): Sylara can use a bonus action to give one creature within 60 feet an inspiration die."
        in sylara_leafweaver_stat_block.special_abilities
    )
    assert (
        sylara_leafweaver_stat_block.legendary_actions["Detect"]
        == "Sylara makes a Wisdom (Perception) check."
    )
    assert (
        sylara_leafweaver_stat_block.actions[0]
        == "Multiattack: Sylara makes two attacks with her Rapier."
    )
    assert (
        sylara_leafweaver_stat_block.actions[1]
        == "Rapier: Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 15 (2d8 + 6) piercing damage."
    )
    # No bonus actions defined, but including an empty check
    assert sylara_leafweaver_stat_block.bonus_actions == []
    assert (
        sylara_leafweaver_stat_block.reactions[0]
        == "Cutting Words: When a creature Sylara can see within 60 feet makes an attack roll, ability check, or damage roll, she can use her reaction to expend one use of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature’s roll."
    )


@pytest.fixture
def thalia_rock_carver_stat_block():
    # Fixture to provide a sample instance of LegendaryGiantStatBlock for testing
    return LegendaryGiantStatBlock(**legendary_giants.thalia_rock_carver_custom_stat_block)

def test_thalia_rock_carver_stat_block(thalia_rock_carver_stat_block):
    # Check if the Thalia Rock-Carver StatBlock instance is created correctly
    assert thalia_rock_carver_stat_block.name == "Thalia Rock-Carver"
    assert thalia_rock_carver_stat_block.hit_points == 400
    assert thalia_rock_carver_stat_block.armor_class == 22
    assert thalia_rock_carver_stat_block.speed == "40 ft."
    assert thalia_rock_carver_stat_block.abilities.strength == 24
    assert thalia_rock_carver_stat_block.saving_throws.strength == 12
    assert "Insight +11" in thalia_rock_carver_stat_block.skills
    assert thalia_rock_carver_stat_block.damage_resistances == "bludgeoning, piercing, and slashing from nonmagical attacks"
    assert thalia_rock_carver_stat_block.condition_immunities == "none"
    assert thalia_rock_carver_stat_block.senses == "darkvision 60 ft., passive Perception 21"
    assert thalia_rock_carver_stat_block.languages == "Giant, Common, Terran"
    assert thalia_rock_carver_stat_block.challenge == 20
    assert (
        "Divine Intervention (1/Day): Thalia can call on her deity to intervene on her behalf when her need is great."
        in thalia_rock_carver_stat_block.special_abilities
    )
    assert (
        thalia_rock_carver_stat_block.legendary_actions["Detect"]
        == "Thalia makes a Wisdom (Perception) check."
    )
    assert (
        thalia_rock_carver_stat_block.actions[0]
        == "Multiattack: Thalia makes two attacks with her Warhammer."
    )
    assert (
        thalia_rock_carver_stat_block.actions[1]
        == "Warhammer: Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage."
    )
    # No bonus actions defined, but including an empty check
    assert thalia_rock_carver_stat_block.bonus_actions == []
    assert (
        thalia_rock_carver_stat_block.reactions[0]
        == "Stone Wall: Thalia can use her reaction to create a wall of stone that provides cover to her allies within 30 feet."
    )
