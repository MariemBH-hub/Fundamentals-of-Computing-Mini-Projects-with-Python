# Implementation of classic arcade game Pong
# by Mariem Ben Hssine: benhssinemariem@gmail.com

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
paddle1_pos = [0, HEIGHT / 2]
paddle2_pos = [WIDTH, HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 20
ball_vel = [0, 0]
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global RIGHT, LEFT
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[1] = random.choice(range(60, 180) + range(-180, -60)) / 60.0
    if direction == RIGHT:
        if LEFT == True:
            ball_vel[0] = 1.1 * random.randrange(120, 240) / 60.0
        else:
            ball_vel[0] = random.randrange(120, 240) / 60.0
        
    elif direction == LEFT:
        if RIGHT == True:
            ball_vel[0] = -1.1 * random.randrange(120, 240) / 60.0
        else:
            ball_vel[0] = -random.randrange(120, 240) / 60.0


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos,ball_vel
    global LEFT, RIGHT, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]        
 
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] < paddle1_pos[1] - HALF_PAD_HEIGHT) or (ball_pos[1] > paddle1_pos[1] + HALF_PAD_HEIGHT):
            spawn_ball(RIGHT)
            score2 += 1
        else:
            LEFT = True
            RIGHT = False
            ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] < (paddle2_pos[1] - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos[1] + HALF_PAD_HEIGHT):
            spawn_ball(LEFT)
            score1 += 1
        else:
            ball_vel[0] = - ball_vel[0]
            RIGHT = True
            LEFT = False
    elif (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
  
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

  
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    if (paddle1_pos[1] - PAD_HEIGHT < HALF_PAD_HEIGHT) and (paddle1_vel <0):
        paddle1_pos[1] = HALF_PAD_HEIGHT
    if (paddle1_pos[1] + PAD_HEIGHT > HEIGHT) and (paddle1_vel > 0):
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    if (paddle2_pos[1] - PAD_HEIGHT < HALF_PAD_HEIGHT) and (paddle2_vel <0):
        paddle2_pos[1] = HALF_PAD_HEIGHT
    if (paddle2_pos[1] + PAD_HEIGHT > HEIGHT) and (paddle2_vel > 0):
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
        
    
    # draw paddles
    canvas.draw_line([paddle1_pos[0], paddle1_pos[1] - HALF_PAD_HEIGHT],[paddle1_pos[0], paddle1_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1] - HALF_PAD_HEIGHT],[paddle2_pos[0], paddle2_pos[1] + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
   
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, HEIGHT / 2], 50, "Red")
    canvas.draw_text(str(score2), [3 * WIDTH / 4, HEIGHT / 2], 50, "Red")
   
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = -5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
        
        
def restart():
    global score1, score2
    new_game()
    score1 = 0
    score2 = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)
label1 = frame.add_label('')
label2 = frame.add_label('Use "w" and "s" keys to move up and down left paddle and "up" and "down" keys for the opposite paddle')


# start frame
new_game()
frame.start()

