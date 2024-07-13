# Example stat block customization
from typing import List, Dict

from pydantic import BaseModel

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows

asmodeus_custom_stat_block = {
    "unique_attacks_weapons": ["Infernal Sword", "Hellfire Whip"],
    "common_behaviors_actions": [
        "Manipulative schemes",
        "Deals with mortals and other beings for power",
        "Strategic planning",
        "Master of manipulation and deception",
    ],
    "name": "Asmodeus",
    "hit_points": 500,
    "armor_class": 25,
    "speed": "40 ft, fly 60 ft",
    "abilities": {
        "strength": 24,
        "dexterity": 18,
        "constitution": 26,
        "intelligence": 30,
        "wisdom": 24,
        "charisma": 32,
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+11",
        "constitution": "+15",
        "intelligence": "+17",
        "wisdom": "+14",
        "charisma": "+19",
    },
    "skills": [
        "Arcana +17",
        "Deception +19",
        "Insight +14",
        "Intimidation +19",
        "Perception +14",
        "Persuasion +19",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 24",
    "languages": "all, telepathy 120 ft.",
    "challenge": 30,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Infernal Pact",
        "Infernal Glare",
        "Hellish Rejuvenation",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Asmodeus commands his minions with unparalleled authority."
    },
}

baalzebul_custom_stat_block = {
    "unique_attacks_weapons": ["Pestilent Touch", "Corruption Blade"],
    "common_behaviors_actions": [
        "Deals in secrets, corruption, manipulation",
        "Bargaining, offers deals with a hidden price",
        "Specializes in spreading disease and corruption",
    ],
    "name": "Baalzebul",
    "hit_points": 450,
    "armor_class": 24,
    "speed": "40 ft, fly 60 ft",
    "abilities": {
        "strength": 22,
        "dexterity": 18,
        "constitution": 24,
        "intelligence": 28,
        "wisdom": 22,
        "charisma": 30,
    },
    "saving_throws": {
        "strength": "+13",
        "dexterity": "+11",
        "constitution": "+14",
        "intelligence": "+16",
        "wisdom": "+13",
        "charisma": "+18",
    },
    "skills": [
        "Arcana +16",
        "Deception +18",
        "Insight +13",
        "Intimidation +18",
        "Perception +13",
        "Persuasion +18",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 23",
    "languages": "all, telepathy 120 ft.",
    "challenge": 29,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Corrupting Touch",
        "Hellish Rejuvenation",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Baalzebul commands his minions with unparalleled authority."
    },
}

belial_custom_stat_block = {
    "unique_attacks_weapons": ["Inferno Fist", "Deceptive Blade"],
    "common_behaviors_actions": [
        "Intrigue, seduction, manipulation",
        "Deals with mortals for power",
        "Expert in deception and persuasion",
    ],
    "name": "Belial",
    "hit_points": 480,
    "armor_class": 25,
    "speed": "40 ft, fly 60 ft",
    "abilities": {
        "strength": 24,
        "dexterity": 18,
        "constitution": 25,
        "intelligence": 26,
        "wisdom": 22,
        "charisma": 28,
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+11",
        "constitution": "+15",
        "intelligence": "+15",
        "wisdom": "+13",
        "charisma": "+17",
    },
    "skills": [
        "Arcana +15",
        "Deception +17",
        "Insight +13",
        "Intimidation +17",
        "Perception +13",
        "Persuasion +17",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 23",
    "languages": "all, telepathy 120 ft.",
    "challenge": 28,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Fire Aura",
        "Infernal Command",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Belial commands his minions with unparalleled authority."
    },
}

dispater_custom_stat_block = {
    "common_behaviors_actions": [
        "Master of intrigue and espionage",
        "Deals in secrets and information",
        "Uses spies and manipulative tactics",
    ],
    "unique_attacks_weapons": ["Chains of Dis", "Disintegrator Ray"],
    "name": "Dispater",
    "hit_points": 470,
    "armor_class": 25,
    "speed": "40 ft, fly 60 ft",
    "abilities": {
        "strength": 22,
        "dexterity": 18,
        "constitution": 24,
        "intelligence": 30,
        "wisdom": 22,
        "charisma": 28,
    },
    "saving_throws": {
        "strength": "+13",
        "dexterity": "+11",
        "constitution": "+14",
        "intelligence": "+17",
        "wisdom": "+13",
        "charisma": "+17",
    },
    "skills": [
        "Arcana +17",
        "Deception +17",
        "Insight +13",
        "Intimidation +17",
        "Perception +13",
        "Persuasion +17",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 23",
    "languages": "all, telepathy 120 ft.",
    "challenge": 28,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Lord of Dis",
        "Infernal Regeneration",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Dispater commands his minions with unparalleled authority."
    },
}

mammon_custom_stat_block = {
    "common_behaviors_actions": [
        "Greed, wealth",
        "Deals in trade and commerce",
        "Focuses on hoarding and controlling resources",
    ],
    "unique_attacks_weapons": ["Greed's Grasp", "Golden Scepter"],
    "name": "Mammon",
    "hit_points": 460,
    "armor_class": 24,
    "speed": "40 ft, fly 60 ft",
    "abilities": {
        "strength": 22,
        "dexterity": 18,
        "constitution": 24,
        "intelligence": 28,
        "wisdom": 22,
        "charisma": 30,
    },
    "saving_throws": {
        "strength": "+13",
        "dexterity": "+11",
        "constitution": "+14",
        "intelligence": "+16",
        "wisdom": "+13",
        "charisma": "+18",
    },
    "skills": [
        "Arcana +16",
        "Deception +18",
        "Insight +13",
        "Intimidation +18",
        "Perception +13",
        "Persuasion +18",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 23",
    "languages": "all, telepathy 120 ft.",
    "challenge": 28,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Golden Gaze",
        "Greed's Reward",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Mammon commands his minions with unparalleled authority."
    },
}

mephistopheles_custom_stat_block = {
    "common_behaviors_actions": [
        "Mastery of magic",
        "Deals in contracts and pacts",
        "Specializes in infernal magic and arcane knowledge",
    ],
    "unique_attacks_weapons": ["Hellfire Blast", "Infernal Pactblade"],
    "name": "Mephistopheles",
    "hit_points": 500,
    "armor_class": 26,
    "speed": "40 ft, fly 60 ft",
    "abilities": {
        "strength": 24,
        "dexterity": 18,
        "constitution": 26,
        "intelligence": 30,
        "wisdom": 22,
        "charisma": 32,
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+11",
        "constitution": "+15",
        "intelligence": "+17",
        "wisdom": "+13",
        "charisma": "+19",
    },
    "skills": [
        "Arcana +17",
        "Deception +19",
        "Insight +14",
        "Intimidation +19",
        "Perception +14",
        "Persuasion +19",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 24",
    "languages": "all, telepathy 120 ft.",
    "challenge": 30,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Hellfire Aura",
        "Infernal Rejuvenation",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Mephistopheles commands his minions with unparalleled authority."
    },
}

geryon_custom_stat_block = {
    "unique_attacks_weapons": ["Stygian Horns", "Abyssal Claws"],
    "common_behaviors_actions": [
        "Fear, intimidation",
        "Control over beasts and monsters",
        "Focuses on terrorizing and subjugating enemies",
    ],
    "name": "Geryon",
    "hit_points": 480,
    "armor_class": 25,
    "speed": "40 ft, fly 60 ft",
    "abilities": {
        "strength": 24,
        "dexterity": 18,
        "constitution": 26,
        "intelligence": 22,
        "wisdom": 24,
        "charisma": 28,
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+11",
        "constitution": "+15",
        "intelligence": "+13",
        "wisdom": "+14",
        "charisma": "+17",
    },
    "skills": [
        "Arcana +13",
        "Deception +17",
        "Insight +14",
        "Intimidation +17",
        "Perception +14",
        "Persuasion +17",
    ],
    "damage_resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "fire, poison",
    "condition_immunities": "charmed, exhausted, frightened, poisoned",
    "senses": "truesight 120 ft., passive Perception 24",
    "languages": "all, telepathy 120 ft.",
    "challenge": 29,
    "special_abilities": [
        "Innate Spellcasting",
        "Magic Resistance",
        "Fear Aura",
        "Infernal Regeneration",
        "Legendary Actions",
    ],
    "legendary_actions": {
        "Infernal Command": "Geryon commands his minions with unparalleled authority."
    },
}


devil_stat_blocks = [
    asmodeus_custom_stat_block,
    baalzebul_custom_stat_block,
    belial_custom_stat_block,
    dispater_custom_stat_block,
    geryon_custom_stat_block,
    mammon_custom_stat_block,
    mephistopheles_custom_stat_block,
]
devil_stat_blocks = {devil["name"]: devil for devil in devil_stat_blocks}


class ArchdevilStatBlock(BaseModel):
    unique_attacks_weapons: List[str]
    common_behaviors_actions: List[str]
    name: str
    hit_points: int
    armor_class: int
    speed: str
    abilities: AbilityScores
    saving_throws: SavingThrows
    skills: List[str]
    damage_resistances: str
    damage_immunities: str
    condition_immunities: str
    senses: str
    languages: str
    challenge: int
    special_abilities: List[str]
    legendary_actions: Dict[str, str]
