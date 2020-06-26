import math
import basic

# This is a class that was made to organize all my functions relating to the advanced operations
class advancedDef:

    # Function for calculating exponents
    def exponential():
        print()
        first_num = input("Please enter the number that you would like to raise to the given power. ")
        print()
        sec_num = input("Pleae enter the number that you would to be raised to the first number inputted. ")

        while first_num == "back" or sec_num == "back":
            advancedDef.advancedFunctions()

        first_num = int(first_num)
        sec_num = int(sec_num)

        exponentTotal = first_num ** sec_num
        print()
        print(first_num, "raised to the",sec_num,"th power equals to", exponentTotal, ".")
        
    # Function for calculating square roots
    def squareRoot():
        print()
        num = input("Please enter the number of that you would like to find the square root of. ")

        while num == "back":
            advancedDef.advancedFunctions()

        num = int(num)

        sqRoot = math.sqrt(num)
        print()
        print("The square root of ", num, " equals ", sqRoot, ".")

    # What is run if selected "advanced"
    def advancedFunctions():

      print()
      selected_operation = input("Please enter either 'exponent' or 'square root', respectively representing either raising a number to a certain power, or finding the square root of a number. ")
      accepted_outputs = ["exponent", "square root", "back"]

      while selected_operation not in accepted_outputs:
        print()
        selected_operation = input("Invalid input! Please enter either 'exponent' or 'square root', respectively representing either raising a number to a certain power, or finding the square root of a number. ")
      
      if selected_operation == "exponent":
        advancedDef.exponential()
      elif selected_operation == "square root":
        advancedDef.squareRoot()
      elif selected_operation == "back":
        determineDifficulty()


        
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
        print()
    elif selected_difficulty == "advanced":
        advancedDef.advancedFunctions()
        print()

    print()
    player_end_command = input("Press any key, then the Enter key to continue... ")