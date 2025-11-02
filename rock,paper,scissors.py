import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")

  options = ["rock", "paper", "scissors"]  # list of options

  computer_choice = random.choice(options)  # random choice from list

  choices_dict = {
      "player": player_choice,
      "computer": computer_choice
  }  # dictionary of choices
  return choices_dict

def check_win(player, computer):
  print("You chose " + player + ", computer chose " + computer)
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "paper covers rock! You lose."

  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cuts paper! You lose."

  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes scissors! You lose."


choices = get_choices()  #returns the dictionary of choices in the function get_choices()
result = check_win(choices["player"], choices["computer"])  #takes 2 parameters from the get_choices fuction which is the dictionary as player and computer
print(result)
