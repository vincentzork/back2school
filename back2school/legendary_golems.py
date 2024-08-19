from typing import List

import json

from .stat_block_base import StatBlockBase
from .directories import data

with open(data("legendary_golem_stat_blocks.json")) as f:
    legendary_golem_stat_blocks = json.load(f)

iron_golem_of_acererak_custom_stat_block = legendary_golem_stat_blocks["Iron Golem of Acererak"]
aegis_fang_golem_custom_stat_block = legendary_golem_stat_blocks["Aegis Fang Golem"]
mithral_golem_of_myth_drannor_custom_stat_block = legendary_golem_stat_blocks["Mithral Golem of Myth Drannor"]
adamantine_golem_of_undermountain_custom_stat_block = legendary_golem_stat_blocks["Adamantine Golem of Undermountain"]

class LegendaryGolemStatBlock(StatBlockBase):
    race: str
    actions: List[str]
    bonus_actions: List[str]
    reactions: List[str]

    class Config:
        validate_assignment = True