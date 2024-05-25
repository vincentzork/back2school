import pytest

from back2school.abililty_scores import AbilityScores


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
