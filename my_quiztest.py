easy_paragraph = '\n ___1-___ is widely used general-purpose, high-level ___2___ language. Its design philosophy emphasizes __3___ readability, and its syntax allows programmers to express concepts in fewer lines of ___3___ than would be possible in ___4___ such as C++ or Java. \n'
easy_answers = ['python',
 'programming',
 'code'
 'languages']
medium_paragraph = "\n Python has a large standard ___1__  commonly cited as one of Python's greatest strengths, providing __2__ suited to many tasks. This is deliberate and has been described as a batteries included Python philosophy. For Internet-facing applications, a large number of standard formats and ___3___ are supported. ___4___ for creating graphical user interfaces, connecting to relational databases, pseudorandom number generators, arithmetic with arbitrary precision decimals, manipulating regular expressions, and doing unit testing are also included. "
medium_answers = ['library',
 'tools',
 'protocols',
 'modules']
hard_paragraph = "___1___can serve as a ___2___ language for web applications,  for the Apache web server. With Web Server Gateway Interface, a standard API has evolved to facilitate these applications. Web frameworks like ___3___, Pylons, Pyramid, TurboGears, web2py, Tornado, Flask, Bottle and Zope support developers in the design and maintenance of complex ___4____. Pyjamas and IronPython can be used to develop the client-side of Ajax-based applications. SQLAlchemy can be used as data mapper to a relational __6___. Twisted is a framework to program communications between computers, and is used by Dropbox."
hard_answers = ['Python',
 'scripting',
 'Django',
 'applications',
 'databases']


print "Would you like to play a game?"
answer = raw_input("type yes or no ")
if answer == 'yes' or answer == 'y':
    print  "Welcome to the fill in the blank game. Choose your level of diffculty, Easy, Medium and Hard"
    answer1 = raw_input("type Easy, Medium or Hard  ")
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