from typing import List

import json

from .stat_block_base import StatBlockBase
from .directories import data

with open(data("tiger_general_stat_blocks.json")) as f:
    tiger_general_stat_blocks = json.load(f)

zhang_fei_custom_stat_block = tiger_general_stat_blocks["Zhang Fei"]
guan_yu_custom_stat_block = tiger_general_stat_blocks["Guan Yu"]
huang_zhong_custom_stat_block = tiger_general_stat_blocks["Huang Zhong"]
zhao_yun_custom_stat_block = tiger_general_stat_blocks["Zhao Yun"]
ma_chao_custom_stat_block = tiger_general_stat_blocks["Ma Chao"]


class R3KTigerGeneralStatBlock(StatBlockBase):
    actions: List[str]
    bonus_actions: List[str]
    reactions: List[str]

    class Config:
        validate_assignment = True
