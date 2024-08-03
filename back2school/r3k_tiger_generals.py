from typing import List, Dict

from pydantic import BaseModel
import json

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows
from .directories import data

with open(data("tiger_general_stat_blocks.json")) as f:
    tiger_general_stat_blocks = json.load(f)

zhang_fei_custom_stat_block = tiger_general_stat_blocks["Zhang Fei"]
guan_yu_custom_stat_block = tiger_general_stat_blocks["Guan Yu"]
huang_zhong_custom_stat_block = tiger_general_stat_blocks["Huang Zhong"]
zhao_yun_custom_stat_block = tiger_general_stat_blocks["Zhao Yun"]
ma_chao_custom_stat_block = tiger_general_stat_blocks["Ma Chao"]


class CharacterClass(BaseModel):
    class_name: str
    archetype: str
    level: int


class R3KTigerGeneralStatBlock(BaseModel):
    character_class: Dict[str, CharacterClass]
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
