import random 

#Define the game as a function
def game_play (user_choice, computer_choice):
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors" or user_choice == "lizard" or user_choice == "spock":
        if computer_choice == user_choice:
            print("It's a tie!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("Scissors cuts paper.\nYou win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("Paper covers rock.\nYou win!")
        elif user_choice == "rock" and computer_choice == "lizard":
            print("Rock crushes lizard.\nYou win!")
        elif user_choice == "lizard" and computer_choice == "spock":
            print("Lizard poisons Spock.\nYou win!")
        elif user_choice == "Spock" and computer_choice == "scissons":
            print("Spock smashes scissors.\nYou win!")
        elif user_choice == "scissors" and computer_choice == "lizard":
            print("Scissors decapitates lizard.\nYou win!")
        elif user_choice == "lizard" and computer_choice == "paper":
            print("Lizard eats paper.\nYou win!")
        elif user_choice == "paper" and computer_choice == "spock":
            print("Paper disproves Spock.\nYou win!")
        elif user_choice == "spock" and computer_choice == "rock":
            print("Spock vaporizes rock.\nYou win!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("Rock crushes scissors.\nYou win!")
        elif computer_choice == "scissors" and user_choice == "paper":
            print("Scissors cuts paper.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "paper" and user_choice == "rock":
            print("Paper covers rock.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "rock" and user_choice == "lizard":
            print("Rock crushes lizard.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "lizard" and user_choice == "spock":
            print("Lizard poisons Spock.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "Spock" and user_choice == "scissons":
            print("Spock smashes scissors.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "scissors" and user_choice == "lizard":
            print("Scissors decapitates lizard.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "lizard" and user_choice == "paper":
            print("Lizard eats paper.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "paper" and user_choice == "spock":
            print("Paper disproves Spock.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "spock" and user_choice == "rock":
            print("Spock vaporizes rock.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "rock" and user_choice == "scissors":
            print("Rock crushes scissors.\nAnother meat bag beaten by your future AI overloads!!")
    else:
        print("Tsk Tsk. Play fair.")

#generate computers answer
computer_choice = random.choice(["rock","paper","scissors", "lizard", "spock"])

#prompt for user answer
user_choice = input("Do you choose rock, paper, scissors, lizard, or Spock?\n")
#make capitalization uniform
user_choice = user_choice.lower()

#run game
game_play(user_choice, computer_choice)

