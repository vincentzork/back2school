from typing import Dict

import json

from .stat_block_base import StatBlockBase
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


class LegendaryDragonStatBlock(StatBlockBase):
    dragon_type: str
    actions: Dict[str, str]

    class Config:
        validate_assignment = True
