# Mini-project #6 - Blackjack
# by Mariem Ben Hssine: benhssinemariem@gmail.com

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
p_score = 0
d_score = 0

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
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos, state):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if state == False:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        elif state == True:
            canvas.draw_image(card_back, (36, 48), CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        ans = "Hand contains:"
        for i in range(len(self.hand)):
                ans = ans + " " + str(self.hand[i])
        return ans

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        val = 0
        a = 0
        for card in self.hand:
            val += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                a += 1
        if a != 0 and val + 10 < 21:
            val += 10
        return val
   
    def draw(self, canvas, l, state):
        self.hand[0].draw(canvas, [3, l[1]], state)
        for j in range(1, len(self.hand)):
            self.hand[j].draw(canvas, [l[0] * j + 3, l[1]], False)
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
        
        
    def deal_card(self):
        self.shuffle()
        return self.deck.pop(0)
    
    
    def __str__(self):
        ans = "Deck contains:"
        for i in range(len(self.deck)):
                ans = ans + " " + str(self.deck[i])
        return ans


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, p_score, d_score
    if in_play:
        outcome = "Player loses. Hit or Stand?"
        p_score -= 1
        d_score += 1
    else:
        in_play = True
        outcome = "Hit or Stand?"
    deck = Deck()
    dealer_hand = Hand()
    player_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())



    
    
    
    
def hit():
    global outcome, in_play, deck, dealer_hand, player_hand, d_score, p_score
 
    # if the hand is in play, hit the player
    if in_play == True and player_hand.get_value() <= 21:
        player_hand.add_card(deck.deal_card())
   
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21 and in_play == True:
        outcome = "You have busted. New Deal?"
        p_score -= 1
        d_score += 1
        in_play = False

        
        
        
         
def stand():
    global outcome, in_play, deck, dealer_hand, player_hand, d_score, p_score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealer_hand.get_value() < 17 and in_play == True:
        dealer_hand.add_card(deck.deal_card())
        
    # assign a message to outcome, update in_play and score
    if dealer_hand.get_value() > 21 and in_play == True:
        outcome = "Dealer busted. New Deal?"
        p_score += 1
        d_score -= 1
        in_play = False
    elif dealer_hand.get_value() <= 21 and dealer_hand.get_value() >= player_hand.get_value() and in_play == True:
        outcome = "Dealer wins. New Deal?"
        p_score -= 1
        d_score += 1
        in_play = False
    elif dealer_hand.get_value() > 21 and dealer_hand.get_value() < player_hand.get_value() and in_paly == True:
        outcome = "Player wins. New Deal?"
        p_score += 1
        d_score -= 1
        in_play = False

# draw handler    



def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play
    canvas.draw_text("BlackJack", [220, 40], 34, "Red")
    player_hand.draw(canvas, [72 , 300], False)
    canvas.draw_text("Player: " + str(p_score), [3, 275], 24, "White")
    dealer_hand.draw(canvas, [72 , 140], in_play)
    canvas.draw_text("Dealer: " + str(d_score), [3, 115], 24, "White")
    canvas.draw_text(outcome, [300, 100], 24, "Yellow")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
label = frame.add_label(outcome)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric