import random
import time

from .dragons import Dragon


class MetallicDragon(Dragon):
    def __init__(self, name, age_category, dragon_type):
        self.name = name
        self.age_category = age_category
        self.dragon_type = dragon_type
        self.hit_points = self.calculate_hit_points()
        self.armor_class = self.calculate_armor_class()
        self.breath_weapon = self.get_breath_weapon()
        self.special_attack = self.get_special_attack()
        self.finishing_move_threshold = self.calculate_finishing_move_threshold()
        self.last_breath_time = time.time()  # Track time of last breath weapon usage
        self.breath_cooldown = (
            60 * 10
        )  # Cooldown time for breath weapon in seconds (10 minutes)

    def calculate_hit_points(self):
        hit_points_mapping = {
            "Wyrmling": "10d8+20",
            "Very Young": "15d10+45",
            "Young": "20d10+80",
            "Adult": "30d10+150",
            "Old": "40d10+240",
            "Ancient": "50d10+350",
        }
        hit_points_dice = hit_points_mapping.get(self.age_category, "0")
        return self.roll_dice(hit_points_dice)

    def calculate_armor_class(self):
        armor_class_mapping = {
            "Wyrmling": 17,
            "Very Young": 18,
            "Young": 19,
            "Adult": 20,
            "Old": 21,
            "Ancient": 22,
        }
        return armor_class_mapping.get(self.age_category, 10)

    def get_breath_weapon(self):
        breath_weapon_mapping = {
            "Gold": "Fire Breath",
            "Silver": "Cold Breath",
            "Copper": "Acid Breath",
            "Brass": "Fire Breath",
            "Bronze": "Lightning Breath",
            "Cobalt": "Force Breath",
            "Mercury": "Poison Breath",
        }
        return breath_weapon_mapping.get(self.dragon_type, "Unknown Breath")

    def get_special_attack(self):
        special_attacks = {
            "Gold": "Golden Blaze",
            "Silver": "Freezing Gaze",
            "Copper": "Acidic Bite",
            "Brass": "Inferno Roar",
            "Bronze": "Thunderous Charge",
            "Cobalt": "Forceful Blast",
            "Mercury": "Toxic Cloud",
        }
        return special_attacks.get(self.dragon_type, "Unknown Attack")

    def calculate_finishing_move_threshold(self):
        threshold_mapping = {
            "Wyrmling": 50,
            "Very Young": 75,
            "Young": 100,
            "Adult": 150,
            "Old": 200,
            "Ancient": 300,
        }
        return threshold_mapping.get(
            self.age_category, 100
        )  # Default threshold if age category is not found

    def can_use_breath_weapon(self):
        current_time = time.time()
        time_since_last_breath = current_time - self.last_breath_time
        return time_since_last_breath >= self.breath_cooldown

    def use_breath_weapon(self):
        if self.can_use_breath_weapon():
            self.last_breath_time = time.time()
            print(f"{self.name} uses {self.breath_weapon}!")
            # Add breath weapon effect here
        else:
            print(
                f"{self.name} cannot use {self.breath_weapon} yet. Cooldown in progress."
            )

    def attack(self, target):
        physical_attack = random.choice(["claw", "bite", "tail"])

        if physical_attack == "claw":
            damage = self.calculate_claw_damage()
            print(f"{self.name} attacks with a claw!")
        elif physical_attack == "bite":
            damage = self.calculate_bite_damage()
            print(f"{self.name} attacks with a bite!")
        else:  # physical_attack == 'tail'
            damage = self.calculate_tail_damage()
            print(f"{self.name} attacks with its tail!")

        if self.hit_points >= self.finishing_move_threshold:
            finishing_damage = self.calculate_special_attack_damage()
            total_damage = damage + finishing_damage
            print(
                f"{self.name} executes a powerful finishing move with {self.special_attack}!"
            )
            target.take_damage(total_damage)
        else:
            print(f"{self.name} deals {damage} damage to {target.name}!")
            target.take_damage(damage)

    def calculate_claw_damage(self):
        claw_damage_mapping = {
            "Wyrmling": "2d6",
            "Very Young": "2d8",
            "Young": "2d10",
            "Adult": "3d6",
            "Old": "3d8",
            "Ancient": "4d6",
        }
        damage_roll = claw_damage_mapping.get(self.age_category, "0")
        return self.roll_dice(damage_roll)

    def calculate_bite_damage(self):
        bite_damage_mapping = {
            "Wyrmling": "1d10",
            "Very Young": "2d6",
            "Young": "2d8",
            "Adult": "2d10",
            "Old": "3d8",
            "Ancient": "3d10",
        }
        damage_roll = bite_damage_mapping.get(self.age_category, "0")
        return self.roll_dice(damage_roll)

    def calculate_tail_damage(self):
        tail_damage_mapping = {
            "Wyrmling": "1d8",
            "Very Young": "1d10",
            "Young": "2d6",
            "Adult": "2d8",
            "Old": "3d6",
            "Ancient": "3d8",
        }
        damage_roll = tail_damage_mapping.get(self.age_category, "0")
        return self.roll_dice(damage_roll)

    def calculate_special_attack_damage(self):
        special_attack_damage_mapping = {
            "Gold": "3d8",
            "Silver": "3d8",
            "Copper": "3d8",
            "Brass": "3d8",
            "Bronze": "3d8",
            "Cobalt": "3d8",
            "Mercury": "3d8",
        }
        damage_roll = special_attack_damage_mapping.get(self.dragon_type, "0")
        return self.roll_dice(damage_roll)

    def roll_dice(self, dice_code):
        num_dice, dice_sides, modifier = self.parse_dice_code(dice_code)
        return sum(random.randint(1, dice_sides) for _ in range(num_dice)) + modifier

    def take_damage(self, damage):
        self.hit_points -= damage
        print(
            f"{self.name} takes {damage} damage! Remaining hit points: {self.hit_points}"
        )


# Testing the MetallicDragon class
gold_dragon = MetallicDragon("Gold Dragon", "Adult", "Gold")
player = MetallicDragon("Player", "Adult", "Human")

for _ in range(5):
    gold_dragon.attack(player)
