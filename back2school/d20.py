import random
import time

class ChromaticDragon:
    def __init__(self, name, age_category, dragon_type):
        self.name = name
        self.age_category = age_category
        self.dragon_type = dragon_type
        self.hit_points = self.calculate_hit_points()
        self.armor_class = self.calculate_armor_class()
        self.breath_weapon = self.get_breath_weapon()
        self.special_attack = self.get_special_attack()
        self.breath_weapon_recharge = self.calculate_breath_weapon_recharge()
        self.last_breath_weapon_time = 0  # Initialize last breath weapon usage time

    def calculate_hit_points(self):
        hit_points_mapping = {
            'Wyrmling': '8d8+16',
            'Very Young': '12d10+36',
            'Young': '16d10+64',
            'Adult': '24d10+120',
            'Old': '30d10+180',
            'Ancient': '36d10+252',
        }
        hit_points_dice = hit_points_mapping.get(self.age_category, '0')
        return self.roll_dice(hit_points_dice)

    def calculate_armor_class(self):
        armor_class_mapping = {
            'Wyrmling': 17,
            'Very Young': 19,
            'Young': 20,
            'Adult': 21,
            'Old': 22,
            'Ancient': 23,
        }
        return armor_class_mapping.get(self.age_category, 10)

    def get_breath_weapon(self):
        breath_weapon_mapping = {
            'Black': 'Acid Breath',
            'Blue': 'Lightning Breath',
            'Green': 'Poison Breath',
            'Red': 'Fire Breath',
            'White': 'Cold Breath',
            'Gray': 'Sleep Breath',
        }
        return breath_weapon_mapping.get(self.dragon_type, 'Unknown Breath')

    def get_special_attack(self):
        special_attacks = {
            'Black': 'Acidic Touch',
            'Blue': 'Electrical Aura',
            'Green': 'Poisonous Touch',
            'Red': 'Spell-like Abilities',
            'White': 'Freezing Aura',
            'Gray': 'Camouflage',
        }
        return special_attacks.get(self.dragon_type, 'Unknown Attack')

    def calculate_breath_weapon_recharge(self):
        recharge_times = {
            'Wyrmling': 1 * 60,  # 1 minute
            'Very Young': 2 * 60,  # 2 minutes
            'Young': 3 * 60,  # 3 minutes
            'Adult': 4 * 60,  # 4 minutes
            'Old': 5 * 60,  # 5 minutes
            'Ancient': 6 * 60,  # 6 minutes
        }
        return recharge_times.get(self.age_category, 0)

    def attack(self, target):
        current_time = time.time()

        # Check if enough time has passed since the last breath weapon usage
        if current_time - self.last_breath_weapon_time >= self.breath_weapon_recharge:
            attacks = ['Breath Weapon', 'Claw', 'Bite', 'Tail', 'Special Attack']
            attack_type = random.choice(attacks)

            if attack_type == 'Breath Weapon':
                print(f'{self.name} uses {self.breath_weapon}!')
                damage = self.calculate_breath_weapon_damage()
                self.last_breath_weapon_time = current_time  # Update last breath weapon usage time
            elif attack_type == 'Claw':
                print(f'{self.name} attacks with Claw!')
                damage = self.calculate_claw_damage()
            elif attack_type == 'Bite':
                print(f'{self.name} attacks with Bite!')
                damage = self.calculate_bite_damage()
            elif attack_type == 'Tail':
                print(f'{self.name} attacks with Tail!')
                damage = self.calculate_tail_damage()
            else:
                print(f'{self.name} uses {self.special_attack}!')
                damage = self.calculate_special_attack_damage()

            target.take_damage(damage)
        else:
            print(f'{self.name} is recharging its breath weapon.')

    def calculate_breath_weapon_damage(self):
        breath_weapon_damage_mapping = {
            'Wyrmling': '3d6',
            'Very Young': '4d6',
            'Young': '5d6',
            'Adult': '6d6',
            'Old': '7d6',
            'Ancient': '8d6',
        }
        damage_roll = breath_weapon_damage_mapping.get(self.age_category, '0')
        return self.roll_dice(damage_roll)

    def calculate_claw_damage(self):
        claw_damage_mapping = {
            'Wyrmling': '2d6',
            'Very Young': '2d8',
            'Young': '2d10',
            'Adult': '2d12',
            'Old': '2d12',
            'Ancient': '2d12',
        }
        damage_roll = claw_damage_mapping.get(self.age_category, '0')
        return self.roll_dice(damage_roll)

    def calculate_bite_damage(self):
        bite_damage_mapping = {
            'Wyrmling': '2d8',
            'Very Young': '2d10',
            'Young': '2d12',
            'Adult': '4d10',
            'Old': '4d10',
            'Ancient': '4d10',
        }
        damage_roll = bite_damage_mapping.get(self.age_category, '0')
        return self.roll_dice(damage_roll)

    def calculate_tail_damage(self):
        tail_damage_mapping = {
            'Wyrmling': '2d6',
            'Very Young': '2d8',
            'Young': '2d10',
            'Adult': '2d12',
            'Old': '3d8',
            'Ancient': '3d8',
        }
        damage_roll = tail_damage_mapping.get(self.age_category, '0')
        return self.roll_dice(damage_roll)

    def calculate_special_attack_damage(self):
        special_attack_damage_mapping = {
            'Black': '1d6',
            'Blue': '1d6',
            'Green': '1d6',
            'Red': '2d6',
            'White': '1d6',
            'Gray': '1d4',
        }
        damage_roll = special_attack_damage_mapping.get(self.dragon_type, '0')
        return self.roll_dice(damage_roll)

    def roll_dice(self, dice_code):
        num_dice, dice_sides, modifier = self.parse_dice_code(dice_code)
        return sum(random.randint(1, dice_sides) for _ in range(num_dice)) + modifier

    def parse_dice_code(self, dice_code):
        parts = dice_code.split('+')
        num_dice, dice_sides = map(int, parts[0].split('d'))
        modifier = int(parts[1]) if len(parts) > 1 else 0
        return num_dice, dice_sides, modifier

    def take_damage(self, damage):
        # Simulate taking damage
        self.hit_points -= damage
        print(f'{self.name} takes {damage} damage! Remaining hit points: {self.hit_points}')

# Testing the ChromaticDragon class
red_dragon = ChromaticDragon('Red Dragon', 'Adult', 'Red')
player = ChromaticDragon('Player', 'Adult', 'Human')

# Simulate combat
for _ in range(5):
    red_dragon.attack(player)
    time.sleep(1)  # Simulate time passing between attacks



