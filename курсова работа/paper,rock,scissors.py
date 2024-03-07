import random
import cowsay
from game_logic import logic
 
print()
print(cowsay.trex("This is Rock/Paper/Scissors Game!"))
print("WELCOME!")
print()
player_name = input("Enter your name here: ")
print()

globaluser_wins = 0
globalcomp_wins = 0

answer = ["y", "n"]
options = ("rock", "paper", "scissors")

is_continuous = False


def points(result):
    if result == "p":
        globaluser_wins +=1
        return
    if result == "c":
        globalcomp_wins +=1
        return



while True:
    if is_continuous:
                question = input("Do you want to continue play? Y/N: ").lower()
                print()
                if question == "y":
                    is_continuous = False
                    continue
                elif question == "n":
                    print(f"{player_name} won", globaluser_wins, "times")
                    print("The computer won", globalcomp_wins, "times")
                    print("Goodbye!")
                    exit()
                if question not in answer:
                    print("Incorrect answer")
                    continue


    user_input = input("Type Rock/Scissors/Paper: ").lower()

    if user_input not in options:
        print("Sorry, I don't understand")
        continue

    random_number = random.choice(range(0, 2))
    comp_pick = options[random_number]
    print("Computer picked", comp_pick + ".")

    winner = logic(user_input, comp_pick)
    points(winner)
    is_continuous = True
   
    
 