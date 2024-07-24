
from typing import List, Dict

from pydantic import BaseModel

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows

tiamat_custom_stat_block = {
    "Dragon Type": "Unique Dragon",
    "Name": "Tiamat",
    "Hit Points": 615,
    "Armor Class": 25,
    "Speed": "60 ft, fly 120 ft",
    "Abilities": {
        "Strength": 30,
        "Dexterity": 16,
        "Constitution": 30,
        "Intelligence": 26,
        "Wisdom": 26,
        "Charisma": 28
    },
    "Saving Throws": {
        "STR": "+17",
        "DEX": "+13",
        "CON": "+17",
        "INT": "+15",
        "WIS": "+15",
        "CHA": "+16"
    },
    "Skills": [
        "Arcana +15",
        "Deception +16",
        "Insight +15",
        "Intimidation +16",
        "Perception +22",
        "Persuasion +16"
    ],
    "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "acid, cold, fire, lightning, poison",
    "Condition Immunities": "charmed, frightened, poisoned",
    "Senses": "darkvision 240 ft., truesight 120 ft., passive Perception 32",
    "Languages": "all, telepathy 120 ft.",
    "Challenge": 30,
    "Special Abilities": [
        "Legendary Resistance (5/Day): If Tiamat fails a saving throw, she can choose to succeed instead.",
        "Magic Resistance: Tiamat has advantage on saving throws against spells and other magical effects.",
        "Multiple Heads: Tiamat can take one reaction per turn, rather than only one per round. She also has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious.",
        "Regeneration: Tiamat regains 30 hit points at the start of her turn if she has at least 1 hit point.",
        "Innate Spellcasting: Tiamat's spellcasting ability is Charisma (spell save DC 24). She can innately cast the following spells, requiring no material components: 3/day each: divine word, teleport",
        "Legendary Actions: Tiamat can take 5 legendary actions, choosing from the options below."
    ],
    "Actions": {
        "Multiattack": "Tiamat can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "Bite": "Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 32 (4d10 + 10) piercing damage plus 14 (4d6) damage of a type based on the dragon head used: acid (black), lightning (blue), fire (red), poison (green), or cold (white).",
        "Claw": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 22 (4d6 + 10) slashing damage.",
        "Tail": "Melee Weapon Attack: +19 to hit, reach 25 ft., one target. Hit: 24 (4d8 + 10) bludgeoning damage.",
        "Frightful Presence": "Each creature of Tiamat's choice that is within 120 feet of her and aware of her must succeed on a DC 24 Wisdom saving throw or become frightened for 1 minute. A frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if Tiamat is within line of sight, ending the effect on itself on a success.",
        "Breath Weapons (Recharge 5-6)": "Tiamat uses one of the following breath weapons. She can use each breath weapon only once per recharge cycle.",
        "Acid Breath (Black Dragon Head)": "Tiamat exhales acid in a 90-foot line that is 10 feet wide. Each creature in that line must make a DC 27 Dexterity saving throw, taking 88 (16d10) acid damage on a failed save, or half as much damage on a successful one.",
        "Lightning Breath (Blue Dragon Head)": "Tiamat exhales lightning in a 120-foot line that is 10 feet wide. Each creature in that line must make a DC 27 Dexterity saving throw, taking 110 (20d10) lightning damage on a failed save, or half as much damage on a successful one.",
        "Fire Breath (Red Dragon Head)": "Tiamat exhales fire in a 90-foot cone. Each creature in that area must make a DC 27 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one.",
        "Poison Breath (Green Dragon Head)": "Tiamat exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 27 Constitution saving throw, taking 77 (22d6) poison damage on a failed save, or half as much damage on a successful one.",
        "Cold Breath (White Dragon Head)": "Tiamat exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 27 Constitution saving throw, taking 72 (16d8) cold damage on a failed save, or half as much damage on a successful one."
    },
    "Legendary Actions": {
        "Detect": "Tiamat makes a Wisdom (Perception) check.",
        "Tail Attack": "Tiamat makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Tiamat beats her wings. Each creature within 15 ft. of Tiamat must succeed on a DC 25 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Tiamat can then fly up to half her flying speed.",
        "Bite Attack": "Tiamat makes a bite attack with one of her heads.",
        "Claw Attack": "Tiamat makes a claw attack."
    }
}

"""""
bahamut_custom_stat_block = {
    "Dragon Type": "Gold Dragon",
    "Name": "Bahamut",
    "Hit Points": 585,
    "Armor Class": 24,
    "Speed": "60 ft, fly 120 ft",
    "Abilities": {
        "Strength": 30,
        "Dexterity": 16,
        "Constitution": 30,
        "Intelligence": 26,
        "Wisdom": 27,
        "Charisma": 30
    },
    "Saving Throws": {
        "STR": "+17",
        "DEX": "+13",
        "CON": "+17",
        "INT": "+15",
        "WIS": "+16",
        "CHA": "+18"
    },
    "Skills": [
        "Arcana +15",
        "Insight +16",
        "Perception +26",
        "Persuasion +18",
        "Religion +15"
    ],
    "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "radiant, necrotic",
    "Condition Immunities": "charmed, frightened, poisoned",
    "Senses": "darkvision 240 ft., truesight 120 ft., passive Perception 36",
    "Languages": "all, telepathy 120 ft.",
    "Challenge": 30,
    "Special Abilities": [
        "Legendary Resistance (5/Day): If Bahamut fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Bahamut has advantage on saving throws against spells and other magical effects.",
        "Divine Awareness: Bahamut knows if he hears a lie.",
        "Regeneration: Bahamut regains 30 hit points at the start of his turn if he has at least 1 hit point.",
        "Innate Spellcasting: Bahamut's spellcasting ability is Charisma (spell save DC 26). He can innately cast the following spells, requiring no material components: 3/day each: bless, cure wounds (9th level), divine word, holy aura",
        "Legendary Actions: Bahamut can take 5 legendary actions, choosing from the options below."
    ],
    "Actions": {
        "Multiattack": "Bahamut can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "Bite": "Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 32 (4d10 + 10) piercing damage plus 14 (4d6) radiant damage.",
        "Claw": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 22 (4d6 + 10) slashing damage.",
        "Tail": "Melee Weapon Attack: +19 to hit, reach 25 ft., one target. Hit: 24 (4d8 + 10) bludgeoning damage.",
        "Frightful Presence": "Each creature of Bahamut's choice that is within 120 feet of him and aware of him must succeed on a DC 26 Wisdom saving throw or become frightened for 1 minute. A frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if Bahamut is within line of sight, ending the effect on itself on a success.",
        "Radiant Breath (Recharge 5-6)": "Bahamut exhales radiant energy in a 90-foot cone. Each creature in that area must make a DC 27 Dexterity saving throw, taking 91 (26d6) radiant damage on a failed save, or half as much damage on a successful one.",
        "Platinum Aura": "Bahamut radiates a calming aura in a 60-foot radius. Each creature of Bahamut's choice in that area has advantage on saving throws against being charmed or frightened, and other creatures have disadvantage on attack rolls against them."
    },
    "Legendary Actions": {
        "Detect": "Bahamut makes a Wisdom (Perception) check.",
        "Tail Attack": "Bahamut makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Bahamut beats his wings. Each creature within 15 ft. of Bahamut must succeed on a DC 25 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Bahamut can then fly up to half his flying speed.",
        "Bite Attack": "Bahamut makes a bite attack.",
        "Claw Attack": "Bahamut makes a claw attack."
    }
}

"""""

bahamut_custom_stat_block = {
    "dragon_type": "Gold Dragon",
    "name": "Bahamut",
    "hit_points": 585,
    "armor_class": 24,
    "speed": "60 ft, fly 120 ft",
    "abilities": {
        "strength": 30,
        "dexterity": 16,
        "constitution": 30,
        "intelligence": 26,
        "wisdom": 27,
        "charisma": 30
    },
    "saving_throws": {
        "strength": "+17",
        "dexterity": "+13",
        "constitution": "+17",
        "intelligence": "+15",
        "wisdom": "+16",
        "charisma": "+18"
    },
    "skills": [
        "Arcana +15",
        "Insight +16",
        "Perception +26",
        "Persuasion +18",
        "Religion +15"
    ],
    "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "radiant, necrotic",
    "condition_immunities": "charmed, frightened, poisoned",
    "senses": "darkvision 240 ft., truesight 120 ft., passive Perception 36",
    "languages": "all, telepathy 120 ft.",
    "challenge": 30,
    "special_abilities": [
        "Legendary Resistance (5/Day): If Bahamut fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Bahamut has advantage on saving throws against spells and other magical effects.",
        "Divine Awareness: Bahamut knows if he hears a lie.",
        "Regeneration: Bahamut regains 30 hit points at the start of his turn if he has at least 1 hit point.",
        "Innate Spellcasting: Bahamut's spellcasting ability is Charisma (spell save DC 26). He can innately cast the following spells, requiring no material components: 3/day each: bless, cure wounds (9th level), divine word, holy aura",
        "Legendary Actions: Bahamut can take 5 legendary actions, choosing from the options below."
    ],
    "actions": {
        "Multiattack": "Bahamut can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "Bite": "Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 32 (4d10 + 10) piercing damage plus 14 (4d6) radiant damage.",
        "Claw": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 22 (4d6 + 10) slashing damage.",
        "Tail": "Melee Weapon Attack: +19 to hit, reach 25 ft., one target. Hit: 24 (4d8 + 10) bludgeoning damage.",
        "Frightful Presence": "Each creature of Bahamut's choice that is within 120 feet of him and aware of him must succeed on a DC 26 Wisdom saving throw or become frightened for 1 minute. A frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if Bahamut is within line of sight, ending the effect on itself on a success.",
        "Radiant Breath (Recharge 5-6)": "Bahamut exhales radiant energy in a 90-foot cone. Each creature in that area must make a DC 27 Dexterity saving throw, taking 91 (26d6) radiant damage on a failed save, or half as much damage on a successful one.",
        "Platinum Aura": "Bahamut radiates a calming aura in a 60-foot radius. Each creature of Bahamut's choice in that area has advantage on saving throws against being charmed or frightened, and other creatures have disadvantage on attack rolls against them."
    },
    "legendary_actions": {
        "Detect": "Bahamut makes a Wisdom (Perception) check.",
        "Tail Attack": "Bahamut makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Bahamut beats his wings. Each creature within 15 ft. of Bahamut must succeed on a DC 25 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Bahamut can then fly up to half his flying speed.",
        "Bite Attack": "Bahamut makes a bite attack.",
        "Claw Attack": "Bahamut makes a claw attack."
    }
}


shimmergloom_custom_stat_block = {
    "Dragon Type": "Shadow Dragon",
    "Name": "Shimmergloom",
    "Hit Points": 370,
    "Armor Class": 21,
    "Speed": "60 ft, fly 80 ft",
    "Abilities": {
        "Strength": 23,
        "Dexterity": 18,
        "Constitution": 25,
        "Intelligence": 18,
        "Wisdom": 17,
        "Charisma": 20
    },
    "Saving Throws": {
        "STR": "+13",
        "DEX": "+11",
        "CON": "+14",
        "INT": "+10",
        "WIS": "+10",
        "CHA": "+12"
    },
    "Skills": [
        "Perception +17",
        "Stealth +18"
    ],
    "Damage Resistances": "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "cold, necrotic",
    "Condition Immunities": "charmed, exhaustion, frightened, poisoned",
    "Senses": "darkvision 240 ft., truesight 120 ft., passive Perception 27",
    "Languages": "Common, Draconic, telepathy 120 ft.",
    "Challenge": 24,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Shimmergloom fails a saving throw, it can choose to succeed instead.",
        "Shadow Stealth: While in dim light or darkness, Shimmergloom can take the Hide action as a bonus action.",
        "Magic Resistance: Shimmergloom has advantage on saving throws against spells and other magical effects."
    ],
    "Actions": {
        "Multiattack": "Shimmergloom makes three attacks: one with its bite and two with its claws.",
        "Bite": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 36 (4d10 + 16) piercing damage plus 14 (4d6) necrotic damage.",
        "Claw": "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 28 (4d6 + 16) slashing damage.",
        "Shadow Breath (Recharge 5-6)": "Shimmergloom exhales shadowy energy in a 90-foot cone. Each creature in that area must make a DC 21 Dexterity saving throw, taking 63 (18d6) necrotic damage on a failed save, or half as much damage on a successful one."
    },
    "Legendary Actions": {
        "Detect": "Shimmergloom makes a Wisdom (Perception) check.",
        "Tail Attack": "Shimmergloom makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Shimmergloom beats its wings. Each creature within 15 feet of it must succeed on a DC 21 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Shimmergloom can then fly up to half its flying speed."
    }
}

ashardalon_custom_stat_block = {
    "Dragon Type": "Red Dragon",
    "Name": "Ashardalon",
    "Hit Points": 500,
    "Armor Class": 21,
    "Speed": "40 ft, fly 80 ft (hover)",
    "Abilities": {
        "Strength": 27,
        "Dexterity": 10,
        "Constitution": 25,
        "Intelligence": 18,
        "Wisdom": 15,
        "Charisma": 22
    },
    "Saving Throws": {
        "STR": "+15",
        "DEX": "+5",
        "CON": "+14",
        "INT": "+10",
        "WIS": "+9",
        "CHA": "+12"
    },
    "Skills": [
        "Perception +16"
    ],
    "Damage Resistances": "fire; bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "none",
    "Condition Immunities": "exhausted, frightened",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 26",
    "Languages": "Common, Draconic",
    "Challenge": 24,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Ashardalon fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Ashardalon has advantage on saving throws against spells and other magical effects.",
        "Fire Breath (Recharge 5-6): Ashardalon exhales fire in a 90-foot cone. Each creature in that area must make a DC 22 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one.",
        "Summon Demons: Ashardalon can summon demons to aid him in battle. He can summon 2d6 dretches, 1d4 babaus, or 1 balor.",
        "Demonic Heart: Ashardalon's heart contains demonic essence, granting him increased physical prowess."
    ],
    "Actions": {
        "Multiattack": "Ashardalon can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "Bite": "Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 34 (4d10 + 13) piercing damage plus 14 (4d6) fire damage.",
        "Claw": "Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 27 (4d6 + 13) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Ashardalon makes a Wisdom (Perception) check.",
        "Tail Attack": "Ashardalon makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Ashardalon beats his wings. Each creature within 15 feet of him must succeed on a DC 23 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Ashardalon can then fly up to half his flying speed."
    }
}

null_custom_stat_block = {
    "Dragon Type": "Shadow Dragon",
    "Name": "Null, The Deathwyrm",
    "Hit Points": 550,
    "Armor Class": 23,
    "Speed": "40 ft, fly 80 ft (hover)",
    "Abilities": {
        "Strength": 24,
        "Dexterity": 12,
        "Constitution": 23,
        "Intelligence": 18,
        "Wisdom": 16,
        "Charisma": 20
    },
    "Saving Throws": {
        "STR": "+14",
        "DEX": "+8",
        "CON": "+13",
        "INT": "+10",
        "WIS": "+9",
        "CHA": "+11"
    },
    "Skills": [
        "Perception +16",
        "Stealth +12"
    ],
    "Damage Resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "necrotic, poison",
    "Condition Immunities": "exhausted, frightened, paralyzed, poisoned",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 26",
    "Languages": "Common, Draconic",
    "Challenge": 26,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Null fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Null has advantage on saving throws against spells and other magical effects.",
        "Shadow Stealth: While in dim light or darkness, Null can take the Hide action as a bonus action.",
        "Necrotic Breath (Recharge 5-6): Null exhales necrotic energy in a 90-foot cone. Each creature in that area must make a DC 23 Dexterity saving throw, taking 84 (24d6) necrotic damage on a failed save, or half as much damage on a successful one.",
        "Life Drain: When Null hits a creature with its bite attack, it can choose to drain life energy. The target must succeed on a DC 23 Constitution saving throw or take 21 (6d6) necrotic damage, and Null regains hit points equal to the damage dealt.",
        "Command Undead: Null can magically command undead creatures within 120 feet of it. Undead creatures must make a DC 23 Wisdom saving throw or be charmed by Null for 24 hours."
    ],
    "Actions": {
        "Multiattack": "Null can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "Bite": "Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 34 (4d10 + 12) piercing damage plus 14 (4d6) necrotic damage. On a hit, Null can use Life Drain.",
        "Claw": "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 27 (4d6 + 12) slashing damage.",
        "Shadow Breath (Recharge 5-6)": "Null exhales shadowy energy in a 90-foot cone. Each creature in that area must make a DC 23 Dexterity saving throw, taking 84 (24d6) necrotic damage on a failed save, or half as much damage on a successful one."
    },
    "Legendary Actions": {
        "Detect": "Null makes a Wisdom (Perception) check.",
        "Tail Attack": "Null makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Null beats his wings. Each creature within 15 feet of him must succeed on a DC 24 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. Null can then fly up to half his flying speed."
    }
}

iymrith_custom_stat_block = {
    "Dragon Type": "Blue Dragon",
    "Name": "Iymrith, the Doom of the Desert",
    "Hit Points": 481,
    "Armor Class": 22,
    "Speed": "40 ft, burrow 40 ft, fly 120 ft",
    "Abilities": {
        "Strength": 27,
        "Dexterity": 10,
        "Constitution": 25,
        "Intelligence": 18,
        "Wisdom": 17,
        "Charisma": 21
    },
    "Saving Throws": {
        "STR": "+16",
        "DEX": "+8",
        "CON": "+14",
        "INT": "+10",
        "WIS": "+11",
        "CHA": "+12"
    },
    "Skills": [
        "Perception +17",
        "Stealth +8"
    ],
    "Damage Immunities": "lightning",
    "Condition Immunities": "exhausted, paralyzed",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
    "Languages": "Common, Draconic",
    "Challenge": 23,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Iymrith fails a saving throw, she can choose to succeed instead.",
        "Magic Resistance: Iymrith has advantage on saving throws against spells and other magical effects.",
        "Electrical Breath (Recharge 5-6): Iymrith exhales lightning in a 90-foot line that is 10 feet wide. Each creature in that line must make a DC 23 Dexterity saving throw, taking 88 (16d10) lightning damage on a failed save, or half as much damage on a successful one.",
        "Spellcasting: Iymrith is a 17th-level spellcaster. Her spellcasting ability is Intelligence (spell save DC 18, +10 to hit with spell attacks). She has the following spells prepared:",
        "- Cantrips (at will): Mage Hand, Shocking Grasp, Thunderclap",
        "- 1st level (4 slots): Thunderwave, Witch Bolt",
        "- 2nd level (3 slots): Gust of Wind, Shatter",
        "- 3rd level (3 slots): Lightning Bolt, Counterspell",
        "- 4th level (3 slots): Storm Sphere, Greater Invisibility",
        "- 5th level (3 slots): Cloudkill, Cone of Cold",
        "- 6th level (1 slot): Chain Lightning"
    ],
    "Actions": {
        "Multiattack": "Iymrith can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "Bite": "Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 36 (4d10 + 16) piercing damage.",
        "Claw": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 28 (4d6 + 16) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Iymrith makes a Wisdom (Perception) check.",
        "Tail Attack": "Iymrith makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Iymrith beats her wings. Each creature within 15 feet of her must succeed on a DC 24 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Iymrith can then fly up to half her flying speed."
    }
}

dragotha_custom_stat_block = {
    "Dragon Type": "Dracolich",
    "Name": "Dragotha",
    "Hit Points": 367,
    "Armor Class": 20,
    "Speed": "40 ft, fly 80 ft (hover)",
    "Abilities": {
        "Strength": 22,
        "Dexterity": 10,
        "Constitution": 20,
        "Intelligence": 18,
        "Wisdom": 15,
        "Charisma": 21
    },
    "Saving Throws": {
        "STR": "+12",
        "DEX": "+6",
        "CON": "+11",
        "INT": "+10",
        "WIS": "+9",
        "CHA": "+11"
    },
    "Skills": [
        "Perception +15"
    ],
    "Damage Resistances": "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "cold, poison",
    "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 25",
    "Languages": "Common, Draconic, plus any three languages",
    "Challenge": 22,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Dragotha fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Dragotha has advantage on saving throws against spells and other magical effects.",
        "Icy Breath (Recharge 5-6): Dragotha exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 21 Constitution saving throw, taking 66 (12d10) cold damage on a failed save, or half as much damage on a successful one.",
        "Spellcasting: Dragotha is a 17th-level spellcaster. His spellcasting ability is Intelligence (spell save DC 18, +10 to hit with spell attacks). He has the following spells prepared:",
        "- Cantrips (at will): Chill Touch, Ray of Frost, Mage Hand",
        "- 1st level (4 slots): Magic Missile, Ray of Sickness",
        "- 2nd level (3 slots): Ray of Enfeeblement, Misty Step",
        "- 3rd level (3 slots): Counterspell, Bestow Curse",
        "- 4th level (3 slots): Blight, Greater Invisibility",
        "- 5th level (3 slots): Cloudkill, Cone of Cold",
        "- 6th level (1 slot): Disintegrate"
    ],
    "Actions": {
        "Multiattack": "Dragotha can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "Bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 23 (3d10 + 7) piercing damage plus 14 (4d6) necrotic damage.",
        "Claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 7) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Dragotha makes a Wisdom (Perception) check.",
        "Tail Attack": "Dragotha makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Dragotha beats his wings. Each creature within 15 feet of him must succeed on a DC 21 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Dragotha can then fly up to half his flying speed."
    }
}

klauth_custom_stat_block = {
    "Dragon Type": "Red Dragon",
    "Name": "Klauth",
    "Hit Points": 546,
    "Armor Class": 24,
    "Speed": "40 ft, burrow 40 ft, fly 80 ft",
    "Abilities": {
        "Strength": 30,
        "Dexterity": 10,
        "Constitution": 28,
        "Intelligence": 18,
        "Wisdom": 15,
        "Charisma": 22
    },
    "Saving Throws": {
        "STR": "+19",
        "DEX": "+9",
        "CON": "+18",
        "INT": "+12",
        "WIS": "+11",
        "CHA": "+14"
    },
    "Skills": [
        "Perception +17",
        "Stealth +9"
    ],
    "Damage Immunities": "fire",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
    "Languages": "Common, Draconic",
    "Challenge": 23,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Klauth fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Klauth has advantage on saving throws against spells and other magical effects.",
        "Fire Breath (Recharge 5-6): Klauth exhales fire in a 90-foot cone. Each creature in that area must make a DC 26 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one.",
        "Spellcasting: Klauth is a 17th-level spellcaster. His spellcasting ability is Charisma (spell save DC 22, +14 to hit with spell attacks). He has the following spells prepared:",
        "- Cantrips (at will): Fire Bolt, Mage Hand, Prestidigitation",
        "- 1st level (4 slots): Burning Hands, Shield",
        "- 2nd level (3 slots): Scorching Ray, Mirror Image",
        "- 3rd level (3 slots): Fireball, Counterspell",
        "- 4th level (3 slots): Wall of Fire, Greater Invisibility",
        "- 5th level (3 slots): Immolation, Cone of Cold",
        "- 6th level (1 slot): Chain Lightning"
    ],
    "Actions": {
        "Multiattack": "Klauth can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "Bite": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 30 (4d6 + 19) piercing damage plus 14 (4d6) fire damage.",
        "Claw": "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 24 (3d8 + 19) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Klauth makes a Wisdom (Perception) check.",
        "Tail Attack": "Klauth makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Klauth beats his wings. Each creature within 15 feet of him must succeed on a DC 27 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Klauth can then fly up to half his flying speed."
    }
}

ilnezhara_custom_stat_block = {
    "Dragon Type": "Green Dragon",
    "Name": "Ilnezhara",
    "Hit Points": 367,
    "Armor Class": 21,
    "Speed": "40 ft, fly 80 ft, swim 40 ft",
    "Abilities": {
        "Strength": 23,
        "Dexterity": 14,
        "Constitution": 21,
        "Intelligence": 18,
        "Wisdom": 17,
        "Charisma": 20
    },
    "Saving Throws": {
        "STR": "+12",
        "DEX": "+8",
        "CON": "+11",
        "INT": "+10",
        "WIS": "+9",
        "CHA": "+10"
    },
    "Skills": [
        "Perception +13",
        "Stealth +8",
        "Deception +10",
        "Persuasion +10"
    ],
    "Damage Immunities": "poison",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
    "Languages": "Common, Draconic, Elvish",
    "Challenge": 22,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Ilnezhara fails a saving throw, she can choose to succeed instead.",
        "Magic Resistance: Ilnezhara has advantage on saving throws against spells and other magical effects.",
        "Poison Breath (Recharge 5-6): Ilnezhara exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 20 Constitution saving throw, taking 70 (20d6) poison damage on a failed save, or half as much damage on a successful one.",
        "Spellcasting: Ilnezhara is a 16th-level spellcaster. Her spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). She has the following spells prepared:",
        "- Cantrips (at will): Druidcraft, Poison Spray, Thaumaturgy",
        "- 1st level (4 slots): Entangle, Fog Cloud, Charm Person",
        "- 2nd level (3 slots): Barkskin, Enhance Ability, Pass without Trace",
        "- 3rd level (3 slots): Plant Growth, Protection from Energy, Sleet Storm",
        "- 4th level (3 slots): Blight, Dominate Beast, Greater Invisibility",
        "- 5th level (2 slots): Cloudkill, Insect Plague"
    ],
    "Actions": {
        "Multiattack": "Ilnezhara can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "Bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) poison damage.",
        "Claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Ilnezhara makes a Wisdom (Perception) check.",
        "Tail Attack": "Ilnezhara makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Ilnezhara beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Ilnezhara can then fly up to half her flying speed."
    }
}

tazmikella_custom_stat_block = {
    "Dragon Type": "Green Dragon",
    "Name": "Tazmikella",
    "Hit Points": 367,
    "Armor Class": 21,
    "Speed": "40 ft, fly 80 ft, swim 40 ft",
    "Abilities": {
        "Strength": 23,
        "Dexterity": 14,
        "Constitution": 21,
        "Intelligence": 18,
        "Wisdom": 17,
        "Charisma": 20
    },
    "Saving Throws": {
        "STR": "+12",
        "DEX": "+8",
        "CON": "+11",
        "INT": "+10",
        "WIS": "+9",
        "CHA": "+10"
    },
    "Skills": [
        "Perception +13",
        "Stealth +8",
        "Deception +10",
        "Persuasion +10"
    ],
    "Damage Immunities": "poison",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
    "Languages": "Common, Draconic, Elvish",
    "Challenge": 22,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Tazmikella fails a saving throw, she can choose to succeed instead.",
        "Magic Resistance: Tazmikella has advantage on saving throws against spells and other magical effects.",
        "Poison Breath (Recharge 5-6): Tazmikella exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 20 Constitution saving throw, taking 70 (20d6) poison damage on a failed save, or half as much damage on a successful one.",
        "Spellcasting: Tazmikella is a 16th-level spellcaster. Her spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). She has the following spells prepared:",
        "- Cantrips (at will): Druidcraft, Poison Spray, Thaumaturgy",
        "- 1st level (4 slots): Entangle, Fog Cloud, Charm Person",
        "- 2nd level (3 slots): Barkskin, Enhance Ability, Pass without Trace",
        "- 3rd level (3 slots): Plant Growth, Protection from Energy, Sleet Storm",
        "- 4th level (3 slots): Blight, Dominate Beast, Greater Invisibility",
        "- 5th level (2 slots): Cloudkill, Insect Plague"
    ],
    "Actions": {
        "Multiattack": "Tazmikella can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "Bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) poison damage.",
        "Claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Tazmikella makes a Wisdom (Perception) check.",
        "Tail Attack": "Tazmikella makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Tazmikella beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Tazmikella can then fly up to half her flying speed."
    }
}


aurgloroasa_custom_stat_block = {
    "Dragon Type": "Shadow Dracolich",
    "Name": "Aurgloroasa",
    "Hit Points": 350,
    "Armor Class": 19,
    "Speed": "40 ft, fly 80 ft, swim 40 ft",
    "Abilities": {
        "Strength": 22,
        "Dexterity": 14,
        "Constitution": 21,
        "Intelligence": 18,
        "Wisdom": 17,
        "Charisma": 20
    },
    "Saving Throws": {
        "STR": "+12",
        "DEX": "+8",
        "CON": "+11",
        "INT": "+10",
        "WIS": "+9",
        "CHA": "+10"
    },
    "Skills": [
        "Perception +13",
        "Stealth +8",
        "Deception +10",
        "Arcana +10"
    ],
    "Damage Resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
    "Damage Immunities": "necrotic, poison; bludgeoning, piercing, and slashing from nonmagical attacks",
    "Condition Immunities": "charmed, frightened, paralyzed, poisoned",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
    "Languages": "Common, Draconic, Abyssal",
    "Challenge": 23,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Aurgloroasa fails a saving throw, she can choose to succeed instead.",
        "Magic Resistance: Aurgloroasa has advantage on saving throws against spells and other magical effects.",
        "Life Drain (Recharge 5-6): Aurgloroasa targets one creature she can see within 30 feet of her. The target must succeed on a DC 20 Constitution saving throw or take 45 (10d8) necrotic damage and Aurgloroasa regains hit points equal to the necrotic damage dealt.",
        "Shadow Control: Aurgloroasa can manipulate shadows within 120 feet of her, using them to obscure vision or create areas of darkness as if casting the darkness spell.",
        "Spellcasting: Aurgloroasa is a 16th-level spellcaster. Her spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). She has the following spells prepared:",
        "- Cantrips (at will): Chill Touch, Mage Hand, Minor Illusion",
        "- 1st level (4 slots): Detect Magic, Ray of Sickness, Shield",
        "- 2nd level (3 slots): Blindness/Deafness, Misty Step, Ray of Enfeeblement",
        "- 3rd level (3 slots): Counterspell, Fear, Lightning Bolt",
        "- 4th level (3 slots): Blight, Greater Invisibility, Phantasmal Killer",
        "- 5th level (2 slots): Cloudkill, Dominate Person"
    ],
    "Actions": {
        "Multiattack": "Aurgloroasa can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "Bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) necrotic damage.",
        "Claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Aurgloroasa makes a Wisdom (Perception) check.",
        "Tail Attack": "Aurgloroasa makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Aurgloroasa beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Aurgloroasa can then fly up to half her flying speed."
    }
}

niv_mizzet_custom_stat_block = {
    "Dragon Type": "Ancient Red Dragon (Unique)",
    "Name": "Niv-Mizzet, the Firemind",
    "Hit Points": 546,
    "Armor Class": 22,
    "Speed": "40 ft, fly 80 ft",
    "Abilities": {
        "Strength": 23,
        "Dexterity": 10,
        "Constitution": 21,
        "Intelligence": 26,
        "Wisdom": 17,
        "Charisma": 24
    },
    "Saving Throws": {
        "STR": "+13",
        "DEX": "+6",
        "CON": "+12",
        "INT": "+15",
        "WIS": "+10",
        "CHA": "+14"
    },
    "Skills": [
        "Arcana +15",
        "History +15",
        "Insight +10",
        "Perception +10",
        "Persuasion +14"
    ],
    "Damage Resistances": "fire",
    "Condition Immunities": "charmed, frightened",
    "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 20",
    "Languages": "Common, Draconic, Ravnican, telepathy 120 ft.",
    "Challenge": 26,
    "Special Abilities": [
        "Legendary Resistance (3/Day): If Niv-Mizzet fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Niv-Mizzet has advantage on saving throws against spells and other magical effects.",
        "Fire Breath (Recharge 5-6): Niv-Mizzet exhales fire in a 90-foot cone. Each creature in that area must make a DC 20 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one.",
        "Spellcasting: Niv-Mizzet is an 18th-level spellcaster. His spellcasting ability is Intelligence (spell save DC 23, +15 to hit with spell attacks). He has the following spells prepared:",
        "- Cantrips (at will): Fire Bolt, Mage Hand, Prestidigitation, Shocking Grasp",
        "- 1st level (4 slots): Chromatic Orb, Detect Magic, Feather Fall, Magic Missile",
        "- 2nd level (3 slots): Detect Thoughts, Mirror Image, Scorching Ray",
        "- 3rd level (3 slots): Counterspell, Fireball, Lightning Bolt",
        "- 4th level (3 slots): Fabricate, Greater Invisibility, Ice Storm",
        "- 5th level (3 slots): Cone of Cold, Telekinesis",
        "- 6th level (2 slots): Chain Lightning, Globe of Invulnerability",
        "- 7th level (2 slots): Delayed Blast Fireball, Plane Shift",
        "- 8th level (1 slot): Dominate Monster, Sunburst",
        "- 9th level (1 slot): Meteor Swarm, Wish"
    ],
    "Actions": {
        "Multiattack": "Niv-Mizzet can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "Bite": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage plus 14 (4d6) fire damage.",
        "Claw": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage."
    },
    "Legendary Actions": {
        "Detect": "Niv-Mizzet makes a Wisdom (Perception) check.",
        "Tail Attack": "Niv-Mizzet makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Niv-Mizzet beats his wings. Each creature within 15 feet of him must succeed on a DC 21 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Niv-Mizzet can then fly up to half his flying speed."
    }
}


class LegendaryDragonStatBlock(BaseModel):
    dragon_type: str
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
    actions: Dict[str, str]
    legendary_actions: Dict[str, str]

