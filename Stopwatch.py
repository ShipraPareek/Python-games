# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
count = 0
t_stops = 0
s_stops = 0
stop = True


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenth_sec = (t) % 10
    sec = int(t / 10) % 10
    minutes = int(t / 600) % 600
    ten_min = int(t / 100) % 6
    time_string = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return time_string


    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global count, stop
    stop = False
    timer.start()
    
def Stop():
    global t_stops, s_stops, stop
    if stop == False:
        if count % 10 == 0 and count != 0:
            s_stops = s_stops + 1
            t_stops = t_stops + 1
        elif count != 0:
            t_stops = t_stops + 1
    stop = True
    timer.stop()
    
def Reset():
    global count, s_stops, t_stops
    count = 0
    stop = True
    s_stops = 0
    t_stops = 0
    timer.stop()
    
def tick():
    global count
    count = count + 1
    

# define draw handler
def draw(canvas): 
    text = format(count) 
    canvas.draw_text( text, (55, 105), 42, "Red") 
    canvas.draw_text(str(s_stops) + '/' + str(t_stops), (160,20), 24, "Blue") 
    
# create frame
frame = simplegui.create_frame("Stopwatch: The game", 200, 200) 
frame.set_canvas_background('Pink') 

frame.add_button("Start the watch", Start, 200) 
frame.add_button("Stop the watch", Stop, 200) 
frame.add_button("Reset", Reset, 200) 
frame.set_draw_handler(draw) 
timer = simplegui.create_timer(interval, tick) 

 
frame.start() 
Reset() 


# Please remember to review the grading rubric
