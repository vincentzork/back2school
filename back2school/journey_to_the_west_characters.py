from typing import List

import json

from .stat_block_base import StatBlockBase
from .directories import data

with open(data("journey_to_the_west_characters.json")) as f:
    journey_to_the_west_characters = json.load(f)


sun_wukong_custom_stat_block = journey_to_the_west_characters["Sun Wukong"]



class journeytotheWestCharacterStatBlock(StatBlockBase):
    race: str
    actions: List[str]
    bonus_actions: List[str]
    reactions: List[str]
    armor: List[str]

    class Config:
        validate_assignment = True