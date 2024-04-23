# template for "Guess the number" mini-project
# By Mariem Ben Hssine: benhssinemariem@gmail.com


import random
import simplegui
select = 0
secret_number = False
remain = 0

# helper function to start and restart the game
def new_game():
  
    global secret_number
    global select
    if select == 0:
        print ("New Game, Please select a range")
    elif select == 1:
        secret_number = range100()
    else:
        secret_number = range1000()
    return secret_number   
    pass

# define event handlers for control panel

def range100():
    global secret_number
    global select
    global remain
    select = 1
    remain = 7
    secret_number = random.randrange(0,100)
    print ("Enter a Guess in the range [0,100) , Good Luck!")
    return secret_number 
    pass

def range1000():
    global secret_number
    global select
    global remain
    select = 2
    remain = 10
    secret_number = random.randrange(0,1000)
    game = secret_number
    print ("Enter a Guess in the range [0,1000) , Good Luck!")
    return secret_number
    pass
    
def input_guess(guess):
    global secret_number
    global remain
    n = int(guess)
    print ("Guess was: ",n)
    if (n < secret_number) and (remain <> 1):
        remain -= 1
        print ("Lower, You still have " + str(remain) + " guesses")
    elif (n > secret_number) and (remain <> 1):
        remain -= 1
        print ("Higher, You still have " + str(remain) + " guesses")
    elif (n == secret_number) and (remain <> 1):
        print ("Correct!! Congratulations \n")
        new_game()
    else:
        print ("Game Over")
        new_game()
    pass  
# create frame
frame = simplegui.create_frame("Guess Game", 200, 200)
button0 = frame.add_button('New Game', new_game, 100)
button1 = frame.add_button('Range100', range100, 100)
button2 = frame.add_button('Range1000', range1000, 100)
inp = frame.add_input('Input Guess', input_guess, 50)
# register event handlers for control elements and start frame
new_game()
frame.start()
