from typing import List, Dict

from pydantic import BaseModel

from back2school import abililty_scores, savings_throws




class DemonLordStatBlock(BaseModel):
    unique_attacks_weapons: List[str]
    common_behaviors_actions: List[str]
    name: str
    hit_points: int
    armor_class: int
    speed: str
    abilities: abililty_scores.AbilityScores
    saving_throws: savings_throws.SavingThrows
    skills: List[str]
    damage_resistances: str
    damage_immunities: str
    condition_immunities: str
    senses: str
    languages: str
    challenge: int
    special_abilities: List[str]
    legendary_actions: Dict[str, str]
