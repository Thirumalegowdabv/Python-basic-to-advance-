#....variables....
#...list = is used to store a multiple elements in a single variable 
#...ex for list 
#..food = ["pizza","carrots","eggs"]


import random
def get_choices():
    player_choice = input("enter a choice(rock,paper,scissors):")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices
 
def check_win(player, computer):
    print(f"You chose  {player} , Computer chose {computer} ")
    if player == computer:
        return "it's a tie"
    elif player == "rock":
      if computer == "scissors":
        return "Rock smashes scissors! You win!"
      else:
        return "Paper cover rock! You loose."
    elif player == "paper":
      if computer == "rock":
        return "Paper covers rock! You win!"
      else:
        return "Scissors cuts paper! You loose."
    elif player == "scissors":
      if computer == "paper":
        return "Scissors cuts paper! You win!"
      else:
        return "Rock smashes scissors! You loose."
 
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
