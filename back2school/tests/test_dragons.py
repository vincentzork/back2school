# test_dragon.py

from ..chromaticdragons import ChromaticDragon
from ..metallicdragons import MetallicDragon

# def test_calculate_hit_points_consistency():
#     metallic_dragon = MetallicDragon("Silverwing", "Adult", "Silver")
#     chromatic_dragon = ChromaticDragon("Redfang", "Adult", "Red")
#
#     assert metallic_dragon.calculate_hit_points() == chromatic_dragon.calculate_hit_points()


def test_parse_dice_code_consistency():
    metallic_dragon = MetallicDragon("Silverwing", "Adult", "Silver")
    chromatic_dragon = ChromaticDragon("Redfang", "Adult", "Red")

    metallic_dice_code = "10d8+20"
    chromatic_dice_code = "10d8+20"

    metallic_result = metallic_dragon.parse_dice_code(metallic_dice_code)
    chromatic_result = chromatic_dragon.parse_dice_code(chromatic_dice_code)

    assert metallic_result == chromatic_result


def test_metallic_dragon_parse_dice_code():
    metallic_dragon = MetallicDragon("Silverwing", "Adult", "Silver")

    # Example 1: Standard dice code with modifier
    result1 = metallic_dragon.parse_dice_code("10d8+20")
    assert result1 == (10, 8, 20)

    # Example 2: Standard dice code without modifier
    result2 = metallic_dragon.parse_dice_code("15d10")
    assert result2 == (15, 10, 0)

    # Example 3: Dice code with zero modifier
    result3 = metallic_dragon.parse_dice_code("5d6+0")
    assert result3 == (5, 6, 0)

    # Example 4: Dice code with negative modifier
    result4 = metallic_dragon.parse_dice_code("8d12-5")
    assert result4 == (8, 12, -5)

    # Example 5: Dice code with single die
    result5 = metallic_dragon.parse_dice_code("1d4")
    assert result5 == (1, 4, 0)
