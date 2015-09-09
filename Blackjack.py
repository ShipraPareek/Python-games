# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

WIDTH = 600
HEIGHT = 600


# initialize some useful global variables

in_play = False		# For each game, it is true until player stands
round_win = None	# True when the player has won the round, False otherwise
wins = 0			# Number of rounds won by the player
losses = 0
deck = None
player_hand = None
dealer_hand = None
outcome = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, rotation = 0.0):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE, rotation)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        hand_str = "Hand contains"
        for card in self.cards:
            hand_str += " " + str(card)
        return hand_str

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        has_ace = False
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True
        if has_ace and hand_value + 10 <= 21:
            hand_value += 10
        return hand_value
   
    def draw(self, canvas, pos):
        y = pos[1]
        for i in range(len(self.cards)):
            x = pos[0] + i * (CARD_SIZE[0] + 10)
            self.cards[i].draw(canvas, [x, y])
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            self.cards += [Card(suit, rank) for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        deck_str = "Deck contains"
        for card in self.cards:
            deck_str += " " + str(card)

        return deck_str

def player_win():
    global round_win, wins
    round_win = True
    wins += 1

def player_loss():
    global round_win, losses
    round_win = False
    losses += 1

#define event handlers for buttons
def deal():
    global deck, player_hand, dealer_hand, in_play

    if in_play:
        player_loss()

    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    in_play = True
    round_win = None

def hit():
    global in_play, player_hand, outcome
    
    outcome = False
    if in_play:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            in_play = False
            outcome = True
            player_loss()
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, player_hand, dealer_hand, outcome
    
    outcome = False
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        in_play = False
        if dealer_hand.get_value() > 21:
            outcome = True
            player_win()
        elif dealer_hand.get_value() < player_hand.get_value():
            player_win()
        else:
            player_loss()
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler 

TEXT_COLOR = "Lime"
FONT_FACE = "monospace"

def draw_text(canvas, text, pos, font_size, font_color, centered=False, shadow_offset=None, shadow_color=None):
   
    if centered:
        text_width = frame.get_canvas_textwidth(text, font_size, FONT_FACE)
        pos = (pos[0] - text_width / 2, pos[1] + (font_size * 0.6) / 2)

    canvas.draw_text(text, pos, font_size, font_color, FONT_FACE)
    
def draw_title(canvas, pos):
    """
    Draw the title of the game.
    """
    x = pos[0]
    y = pos[1]
    
    # Border
    boder = ((x, y), (x + 580, y), (x + 580, y + 120), (x, y + 120))
    canvas.draw_polygon(boder, 3, "Fuchsia", "Black")

    # Blackjack cards
#    Card("S", "A").draw(canvas, (x + 30, y + 10), -1.0 / 6)
#    Card("S", "J").draw(canvas, (x + 30 + CARD_SIZE[0] // 3, y + 10), 1.0 / 6)

    # The title
    text_center = (pos[0] + CARD_SIZE[0] * 5.0 / 3.0 + 180, pos[0] + 30)
    draw_text(canvas, "Blackjack!", \
                   text_center, 50, "Lime", \
                   True, (4,4), "Green")
    canvas.draw_text("Wins:" + str(wins), (x + 10, y + 90), 32, TEXT_COLOR, FONT_FACE)
    canvas.draw_text("Loses:" + str(losses), (x + 215, y + 90), 32, TEXT_COLOR, FONT_FACE)
    canvas.draw_text("Score:" + str(wins - losses), (x + 410, y + 90), 32, TEXT_COLOR, FONT_FACE)

def draw_dealer_hand(canvas, pos):
    
    # Dealer name and score
    text = "Dealer"
    if not in_play:
        text += " - " + str(dealer_hand.get_value()) 
    canvas.draw_text(text, (pos[0], pos[1] - 20), 32, TEXT_COLOR, "sans-serif")
    
    # Cards
    dealer_hand.draw(canvas, pos)

    # Cover first card if still playing...
    if in_play:
        canvas.draw_image(card_back, (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]), CARD_BACK_SIZE, \
                          [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], \
                          CARD_BACK_SIZE)

def draw_player_hand(canvas, pos):
    """
    Draw player's hand, name, and score.
    """
    # Player name and score
    text = "Player - " + str(player_hand.get_value()) 
    canvas.draw_text(text, (pos[0], pos[1] - 20), 32, TEXT_COLOR, "sans-serif")

    # Cards
    player_hand.draw(canvas, pos)

    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global round_win
    
    
    canvas.draw_circle((WIDTH / 2, HEIGHT - WIDTH*3/2.0 - 20), WIDTH*3/2.0, 40, 'Fuchsia', "GREEN")

    # Game
    draw_title(canvas, (10, 10))    
    draw_dealer_hand(canvas, (105, 190))
    draw_player_hand(canvas, (105, 440))
    
    canvas.draw_line((0, 300), (600, 300), 3, 'Fuchsia')
    canvas.draw_line((0, 380), (600, 380), 3, 'Fuchsia')
        
    # Messages
    if in_play:
        # Hit or stand?
        draw_text(canvas, "Hit or stand?", \
                              (WIDTH / 2, 340), 32, "Cyan", \
                              True, (3,3), "Blue")
    else:
        # Winner
        if round_win:
            if outcome:
                winner_msg = "Dealer Busted!"
            else:
                winner_msg = "You win!"
            
        else:
            if outcome:
                winner_msg = "You Busted!"
            else:
                winner_msg = "Dealer wins!"
        draw_text(canvas, winner_msg, \
                       (WIDTH / 3, 340), 42, "Yellow", \
                       True, (4,4), "Red")
        # New deal?
        draw_text(canvas, "New deal?", \
                       (500, 340), 32, "Cyan", \
                       True, (3,3), "Blue")
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 100)
frame.add_label('')
frame.add_button("Hit",  hit, 100)
frame.add_label('')
frame.add_button("Stand", stand, 100)
frame.set_draw_handler(draw)
frame.add_label('')
frame.add_button('Quit', frame.stop, 100)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric