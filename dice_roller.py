import random

# Dice faces
dice_faces = {
    1: """
    ┌─────────┐
    │         │
    │    ●    │
    │         │
    └─────────┘
    """,
    2: """
    ┌─────────┐
    │  ●      │
    │         │
    │      ●  │
    └─────────┘
    """,
    3: """
    ┌─────────┐
    │  ●      │
    │    ●    │
    │      ●  │
    └─────────┘
    """,
    4: """
    ┌─────────┐
    │  ●   ●  │
    │         │
    │  ●   ●  │
    └─────────┘
    """,
    5: """
    ┌─────────┐
    │  ●   ●  │
    │    ●    │
    │  ●   ●  │
    └─────────┘
    """,
    6: """
    ┌─────────┐
    │  ●   ●  │
    │  ●   ●  │
    │  ●   ●  │
    └─────────┘
    """
}

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice... ")
    result = roll_dice()
    print(f"You rolled a {result} 🎲")
    print(dice_faces[result])

    play_again = input("Roll again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! 🎲")
        break
