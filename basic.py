import math
import advanced

# This is a class that was made to organize all my functions relating to the basic operations
class basicDef:

    # Function for calculating addition
    def addition():

        print()
        first_num = input("Please enter the first number that you would like to add. ")
        print()
        sec_num = input("Please enter the second number that you would like to add. ")

        while first_num == "back" or sec_num == "back":
            basicDef.basicOperations()

        first_num = int(first_num)
        sec_num = int(sec_num)

        total = first_num + sec_num
        print()
        print(first_num, "+", sec_num, "=", total)

    # Function for calculating subtraction
    def subtraction():
        first_num = input("Please enter the first number that you would like to subtract. ")
        sec_num = input("Please enter the second number that you would like to subtract. ")

        while first_num == "back" or sec_num == "back":
            basicDef.basicOperations()

        first_num = int(first_num)
        sec_num = int(sec_num)

        difference = first_num - sec_num
        print(first_num, "-", sec_num, "=", difference)
    
    # Function for calculating multiplication
    def multiplication():
        print()
        first_num = input("Please enter the first number that you would like to multiply. ")
        print()
        sec_num = input("Please enter the second number that you would like to mulitply")

        while first_num == "back" or sec_num == "back":
            basicDef.basicOperations()

        first_num = int(first_num)
        sec_num = int(sec_num)

        product = first_num * sec_num
        print()
        print(first_num, "X", sec_num, "=", product)

    # Function for calculating division
    def division():
        print()
        first_num = input("Please enter the first number that you would like to divide. ")
        print()
        sec_num = input("Please enter the second number that you would like to divide. ")

        while first_num == "back" or sec_num == "back":
            basicDef.basicOperations()

        first_num = int(first_num)
        sec_num = int(sec_num)

        quotient = first_num / sec_num
        print()
        print(first_num, "/", sec_num, "=", quotient)
    
    # What is run if selected "basic"
    def basicOperations():

        print()
        selected_operation = input("Please enter one of the four operations in the given space. ")

        accepted_inputs = ["addition", "subtraction", "multiplication", "division", "back"]
        
        while selected_operation not in accepted_inputs:
            print()
            selected_operation = input("Invalid input! Please enter one of the four operations in the given space. ")

        if selected_operation == "addition":
            basicDef.addition()
        elif selected_operation == "subtraction":
            basicDef.subtraction()
        elif selected_operation == "multiplication":
           basicDef.multiplication()
        elif selected_operation == "division":
            basicDef.division()
        elif selected_operation == "back":
            determineDifficulty()


# Copied version of function from main.py to handle additional capablilites
def determineDifficulty():
    print()
    selected_difficulty = input("Please specify if you would like to carry out basic or advanced operations. Note that basic operations are your 4 operations, and advanced operations include exponents and square roots. If you would like to go back to any of the previous commands anytime, type in 'back'. ")

    allowed_inputs = ["basic", "advanced"]

    while selected_difficulty not in allowed_inputs:
        print()
        selected_difficulty = input("Invalid input! Please specify if you would like to carry out basic or advanced operations. Note that basic operations are your 4 operations, and advanced operations include exponents and square roots. If you would like to go back to any of the previous commands anytime, type in 'back'. ")

    if selected_difficulty == "basic":
        basicDef.basicOperations() 
    elif selected_difficulty == "advanced":
        advanced.advancedDef.advancedFunctions()