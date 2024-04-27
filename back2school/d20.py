import random

import random

def generate_barbarian_constitution(min_con=13):
    # Ensure the minimum Constitution requirement
    constitution = max(min_con, random.randint(3, 21))
    return constitution

def barbarian_hit_points(level, constitution):
    hit_dice = 12  # Barbarians use a d12 for hit points
    hit_points = hit_dice  # Starting hit points at level 1 based on hit dice
    for lvl in range(2, level + 1):  # Starting from level 2
        # Calculate hit points gained at each level, including Constitution bonus
        hit_points += max(1, random.randint(1, hit_dice)) + (constitution - 10) // 2
    return hit_points

# Generate a Barbarian's Constitution score
barbarian_constitution = generate_barbarian_constitution()
print(f"Barbarian's Constitution Score: {barbarian_constitution}")

# Generate Barbarian hit points from level 1 to 20 based on the generated Constitution score
for lvl in range(1, 21):
    print(f"Level {lvl}: {barbarian_hit_points(lvl, barbarian_constitution)} hit points")



