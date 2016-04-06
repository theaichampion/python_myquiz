# IPND Stage 2 Final Project

# Now you'll work on your own game to practice your skills and demonstrate what you've learned.
# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
easy_paragraph = '\n __1__ is widely used general-purpose, high-level  __2__  language. Its design philosophy emphasizes __3__ readability, and its syntax allows programmers to express concepts in fewer lines of __3__ than would be possible in __4__ such as C++ or Java. \n'
easy_answers = ['python',
 'programming',
 'code',
 'languages']
medium_paragraph = "\n Python has a large standard __1__  commonly cited as one of Python's greatest strengths, providing __2__ suited to many tasks. This is deliberate and has been described as a batteries included Python philosophy. For Internet-facing applications, a large number of standard formats and __3__ are supported. __4__ for creating graphical user interfaces, connecting to relational databases, pseudorandom number generators, arithmetic with arbitrary precision decimals, manipulating regular expressions, and doing unit testing are also included. "
medium_answers = ['library',
 'tools',
 'protocols',
 'modules']
hard_paragraph = "__1__can serve as a __2__ language for web applications,  for the Apache web server. With Web Server Gateway Interface, a standard API has evolved to facilitate these applications. Web frameworks like __3__, Pylons, Pyramid, TurboGears, web2py, Tornado, Flask, Bottle and Zope support developers in the design and maintenance of complex __4__. Pyjamas and IronPython can be used to develop the client-side of Ajax-based applications. SQLAlchemy can be used as data mapper to a relational __5__. Twisted is a framework to program communications between computers, and is used by Dropbox."
hard_answers = ['Python',
 'scripting',
 'Django',
 'applications',
 'databases']

 def select_game_difficulty():
    """hello I'm a function that will help the user decide on the challenge level. As a function I'm going to ask the user to select one 
    of three options Easy, Medium or Hard to determine the difficulty in the trivia quiz returned"""
    print  "Welcome to the fill in the blank game. Choose your level of diffculty, Easy, Medium and Hard"
    answer = raw_input("type Easy, Medium or Hard  ").lower()
    diffculty = ['easy', 'medium', 'hard']
    while answer not in diffculty:
        print "That's not an option!"
        print 'Choose your level of diffculty, Easy, Medium and Hard'
        chosen_difficulty = raw_input(prompt).lower()

    print "You've chosen " +  answer+ '!\n'
    return answer

def send_me_my_trivia(answer):
    """this function requests a level called an answer  which can be easy, medium, or hard and returns 
       a fill in the blank paragraph and answers"""
    if  answer  == 'easy':
        return (easy_paragraph, easy_answers)
    if answer == 'medium':
        return (medium_paragraph, medium_answers)
    if answer  == 'hard':
        return (hard_paragraph, hard_answers)

def ask_question(mad_lib, blank_num, answer, max_attempts = 5):
    #this function is used to see if the user's answer matches the answer for the quiz. If this user's answer is correct the answer is replaced within the quiz. if the answer is incorrect then this function will let the user know. 
    """Takes the current madlib (str), current_question (int), and 
    answer (str).  Returns the partially answered madlib (or None if the user 
    takes too many guesses) and the number of the next blank."""
    attempts_left = max_attempts
    to_replace = '__' + str(blank_num) + '__'
    prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
    user_guess = raw_input(prompt).lower()
    while user_guess != answer.lower() and attempts_left > 1:
        attempts_left -= 1
        prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
        user_guess = raw_input(prompt).lower()

    if attempts_left > 1:
        print '\nCorrect!\n'
        return (mad_lib.replace(to_replace, answer), blank_num + 1)
    else:
        return (None, blank_num + 1)


def make_display(current_mad_lib, to_replace, attempts_left, max_attempts):
    #this function takes the quiz and asks the user to attempt a guess to fill in the missing value
    """This function takes ask the user for their input . the user is expected to provide an answer that corresponds to the 
    fill in the blank question. The function will count the number of answers the user provides and compare it the the max number
    of answers he or she can give."""
    prompt = '\nThe current paragraph reads as such:\n{}\n\n'
    prompt += 'What should be substituted in for {}? '
    prompt = prompt.format(current_mad_lib, to_replace)
    if attempts_left == max_attempts:
        return prompt
    new_prompt = "That isn't the correct answer!  "
    if attempts_left > 1:
        new_prompt += "Let's try again; you have {} trys left!\n\n"
    else:
        new_prompt += 'You only have {} try left!  Make it count!\n\n'
    return new_prompt.format(attempts_left) + prompt


def find_max_guesses():
    """this function will provide the user with the maximum number of guesses per quiz answer.
     this is a user generated variable with a max number of guesses capped at five. The user will be prompted to enter the 
     number of guesses or tries he or she will get per trivia question"""
    prompt = 'How many guesses would you like per problem?'
    prompt += '\nPlease enter a possitive integer number: '
    while True:
        try:
            max_guesses = int(raw_input(prompt))
            if max_guesses < 1:
                print 'You need at least one guess!\n'
            else:
                return max_guesses
        except:
            print "That isn't an integer!\n"



current_blank = 1
select_game_difficulty()
send_me_my_trivia(answer)
max_guesses = find_max_guesses()
    while current_blank <= len(easy_answers): 
        easy_paragraph, current_blank = ask_question(easy_paragraph, current_blank, easy_answers[current_blank - 1], max_guesses)
        if hard_paragraph is None:
            print "You've failed too many straight guesses!  Game over!"
    while current_blank <= len(hard_answers):
        hard_paragraph, current_blank = ask_question(hard_paragraph, current_blank, hard_answers[current_blank - 1], max_guesses)
        if hard_paragraph is None:
                print "You've failed too many straight guesses!  Game over!"
    while current_blank <= len(medium_answers):
        medium_paragraph, current_blank = ask_question(medium_paragraph, current_blank, medium_answers[current_blank - 1], max_guesses)
        if medium_paragraph is None:
            print "You've failed too many straight guesses!  Game over!"