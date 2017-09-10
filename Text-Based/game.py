# imports
import time
import random

moveon = False

# Game function
def game():
    """

    :rtype: object
    """
    print ( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
    print ( 'Welcome to DragonClaw!' )
    print ( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )

    time.sleep ( 0 )

    print('What is your name?')
    name = input('Your name is: ')

    print('Welcome ' + name)

    print(name + ' you have been chosen to go on a quest to find the valuable object located in the dungeon!')

    proceed = input('Do you want to proceed? ')

    if proceed in ['y', 'Y', 'Yes', 'YES', 'yes']:
        print('Lets move on')
        moveon = True
    else:
        moveon = False

    if moveon == True:
        print('We Continue')

    else:
        print('Goodbye ' + name)

game ( )
