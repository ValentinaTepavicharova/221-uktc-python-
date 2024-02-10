import random

print("This is Rock/Paper/Scissors Game!")
print("WELCOME!")
print()
player_name = input("Enter your name here: ")
print()

user_wins = 0
comp_wins = 0

answer = ["y", "n"]
options = ["rock", "paper", "scissors"]

is_continuous = False

while True:
    if is_continuous:
                question = input("Do you want to continue play? Y/N: ").lower()
                if question == "y":
                    continue
                elif question == "n":
                    print(f"{player_name} won", user_wins, "times")
                    print("The computer won", comp_wins, "times")
                    print("Goodbye!")
                    exit()
                if question not in answer:
                    print("Incorrect answer")
                    continue


    user_input = input("Type Rock/Scissors/Paper: ").lower()

    if user_input not in options:
        print("Sorry, I don't understand")
        continue

    is_continuous = True
    random_number = random.choice(range(0, 2))
    comp_pick = options[random_number]
    print("Computer picked", comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissors":
        user_wins += 1
        print("You won!")
        print()
        continue

    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user_wins += 1
        print()
        continue

    elif user_input == "scissors" and comp_pick == "paper":
        print("You won!")
        user_wins += 1
        print()
        continue

    elif user_input == "scissors" and comp_pick == "scissors":
        print("YOU ARE EVEN!")
        print()
        continue

    elif user_input == "rock" and comp_pick == "rock":
        print("YOU ARE EVEN!")
        print()
        continue

    elif user_input == "paper" and comp_pick == "paper":
        print("YOU ARE EVEN!")
        print()
        continue

    else:
        print("YOU LOST! :(")
        print()
        comp_wins += 1

