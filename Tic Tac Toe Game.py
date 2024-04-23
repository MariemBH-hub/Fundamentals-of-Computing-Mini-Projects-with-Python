"""
Monte Carlo Tic-Tac-Toe Player
"""
# https://py2.codeskulptor.org/#user49_qE4oNngV4LlwJHj.py
import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 3         # Number of trials to run
SCORE_CURRENT = 2.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

PLAYERX = 1
PLAYERO = 2
EMPTY = 3
DRAW = 4
# Add your functions here.
def mc_switch_player(player):
    
    """
    al helper function alternating player
    """
    if player == PLAYERX:
        player = PLAYERO
    else:
        player = PLAYERX
    
    return player

def mc_trial(board, player):
    """
    a function taking a current board and the next player 
    plays a whole game by assigning random choice for players
    """
    
    winner = board.check_win()
    
    while winner == None:
        move = random.choice(board.get_empty_squares())
        board.move(move[0], move[1], player)
        player = mc_switch_player(player)
        winner = board.check_win()
          
def score_board(board, scores, player, state):
    """
    a function which starts with the current board
    adds scores to a board and returns 
    a grid of scores
    """
    dim = board.get_dim()
    # state is a logical input telling about the game
    # state = True if player wins, False if other wins
    if state == True:
        for dummy_row in range(dim):
            for dummy_col in range(dim):
                if board.square(dummy_row, dummy_col) == EMPTY:
                    scores[dummy_row][dummy_col] += 0.0
                elif board.square(dummy_row, dummy_col) == player:
                    scores[dummy_row][dummy_col] += SCORE_CURRENT
                else: 
                    scores[dummy_row][dummy_col] -= SCORE_OTHER
    else:
        for dummy_row in range(dim):
            for dummy_col in range(dim):
                if board.square(dummy_row, dummy_col) == EMPTY:
                    scores[dummy_row][dummy_col] += 0.0
                elif board.square(dummy_row, dummy_col) == player:
                    scores[dummy_row][dummy_col] -= SCORE_CURRENT
                else: 
                    scores[dummy_row][dummy_col] += SCORE_OTHER

def mc_update_scores(scores, board, player):
    """
    function that updates scores
    """
    winner = board.check_win()
    if winner == player:
        score_board(board, scores, player, True)
    elif winner == DRAW:
        pass
    else:
        score_board(board, scores, player, False)
    

def get_best_move(board, scores):
    """
    a function that returns randomly one of the empty square with
    max score as a tuple (row, col)
    """
    max_vals =[]
    # empty contains the board empty cells indices
    empty = board.get_empty_squares()
    # emty_scores contains scores of empty cells
    empty_scores = [scores[empty[dum_i][0]][empty[dum_i][1]] for dum_i in range(len(empty))]
    # maxval stands for the max score
    maxval = max(empty_scores)
    if len(empty) == 0:
        pass
    else:
        for dummy_i in range(len(empty)):
            if empty_scores[dummy_i] == maxval:
                max_vals.append(empty[dummy_i])
    return random.choice(max_vals)
            
                                 

def mc_move(board, player, trials):
    """
    Monte Carlo Simulation function
    """
    clone = board.clone()
    scores = [ [0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for _ in range(NTRIALS):
        mc_trial(clone, player)
        mc_update_scores(scores, clone, player)
    return get_best_move(board,scores)
            

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
