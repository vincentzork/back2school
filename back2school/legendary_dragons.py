from typing import List, Dict

from pydantic import BaseModel
import json

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows
from .directories import data

with open(data("legendary_dragon_stat_blocks.json")) as f:
    legendary_dragon_stat_blocks = json.load(f)

ashardalon_custom_stat_block = legendary_dragon_stat_blocks["Ashardalon"]
aurgloroasa_custom_stat_block = legendary_dragon_stat_blocks["Aurgloroasa"]
bahamut_custom_stat_block = legendary_dragon_stat_blocks["Bahamut"]
dragotha_custom_stat_block = legendary_dragon_stat_blocks["Dragotha"]
ilnezhara_custom_stat_block = legendary_dragon_stat_blocks["Ilnezhara"]
iymrith_custom_stat_block = legendary_dragon_stat_blocks["Iymrith"]
klauth_custom_stat_block = legendary_dragon_stat_blocks["Klauth"]
niv_mizzet_custom_stat_block = legendary_dragon_stat_blocks["Niv-Mizzet"]
null_custom_stat_block = legendary_dragon_stat_blocks["Null"]
shimmergloom_custom_stat_block = legendary_dragon_stat_blocks["Shimmergloom"]
tazmikella_custom_stat_block = legendary_dragon_stat_blocks["Tazmikella"]
tiamat_custom_stat_block = legendary_dragon_stat_blocks["Tiamat"]
# zundaerazylym_custom_stat_block = legendary_dragon_stat_blocks["Zundaerazylym"]


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
