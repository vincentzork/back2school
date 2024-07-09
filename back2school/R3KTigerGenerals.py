from typing import List, Dict

from pydantic import BaseModel

from back2school import abililty_scores, savings_throws

zhang_fei_custom_stat_block = {
    "character_class": {
        "primary_class": {
            "class": "Fighter",
            "archetype": "Champion or Battle Master",
            "level": 15
        },
        "secondary_class": {
            "class": "Barbarian",
            "path": "Berserker",
            "level": 5
        }
    },
    "unique_attacks_weapons": ["Serpent Spear"],
    "common_behaviors_actions": [
        "Engaging in fierce combat, often charging into battle with a war cry.",
        "Defending strategic positions, using his strength to hold the line against multiple enemies.",
        "Exhibiting great loyalty and courage, often taking on dangerous tasks to protect his allies."
    ],
    "name": "Zhang Fei",
    "hit_points": 255,
    "armor_class": 18,
    "speed": "30 ft.",
    "abilities": {
        "strength": 20,
        "dexterity": 14,
        "constitution": 20,
        "intelligence": 10,
        "wisdom": 12,
        "charisma": 13,
    },
    "saving_throws": {
        "strength": "+11",
        "dexterity": "+2",
        "constitution": "+11",
        "intelligence": "+0",
        "wisdom": "+1",
        "charisma": "+1",
    },
    "skills": [
        "Athletics +11",
        "Intimidation +7",
        "Survival +7",
        "Perception +7",
    ],
    "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks (while raging)",
    "condition_immunities": "frightened (while raging)",
    "senses": "passive Perception 17",
    "languages": "Common",
    "challenge": 20,
    "special_abilities": [
        "Unyielding Presence: Zhang Fei can use his Action Surge to emit a terrifying battle cry. Enemies within 30 feet must make a DC 15 Wisdom saving throw or become frightened for 1 minute.",
        "Bridge Defender: Zhang Fei gains a +2 bonus to AC and attack rolls when fighting alone against multiple enemies.",
        "Frenzied Attack: While raging, Zhang Fei can make one additional melee weapon attack as a bonus action.",
    ],
    "legendary_actions": {
        "Indomitable": "Zhang Fei can reroll a saving throw that he fails. If he does so, he must use the new roll.",
        "Unyielding Presence (1/Day)": "Zhang Fei can use his Action Surge to emit a terrifying battle cry. Enemies within 30 feet must make a DC 15 Wisdom saving throw or become frightened for 1 minute."
    },
    "actions": [
        "Multiattack: Zhang Fei makes three attacks with his Serpent Spear.",
        "Serpent Spear: Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 1d10+7 (12) piercing damage (or 1d10+10 (15) while raging).",
        "Sword: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d8+3 slashing damage."
    ],
    "bonus_actions": [
        "Rage (4 uses/day)",
        "Second Wind: Zhang Fei can use a bonus action to regain 1d10+15 hit points."
    ],
    "reactions": [
        "Riposte: When a creature misses Zhang Fei with a melee attack, he can use his reaction to make a melee weapon attack against the creature.",
        "Parry: When a creature hits Zhang Fei with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    ]
}

guan_yu_custom_stat_block = {
    "character_class": {
        "primary_class": {
            "class": "Fighter",
            "archetype": "Champion",
            "level": 15
        },
        "secondary_class": {
            "class": "Paladin",
            "oath": "Oath of Devotion",
            "level": 5
        }
    },
    "unique_attacks_weapons": ["Green Dragon Crescent Blade"],
    "common_behaviors_actions": [
        "Exemplifying unwavering loyalty and righteousness, inspiring allies and intimidating foes.",
        "Using the Green Dragon Crescent Blade to devastating effect, cutting through enemies with precision and power.",
        "Protecting allies and leading them with a sense of duty and honor."
    ],
    "name": "Guan Yu",
    "hit_points": 190,
    "armor_class": 20,  # Assuming Plate Armor + Shield
    "speed": "30 ft.",
    "abilities": {
        "strength": 20,
        "dexterity": 14,
        "constitution": 18,
        "intelligence": 12,
        "wisdom": 14,
        "charisma": 18,
    },
    "saving_throws": {
        "strength": "+8",
        "dexterity": "+2",
        "constitution": "+8",
        "intelligence": "+1",
        "wisdom": "+4",
        "charisma": "+8",
    },
    "skills": [
        "Athletics +8",
        "Intimidation +8",
        "Persuasion +8",
        "Insight +4",
    ],
    "damage_resistances": "",
    "condition_immunities": "",
    "senses": "passive Perception 12",
    "languages": "Common",
    "challenge": 20,
    "special_abilities": [
        "Unyielding Justice: Guan Yu can use his Action Surge to invoke a powerful aura of righteousness. Allies within 30 feet gain advantage on saving throws against fear and charm effects for 1 minute.",
        "Aura of Command: Allies within 10 feet of Guan Yu add his Charisma modifier (+4) to their saving throws."
    ],
    "legendary_actions": {},
    "actions": [
        "Multiattack: Guan Yu makes three attacks with his Green Dragon Crescent Blade.",
        "Green Dragon Crescent Blade: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 1d10+5 slashing damage.",
        "Sword: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d8+3 slashing damage."
    ],
    "bonus_actions": [],
    "reactions": [
        "Parry: When a creature hits Guan Yu with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    ]
}


huang_zhong_custom_stat_block = {
    "character_class": {
        "primary_class": {
            "class": "Fighter",
            "archetype": "Battle Master",
            "level": 20
        },
        "secondary_class": None
    },
    "unique_attacks_weapons": ["Longbow"],
    "common_behaviors_actions": [
        "Demonstrating unparalleled archery skills, striking with precision and power.",
        "Leading from the front, inspiring allies with strategic acumen and bravery.",
        "Mastering hand-to-hand combat, displaying unmatched martial prowess."
    ],
    "name": "Huang Zhong",
    "hit_points": 180,
    "armor_class": 18,  # Assuming Chain Mail and Shield
    "speed": "30 ft.",
    "abilities": {
        "strength": 14,
        "dexterity": 20,
        "constitution": 14,
        "intelligence": 12,
        "wisdom": 16,
        "charisma": 12,
    },
    "saving_throws": {
        "strength": "+7",
        "dexterity": "+10",
        "constitution": "+7",
        "intelligence": "+1",
        "wisdom": "+6",
        "charisma": "+1",
    },
    "skills": [
        "Athletics +7",
        "Perception +10",
        "Insight +6",
        "History +5",
    ],
    "damage_resistances": "",
    "condition_immunities": "",
    "senses": "passive Perception 20",
    "languages": "Common",
    "challenge": 20,
    "special_abilities": [
        "Precision Archer: Huang Zhong can make four attacks with his Longbow, adding his Dexterity modifier to the damage rolls.",
        "Tactical Leader: Huang Zhong can use his Action Surge to grant a bonus action to an ally within 30 feet, allowing them to take an additional action."
    ],
    "legendary_actions": {},
    "actions": [
        "Multiattack: Huang Zhong makes four attacks with his Longbow.",
        "Longbow: Ranged Weapon Attack: +10 to hit, range 150/600 ft., one target. Hit: 1d8+5 piercing damage."
    ],
    "bonus_actions": [],
    "reactions": [
        "Parry: When a creature hits Huang Zhong with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    ]
}

zhao_yun_custom_stat_block = {
    "character_class": {
        "primary_class": {
            "class": "Fighter",
            "archetype": "Champion",
            "level": 18
        },
        "secondary_class": {
            "class": "Fighter",
            "archetype": "Cavalier",
            "level": 2
        }
    },
    "unique_attacks_weapons": ["Sword"],
    "common_behaviors_actions": [
        "Demonstrating exceptional martial skills, both on foot and on horseback.",
        "Leading charges and protecting allies with unwavering loyalty.",
        "Using tactical acumen to outmaneuver opponents and control the battlefield."
    ],
    "name": "Zhao Yun",
    "hit_points": 168,
    "armor_class": 20,  # Assuming Plate Armor and Shield
    "speed": "30 ft., mounted 60 ft.",
    "abilities": {
        "strength": 16,
        "dexterity": 14,
        "constitution": 16,
        "intelligence": 12,
        "wisdom": 14,
        "charisma": 12,
    },
    "saving_throws": {
        "strength": "+7",
        "dexterity": "+4",
        "constitution": "+7",
        "intelligence": "+1",
        "wisdom": "+2",
        "charisma": "+1",
    },
    "skills": [
        "Athletics +7",
        "Acrobatics +4",
        "Perception +4",
        "Insight +2",
    ],
    "damage_resistances": "",
    "condition_immunities": "",
    "senses": "passive Perception 14",
    "languages": "Common",
    "challenge": 18,
    "special_abilities": [
        "Combat Superiority: Zhao Yun has 7 superiority dice, which are d10s. He regains all expended superiority dice on a short or long rest.",
        "Second Wind: Once per short rest, Zhao Yun can use a bonus action to regain hit points equal to 1d10 + his fighter level.",
        "Action Surge: Once per short rest, Zhao Yun can take an additional action on his turn."
    ],
    "legendary_actions": {},
    "actions": [
        "Multiattack: Zhao Yun makes three attacks with his sword or two attacks while mounted.",
        "Sword: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d8+3 slashing damage."
    ],
    "bonus_actions": [],
    "reactions": [
        "Parry: When a creature hits Zhao Yun with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    ]
}

ma_chao_custom_stat_block = {
    "character_class": {
        "primary_class": {
            "class": "Fighter",
            "archetype": "Battlemaster",
            "level": 18
        },
        "secondary_class": {
            "class": "Ranger",
            "archetype": "Hunter",
            "level": 2
        }
    },
    "unique_attacks_weapons": ["Bow", "Sword"],
    "common_behaviors_actions": [
        "Demonstrating exceptional martial skills, both on horseback and in ranged combat.",
        "Leading charges and inspiring allies with bravery and tactical acumen.",
        "Utilizing archery and precision attacks to exploit enemy weaknesses."
    ],
    "name": "Ma Chao",
    "hit_points": 180,
    "armor_class": 18,  # Assuming Chain Mail
    "speed": "30 ft., mounted 60 ft.",
    "abilities": {
        "strength": 16,
        "dexterity": 16,
        "constitution": 14,
        "intelligence": 12,
        "wisdom": 14,
        "charisma": 12,
    },
    "saving_throws": {
        "strength": "+7",
        "dexterity": "+7",
        "constitution": "+5",
        "intelligence": "+1",
        "wisdom": "+2",
        "charisma": "+1",
    },
    "skills": [
        "Athletics +7",
        "Acrobatics +3",
        "Animal Handling +2",
        "Perception +2"
    ],
    "damage_resistances": "",
    "condition_immunities": "",
    "senses": "passive Perception 14",
    "languages": "Common",
    "challenge": 18,
    "special_abilities": [
        "Combat Superiority: Ma Chao has 7 superiority dice, which are d8s. He regains all expended superiority dice on a short or long rest.",
        "Second Wind: Once per short rest, Ma Chao can use a bonus action to regain hit points equal to 1d10 + his fighter level.",
        "Primeval Awareness: As a ranger, Ma Chao can sense aberrations, celestials, dragons, elementals, fey, fiends, and undead within 1 mile."
    ],
    "legendary_actions": {},
    "actions": [
        "Multiattack: Ma Chao makes three attacks with his bow or two attacks with his sword.",
        "Sword: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d8+3 slashing damage.",
        "Longbow: Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target. Hit: 1d8+3 piercing damage."
    ],
    "bonus_actions": [],
    "reactions": [
        "Parry: When a creature hits Ma Chao with a melee attack, he can use his reaction to add 4 to his AC against that attack."
    ]
}

class R3KTigerGeneralStatBlock(BaseModel):
    character_class: Dict[str, Dict[str, str]]
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
    condition_immunities: str
    senses: str
    languages: str
    challenge: int
    special_abilities: List[str]
    legendary_actions: Dict[str, str]
    actions: List[str]
    bonus_actions: List[str]
    reactions: List[str]