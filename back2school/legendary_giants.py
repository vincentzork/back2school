
from typing import List, Dict

from pydantic import BaseModel
import json

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows
from .directories import data

with open(data("legendary_giant_stat_blocks.json")) as f:
    legendary_giant_stat_blocks = json.load(f)

thane_kayalithica_custom_stat_block = legendary_giant_stat_blocks["Thane Kayalithica"]
king_snurre_ironbelly_custom_stat_block = legendary_giant_stat_blocks["King Snurre Ironbelly"]
queen_neri_custom_stat_block = legendary_giant_stat_blocks["Queen Neri"]
king_hekaton_custom_stat_block = legendary_giant_stat_blocks["King Hekaton"]
chief_nosnra_custom_stat_block = legendary_giant_stat_blocks["Chief Nosnra"]
harshnag_the_grim_custom_stat_block = legendary_giant_stat_blocks["Harshnag the Grim"]
jarl_grugnur_custom_stat_block = legendary_giant_stat_blocks["Jarl Grugnur"]

class CharacterClass(BaseModel):
    class_name: str
    archetype: str
    level: int

class LegendaryGiantStatBlock(BaseModel):
    character_class: Dict[str, CharacterClass]
    unique_attacks_weapons: List[str]
    common_behaviors_actions: List[str]
    giant_type: str
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
