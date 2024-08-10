from pydantic import BaseModel
from typing import List, Dict, Optional


from .abililty_scores import AbilityScores
from .savings_throws import SavingThrows
from .character_class import CharacterClass


class StatBlockBase(BaseModel):
    character_class: Optional[Dict[str, CharacterClass]] = None
    unique_attacks_weapons: Optional[List[str]] = None
    common_behaviors_actions: Optional[List[str]] = None
    name: str
    hit_points: int
    armor_class: int
    speed: str
    abilities: AbilityScores
    saving_throws: SavingThrows
    skills: List[str]
    damage_resistances: str
    damage_immunities: Optional[str] = None
    condition_immunities: str
    senses: str
    languages: str
    challenge: int
    special_abilities: List[str]
    legendary_actions: Dict[str, str]

    class Config:
        validate_assignment = True
