# Example stat block customization
from typing import List, Dict
from pydantic import BaseModel
import json

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows
from .directories import data

with open(data("devil_stat_blocks.json")) as f:
    devil_stat_blocks = json.load(f)

asmodeus_custom_stat_block = devil_stat_blocks["Asmodeus"]
baalzebul_custom_stat_block = devil_stat_blocks["Baalzebul"]
belial_custom_stat_block = devil_stat_blocks["Belial"]
dispater_custom_stat_block = devil_stat_blocks["Dispater"]
geryon_custom_stat_block = devil_stat_blocks["Geryon"]
mammon_custom_stat_block = devil_stat_blocks["Mammon"]
mephistopheles_custom_stat_block = devil_stat_blocks["Mephistopheles"]


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
