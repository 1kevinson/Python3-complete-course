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