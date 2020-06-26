import numpy as np
import random
import home

last_1 = 0
last_2 = 0

inputs = np.zeros((2, 2, 2), dtype=int)
scores = [0, 0]

def update_inputs(current):

  global last_2, last_1

  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0
    inputs[last_2][last_1][0] = current
  
  last_2 = last_1
  last_1 = current
 
def prediction():
  if inputs[last_2][last_1][1] == 1:
     predict = inputs[last_2][last_1][0]
  else:
    predict = random.randint(0,1)
  return predict

def update_scores(player_input, predicted):
  if player_input == predicted:
    scores[0] += 1
  else:
    scores[1] += 1

  print()
  print("Computer score:", scores[0], "Player score:", scores[1])

def reset():
  for b in range(0,2):
    for r in range(0,2):
      for c in range(0,2):
        inputs[b][r][c] = 0
  
  for l in range(0,2):
    scores[l] = 0

def gameplay():
  reset()
  valid_entries = ["heads","tails"]
  
  while True:
    predicted = prediction()
    print()
    print("Think you can outsmart the artificial intelligence? Try beating him at heads or tails. Each time he guesses the same answer as you, he gets a point. If you get a different answer from him, you get a point. First player to 20 wins! ")
    player_input = input("Heads or tails? ")

    while player_input not in valid_entries:
      print()
      player_input = input("Invalid input! Would you like to select heads or tails? ")

    if player_input == "heads":
        player_input = "0"
    elif player_input == "tails":
        player_input = "1"
    
    player_input = int(player_input)

    update_inputs(player_input)
    update_scores(player_input, predicted)

    if scores[0] == 20:
      print()
      print("Oh well, the artifical inteligence beat you! ")
      break
    elif scores[1] == 20:
      print()
      print("Nice job! You outsmartted the artifical intelligence! ")
      break

# End handler for calculator program
def gameEndResponse():
    print()
    player_input_end = input("Would you like to play again, or would you like to leave the program? Enter 'play' or 'leave'. ")

    valid_entries_end = ["play", "leave"]

    while player_input_end not in valid_entries_end:
        print()
        player_input = input("Invalid input! Would you like to play again, or would you like to leave the program? Enter 'play' or 'leave'. ")

    if player_input_end == "play":
        print()
        startup()
    else:
        home.startup()


def startup():
    gameplay()
    gameEndResponse()


