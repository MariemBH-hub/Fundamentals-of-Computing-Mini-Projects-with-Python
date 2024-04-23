# template for "Stopwatch: The Game"
# By Mariem Ben Hssine: benhssinemariem@gmail.com
import simplegui
# define global variables
temps = 0
n = 300
m = 300
Count_Stop = 0
x = 0
stp = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = str(t / 600)
    B = str((t % 600) / 100)
    C = str((t / 10) % 10)
    D = str(t % 10)
    return A + ":" + B + C + "." + D
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global Count_Stop
    global x
    global temps
    global stp
    timer.stop()
    if (temps % 10 == 0) and (stp == True) and (temps <> 0):
        stp = False
        x += 1
        Count_Stop += 1
    elif (stp == True) and (temps <> 0):
        stp = False
        Count_Stop += 1

def reset():
    global temps
    global Count_Stop
    global x
    temps = 0
    Count_Stop = 0
    x = 0

# define event handler for timer with 0.1 sec interval
def create_timer():
    global temps
    global stp
    if temps <= 6000:
        temps += 1
        stp = True
        pass

# define draw handler

def draw(canvas):
    canvas.draw_text(format(temps), [n / 2, m / 2], 24, "White")
    canvas.draw_text(str(x) + "/" + str(Count_Stop), [n - 50, 20], 24, "Green")
    
# create frame

frame = simplegui.create_frame("Stop Watch Challenge", n, m)
timer = simplegui.create_timer(100, create_timer)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)


# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
