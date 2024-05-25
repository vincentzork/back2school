import pytest

from back2school.savings_throws import SavingThrows


@pytest.fixture
def saving_throws():
    # Fixture to provide a sample instance of SavingThrows for testing
    return SavingThrows(STR=2, DEX=1, CON=3, INT=0, WIS=2, CHA=1)


def test_saving_throws_initialization(saving_throws):
    # Check if the saving throws are initialized correctly
    assert saving_throws.STR == 2
    assert saving_throws.DEX == 1
    assert saving_throws.CON == 3
    assert saving_throws.INT == 0
    assert saving_throws.WIS == 2
    assert saving_throws.CHA == 1
