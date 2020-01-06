import time
from random import choice
rules = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
previous = ['rock', 'paper', 'scissors']

print(" Welcome to Rock Paper Scissors")
print(" *"*69)
time.sleep(2)

while True:
    start = input(" Your opponent is Joe, Would you like to play?, 'Yes' or 'Whos Joe':")

    if start == 'Yes':
        print(" Great")
    elif start == 'Whos Joe':
        print(" Joe Mama")
        time.sleep(10)
        print(" *"*69)
        time.sleep(10)
        print("YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEET")
        exit()
    break
print("Begin")

while True:
    human = input('\nchoose your weapon: ')
    computer = rules[choice(previous)]  # choose the weapon which beats a randomly chosen weapon from "previous"

    if human in ('quit', 'exit'): break

    elif human in rules:
        previous.append(human)
        print('the computer played', computer, end='; ')

        if rules[computer] == human:  # if what beats the computer's choice is the human's choice...
            print('Congrats youve won nothing!')
        elif rules[human] == computer:  # if what beats the human's choice is the computer's choice...
            print('Joe won get rekt:(')
        else: print("issa whole tie!")

    else: print("that aint it chief (ง ͠° ͟ل͜ ͡°)ง")
time.sleep(3)
print("Для Родины")
input("Вы согласны? Yes or No")

