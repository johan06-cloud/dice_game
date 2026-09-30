import random

while True:
    choice = input("roll the die? (y/n):").lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("invalid input, please enter 'y' or 'n'.")
