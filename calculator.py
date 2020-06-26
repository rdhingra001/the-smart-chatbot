import basic
import advanced
import math
import random
# import home

# First line of code that is run, determining the difficulty of the operations
def determineDifficulty():
    print()
    selected_difficulty = input("Please specify if you would like to carry out basic or advanced operations. Note that basic operations are your 4 operations, and advanced operations include exponents and square roots. If you would like to go back to any of the previous commands anytime, type in 'back'. ")

    allowed_inputs = ["basic", "advanced"]

    while selected_difficulty not in allowed_inputs:
      print()
      selected_difficulty = input("Invalid input! Please specify if you would like to carry out basic or advanced operations. Note that basic operations are your 4 operations, and advanced operations include exponents and square roots. If you would like to go back to any of the previous commands anytime, type in 'back'. ")

    if selected_difficulty == "basic":
        basic.basicDef.basicOperations() 
    elif selected_difficulty == "advanced":
        advanced.advancedDef.advancedFunctions()

    print()


# End handler for calculator program
def gameEndResponse():
    print()
    player_input_end = input("Would you like to play again, or would you like to leave the program? Enter 'play' or 'leave'. ")

    valid_entries_end = ["play", "leave"]

    while player_input_end not in valid_entries_end:
        print()
        player_input = input("Invalid input! Would you like to play again, or would you like to leave the program? Enter 'play' or 'leave'. ")

    if player_input_end == "play":
        startup()
   # else:
      #  home.startup()
        
def runtime():
    determineDifficulty()
    gameEndResponse()

