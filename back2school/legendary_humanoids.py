from typing import List

import json

from .stat_block_base import StatBlockBase
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


class HumanoidChampionStatBlock(StatBlockBase):
    race: str
    actions: List[str]
    bonus_actions: List[str]
    reactions: List[str]

    class Config:
        validate_assignment = True
