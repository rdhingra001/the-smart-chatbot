import math
import random
import home
import games

class functions:
    def learn():
        user_data = []
        print()
        user_name = input("Hi there! Here, we can learn about each other. Let's start by names. What's your's? ")
        print()
        print("Hi,",user_name,"!", "My name is Smartbot. ")
        user_data.append(user_name)
        print()
        user_age = input("How old are you? ")
        print()
        print("Oh wow! You're", user_age,"years old! I'm 3 in robot years, or about BYM67UB in human years.")
        user_data.append(user_age)
        user_color = input("What's your favorite color? ")
        print()
        print("Cool, you like the color", user_color,"! I like the color G567UJH. ")
        user_data.append(user_color)
        print()
        print("Wow! I learned a lot today! Your name is",user_data[0],", you are ",user_data[1], "years old, and your favorite color is",user_data[2],"!")
        print("Oh well, it was nice meeting you! Bye!")
        chatHome()

    def exitHandler():
        calculator_proceed = input("Are you sure that you would like to leave the chatbot? All data will be lost after this process. ")
        valid_entries = ["yes", "no"]

        while calculator_proceed not in valid_entries:
            print()
            calculator_proceed = input("Are you sure that you would like to leave the chatbot? Please specify 'yes' or 'no'. ")

        if calculator_proceed == valid_entries[0]:
            print("Bye!! It was nice meeting you!")
            print("Leaving now...")
            print
            home.startup()
        else:
            print()
            print("Yay, you chose not to leave me! Now, I'm going to have to restore all the inputs to how they were in the beginnning, so all data is lost 😥. ")




class gameHoming:
    def gameHome():
        user = input("What games would you like to play? Some games are riddles, jokes, and more to come! ")
        chatbot_games = ["riddles", "jokes"]

        while user not in chatbot_games:
            user = input("Unfortunately, there isn't a game with that name available. Some games are riddles, jokes, and more to come! ")

        if user == chatbot_games[0]:
            games.games.riddles()



def chatHome():
    print()
    player_input = input("Hey there, let's chat! Some commands that can be used include 'hi', 'home', 'learn', 'leave', and more to come! Later on, use the word 'options' if you ever want to see what commands there are available. ")
    valid_entries = ["hi", "home", "learn", "leave", "options" "mini games"]

    while player_input not in valid_entries:
        print()
        player_input = input("Oops! I don't know those commands yet. Some commands that can be used include 'hi', 'home', 'learn', and more to come! If you ever want to see what commands there are available, use the word 'options'. ")
    
    if player_input == valid_entries[0]:
        player_input = input("Hi there, my name is Ronit Jr. Be sure to use my commands to better take advantage of me! ")
    elif player_input == valid_entries[1]:
        home.startup()
    elif player_input == valid_entries[2]:
        functions.learn()
    elif player_input == valid_entries[3]:
        functions.exitHandler()
    elif player_input == valid_entries[4]:
        gameHoming.gameHome()
        


