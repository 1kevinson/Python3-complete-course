"""
WELCOME IN MAGICAL CALCULATOR

    Program : calculator
    Author : Arsene Kevin
    Copyright: 2020
"""
import re

print('Our Magical Calculator')
print('Type \'quit\' to exit')

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ''

    #If there has been a previous calculation, use that result as the prompt
    if previous == 0:
        equation = input('Enter equation: ')
    else:
        equation = input(str(previous))

    #If user quit ->
    if equation == 'quit':
        print('Goodbye :) !')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()+" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print('You typed', previous)


while run:
    perform_math()

# TYPOS
# To access a global variable inside a function we define with keyword global
# eval is function that does mathematics operations
# re.sub('[a-zA-Z,.:()+" "]','',equation) is a method for regex
