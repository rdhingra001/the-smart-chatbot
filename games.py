import random as rd
import pandas as pd
import numpy as np
import chat as ct
import home

class games:
    def riddles():
        riddle_questions = ["What has to be broken before you can use it? ", "I’m tall when I’m young, and I’m short when I’m old. What am I? ", "What goes up but doesn't go down? ", "The more of this there is, the less you see. What is it? ", "What is so fragile that saying its name breaks it? ", "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps? "]
        riddle_answers = ["egg", "candle", "your age", "darkness", "silence", "river"]

        print()
        approval = input("Before we move on to the riddles, we just want to let you know to not put any articles in an answer. For example, if you think that the answer is 'a pencil', just type 'pencil'. Other articles include 'an' and 'the'. Do you accept? Type in 'True' for yes, and 'False' for no. Be sure to use the capital T or F in those words! ")
        valid_entries = ["True", "False"]

        while approval not in valid_entries:
            print()
            approval = input("Sorry, check your spelling! Smartbot did not recognize this command. Before we move on to the riddles, we just want to let you know to not put any articles in an answer. For example, if you think that the answer is 'a pencil', just type 'pencil'. Other articles include 'an' and 'the'. Do you accept? Type in 'True' for yes, and 'False' for no. Be sure to use the capital T or F in those words! ")

        approval = bool(approval)

        if approval == False:
            print()
            print("Oh well, sorry for the inconvienience. We're taking you back to the Smartbot chat center. Come back if you ever change your command!")
            ct.chatHome()


        for i in range(0,5):
            input_riddles = input(riddle_questions[i])

            if input_riddles == riddle_answers[i]:
                print("Congrats! You got it! You sure are one smart person!")
                print()
            else:
                print("Nice try! The correct answer was", riddle_answers[i],". On the other hand, you answered this:", input_riddles,".")
                print()
        
        print("Unfortunately, this is the end of the riddles section for now. We're now going to send you back to the chat homepage. ")
        print()
        ct.chatHome()


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
    else:
        home.startup()


            

