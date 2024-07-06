import pytest


from .. import demon

from ..demon import DemonLordStatBlock


@pytest.fixture
def demogorgon_stat_block():
    # Fixture to provide a sample instance of DemonLordStatBlock for testing
    return DemonLordStatBlock(**demon.demogorgon_custom_stat_block)


def test_demogorgon_stat_block(demogorgon_stat_block):
    # Check if the DemogorgonStatBlock instance is created correctly
    assert demogorgon_stat_block.name == "Demogorgon"
    assert demogorgon_stat_block.hit_points == 550
    assert demogorgon_stat_block.armor_class == 26
    assert demogorgon_stat_block.speed == "40 ft, swim 60 ft"
    assert demogorgon_stat_block.abilities.strength == 26
    assert demogorgon_stat_block.saving_throws.strength == 15
    assert "Deception +13" in demogorgon_stat_block.skills
    assert (
        demogorgon_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert demogorgon_stat_block.damage_immunities == "fire, poison"
    assert (
        demogorgon_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert demogorgon_stat_block.senses == "truesight 120 ft., passive Perception 22"
    assert demogorgon_stat_block.languages == "Abyssal, telepathy 120 ft."
    assert demogorgon_stat_block.challenge == 30
    assert "Demogorgon's Madness" in demogorgon_stat_block.special_abilities
    assert (
        demogorgon_stat_block.legendary_actions["Baleful Eye"]
        == "Demogorgon targets one creature he can see within 120 feet of him. The target must succeed on a DC 21 Wisdom saving throw or be affected by the madness of Demogorgon for 1 minute."
    )


@pytest.fixture
def orcus_stat_block():
    # Fixture to provide a sample instance of DemonLordStatBlock for testing
    return DemonLordStatBlock(**demon.orcus_custom_stat_block)


def test_orcus_stat_block(orcus_stat_block):
    # Check if the OrcusStatBlock instance is created correctly
    assert orcus_stat_block.name == "Orcus"
    assert orcus_stat_block.hit_points == 600
    assert orcus_stat_block.armor_class == 25
    assert orcus_stat_block.speed == "30 ft, fly 60 ft"
    assert orcus_stat_block.abilities.strength == 24
    assert orcus_stat_block.saving_throws.strength == 14
    assert "Deception +15" in orcus_stat_block.skills
    assert (
        orcus_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert orcus_stat_block.damage_immunities == "fire, poison"
    assert (
        orcus_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert orcus_stat_block.senses == "truesight 120 ft., passive Perception 20"
    assert orcus_stat_block.languages == "Abyssal, telepathy 120 ft."
    assert orcus_stat_block.challenge == 26
    assert "Death's Gaze" in orcus_stat_block.special_abilities
    assert (
        orcus_stat_block.legendary_actions["Teleport"]
        == "Orcus magically teleports, along with any equipment he is wearing or carrying, up to 120 feet to an unoccupied space he can see."
    )


@pytest.fixture
def grazzt_stat_block():
    # Fixture to provide a sample instance of DemonLordStatBlock for testing
    return DemonLordStatBlock(**demon.grazzt_custom_stat_block)


def test_grazzt_stat_block(grazzt_stat_block):
    # Check if the Graz'ztStatBlock instance is created correctly
    assert grazzt_stat_block.name == "Graz'zt"
    assert grazzt_stat_block.hit_points == 500
    assert grazzt_stat_block.armor_class == 26
    assert grazzt_stat_block.speed == "50 ft, fly 90 ft"
    assert grazzt_stat_block.abilities.strength == 24
    assert grazzt_stat_block.saving_throws.strength == 14
    assert "Deception +14" in grazzt_stat_block.skills
    assert (
        grazzt_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert grazzt_stat_block.damage_immunities == "fire, poison"
    assert (
        grazzt_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert grazzt_stat_block.senses == "truesight 120 ft., passive Perception 14"
    assert grazzt_stat_block.languages == "Abyssal, telepathy 120 ft."
    assert grazzt_stat_block.challenge == 29
    assert "Aura of Command" in grazzt_stat_block.special_abilities
    assert (
        grazzt_stat_block.legendary_actions["Infernal Command"]
        == "Graz'zt commands his minions with unparalleled authority."
    )


@pytest.fixture
def baphomet_stat_block():
    # Fixture to provide a sample instance of DemonLordStatBlock for testing
    return DemonLordStatBlock(**demon.baphomet_custom_stat_block)


def test_baphomet_stat_block(baphomet_stat_block):
    # Check if the BaphometStatBlock instance is created correctly
    assert baphomet_stat_block.name == "Baphomet"
    assert baphomet_stat_block.hit_points == 600
    assert baphomet_stat_block.armor_class == 26
    assert baphomet_stat_block.speed == "40 ft"
    assert baphomet_stat_block.abilities.strength == 26
    assert baphomet_stat_block.saving_throws.strength == 15
    assert "Deception +8" in baphomet_stat_block.skills
    assert (
        baphomet_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert baphomet_stat_block.damage_immunities == "fire, poison"
    assert (
        baphomet_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert baphomet_stat_block.senses == "darkvision 120 ft., passive Perception 19"
    assert baphomet_stat_block.languages == "Abyssal"
    assert baphomet_stat_block.challenge == 23
    assert "Labyrinthine Recall" in baphomet_stat_block.special_abilities
    assert (
        baphomet_stat_block.legendary_actions["Teleport"]
        == "Baphomet magically teleports, along with any equipment he is wearing or carrying, up to 120 feet to an unoccupied space he can see."
    )


@pytest.fixture
def yeenoghu_stat_block():
    # Fixture to provide a sample instance of DemonLordStatBlock for testing
    return DemonLordStatBlock(**demon.yeenoghu_custom_stat_block)


def test_yeenoghu_stat_block(yeenoghu_stat_block):
    # Check if the YeenoghuStatBlock instance is created correctly
    assert yeenoghu_stat_block.name == "Yeenoghu"
    assert yeenoghu_stat_block.hit_points == 650
    assert yeenoghu_stat_block.armor_class == 23
    assert yeenoghu_stat_block.speed == "50 ft"
    assert yeenoghu_stat_block.abilities.strength == 25
    assert yeenoghu_stat_block.saving_throws.strength == 14
    assert "Deception +8" in yeenoghu_stat_block.skills
    assert (
        yeenoghu_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert yeenoghu_stat_block.damage_immunities == "fire, poison"
    assert (
        yeenoghu_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert yeenoghu_stat_block.senses == "darkvision 120 ft., passive Perception 13"
    assert yeenoghu_stat_block.languages == "Abyssal"
    assert yeenoghu_stat_block.challenge == 24
    assert "Rampage" in yeenoghu_stat_block.special_abilities
    assert (
        yeenoghu_stat_block.legendary_actions["Rampage"]
        == "Yeenoghu moves up to his speed and makes one flail attack for each enemy he passes within reach during that movement."
    )


@pytest.fixture
def zariel_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return DemonLordStatBlock(**demon.zariel_custom_stat_block)


def test_zariel_stat_block(zariel_stat_block):
    # Check if the ZarielStatBlock instance is created correctly
    assert zariel_stat_block.name == "Zariel"
    assert zariel_stat_block.hit_points == 580
    assert zariel_stat_block.armor_class == 21
    assert zariel_stat_block.speed == "60 ft, fly 120 ft"
    assert zariel_stat_block.abilities.strength == 26
    assert zariel_stat_block.saving_throws.strength == 15
    assert "Deception +14" in zariel_stat_block.skills
    assert (
        zariel_stat_block.damage_resistances
        == "cold; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert zariel_stat_block.damage_immunities == "fire, poison"
    assert (
        zariel_stat_block.condition_immunities
        == "charmed, exhausted, frightened, poisoned"
    )
    assert zariel_stat_block.senses == "truesight 120 ft., passive Perception 15"
    assert zariel_stat_block.languages == "Infernal, telepathy 120 ft."
    assert zariel_stat_block.challenge == 26
    assert "Angel of War" in zariel_stat_block.special_abilities
    assert (
        zariel_stat_block.legendary_actions["Infernal Command"]
        == "Zariel commands her legions with unparalleled authority."
    )


@pytest.fixture
def fraz_urbluu_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return DemonLordStatBlock(**demon.fraz_urbluu_custom_stat_block)


def test_fraz_urbluu_stat_block(fraz_urbluu_stat_block):
    # Check if the Fraz-Urb'luuStatBlock instance is created correctly
    assert fraz_urbluu_stat_block.name == "Fraz-Urb'luu"
    assert fraz_urbluu_stat_block.hit_points == 550
    assert fraz_urbluu_stat_block.armor_class == 21
    assert fraz_urbluu_stat_block.speed == "30 ft, fly 60 ft"
    assert fraz_urbluu_stat_block.abilities.strength == 22
    assert fraz_urbluu_stat_block.saving_throws.strength == 11
    assert "Deception +15" in fraz_urbluu_stat_block.skills
    assert (
        fraz_urbluu_stat_block.damage_resistances
        == "cold, lightning, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert fraz_urbluu_stat_block.damage_immunities == "poison"
    assert (
        fraz_urbluu_stat_block.condition_immunities == "charmed, frightened, poisoned"
    )
    assert fraz_urbluu_stat_block.senses == "truesight 120 ft., passive Perception 18"
    assert fraz_urbluu_stat_block.languages == "Abyssal, Common, telepathy 120 ft."
    assert fraz_urbluu_stat_block.challenge == 23
    assert "Innate Spellcasting" in fraz_urbluu_stat_block.special_abilities
    assert (
        fraz_urbluu_stat_block.legendary_actions["Teleport"]
        == "Fraz-Urb'luu magically teleports to an unoccupied space he can see within 120 feet."
    )


@pytest.fixture
def juiblex_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return DemonLordStatBlock(**demon.juiblex_custom_stat_block)


def test_juiblex_stat_block(juiblex_stat_block):
    # Check if the JuiblexStatBlock instance is created correctly
    assert juiblex_stat_block.name == "Juiblex"
    assert juiblex_stat_block.hit_points == 600
    assert juiblex_stat_block.armor_class == 18
    assert juiblex_stat_block.speed == "20 ft, swim 40 ft"
    assert juiblex_stat_block.abilities.strength == 25
    assert juiblex_stat_block.saving_throws.strength == 12
    assert "Perception +10" in juiblex_stat_block.skills
    assert (
        juiblex_stat_block.damage_resistances
        == "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert juiblex_stat_block.damage_immunities == "poison"
    assert (
        juiblex_stat_block.condition_immunities
        == "blinded, charmed, deafened, frightened, poisoned, prone"
    )
    assert (
        juiblex_stat_block.senses
        == "blindsight 60 ft., darkvision 120 ft., passive Perception 20"
    )
    assert juiblex_stat_block.languages == "Abyssal, telepathy 120 ft."
    assert juiblex_stat_block.challenge == 24
    assert "Amorphous" in juiblex_stat_block.special_abilities
    assert (
        juiblex_stat_block.legendary_actions["Acidic Tendrils"]
        == "Juiblex makes one attack with its Acidic Tendrils."
    )


@pytest.fixture
def zuggtmoy_stat_block():
    # Fixture to provide a sample instance of ArchdevilStatBlock for testing
    return DemonLordStatBlock(**demon.zuggtmoy_custom_stat_block)


def test_zuggtmoy_stat_block(zuggtmoy_stat_block):
    # Check if the ZuggtmoyStatBlock instance is created correctly
    assert zuggtmoy_stat_block.name == "Zuggtmoy"
    assert zuggtmoy_stat_block.hit_points == 550
    assert zuggtmoy_stat_block.armor_class == 20
    assert zuggtmoy_stat_block.speed == "20 ft"
    assert zuggtmoy_stat_block.abilities.strength == 20
    assert zuggtmoy_stat_block.saving_throws.strength == 10
    assert "Arcana +15" in zuggtmoy_stat_block.skills
    assert (
        zuggtmoy_stat_block.damage_resistances
        == "cold, fire, lightning, bludgeoning, piercing, and slashing from nonmagical attacks"
    )
    assert zuggtmoy_stat_block.damage_immunities == "poison"
    assert (
        zuggtmoy_stat_block.condition_immunities
        == "blinded, charmed, deafened, frightened, poisoned"
    )
    assert (
        zuggtmoy_stat_block.senses
        == "truesight 120 ft., darkvision 120 ft., passive Perception 19"
    )
    assert zuggtmoy_stat_block.languages == "Abyssal, telepathy 120 ft."
    assert zuggtmoy_stat_block.challenge == 26
    assert "Fungal Infestation" in zuggtmoy_stat_block.special_abilities
    assert (
        zuggtmoy_stat_block.legendary_actions["Spore Burst"]
        == "Zuggtmoy releases a burst of toxic spores. Each creature within 10 feet of Zuggtmoy must succeed on a DC 20 Constitution saving throw or take 21 (6d6) poison damage and be poisoned for 1 minute."
    )
