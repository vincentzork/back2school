from typing import List, Dict

from pydantic import BaseModel
import json

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows
from .directories import data

with open(data("legendary_humanoid_stat_blocks.json")) as f:
    legendary_humanoid_stat_blocks = json.load(f)

gog_the_crusher_custom_stat_block = legendary_humanoid_stat_blocks["Gog"]
bruthazmus_custom_stat_block = legendary_humanoid_stat_blocks["Bruthazmus"]
throgg_custom_stat_block = legendary_humanoid_stat_blocks["Throgg"]
skalmad_custom_stat_block = legendary_humanoid_stat_blocks["Skalmad"]
kargath_custom_stat_block = legendary_humanoid_stat_blocks["Kargath"]
hartusk_custom_stat_block = legendary_humanoid_stat_blocks["Hartusk"]
obould_custom_stat_block = legendary_humanoid_stat_blocks["Obould"]
karzoug_custom_stat_block = legendary_humanoid_stat_blocks["Karzoug"]
sharak_custom_stat_block = legendary_humanoid_stat_blocks["Sharak"]

class CharacterClass(BaseModel):
    class_name: str
    archetype: str
    level: int

class HumanoidChampionStatBlock(BaseModel):
    character_class: Dict[str, CharacterClass]
    unique_attacks_weapons: List[str]
    common_behaviors_actions: List[str]
    race: str
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