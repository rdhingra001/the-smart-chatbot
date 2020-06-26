import calculator
import chat
import mindreader
import data

def startup():

    response = input("Hi! I'm Smartbot, your custom chatbot! Would you like me to calculate numbers, read your mind, or just hang around and chat? I can also calculate measurements found in data charts, like mean, median, and mode! Use keywords, 'calculator', 'mind reader', 'chat', or 'data'. ")

    accepted_inputs = ['calculator', 'mind reader', 'chat', 'data']

    while response not in accepted_inputs:
        print()
        response = input("Uh oh! I don't recognize this command! Would you like me to calculate numbers, read your mind, or just hang around and chat? I can also calculate measurements found in data charts, like mean, median, and mode! Use keywords, 'calculator', 'mind reader', 'chat', or 'data'. ")

    if response == accepted_inputs[0]:
        calculator.runtime()
    elif response == accepted_inputs[1]:
        mindreader.startup()
    elif response == accepted_inputs[2]:
        chat.chatHome()
    elif response == accepted_inputs[3]:
        data.data.dataHome()
        print()

startup()
   
