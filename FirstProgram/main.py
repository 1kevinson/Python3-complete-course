# Functions ( recommanded to use snake case to define a function)
# In python3 whe use : instead of curly braces {}
def my_function(name='Kevin', age='22'):
    print('my name is ' + name + ' I have ' + age)


my_function('arsene')


#Infinite arguments
def print_people(*people):
    for person in people:
        print('This person is', person)


print_people('Miley','Grant','Barnabe','Rugal')

#Return values from functions
def do_math(n1,n2):
    return n1 + n2

mathResult = do_math(4,9)

print(mathResult)

#If else statement
check = True

if check == False:
    print('It\'s false')
elif check == 'Burger':
    print('Yuuummmm !')
else:
    print('It is actually equal to true')

#For > While > loops
#For
names = ['Nick','Marcel','Klaus','Elijah']

for item in names:
    print('yo ' , item)

#While
run = True
current = 1

while run:
    if current == 10:
        run = False
    else:
        print(current)
        current += 1