import random

def roll_dice():
    """
    Simulates rolling a six-sided dice.
    """
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator Game!")
    player_name = input("Enter your name: ")

    while True:
        print("\nOptions:")
        print("1. Roll the dice")
        print("2. Quit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            dice_roll = roll_dice()
            print(f"\n{player_name}, you rolled a {dice_roll}!")
        elif choice == "2":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
