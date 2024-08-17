from typing import List, Optional
import json

from .stat_block_base import StatBlockBase
from .directories import data

with open(data("legendary_undead.json")) as f:
    stat_block_data = json.load(f)

vecna_custom_stat_block = stat_block_data["Vecna"]
strahd_custom_stat_block = stat_block_data["Strahd"]
azalin_custom_stat_block = stat_block_data["Azalin"]
soth_custom_stat_block = stat_block_data["Soth"]
atemu_ra_custom_stat_block = stat_block_data["Atemu-Ra"]
azoth_custom_stat_block = stat_block_data["Azoth"]
khen_zai_custom_stat_block = stat_block_data["Khen-Zai"]
doresain_custom_stat_block = stat_block_data["Doresain"]
morgana_custom_stat_block = stat_block_data["Morgana"]
valen_custom_stat_block = stat_block_data["Valen"]


class LegendaryUndeadStatBlock(StatBlockBase):
    legendary_resistances: int
    lair_actions: Optional[List[str]] = None
    regional_effects: Optional[List[str]] = None

    class Config:
        validate_assignment = True
