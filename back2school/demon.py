from typing import List, Dict

from pydantic import BaseModel

from back2school import abililty_scores, savings_throws

demogorgon_custom_stat_block = {
    "unique_attacks_weapons": ["Twin Tentacle Strike", "Bite", "Tail Whip"],
    "common_behaviors_actions": [
        "Sowing discord and chaos among mortal realms.",
        "Manipulating cults and followers to serve his whims.",
        "Engaging in political intrigue and power struggles within the Abyss.",
    ],
    "name": "Demogorgon",
    "hit_points": 550,
    "armor_class": 26,
    "speed": "40 ft, swim 60 ft",
    "abilities": {
        "strength": 26,
        "dexterity": 14,
        "constitution": 24,
        "intelligence": 20,
        "wisdom": 22,
        "charisma": 24,
    },
    "saving_throws": {
        "strength": "+15",
        "dexterity": "+8",
        "constitution": "+14",
        "intelligence": "+10",
        "wisdom": "+11",
        "charisma": "+13",
    },
    "skills": [
        "Arcana +10",
        "Deception +13",
        "Insight +11",
        "Intimidation +13",
        "Perception +11",
        "Persuasion +13",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 22",
    "languages": "Abyssal, telepathy 120 ft.",
    "challenge": 30,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Demogorgon's Madness",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Baleful Eye": "Demogorgon targets one creature he can see within 120 feet of him. The target must succeed on a DC 21 Wisdom saving throw or be affected by the madness of Demogorgon for 1 minute."
    },
}

orcus_custom_stat_block = {
    "unique_attacks_weapons": ["Death Scythe", "Ghoul Touch"],
    "common_behaviors_actions": [
        "Spreading undeath and necromancy throughout the planes.",
        "Seeking to dominate the undead and increase his own power.",
        "Conducting dark rituals to summon powerful undead creatures.",
    ],
    "name": "Orcus",
    "hit_points": 600,
    "armor_class": 25,
    "speed": "30 ft, fly 60 ft",
    "abilities": {
        "strength": 24,
        "dexterity": 10,
        "constitution": 26,
        "intelligence": 20,
        "wisdom": 20,
        "charisma": 26,
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+5",
        "constitution": "+15",
        "intelligence": "+10",
        "wisdom": "+10",
        "charisma": "+15",
    },
    "skills": [
        "Arcana +10",
        "Deception +15",
        "Insight +10",
        "Intimidation +15",
        "Perception +10",
        "Persuasion +15",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 20",
    "languages": "Abyssal, telepathy 120 ft.",
    "challenge": 26,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Death's Gaze",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Teleport": "Orcus magically teleports, along with any equipment he is wearing or carrying, up to 120 feet to an unoccupied space he can see."
    },
}

grazzt_custom_stat_block = {
    "unique_attacks_weapons": ["Whip of Seduction", "Blade of Deception"],
    "common_behaviors_actions": [
        "Engaging in seduction and manipulation to gain followers and allies.",
        "Scheming and plotting to expand his influence in the Abyss.",
        "Flaunting his wealth and power, often in decadent displays.",
    ],
    "name": "Graz'zt",
    "hit_points": 500,
    "armor_class": 26,
    "speed": "50 ft, fly 90 ft",
    "abilities": {
        "strength": 24,
        "dexterity": 18,
        "constitution": 24,
        "intelligence": 22,
        "wisdom": 18,
        "charisma": 26,
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+10",
        "constitution": "+14",
        "intelligence": "+11",
        "wisdom": "+8",
        "charisma": "+14",
    },
    "skills": [
        "Arcana +11",
        "Deception +14",
        "Insight +8",
        "Intimidation +14",
        "Perception +8",
        "Persuasion +14",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 14",
    "languages": "Abyssal, telepathy 120 ft.",
    "challenge": 29,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Aura of Command",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Graz'zt commands his minions with unparalleled authority."
    },
}

baphomet_custom_stat_block = {
    "unique_attacks_weapons": ["Gore", "Great Axe"],
    "common_behaviors_actions": [
        "Fomenting chaos and violence among the lesser demons and cults.",
        "Seeking to dominate and control labyrinths and mazes.",
        "Engaging in brutal combat and displays of physical strength.",
    ],
    "name": "Baphomet",
    "hit_points": 600,
    "armor_class": 26,
    "speed": "40 ft",
    "abilities": {
        "strength": 26,
        "dexterity": 14,
        "constitution": 24,
        "intelligence": 16,
        "wisdom": 18,
        "charisma": 16,
    },
    "saving_throws": {
        "strength": "+15",
        "dexterity": "+7",
        "constitution": "+14",
        "intelligence": "+8",
        "wisdom": "+9",
        "charisma": "+8",
    },
    "skills": [
        "Arcana +8",
        "Deception +8",
        "Insight +9",
        "Intimidation +8",
        "Perception +9",
        "Persuasion +8",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "darkvision 120 ft., passive Perception 19",
    "languages": "Abyssal",
    "challenge": 23,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Labyrinthine Recall",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Teleport": "Baphomet magically teleports, along with any equipment he is wearing or carrying, up to 120 feet to an unoccupied space he can see."
    },
}

yeenoghu_custom_stat_block = {
    "unique_attacks_weapons": ["Flail of Madness", "Gnoll Horde"],
    "common_behaviors_actions": [
        "Leading hordes of gnolls in raids and pillaging across the Material Plane.",
        "Spreading savagery and madness, inciting bloodlust among his followers.",
        "Corrupting lands and turning them into desolate wastelands.",
    ],
    "name": "Yeenoghu",
    "hit_points": 650,
    "armor_class": 23,
    "speed": "50 ft",
    "abilities": {
        "strength": 25,
        "dexterity": 13,
        "constitution": 24,
        "intelligence": 14,
        "wisdom": 16,
        "charisma": 18,
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+6",
        "constitution": "+14",
        "intelligence": "+5",
        "wisdom": "+7",
        "charisma": "+8",
    },
    "skills": [
        "Arcana +5",
        "Deception +8",
        "Insight +7",
        "Intimidation +8",
        "Perception +7",
        "Persuasion +8",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "darkvision 120 ft., passive Perception 13",
    "languages": "Abyssal",
    "challenge": 24,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Rampage",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Rampage": "Yeenoghu moves up to his speed and makes one flail attack for each enemy he passes within reach during that movement."
    },
}

zariel_custom_stat_block = {
    "unique_attacks_weapons": ["Hellfire Lance", "Sword of Zariel"],
    "common_behaviors_actions": [
        "Leading legions of devils in battles against demons and other enemies.",
        "Imposing order and discipline in the Nine Hells, punishing disobedience.",
        "Seeking to ascend to greater power and challenge the rulership of the Nine Hells.",
    ],
    "name": "Zariel",
    "hit_points": 580,
    "armor_class": 21,
    "speed": "60 ft, fly 120 ft",
    "abilities": {
        "strength": 26,
        "dexterity": 16,
        "constitution": 24,
        "intelligence": 22,
        "wisdom": 20,
        "charisma": 24,
    },
    "saving_throws": {
        "strength": "+15",
        "dexterity": "+8",
        "constitution": "+14",
        "intelligence": "+12",
        "wisdom": "+11",
        "charisma": "+14",
    },
    "skills": [
        "Arcana +12",
        "Deception +14",
        "Insight +11",
        "Intimidation +14",
        "Perception +11",
        "Persuasion +14",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 15",
    "languages": "Infernal, telepathy 120 ft.",
    "challenge": 26,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Angel of War",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Zariel commands her legions with unparalleled authority."
    },
}

fraz_urbluu_custom_stat_block = {
    "Name": "Fraz-Urb'luu",
    "Hit Points": 550,  # Adjust based on desired difficulty
    "Armor Class": 21,  # Reflecting magical defenses
    "Speed": "30 ft, fly 60 ft",
    "Abilities": {
        "Strength": 22,
        "Dexterity": 18,
        "Constitution": 20,
        "Intelligence": 26,
        "Wisdom": 18,
        "Charisma": 30,
    },
    "Saving Throws": {
        "STR": "+11",
        "DEX": "+8",
        "CON": "+10",
        "INT": "+13",
        "WIS": "+8",
        "CHA": "+15",
    },
    "Skills": [
        "Arcana +13",
        "Deception +15",
        "Insight +8",
        "Intimidation +15",
        "Perception +8",
        "Persuasion +15",
    ],
    "Damage Resistances": "cold, lightning, bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "poison",
    "Condition Immunities": "charmed, frightened, poisoned",
    "Senses": "truesight 120 ft., passive Perception 18",
    "Languages": "Abyssal, Common, telepathy 120 ft.",
    "Challenge": 23,
    "Special Abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Teleportation",
        "Psychic Bond",
        "Legendary Resistance",
        "Legendary Actions",
    ],
    "Legendary Actions": {
        "Teleport": "Fraz-Urb'luu magically teleports to an unoccupied space he can see within 120 feet.",
        "Telepathic Command": "Fraz-Urb'luu targets one creature he can see within 120 feet. The target must succeed on a DC 23 Wisdom saving throw or be charmed by Fraz-Urb'luu for 1 minute.",
    },
}

juiblex_custom_stat_block = {
    "Name": "Juiblex",
    "Hit Points": 600,  # Adjust based on desired difficulty
    "Armor Class": 18,  # Reflecting its amorphous form
    "Speed": "20 ft, swim 40 ft",
    "Abilities": {
        "Strength": 25,
        "Dexterity": 8,
        "Constitution": 22,
        "Intelligence": 14,
        "Wisdom": 16,
        "Charisma": 12,
    },
    "Saving Throws": {
        "STR": "+12",
        "DEX": "-1",
        "CON": "+11",
        "INT": "+4",
        "WIS": "+6",
        "CHA": "+3",
    },
    "Skills": ["Perception +10", "Stealth +5"],
    "Damage Resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "poison",
    "Condition Immunities": "blinded, charmed, deafened, frightened, poisoned, prone",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 20",
    "Languages": "Abyssal, telepathy 120 ft.",
    "Challenge": 24,
    "Special Abilities": [
        "Amorphous",
        "Corrosive Aura",
        "Innate Spellcasting",
        "Magic Resistance",
        "Swallow",
        "Legendary Actions",
    ],
    "Legendary Actions": {
        "Acidic Tendrils": "Juiblex makes one attack with its Acidic Tendrils.",
        "Slime Wave (Costs 2 Actions)": "Juiblex creates a wave of acidic slime in a 30-foot cone. Each creature in that area must make a DC 20 Dexterity saving throw, taking 36 (8d8) acid damage on a failed save, or half as much damage on a successful one.",
    },
}

zuggtmoy_custom_stat_block = {
    "Name": "Zuggtmoy",
    "Hit Points": 550,  # Adjust based on desired difficulty
    "Armor Class": 20,  # Reflecting her fungal defenses
    "Speed": "20 ft",
    "Abilities": {
        "Strength": 20,
        "Dexterity": 10,
        "Constitution": 22,
        "Intelligence": 18,
        "Wisdom": 16,
        "Charisma": 24,
    },
    "Saving Throws": {
        "STR": "+10",
        "DEX": "+3",
        "CON": "+11",
        "INT": "+8",
        "WIS": "+9",
        "CHA": "+12",
    },
    "Skills": ["Arcana +15", "Perception +9", "Nature +15", "Stealth +6"],
    "Damage Resistances": "cold, fire, lightning, bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "poison",
    "Condition Immunities": "blinded, charmed, deafened, frightened, poisoned",
    "Senses": "truesight 120 ft., darkvision 120 ft., passive Perception 19",
    "Languages": "Abyssal, telepathy 120 ft.",
    "Challenge": 26,
    "Special Abilities": [
        "Fungal Infestation",
        "Innate Spellcasting",
        "Magic Resistance",
        "Spore Cloud",
        "Legendary Actions",
    ],
    "Legendary Actions": {
        "Spore Burst": "Zuggtmoy releases a burst of toxic spores. Each creature within 10 feet of Zuggtmoy must succeed on a DC 20 Constitution saving throw or take 21 (6d6) poison damage and be poisoned for 1 minute.",
        "Animate Spore Servants": "Zuggtmoy animates up to three dead creatures within 30 feet of her as spore servants under her control for 1 hour.",
    },
}


class DemonLordStatBlock(BaseModel):
    unique_attacks_weapons: List[str]
    common_behaviors_actions: List[str]
    name: str
    hit_points: int
    armor_class: int
    speed: str
    abilities: abililty_scores.AbilityScores
    saving_throws: savings_throws.SavingThrows
    skills: List[str]
    damage_resistances: str
    damage_immunities: str
    condition_immunities: str
    senses: str
    languages: str
    challenge: int
    special_abilities: List[str]
    legendary_actions: Dict[str, str]
