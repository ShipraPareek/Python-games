# implementation of card game - Memory

import simplegui
import random



# helper function to initialize globals
def new_game():
    global cards, exposed_cards, correct_cards, state, pre_card, turns
    cards = [(i % 8) for i in range(16)]
    random.shuffle(cards)
    exposed_cards = [False for i in range(16)]
    correct_cards = [False for i in range(8)]
    state = 0
    pre_card = -1
    turns = 0
    label.set_text("Turns = " + str(turns))

def new_state(current_card):
    global state, exposed_cards, pre_card, turns
    if state == 0:
        turns = turns + 1
        state = 1
    elif state == 1:
        if pre_card == cards[current_card]:
            correct_cards[cards[current_card]] = True
        state = 2
    else:
        for i in range(16):
            if not correct_cards[cards[i]]:
                exposed_cards[i] = False
        turns = turns + 1
        state = 1
    label.set_text("Turns = " + str(turns))

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed_cards, pre_card
    card_width = 800 / 16
    for i in range(16):
        if pos[0] >= card_width * i and pos[0] < card_width * (i + 1) and not exposed_cards[i]:
            new_state(i)
            pre_card = cards[i]
            exposed_cards[i] = True
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed_cards[i]:
            canvas.draw_polygon([[i*50, 0], [(i+1)*50, 0], [(i+1)*50, 150], [i*50, 150]], 1, "Black", "Green")
            canvas.draw_text(str(cards[i]), [800 / 16 * i + 800 / 64, 150 / 2 + 20], 60, "White")
        else:
            canvas.draw_text(" ", [800 / 16 * i + 800 / 64, 60], 30, "White")
        canvas.draw_line([800 / 16 * (i + 1), 0], [800 / 16 * (i + 1), 150], 2, "Orange")
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 150)
frame.add_button("Reset", new_game)
l1 = frame.add_label("")
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric