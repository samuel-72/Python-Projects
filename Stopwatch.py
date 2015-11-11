#This program uses the simplegui package available in CodeSkulptor

import simplegui

# template for "Stopwatch: The Game"

# define global variables
time = noOfStops = noOfSuccessfulStops = 0
message = "0:00:0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    A = BC = D = res = ""    
    tempSec = 0
    D = str(t)[-1]
        
    tempSec = t/10
    
    if (tempSec <= 59):
        if (tempSec < 10):
            res = "0:0" + str(tempSec) + ":" + D
            
        else:
            res = "0:" +str(tempSec) + ":" + D
    
    else:
        if (tempSec % 60 < 10):
            BC = "0" + str(tempSec % 60)
        else:
            BC = str(tempSec % 60)
        
        A = str(tempSec/60)
        res = A + ":" + BC + ":" + D
        
    return ( res )

# define event handlers for buttons; "Start", "Stop", "Reset"

def Start():
    timer.start()
    
def Stop():
    global noOfStops, noOfSuccessfulStops
    if (timer.is_running()):
        timer.stop()
        noOfStops += 1
        if (time % 10 == 0):
            noOfSuccessfulStops += 1
        
    
def Reset():
    global time, noOfStops, noOfSuccessfulStops
    timer.stop()
    time = noOfSuccessfulStops = noOfStops = 0
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    global message
    
    message = format(time)
    score = str(noOfSuccessfulStops) + "/" + str(noOfStops)
    
    canvas.draw_text(message, [150,200], 50, "Black")
    canvas.draw_text(score, [350,30], 30, "Black")
    
# create frame

frame = simplegui.create_frame('STOPWATCH', 400, 400)
frame.set_canvas_background('Teal')

# register event handlers
Start = frame.add_button('START', Start, 100)
Stop = frame.add_button('STOP', Stop, 100)
Reset = frame.add_button('RESET', Reset, 100)

frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(0.1,timer_handler)

# start frame
frame.start()

