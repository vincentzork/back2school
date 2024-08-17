import pytest

from .. import legendary_undead
from ..legendary_undead import LegendaryUndeadStatBlock


@pytest.fixture
def vecna_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Vecna
    return LegendaryUndeadStatBlock(**legendary_undead.vecna_custom_stat_block)


@pytest.fixture
def strahd_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Strahd
    return LegendaryUndeadStatBlock(**legendary_undead.strahd_custom_stat_block)


@pytest.fixture
def azalin_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Azalin
    return LegendaryUndeadStatBlock(**legendary_undead.azalin_custom_stat_block)


@pytest.fixture
def soth_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Lord Soth
    return LegendaryUndeadStatBlock(**legendary_undead.soth_custom_stat_block)


def test_vecna_stat_block(vecna_stat_block):
    # Check if the Vecna StatBlock instance is created correctly
    assert vecna_stat_block.name == "Vecna"
    assert vecna_stat_block.hit_points == 400
    assert vecna_stat_block.armor_class == 22
    assert vecna_stat_block.speed == "30 ft."
    assert vecna_stat_block.abilities.intelligence == 26
    assert vecna_stat_block.saving_throws.intelligence == 18
    assert "Arcana +18" in vecna_stat_block.skills
    assert (
        vecna_stat_block.damage_resistances
        == "necrotic, cold, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        vecna_stat_block.condition_immunities
        == "charmed, frightened, paralyzed, poisoned"
    )
    assert vecna_stat_block.senses == "truesight 120 ft., passive Perception 27"
    assert (
        vecna_stat_block.languages
        == "Common, Draconic, Infernal, Elvish, telepathy 120 ft."
    )
    assert vecna_stat_block.challenge == 26
    assert (
        "Undying Mastery: Vecna can never be truly destroyed as long as his phylactery remains intact."
        in vecna_stat_block.special_abilities
    )
    assert (
        vecna_stat_block.legendary_actions["Cast a Spell"]
        == "Vecna casts one of his prepared spells."
    )
    assert vecna_stat_block.legendary_resistances == 3
    assert (
        "Vecna can cast the spell 'detect magic' without using a spell slot."
        in vecna_stat_block.lair_actions
    )
    assert (
        "Dead creatures within 1 mile of Vecna's lair cannot be resurrected except by wish."
        in vecna_stat_block.regional_effects
    )


def test_strahd_stat_block(strahd_stat_block):
    # Check if the Strahd StatBlock instance is created correctly
    assert strahd_stat_block.name == "Strahd"
    assert strahd_stat_block.hit_points == 300
    assert strahd_stat_block.armor_class == 20
    assert strahd_stat_block.speed == "30 ft., fly 60 ft."
    assert strahd_stat_block.abilities.charisma == 22
    assert strahd_stat_block.saving_throws.charisma == 14
    assert "Persuasion +14" in strahd_stat_block.skills
    assert (
        strahd_stat_block.damage_resistances
        == "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert strahd_stat_block.condition_immunities == "charmed, exhaustion, frightened"
    assert strahd_stat_block.senses == "darkvision 120 ft., passive Perception 22"
    assert strahd_stat_block.languages == "Common, Elvish, Draconic"
    assert strahd_stat_block.challenge == 23
    assert (
        "Shapechanger: Strahd can polymorph into a bat, wolf, or mist."
        in strahd_stat_block.special_abilities
    )
    assert (
        strahd_stat_block.legendary_actions["Move"]
        == "Strahd can move up to his speed without provoking opportunity attacks."
    )
    assert strahd_stat_block.legendary_resistances == 3
    assert (
        "Strahd can summon a swarm of bats or rats to aid him in combat."
        in strahd_stat_block.lair_actions
    )
    assert (
        "The area within 6 miles of Castle Ravenloft is perpetually covered in mist."
        in strahd_stat_block.regional_effects
    )


def test_azalin_stat_block(azalin_stat_block):
    # Check if the Azalin StatBlock instance is created correctly
    assert azalin_stat_block.name == "Azalin"
    assert azalin_stat_block.hit_points == 350
    assert azalin_stat_block.armor_class == 22
    assert azalin_stat_block.speed == "30 ft., fly 60 ft."
    assert azalin_stat_block.abilities.intelligence == 28
    assert azalin_stat_block.saving_throws.intelligence == 20
    assert "Arcana +20" in azalin_stat_block.skills
    assert (
        azalin_stat_block.damage_resistances
        == "necrotic, cold, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        azalin_stat_block.condition_immunities
        == "charmed, frightened, paralyzed, poisoned"
    )
    assert azalin_stat_block.senses == "truesight 120 ft., passive Perception 25"
    assert (
        azalin_stat_block.languages
        == "Common, Draconic, Infernal, Elvish, telepathy 120 ft."
    )
    assert azalin_stat_block.challenge == 24
    assert (
        "Undying Will: Azalin can never be truly destroyed as long as his phylactery remains intact."
        in azalin_stat_block.special_abilities
    )
    assert (
        azalin_stat_block.legendary_actions["Cast a Spell"]
        == "Azalin casts one of his prepared spells."
    )
    assert azalin_stat_block.legendary_resistances == 3
    assert (
        "Azalin can create an anti-magic field in a 30-foot radius around him."
        in azalin_stat_block.lair_actions
    )
    assert (
        "Undead creatures within 1 mile of Azalin's lair gain resistance to necrotic damage."
        in azalin_stat_block.regional_effects
    )


def test_soth_stat_block(soth_stat_block):
    # Check if the Lord Soth StatBlock instance is created correctly
    assert soth_stat_block.name == "Soth"
    assert soth_stat_block.hit_points == 350
    assert soth_stat_block.armor_class == 22
    assert soth_stat_block.speed == "30 ft., fly 60 ft. (on nightmare steed)"
    assert soth_stat_block.abilities.strength == 24
    assert soth_stat_block.saving_throws.strength == 15
    assert "Athletics +15" in soth_stat_block.skills
    assert (
        soth_stat_block.damage_resistances
        == "necrotic, fire, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert soth_stat_block.condition_immunities == "charmed, frightened, poisoned"
    assert soth_stat_block.senses == "darkvision 120 ft., passive Perception 20"
    assert soth_stat_block.languages == "Common, Infernal"
    assert soth_stat_block.challenge == 25
    assert (
        "Aura of Fear: Enemies within 10 feet of Soth must succeed on a DC 18 Wisdom saving throw or be frightened for 1 minute."
        in soth_stat_block.special_abilities
    )
    assert (
        soth_stat_block.legendary_actions["Move"]
        == "Soth can move up to his speed without provoking opportunity attacks."
    )
    assert soth_stat_block.legendary_resistances == 3
    assert (
        "Soth can summon ghostly knights to fight for him."
        in soth_stat_block.lair_actions
    )
    assert (
        "The area within 1 mile of Soth's lair is filled with the sound of distant wailing and screams."
        in soth_stat_block.regional_effects
    )


@pytest.fixture
def atemu_ra_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Atemu-Ra
    return LegendaryUndeadStatBlock(**legendary_undead.atemu_ra_custom_stat_block)


@pytest.fixture
def azoth_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Azoth
    return LegendaryUndeadStatBlock(**legendary_undead.azoth_custom_stat_block)


@pytest.fixture
def khen_zai_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Khen-Zai
    return LegendaryUndeadStatBlock(**legendary_undead.khen_zai_custom_stat_block)


@pytest.fixture
def doresain_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Doresain
    return LegendaryUndeadStatBlock(**legendary_undead.doresain_custom_stat_block)


@pytest.fixture
def morgana_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Morgana
    return LegendaryUndeadStatBlock(**legendary_undead.morgana_custom_stat_block)


@pytest.fixture
def valen_stat_block():
    # Fixture to provide a sample instance of LegendaryUndeadStatBlock for Valen
    return LegendaryUndeadStatBlock(**legendary_undead.valen_custom_stat_block)


def test_atemu_ra_stat_block(atemu_ra_stat_block):
    # Check if the Atemu-Ra StatBlock instance is created correctly
    assert atemu_ra_stat_block.name == "Atemu-Ra"
    assert atemu_ra_stat_block.hit_points == 275
    assert atemu_ra_stat_block.armor_class == 19
    assert atemu_ra_stat_block.speed == "20 ft."
    assert atemu_ra_stat_block.abilities.strength == 20
    assert atemu_ra_stat_block.saving_throws.strength == 10
    assert "Religion +9" in atemu_ra_stat_block.skills
    assert (
        atemu_ra_stat_block.damage_resistances
        == "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        atemu_ra_stat_block.condition_immunities
        == "charmed, frightened, paralyzed, poisoned"
    )
    assert atemu_ra_stat_block.senses == "darkvision 60 ft., passive Perception 20"
    assert atemu_ra_stat_block.languages == "Common, Ancient Osirian"
    assert atemu_ra_stat_block.challenge == 20
    assert (
        "Mummy Rot: Atemu-Ra's touch can inflict a curse that causes the victim's body to wither and rot."
        in atemu_ra_stat_block.special_abilities
    )
    assert (
        atemu_ra_stat_block.legendary_actions["Blinding Sand"]
        == "Atemu-Ra can summon sand to blind his enemies."
    )
    assert atemu_ra_stat_block.legendary_resistances == 3
    assert (
        "Atemu-Ra can animate the dead within his tomb to rise as mummies or skeletons."
        in atemu_ra_stat_block.lair_actions
    )
    assert (
        "The area within 1 mile of Atemu-Ra's tomb is covered in a perpetual sandstorm."
        in atemu_ra_stat_block.regional_effects
    )


def test_azoth_stat_block(azoth_stat_block):
    # Check if the Azoth StatBlock instance is created correctly
    assert azoth_stat_block.name == "Azoth"
    assert azoth_stat_block.hit_points == 250
    assert azoth_stat_block.armor_class == 17
    assert azoth_stat_block.speed == "30 ft."
    assert azoth_stat_block.abilities.strength == 18
    assert azoth_stat_block.saving_throws.strength == 10
    assert "Arcana +9" in azoth_stat_block.skills
    assert (
        azoth_stat_block.damage_resistances
        == "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        azoth_stat_block.condition_immunities
        == "charmed, frightened, paralyzed, poisoned"
    )
    assert azoth_stat_block.senses == "darkvision 60 ft., passive Perception 20"
    assert azoth_stat_block.languages == "Common, Abyssal"
    assert azoth_stat_block.challenge == 21
    assert (
        "Life Drain: Azoth's attacks drain life from his enemies, healing him for the damage dealt."
        in azoth_stat_block.special_abilities
    )
    assert (
        azoth_stat_block.legendary_actions["Shadow Step"]
        == "Azoth can teleport through shadows to an unoccupied space he can see."
    )
    assert azoth_stat_block.legendary_resistances == 3
    assert (
        "Azoth can summon shadows or specters to assist him in combat."
        in azoth_stat_block.lair_actions
    )
    assert (
        "The area within 1 mile of Azoth's lair is cloaked in perpetual darkness."
        in azoth_stat_block.regional_effects
    )


def test_khen_zai_stat_block(khen_zai_stat_block):
    # Check if the Khen-Zai StatBlock instance is created correctly
    assert khen_zai_stat_block.name == "Khen-Zai"
    assert khen_zai_stat_block.hit_points == 225
    assert khen_zai_stat_block.armor_class == 18
    assert khen_zai_stat_block.speed == "0 ft., fly 60 ft. (hover)"
    assert khen_zai_stat_block.abilities.dexterity == 20
    assert khen_zai_stat_block.saving_throws.dexterity == 12
    assert "Arcana +11" in khen_zai_stat_block.skills
    assert (
        khen_zai_stat_block.damage_resistances
        == "necrotic, cold, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        khen_zai_stat_block.condition_immunities
        == "charmed, frightened, grappled, paralyzed, poisoned, prone, restrained"
    )
    assert khen_zai_stat_block.senses == "darkvision 120 ft., passive Perception 20"
    assert khen_zai_stat_block.languages == "Common, Elvish, Infernal"
    assert khen_zai_stat_block.challenge == 22
    assert (
        "Incorporeal Movement: Khen-Zai can move through other creatures and objects as if they were difficult terrain."
        in khen_zai_stat_block.special_abilities
    )
    assert (
        khen_zai_stat_block.legendary_actions["Etherealness"]
        == "Khen-Zai can move into the Ethereal Plane and return to the Material Plane at will."
    )
    assert khen_zai_stat_block.legendary_resistances == 3
    assert (
        "Khen-Zai can cause shadows to animate and attack intruders."
        in khen_zai_stat_block.lair_actions
    )
    assert (
        "The area within 1 mile of Khen-Zai's lair is filled with oppressive gloom, reducing natural light levels by half."
        in khen_zai_stat_block.regional_effects
    )


def test_doresain_stat_block(doresain_stat_block):
    # Check if the Doresain StatBlock instance is created correctly
    assert doresain_stat_block.name == "Doresain"
    assert doresain_stat_block.hit_points == 275
    assert doresain_stat_block.armor_class == 19
    assert doresain_stat_block.speed == "30 ft."
    assert doresain_stat_block.abilities.strength == 20
    assert doresain_stat_block.saving_throws.strength == 11
    assert "Religion +9" in doresain_stat_block.skills
    assert (
        doresain_stat_block.damage_resistances
        == "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        doresain_stat_block.condition_immunities
        == "charmed, frightened, paralyzed, poisoned"
    )
    assert doresain_stat_block.senses == "darkvision 60 ft., passive Perception 20"
    assert doresain_stat_block.languages == "Common, Abyssal, Ghoul"
    assert doresain_stat_block.challenge == 22
    assert (
        "Ghoul's Claw: Doresain's claws can paralyze living creatures with a single strike."
        in doresain_stat_block.special_abilities
    )
    assert (
        doresain_stat_block.legendary_actions["Ravenous Bite"]
        == "Doresain can make an Unholy Bite attack as a legendary action."
    )
    assert doresain_stat_block.legendary_resistances == 3
    assert (
        "Doresain can summon a wave of ghouls to attack intruders."
        in doresain_stat_block.lair_actions
    )
    assert (
        "The area within 1 mile of Doresain's lair is tainted with the stench of death, causing living creatures to become sickened."
        in doresain_stat_block.regional_effects
    )


def test_morgana_stat_block(morgana_stat_block):
    # Check if the Morgana StatBlock instance is created correctly
    assert morgana_stat_block.name == "Morgana"
    assert morgana_stat_block.hit_points == 180
    assert morgana_stat_block.armor_class == 15
    assert morgana_stat_block.speed == "0 ft., fly 40 ft. (hover)"
    assert morgana_stat_block.abilities.charisma == 20
    assert morgana_stat_block.saving_throws.charisma == 12
    assert "Deception +12" in morgana_stat_block.skills
    assert (
        morgana_stat_block.damage_resistances
        == "necrotic, cold, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        morgana_stat_block.condition_immunities
        == "charmed, exhaustion, frightened, grappled, paralyzed, poisoned, prone, restrained"
    )
    assert morgana_stat_block.senses == "darkvision 120 ft., passive Perception 21"
    assert morgana_stat_block.languages == "Common, Elvish, Infernal"
    assert morgana_stat_block.challenge == 16
    assert (
        "Horrifying Visage: Morgana can cause any creature that sees her to become frightened."
        in morgana_stat_block.special_abilities
    )
    assert (
        morgana_stat_block.legendary_actions["Ghostly Presence"]
        == "Morgana can become invisible until she attacks or casts a spell."
    )
    assert morgana_stat_block.legendary_resistances == 3
    assert (
        "Morgana can cause doors and windows to slam shut and lock within her lair."
        in morgana_stat_block.lair_actions
    )
    assert (
        "The area within 1 mile of Morgana's lair is haunted by ghostly apparitions and eerie whispers."
        in morgana_stat_block.regional_effects
    )


def test_valen_stat_block(valen_stat_block):
    # Check if the Valen StatBlock instance is created correctly
    assert valen_stat_block.name == "Valen"
    assert valen_stat_block.hit_points == 200
    assert valen_stat_block.armor_class == 18
    assert valen_stat_block.speed == "0 ft., fly 60 ft. (hover)"
    assert valen_stat_block.abilities.strength == 22
    assert valen_stat_block.saving_throws.strength == 12
    assert "Athletics +12" in valen_stat_block.skills
    assert (
        valen_stat_block.damage_resistances
        == "necrotic, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert (
        valen_stat_block.condition_immunities
        == "charmed, exhaustion, frightened, grappled, paralyzed, poisoned, prone, restrained"
    )
    assert valen_stat_block.senses == "darkvision 120 ft., passive Perception 19"
    assert valen_stat_block.languages == "Common, Celestial"
    assert valen_stat_block.challenge == 18
    assert (
        "Terrifying Glare: Valen can force a creature to make a Wisdom saving throw or be frightened for 1 minute."
        in valen_stat_block.special_abilities
    )
    assert (
        valen_stat_block.legendary_actions["Vengeful Pursuit"]
        == "Valen can move up to his speed towards a target he is pursuing."
    )
    assert valen_stat_block.legendary_resistances == 3
    assert (
        "Valen can summon spectral knights to assist him in battle."
        in valen_stat_block.lair_actions
    )
    assert (
        "The area within 1 mile of Valen's lair is cloaked in an eerie fog that muffles sound."
        in valen_stat_block.regional_effects
    )
