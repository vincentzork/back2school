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
