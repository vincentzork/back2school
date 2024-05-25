from pydantic import BaseModel, Field


class AbilityScores(BaseModel):
    strength: int = Field(..., ge=1)
    dexterity: int = Field(..., ge=1)
    constitution: int = Field(..., ge=1)
    intelligence: int = Field(..., ge=1)
    wisdom: int = Field(..., ge=1)
    charisma: int = Field(..., ge=1)

    @property
    def modifiers(self):
        return {
            "strength": self._calculate_modifier(self.strength),
            "dexterity": self._calculate_modifier(self.dexterity),
            "constitution": self._calculate_modifier(self.constitution),
            "intelligence": self._calculate_modifier(self.intelligence),
            "wisdom": self._calculate_modifier(self.wisdom),
            "charisma": self._calculate_modifier(self.charisma),
        }

    @staticmethod
    def _calculate_modifier(score: int) -> int:
        return (score - 10) // 2

    class Config:
        validate_assignment = True
