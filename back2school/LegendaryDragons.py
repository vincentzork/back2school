
from typing import List, Dict

from pydantic import BaseModel

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows

tiamat_custom_stat_block = {
    "dragon_type": "Unique Dragon",
    "name": "Tiamat",
    "hit_points": 615,
    "armor_class": 25,
    "speed": "60 ft, fly 120 ft",
    "abilities": {
        "strength": 30,
        "dexterity": 16,
        "constitution": 30,
        "intelligence": 26,
        "wisdom": 26,
        "charisma": 28
    },
    "saving_throws": {
        "strength": "+17",
        "dexterity": "+13",
        "constitution": "+17",
        "intelligence": "+15",
        "wisdom": "+15",
        "charisma": "+16"
    },
    "skills": [
        "Arcana +15",
        "Deception +16",
        "Insight +15",
        "Intimidation +16",
        "Perception +22",
        "Persuasion +16"
    ],
    "damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "acid, cold, fire, lightning, poison",
    "condition_immunities": "charmed, frightened, poisoned",
    "senses": "darkvision 240 ft., truesight 120 ft., passive Perception 32",
    "languages": "all, telepathy 120 ft.",
    "challenge": 30,
    "special_abilities": [
        "Legendary Resistance (5/Day): If Tiamat fails a saving throw, she can choose to succeed instead.",
        "Magic Resistance: Tiamat has advantage on saving throws against spells and other magical effects.",
        "Multiple Heads: Tiamat can take one reaction per turn, rather than only one per round. She also has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious.",
        "Regeneration: Tiamat regains 30 hit points at the start of her turn if she has at least 1 hit point.",
        "Innate Spellcasting: Tiamat's spellcasting ability is Charisma (spell save DC 24). She can innately cast the following spells, requiring no material components: 3/day each: divine word, teleport",
        "Legendary Actions: Tiamat can take 5 legendary actions, choosing from the options below."
    ],
    "actions": {
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
    "legendary_actions": {
        "Detect": "Tiamat makes a Wisdom (Perception) check.",
        "Tail Attack": "Tiamat makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Tiamat beats her wings. Each creature within 15 ft. of Tiamat must succeed on a DC 25 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Tiamat can then fly up to half her flying speed.",
        "Bite Attack": "Tiamat makes a bite attack with one of her heads.",
        "Claw Attack": "Tiamat makes a claw attack."
    }
}

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
    "dragon_type": "Shadow Dragon",
    "name": "Shimmergloom",
    "hit_points": 370,
    "armor_class": 21,
    "speed": "60 ft, fly 80 ft",
    "abilities": {
        "strength": 23,
        "dexterity": 18,
        "constitution": 25,
        "intelligence": 18,
        "wisdom": 17,
        "charisma": 20
    },
    "saving_throws": {
        "strength": "+13",
        "dexterity": "+11",
        "constitution": "+14",
        "intelligence": "+10",
        "wisdom": "+10",
        "charisma": "+12"
    },
    "skills": [
        "Perception +17",
        "Stealth +18"
    ],
    "damage_resistances": "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "cold, necrotic",
    "condition_immunities": "charmed, exhaustion, frightened, poisoned",
    "senses": "darkvision 240 ft., truesight 120 ft., passive Perception 27",
    "languages": "Common, Draconic, telepathy 120 ft.",
    "challenge": 24,
    "special_abilities": [
        "Legendary Resistance (3/Day): If Shimmergloom fails a saving throw, it can choose to succeed instead.",
        "Shadow Stealth: While in dim light or darkness, Shimmergloom can take the Hide action as a bonus action.",
        "Magic Resistance: Shimmergloom has advantage on saving throws against spells and other magical effects."
    ],
    "actions": {
        "Multiattack": "Shimmergloom makes three attacks: one with its bite and two with its claws.",
        "Bite": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 36 (4d10 + 16) piercing damage plus 14 (4d6) necrotic damage.",
        "Claw": "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 28 (4d6 + 16) slashing damage.",
        "Shadow Breath (Recharge 5-6)": "Shimmergloom exhales shadowy energy in a 90-foot cone. Each creature in that area must make a DC 21 Dexterity saving throw, taking 63 (18d6) necrotic damage on a failed save, or half as much damage on a successful one."
    },
    "legendary_actions": {
        "Detect": "Shimmergloom makes a Wisdom (Perception) check.",
        "Tail Attack": "Shimmergloom makes a tail attack.",
        "Wing Attack (Costs 2 Actions)": "Shimmergloom beats its wings. Each creature within 15 feet of it must succeed on a DC 21 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Shimmergloom can then fly up to half its flying speed."
    }
}

ashardalon_custom_stat_block = {
    "dragon_type": "Red Dragon",
    "name": "Ashardalon",
    "hit_points": 500,
    "armor_class": 21,
    "speed": "40 ft, fly 80 ft (hover)",
    "abilities": {
        "strength": 27,
        "dexterity": 10,
        "constitution": 25,
        "intelligence": 18,
        "wisdom": 15,
        "charisma": 22
    },
    "saving_throws": {
        "strength": "+15",
        "dexterity": "+5",
        "constitution": "+14",
        "intelligence": "+10",
        "wisdom": "+9",
        "charisma": "+12"
    },
    "skills": [
        "Perception +16"
    ],
    "damage_resistances": "fire; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "none",
    "condition_immunities": "exhausted, frightened",
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 26",
    "languages": "Common, Draconic",
    "challenge": 24,
    "special_abilities": [
        "Legendary Resistance (3/Day): If Ashardalon fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Ashardalon has advantage on saving throws against spells and other magical effects.",
        "Fire Breath (Recharge 5-6): Ashardalon exhales fire in a 90-foot cone. Each creature in that area must make a DC 22 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one.",
        "Summon Demons: Ashardalon can summon demons to aid him in battle. He can summon 2d6 dretches, 1d4 babaus, or 1 balor.",
        "Demonic Heart: Ashardalon's heart contains demonic essence, granting him increased physical prowess."
    ],
    "actions": {
        "multiattack": "Ashardalon can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "bite": "Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 34 (4d10 + 13) piercing damage plus 14 (4d6) fire damage.",
        "claw": "Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 27 (4d6 + 13) slashing damage."
    },
    "legendary_actions": {
        "detect": "Ashardalon makes a Wisdom (Perception) check.",
        "tail_attack": "Ashardalon makes a tail attack.",
        "wing_attack (costs 2 actions)": "Ashardalon beats his wings. Each creature within 15 feet of him must succeed on a DC 23 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Ashardalon can then fly up to half his flying speed."
    }
}

null_custom_stat_block = {
    "dragon_type": "Shadow Dragon",
    "name": "Null, The Deathwyrm",
    "hit_points": 550,
    "armor_class": 23,
    "speed": "40 ft, fly 80 ft (hover)",
    "abilities": {
        "strength": 24,
        "dexterity": 12,
        "constitution": 23,
        "intelligence": 18,
        "wisdom": 16,
        "charisma": 20
    },
    "saving_throws": {
        "strength": "+14",
        "dexterity": "+8",
        "constitution": "+13",
        "intelligence": "+10",
        "wisdom": "+9",
        "charisma": "+11"
    },
    "skills": [
        "Perception +16",
        "Stealth +12"
    ],
    "damage_resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "necrotic, poison",
    "condition_immunities": "exhausted, frightened, paralyzed, poisoned",
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 26",
    "languages": "Common, Draconic",
    "challenge": 26,
    "special_abilities": [
        "Legendary Resistance (3/Day): If Null fails a saving throw, he can choose to succeed instead.",
        "Magic Resistance: Null has advantage on saving throws against spells and other magical effects.",
        "Shadow Stealth: While in dim light or darkness, Null can take the Hide action as a bonus action.",
        "Necrotic Breath (Recharge 5-6): Null exhales necrotic energy in a 90-foot cone. Each creature in that area must make a DC 23 Dexterity saving throw, taking 84 (24d6) necrotic damage on a failed save, or half as much damage on a successful one.",
        "Life Drain: When Null hits a creature with its bite attack, it can choose to drain life energy. The target must succeed on a DC 23 Constitution saving throw or take 21 (6d6) necrotic damage, and Null regains hit points equal to the damage dealt.",
        "Command Undead: Null can magically command undead creatures within 120 feet of it. Undead creatures must make a DC 23 Wisdom saving throw or be charmed by Null for 24 hours."
    ],
    "actions": {
        "multiattack": "Null can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "bite": "Melee Weapon Attack: +14 to hit, reach 15 ft., one target. Hit: 34 (4d10 + 12) piercing damage plus 14 (4d6) necrotic damage. On a hit, Null can use Life Drain.",
        "claw": "Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 27 (4d6 + 12) slashing damage.",
        "shadow_breath (recharge 5-6)": "Null exhales shadowy energy in a 90-foot cone. Each creature in that area must make a DC 23 Dexterity saving throw, taking 84 (24d6) necrotic damage on a failed save, or half as much damage on a successful one."
    },
    "legendary_actions": {
        "detect": "Null makes a Wisdom (Perception) check.",
        "tail_attack": "Null makes a tail attack.",
        "wing_attack (costs 2 actions)": "Null beats his wings. Each creature within 15 feet of him must succeed on a DC 24 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. Null can then fly up to half his flying speed."
    }
}


iymrith_custom_stat_block = {
    "dragon_type": "Blue Dragon",
    "name": "Iymrith, the Doom of the Desert",
    "hit_points": 481,
    "armor_class": 22,
    "speed": "40 ft, burrow 40 ft, fly 120 ft",
    "abilities": {
        "strength": 27,
        "dexterity": 10,
        "constitution": 25,
        "intelligence": 18,
        "wisdom": 17,
        "charisma": 21
    },
    "saving_throws": {
        "strength": 16,
        "dexterity": 8,
        "constitution": 14,
        "intelligence": 10,
        "wisdom": 11,
        "charisma": 12
    },
    "skills": [
        "Perception +17",
        "Stealth +8"
    ],
    "damage_resistances": "",
    "damage_immunities": "lightning",
    "condition_immunities": "exhausted, paralyzed",
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
    "languages": "Common, Draconic",
    "challenge": 23,
    "special_abilities": [
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
    "actions": {
        "multiattack": "Iymrith can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "bite": "Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 36 (4d10 + 16) piercing damage.",
        "claw": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 28 (4d6 + 16) slashing damage."
    },
    "legendary_actions": {
        "detect": "Iymrith makes a Wisdom (Perception) check.",
        "tail_attack": "Iymrith makes a tail attack.",
        "wing_attack (costs 2 actions)": "Iymrith beats her wings. Each creature within 15 feet of her must succeed on a DC 24 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Iymrith can then fly up to half her flying speed."
    }
}


dragotha_custom_stat_block = {
    "dragon_type": "Dracolich",
    "name": "Dragotha",
    "hit_points": 367,
    "armor_class": 20,
    "speed": "40 ft, fly 80 ft (hover)",
    "abilities": {
        "strength": 22,
        "dexterity": 10,
        "constitution": 20,
        "intelligence": 18,
        "wisdom": 15,
        "charisma": 21
    },
    "saving_throws": {
        "strength": "+12",
        "dexterity": "+6",
        "constitution": "+11",
        "intelligence": "+10",
        "wisdom": "+9",
        "charisma": "+11"
    },
    "skills": [
        "Perception +15"
    ],
    "damage_resistances": "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "cold, poison",
    "condition_immunities": "charmed, exhausted, frightened, paralyzed, poisoned",
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 25",
    "languages": "Common, Draconic, plus any three languages",
    "challenge": 22,
    "special_abilities": [
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
    "actions": {
        "multiattack": "Dragotha can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 23 (3d10 + 7) piercing damage plus 14 (4d6) necrotic damage.",
        "claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 7) slashing damage."
    },
    "legendary_actions": {
        "detect": "Dragotha makes a Wisdom (Perception) check.",
        "tail_attack": "Dragotha makes a tail attack.",
        "wing_attack (costs 2 actions)": "Dragotha beats his wings. Each creature within 15 feet of him must succeed on a DC 21 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Dragotha can then fly up to half his flying speed."
    }
}


klauth_custom_stat_block = {
    "dragon_type": "Red Dragon",
    "name": "Klauth",
    "hit_points": 546,
    "armor_class": 24,
    "speed": "40 ft, burrow 40 ft, fly 80 ft",
    "abilities": {
        "strength": 30,
        "dexterity": 10,
        "constitution": 28,
        "intelligence": 18,
        "wisdom": 15,
        "charisma": 22
    },
    "saving_throws": {
        "strength": "+19",
        "dexterity": "+9",
        "constitution": "+18",
        "intelligence": "+12",
        "wisdom": "+11",
        "charisma": "+14"
    },
    "skills": [
        "Perception +17",
        "Stealth +9"
    ],
    "damage_resistances": "",  # Add appropriate resistances if any
    "damage_immunities": "fire",
    "condition_immunities": "",  # Add appropriate condition immunities if any
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
    "languages": "Common, Draconic",
    "challenge": 23,
    "special_abilities": [
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
    "actions": {
        "multiattack": "Klauth can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "bite": "Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 30 (4d6 + 19) piercing damage plus 14 (4d6) fire damage.",
        "claw": "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 24 (3d8 + 19) slashing damage."
    },
    "legendary_actions": {
        "detect": "Klauth makes a Wisdom (Perception) check.",
        "tail_attack": "Klauth makes a tail attack.",
        "wing_attack (costs 2 actions)": "Klauth beats his wings. Each creature within 15 feet of him must succeed on a DC 27 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Klauth can then fly up to half his flying speed."
    }
}


ilnezhara_custom_stat_block = {
    "dragon_type": "Green Dragon",
    "name": "Ilnezhara",
    "hit_points": 367,
    "armor_class": 21,
    "speed": "40 ft, fly 80 ft, swim 40 ft",
    "abilities": {
        "strength": 23,
        "dexterity": 14,
        "constitution": 21,
        "intelligence": 18,
        "wisdom": 17,
        "charisma": 20
    },
    "saving_throws": {
        "strength": "+12",
        "dexterity": "+8",
        "constitution": "+11",
        "intelligence": "+10",
        "wisdom": "+9",
        "charisma": "+10"
    },
    "skills": [
        "Perception +13",
        "Stealth +8",
        "Deception +10",
        "Persuasion +10"
    ],
    "damage_resistances": "",  # Add appropriate resistances if any
    "damage_immunities": "poison",
    "condition_immunities": "",  # Add appropriate condition immunities if any
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
    "languages": "Common, Draconic, Elvish",
    "challenge": 22,
    "special_abilities": [
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
    "actions": {
        "multiattack": "Ilnezhara can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) poison damage.",
        "claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    },
    "legendary_actions": {
        "detect": "Ilnezhara makes a Wisdom (Perception) check.",
        "tail_attack": "Ilnezhara makes a tail attack.",
        "wing_attack (costs 2 actions)": "Ilnezhara beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Ilnezhara can then fly up to half her flying speed."
    }
}


tazmikella_custom_stat_block = {
    "dragon_type": "Green Dragon",
    "name": "Tazmikella",
    "hit_points": 367,
    "armor_class": 21,
    "speed": "40 ft, fly 80 ft, swim 40 ft",
    "abilities": {
        "strength": 23,
        "dexterity": 14,
        "constitution": 21,
        "intelligence": 18,
        "wisdom": 17,
        "charisma": 20
    },
    "saving_throws": {
        "strength": "+12",
        "dexterity": "+8",
        "constitution": "+11",
        "intelligence": "+10",
        "wisdom": "+9",
        "charisma": "+10"
    },
    "skills": [
        "Perception +13",
        "Stealth +8",
        "Deception +10",
        "Persuasion +10"
    ],
    "damage_resistances": "",  # Default or appropriate value
    "damage_immunities": "poison",
    "condition_immunities": "",  # Default or appropriate value
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
    "languages": "Common, Draconic, Elvish",
    "challenge": 22,
    "special_abilities": [
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
    "actions": {
        "multiattack": "Tazmikella can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) poison damage.",
        "claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    },
    "legendary_actions": {
        "detect": "Tazmikella makes a Wisdom (Perception) check.",
        "tail_attack": "Tazmikella makes a tail attack.",
        "wing_attack (costs 2 actions)": "Tazmikella beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Tazmikella can then fly up to half her flying speed."
    }
}


aurgloroasa_custom_stat_block = {
    "dragon_type": "Shadow Dragon",
    "name": "Aurgloroasa",
    "hit_points": 350,
    "armor_class": 19,
    "speed": "40 ft, fly 80 ft, swim 40 ft",
    "abilities": {
        "strength": 22,
        "dexterity": 14,
        "constitution": 21,
        "intelligence": 18,
        "wisdom": 17,
        "charisma": 20
    },
    "saving_throws": {
        "strength": 12,
        "dexterity": 8,
        "constitution": 11,
        "intelligence": 10,
        "wisdom": 9,
        "charisma": 10
    },
    "skills": ["Perception +13", "Stealth +8", "Deception +10", "Arcana +10"],
    "damage_resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
    "damage_immunities": "necrotic, poison; bludgeoning, piercing, and slashing from nonmagical attacks",
    "condition_immunities": "charmed, frightened, paralyzed, poisoned",
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
    "languages": "Common, Draconic, Abyssal",
    "challenge": 23,
    "special_abilities": [
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
    "actions": {
        "multiattack": "Aurgloroasa can use her Frightful Presence. She then makes three attacks: one with her bite and two with her claws.",
        "bite": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 14 (4d6) necrotic damage.",
        "claw": "Melee Weapon Attack: +12 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."
    },
    "legendary_actions": {
        "detect": "Aurgloroasa makes a Wisdom (Perception) check.",
        "tail_attack": "Aurgloroasa makes a tail attack.",
        "wing_attack (costs 2 actions)": "Aurgloroasa beats her wings. Each creature within 15 feet of her must succeed on a DC 20 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. Aurgloroasa can then fly up to half her flying speed."
    }
}

niv_mizzet_custom_stat_block = {
    "dragon_type": "Ancient Red Dragon (Unique)",
    "name": "Niv-Mizzet, the Firemind",
    "hit_points": 546,
    "armor_class": 22,
    "speed": "40 ft, fly 80 ft",
    "abilities": {
        "strength": 23,
        "dexterity": 10,
        "constitution": 21,
        "intelligence": 26,
        "wisdom": 17,
        "charisma": 24
    },
    "saving_throws": {
        "strength": 13,
        "dexterity": 6,
        "constitution": 12,
        "intelligence": 15,
        "wisdom": 10,
        "charisma": 14
    },
    "skills": ["Arcana +15", "History +15", "Insight +10", "Perception +10", "Persuasion +14"],
    "damage_resistances": "fire",
    "damage_immunities": "",
    "condition_immunities": "charmed, frightened",
    "senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 20",
    "languages": "Common, Draconic, Ravnican, telepathy 120 ft.",
    "challenge": 26,
    "special_abilities": [
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
    "actions": {
        "multiattack": "Niv-Mizzet can use his Frightful Presence. He then makes three attacks: one with his bite and two with his claws.",
        "bite": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 19 (2d10 + 8) piercing damage plus 14 (4d6) fire damage.",
        "claw": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 15 (2d6 + 8) slashing damage."
    },
    "legendary_actions": {
        "detect": "Niv-Mizzet makes a Wisdom (Perception) check.",
        "tail_attack": "Niv-Mizzet makes a tail attack.",
        "wing_attack (costs 2 actions)": "Niv-Mizzet beats his wings. Each creature within 15 feet of him must succeed on a DC 21 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. Niv-Mizzet can then fly up to half his flying speed."
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

