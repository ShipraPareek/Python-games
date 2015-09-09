# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import math
import random
import simplegui

secret_number = 0
remaining_guesses = 0
low = 0
high = 100

# helper function to start and restart the game
# def start_game():
#    new_game(0,100)

def new_game(low_value, high_value):
    global secret_number
    global remaining_guesses
    global low
    global high
    
    low = low_value
    high = high_value
    secret_number = random.randrange(low, high)
    remaining_guesses = int(math.ceil(math.log(high - low,2)))
    
    print "**************************************"
    print "New game. Range is from", low, "to", high
    print "Number of remaining guesses is", remaining_guesses

    


# define event handlers for control panel
def range100():
    new_game(0, 100)
    
   

def range1000():
    new_game(0, 1000)
    
    
def input_guess(guess):
    global secret_number
    global remaining_guesses
    
    remaining_guesses = remaining_guesses - 1    
    guess = int(guess)
    
    print ""
    print "Guess was", guess
    print "Number of remaining guesses is", remaining_guesses
    
    if remaining_guesses > 0:
        if guess > secret_number:
            print "Lower!"
        elif guess < secret_number:
            print "Higher!"
        else:
            print "Correct!"
            new_game(low,high)
    else:
        if guess == secret_number:
            print "Correct!"
        else:
            print "You ran out of guesses. The number was", secret_number
        new_game(low,high)
    

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game(0, 100)


# always remember to check your completed program against the grading rubric
