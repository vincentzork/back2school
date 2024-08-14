from typing import List

import json

from .stat_block_base import StatBlockBase
from .directories import data

with open(data("legendary_goblinoid_stat_blocks.json")) as f:
    legendary_goblinoid_stat_blocks = json.load(f)

kharza_the_ravager_custom_stat_block = legendary_goblinoid_stat_blocks["Kharza"]
vorgath_the_bloodhowler_custom_stat_block = legendary_goblinoid_stat_blocks["Vorgath"]
general_kazrak_ironblood_custom_stat_block = legendary_goblinoid_stat_blocks["Kazrak"]
thalrak_the_unyielding_custom_stat_block = legendary_goblinoid_stat_blocks["Thalrak"]
morgath_the_red_custom_stat_block = legendary_goblinoid_stat_blocks["Morgath"]
rikard_the_shadowblade_custom_stat_block = legendary_goblinoid_stat_blocks["Rikard"]
skragg_the_warcaller_custom_stat_block = legendary_goblinoid_stat_blocks["Skragg"]
grishna_the_firestarter_custom_stat_block = legendary_goblinoid_stat_blocks["Grishna"]
thorgar_the_silent_hunter_custom_stat_block = legendary_goblinoid_stat_blocks["Thorgar"]
gorruk_the_bonebreaker_custom_stat_block = legendary_goblinoid_stat_blocks["Gorruk"]
kragga_the_huntmaster_custom_stat_block = legendary_goblinoid_stat_blocks["Kragga"]
mazrak_the_darkshadow_custom_stat_block = legendary_goblinoid_stat_blocks["Mazrak"]
vorgeth_the_soulflayer_custom_stat_block = legendary_goblinoid_stat_blocks["Vorgeth"]
zorgath_the_bloodhound_custom_stat_block = legendary_goblinoid_stat_blocks["Zorgath"]


class GoblinoidChampionStatBlock(StatBlockBase):
    race: str
    actions: List[str]
    bonus_actions: List[str]
    reactions: List[str]

    class Config:
        validate_assignment = True
