from pydantic import BaseModel, Field, constr
import pytest

class AbilityScores(BaseModel):
    strength: int = Field(..., ge=1, le=20)
    dexterity: int = Field(..., ge=1, le=20)
    constitution: int = Field(..., ge=1, le=20)
    intelligence: int = Field(..., ge=1, le=20)
    wisdom: int = Field(..., ge=1, le=20)
    charisma: int = Field(..., ge=1, le=20)

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




def test_ability_scores_initialization():
    # Valid input data
    valid_data = {
        "strength": 18,
        "dexterity": 14,
        "constitution": 16,
        "intelligence": 10,
        "wisdom": 12,
        "charisma": 8
    }
    # Invalid input data with one score out of bounds
    invalid_data = valid_data.copy()
    invalid_data["strength"] = 25

    # Test valid input data
    ability_scores_valid = AbilityScores(**valid_data)
    assert ability_scores_valid.dict() == valid_data

    # Test invalid input data
    with pytest.raises(ValueError):
        AbilityScores(**invalid_data)

@pytest.fixture
def ability_scores():
    # Fixture to provide a sample instance of AbilityScores for testing
    return AbilityScores(
        strength=18,
        dexterity=14,
        constitution=16,
        intelligence=10,
        wisdom=12,
        charisma=8
    )

def test_ability_scores_modifiers(ability_scores):
    # Check if the modifiers are calculated correctly
    expected_modifiers = {
        "strength": 4,
        "dexterity": 2,
        "constitution": 3,
        "intelligence": 0,
        "wisdom": 1,
        "charisma": -1
    }

    assert ability_scores.modifiers == expected_modifiers
