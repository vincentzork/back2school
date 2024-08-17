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


class LegendaryUndeadStatBlock(StatBlockBase):
    legendary_resistances: int
    lair_actions: Optional[List[str]] = None
    regional_effects: Optional[List[str]] = None

    class Config:
        validate_assignment = True
