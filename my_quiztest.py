print "Would you like to play a game?"
answer = raw_input("type yes or no ")
if answer == 'yes' or answer == 'y':
    print  "Welcome to the fill in the blank game. Choose your level of diffculty, Easy, Medium and Hard"
    answer1 = raw_input("type Easy, Medium or Hard ")
    if answer1 == "Easy":
        print "welcome to the Easy game" 
        #easygame()
    else:
        if answer1 == "Medium":
            print "welcome to the Medium game" 
            #mediumegame()
        else:
            if answer1 == "Hard":
                print "welcome to the Hard game"
                #hardgame
else:
    print "Maybe next time" 