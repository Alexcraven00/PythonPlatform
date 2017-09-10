print (
        "You enter a dark cavern out of curiosity. It is dark and you can only make out a small sword on the floor." )
    ch1 = str ( input ( "Do you take it? [y/n]: " ) )

    # Takes Sword
    if ch1 == 'y':
        print ( 'You have picked up the sword' )
    else:
        print ( "You have left the sword" )