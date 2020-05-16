"""
WELCOME IN CALCULATOR PROGRAM
"""


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def sub(n1, n2):
    return n1 - n2


# Take the user input
print('Make a operation choice')
print('1 - Addition')
print('2 - Multiplication')
print('3 - Division')
print('4 - Substract')

choice = input('Enter your choice (1/2/3/4): ')

input1 = int(input('Enter first number > '))
input2 = int(input('Enter second number > '))

if choice == '1':
    result = add(input1, input2)
    print(input1 + ' + ' + input2 + ' = ' + result)
if choice == '2':
    result = add(input1, input2)
    print(input1 + ' * ' + input2 + ' = ' + result)
if choice == '3':
    if input2 == 0:
        print('you cannot divide by 0... Try again !')
        exit()
    result = add(input1, input2)
    print(input1 , ' / ' , input2 , ' = ' , result)
if choice == '4':
    result = add(input1, input2)
    print(input1 , ' - ' , input2 , ' = ' , result)
