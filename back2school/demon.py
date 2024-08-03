from typing import List, Dict

from pydantic import BaseModel
import json

from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows
from .directories import data

with open(data("demon_stat_blocks.json")) as f:
    demon_stat_blocks = json.load(f)

demogorgon_custom_stat_block = demon_stat_blocks["Demogorgon"]
orcus_custom_stat_block = demon_stat_blocks["Orcus"]
grazzt_custom_stat_block = demon_stat_blocks["Graz'zt"]
baphomet_custom_stat_block = demon_stat_blocks["Baphomet"]
yeenoghu_custom_stat_block = demon_stat_blocks["Yeenoghu"]
zariel_custom_stat_block = demon_stat_blocks["Zariel"]
fraz_urbluu_custom_stat_block = demon_stat_blocks["Fraz-Urb'luu"]
juiblex_custom_stat_block = demon_stat_blocks["Juiblex"]
zuggtmoy_custom_stat_block = demon_stat_blocks["Zuggtmoy"]


class DemonLordStatBlock(BaseModel):
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
