import random

def get_choices():
    player_choice = input("\n\n*****************Enter a choice ( rock, paper, scissors )   : ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print (f"\nYou chose {player}")
    print (f"\nComputer chose {computer}")
    if player == computer:
        return "\nIt's a tie!\n\n" # this is a nice file!!!\n
    elif player == "rock":
        if computer == "scissors":
            return " \n*****************Rock smashes scissors! You win!*****************\n\n"
        else:
            return " \n*****************Paper covers rock! You lose.*****************\n\n"
    elif player == "paper":
        if computer == "scissors":
            return " \n*****************Scissors tear paper, You lose.*****************\n\n"
        else:
            return " \n*****************Paper covers rock! You Win!*****************\n\n"
    elif player == "scissors":
        if computer == "rock":
            return " \n*****************Rock smashes scissors! You lose.***********************\n\n"
        else:
            return " \n*****************Scissors tear paper, You Win!*****************\n\n"
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)