from typing import List

import json

from .stat_block_base import StatBlockBase
from .directories import data

with open(data("legendary_giant_stat_blocks.json")) as f:
    legendary_giant_stat_blocks = json.load(f)

thane_kayalithica_custom_stat_block = legendary_giant_stat_blocks["Thane Kayalithica"]
king_snurre_ironbelly_custom_stat_block = legendary_giant_stat_blocks[
    "King Snurre Ironbelly"
]
queen_neri_custom_stat_block = legendary_giant_stat_blocks["Queen Neri"]
king_hekaton_custom_stat_block = legendary_giant_stat_blocks["King Hekaton"]
chief_nosnra_custom_stat_block = legendary_giant_stat_blocks["Chief Nosnra"]
harshnag_the_grim_custom_stat_block = legendary_giant_stat_blocks["Harshnag the Grim"]
jarl_grugnur_custom_stat_block = legendary_giant_stat_blocks["Jarl Grugnur"]
sylara_leafweaver_custom_stat_block = legendary_giant_stat_blocks["Sylara Leafweaver"]
thalia_rock_carver_custom_stat_block = legendary_giant_stat_blocks["Thalia Rock-Carver"]
vaald_the_wise_custom_stat_block = legendary_giant_stat_blocks["Vaald the Wise"]
morak_thunderstep_custom_stat_block = legendary_giant_stat_blocks["Morak Thunderstep"]
wiggan_nettlebee_custom_stat_block = legendary_giant_stat_blocks["Wiggan Nettlebee"]
tartha_bear_slayer_custom_stat_block = legendary_giant_stat_blocks["Tartha Bear-Slayer"]


class LegendaryGiantStatBlock(StatBlockBase):
    giant_type: str
    actions: List[str]
    bonus_actions: List[str]
    reactions: List[str]

    class Config:
        validate_assignment = True
