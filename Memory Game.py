# implementation of card game - Memory
# by Mariem Ben Hssine: benhssinemariem@gmail.com


import simplegui
import random
WIDTH = 800
HEIGHT = 100
turns = 0
# helper function to initialize globals
def new_game():
    global state, turns, exposed, DECK
    global crd1, crd2
    state = 0
    turns = 0
    DECK = range(0,8)+range(0,8)
    random.shuffle(DECK)
    exposed = [0] * 16
    crd1 = 59
    crd2 = 63 
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    global exposed, state, crd1, crd2
    global turns
    # add game state logic here
    if state == 0:
         for i in range(0,len(DECK)):
            if (pos[0] >= 50 * i) and (pos[0] < 50 * (i + 1)) and exposed[i] == 0:
                exposed[i] = 1
                crd1 = i
                state = 1
    elif state == 1:
         for i in range(0,len(DECK)):
            if (pos[0] >= 50 * i) and ((pos[0] < 50 * (i + 1))) and exposed[i] == 0:
                exposed[i] = 1
                crd2 = i
                state = 2
    elif state == 2:
        if DECK[crd1] == DECK[crd2]:
            for i in range(0,len(DECK)):
                if (pos[0] >= 50 * i) and (pos[0] < 50 * (i + 1)) and exposed[i] == 0:
                    exposed[i] = 1
                    crd1 = i
                state = 1
        elif DECK[crd1] != DECK[crd2]:
                turns = turns + 1
                exposed[crd1] = 0
                exposed[crd2] = 0
                for i in range(0,len(DECK)):
                    if (pos[0] >= 50 * i) and (pos[0] < 50 * (i + 1)) and exposed[i] == 0:
                        exposed[i] = 1
                        crd1 = i
                state = 1
    label.set_text("Turns = " + str(turns))
                

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for j in range(0,len(DECK)):
        if exposed[j] == 0:
            canvas.draw_line((25 + 50 * j, 0), (25 + 50 * j, HEIGHT), 49.5, "Green")
        else:
            canvas.draw_text(str(DECK[j]), (10 + 50 * j, 65), 60, 'White') 
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = ")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()
 


# Always remember to review the grading rubric