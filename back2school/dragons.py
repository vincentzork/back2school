class Dragon:
    def parse_dice_code(self, dice_code):
        if "+" in dice_code:
            parts = dice_code.split("+")
            num_dice, dice_sides = map(int, parts[0].split("d"))
            modifier = int(parts[1])
        elif "-" in dice_code:
            parts = dice_code.split("-")
            num_dice, dice_sides = map(int, parts[0].split("d"))
            modifier = -int(parts[1])  # Adjust for negative modifier
        else:
            num_dice, dice_sides = map(int, dice_code.split("d"))
            modifier = 0  # No modifier present
        return num_dice, dice_sides, modifier
