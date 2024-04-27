class Dragon:
    def parse_dice_code(self, dice_code):
        parts = dice_code.split("+")
        num_dice, dice_sides = map(int, parts[0].split("d"))
        modifier = int(parts[1]) if len(parts) > 1 else 0
        return num_dice, dice_sides, modifier
