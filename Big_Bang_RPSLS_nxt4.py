"""
A rock paper scissors game expanded to match
the Rock, Paper, Scissors, Lizard, Spock verison in The Big Bang Theory(TV Series)
Option for Best-of-One, or Best-of-Three games
"""
import random 


user_score = 0
computer_score = 0
round_count = 1
#Define the game as a function
def game_play (user_choice, computer_choice):
    global user_score
    global computer_score
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors" or user_choice == "lizard" or user_choice == "spock":
        if computer_choice == user_choice:
            print("It's a tie!")
        elif user_choice == "scissors" and computer_choice == "paper":
            user_score += 1
            print("Scissors cuts paper.\nYou win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("Paper covers rock.\nYou win!")
            user_score += 1
        elif user_choice == "rock" and computer_choice == "lizard":
            print("Rock crushes lizard.\nYou win!")
            user_score += 1
        elif user_choice == "lizard" and computer_choice == "spock":
            print("Lizard poisons Spock.\nYou win!")
            user_score += 1
        elif user_choice == "Spock" and computer_choice == "scissons":
            print("Spock smashes scissors.\nYou win!")
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "lizard":
            print("Scissors decapitates lizard.\nYou win!")
            user_score += 1
        elif user_choice == "lizard" and computer_choice == "paper":
            print("Lizard eats paper.\nYou win!")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "spock":
            print("Paper disproves Spock.\nYou win!")
            user_score += 1
        elif user_choice == "spock" and computer_choice == "rock":
            print("Spock vaporizes rock.\nYou win!")
            user_score += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            print("Rock crushes scissors.\nYou win!")
            user_score += 1
        elif computer_choice == "scissors" and user_choice == "paper":
            print("Scissors cuts paper.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "paper" and user_choice == "rock":
            print("Paper covers rock.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "rock" and user_choice == "lizard":
            print("Rock crushes lizard.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "lizard" and user_choice == "spock":
            print("Lizard poisons Spock.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "Spock" and user_choice == "scissons":
            print("Spock smashes scissors.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "scissors" and user_choice == "lizard":
            print("Scissors decapitates lizard.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "lizard" and user_choice == "paper":
            print("Lizard eats paper.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "paper" and user_choice == "spock":
            print("Paper disproves Spock.\nAnother meat bag beaten by your future AI overloads!!")
        elif computer_choice == "spock" and user_choice == "rock":
            print("Spock vaporizes rock.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
        elif computer_choice == "rock" and user_choice == "scissors":
            print("Rock crushes scissors.\nAnother meat bag beaten by your future AI overloads!!")
            computer_score += 1
    else:
        print("Tsk Tsk. Play fair.")
    print("Your score is " + str(user_score) + "\nMy score is " + str(computer_score))
    print("\n====================\n")

def round():
    global round_count
    print("Round " + str(round_count) + ":")
    #generate computers answer
    computer_choice = random.choice(["rock","paper","scissors", "lizard", "spock"])

    #prompt for user answer
    user_choice = input("Do you choose rock, paper, scissors, lizard, or Spock?\n")
    #make capitalization uniform3
    user_choice = user_choice.lower()

    print("\n")

    #run game
    game_play(user_choice, computer_choice)

    round_count += 1

game_count = input("1 game or best of 3?\n")
game_count_flt = float(game_count)

if game_count_flt == 1:
    round()
    if user_score == 1:
        print("Looks like you win!")
    elif computer_score == 1:
        print("Haha I win!")
    else:
        print("Tie breaker round!")
        round()
        if user_score == 1:
            print("Looks like you win!")
        elif computer_score == 1:
            print("Haha I win!")

elif game_count_flt == 3:
    round()
    round()
    if user_score != 2 and computer_score != 2:
        round()
    while user_score <= 1 and computer_score <= 1:
        print("Tie breaker round!")
        #generate computers answer
        computer_choice = random.choice(["rock","paper","scissors", "lizard", "spock"])

        #prompt for user answer
        user_choice = input("Do you choose rock, paper, scissors, lizard, or Spock?\n")
        #make capitalization uniform3
        user_choice = user_choice.lower()

        #run game
        game_play(user_choice, computer_choice)

    if user_score == 2:
        print("Looks like you win!")
    if computer_score == 2 :
        print("Haha I win!")

