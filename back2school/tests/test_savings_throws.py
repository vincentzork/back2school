import pytest

from back2school.savings_throws import SavingThrows


@pytest.fixture
def saving_throws():
    # Fixture to provide a sample instance of SavingThrows for testing
    return SavingThrows(
        strength=2,
        dexterity=1,
        constitution=3,
        intelligence=0,
        wisdom=2,
        charisma=1
    )

def test_saving_throws_initialization(saving_throws):
    # Check if the saving throws are initialized correctly
    assert saving_throws.strength == 2
    assert saving_throws.dexterity == 1
    assert saving_throws.constitution == 3
    assert saving_throws.intelligence == 0
    assert saving_throws.wisdom == 2
    assert saving_throws.charisma == 1
