""" Projet informatique
auteur: Nicolas Schell, Wilearts Nicolas
date : 6 fevrier 2024
entrée : 
sortie : 
"""

import random
PAWN1 = 0.0
PAWN2 = 1.0
EMPTY_PAWN = 2.0
EMPTY_BLOCKER = 3.0
BLOCKER = 4.0
IMP = 5.0





# Fonction wich says where my pawn is on the board
def evaluate_board(board, pawn):
    position = [0,0] # initialisation of my position
    condition = False
    while condition == False : # Loop to check every position on my board
        for i in range(len(board)):
            for j in range(len(board[i])) :
                if board[i][j] == pawn :
                    position = [i,j]
                    condition = True
    return position
# Function wich tell me if i can move my pawn
def can_move(board, start_pos, final_pos):
    box_to_check_x = 0 # initialisation of my variable in x
    box_to_check_y = 0 # initialisation of my variable in y
    for i in range(2) : # For loop to check the move in every direction
        if final_pos[i]-start_pos[i]==0 or final_pos[i]-start_pos[i] ==2 or final_pos[i]-start_pos[i]==-2 : 
            # Check if my move is ok with the rule :
            # - Can be 0 because we move in only one direction
            # - Can be 2 or -2 because we can go backward
            if i == 0 :
                box_to_check_x = int((final_pos[i] - start_pos[i])/2+start_pos[i]) # Position of the blocker that we want to check
            else :
                box_to_check_y = int((final_pos[i] - start_pos[i])/2+start_pos[i]) # Position of the blocker that we want to check
        else :
            return False
    if box_to_check_x>=len(board) or box_to_check_y>=len(board): # check the fact that it has no blocker 
        return False
    elif board[box_to_check_x][box_to_check_y]== EMPTY_BLOCKER and board[final_pos[0]][final_pos[1]]==EMPTY_PAWN :
        return True 
    else :
        return False

# Function wich tell me if i can place a blocker
def can_place_blocker(board, pos_blocker1, pos_blocker2):
    mid_box_x = 0 #initialisation of my variable in x
    mid_box_y =0 #initialisation of my variable in y
    for i in range(len(pos_blocker1)) : # For loop to check that my Blocker positions are ok
        if pos_blocker1[i]-pos_blocker2[i]==0 or pos_blocker1[i]-pos_blocker2[i] ==2 or pos_blocker1[i]-pos_blocker2[i]==-2 : # same as with the check move
            res = True
        else :
            return False
    if board[pos_blocker1[0]][pos_blocker1[1]] == EMPTY_BLOCKER and board[pos_blocker2[0]][pos_blocker2[1]]== EMPTY_BLOCKER : # check the fact that it has no blocker in the place where we want place a blocker
        mid_box_x = int((pos_blocker1[0]-pos_blocker2[0])/2+pos_blocker2[0])
        mid_box_y=int((pos_blocker1[1]-pos_blocker2[1])/2+pos_blocker2[1])
        if board[mid_box_x][mid_box_y]==EMPTY_PAWN or board[mid_box_x][mid_box_y] == PAWN1 or board[mid_box_x][mid_box_y] == PAWN2 or board[mid_box_x][mid_box_y] == BLOCKER : # check teh fact that between the box it is an intersection
            return False
        elif pos_blocker1[0] % 2 == 1:
            j = min(pos_blocker1[1],pos_blocker2[1])+1
            ortho_1 = [pos_blocker1[0]-1,j]
            ortho_2 = [pos_blocker1[0]+1,j]
            if board[ortho_1[0]][ortho_1[1]] == BLOCKER and board[ortho_2[0]][ortho_2[1]] == BLOCKER:
                return False
        elif pos_blocker1[1]%2==1 :
            i = min(pos_blocker1[0],pos_blocker2[0])+1
            ortho_1 = [i,pos_blocker1[1]-1]
            ortho_2 = [i,pos_blocker1[1]+1]
            if board[ortho_1[0]][ortho_1[1]] == BLOCKER and board[ortho_2[0]][ortho_2[1]] == BLOCKER:
                return False
        else :
            return True
    else :
        return False
    return True
# Function which generates all possible moves
def generate_moves(board, pawn, My_Blockers, pawn2):
    
    b_move= [] # Creation of a list of positions of my blockers
    b_move_a=[] # Creation of a list of positions of my blockers that i can place
    #part for the pawn:
    pos = evaluate_board(board, pawn)
    pos_e = evaluate_board(board, pawn2) # Finding my position
    # Create all my moves
    pos_up= [pos[0]-2,pos[1]]
    pos_down=[pos[0]+2,pos[1]]
    pos_left = [pos[0],pos[1]-2]
    pos_right=[pos[0],pos[1]+2]
    p_moves_b = [pos_up,pos_left,pos_right,pos_down] # Creation of a list of positions of my moves
    p_moves_a = [] # Creation of a list of positions of my good moves
    for i in range(len(p_moves_b)) : # Loop to check every move
        if can_move(board,pos,p_moves_b[i]):
            p_moves_a.append([p_moves_b[i]])
    #part for the blockers :
    if My_Blockers > 0: # two different loops for the blockers because there are vertical ones and the horizontal ones
        for i in range(1,len(board),2):
            for j in range(0,len(board[i]), 2) :
                x = j+2
                if x<len(board):
                    b_move.append([[j,i],[x,i]])
        for i in range(1,len(board),2):
            for j in range(0,len(board[i]), 2) :
                x = j+2
                if x<len(board):
                    b_move.append([[i,j],[i,x]])
        for i in range(len(b_move)): #check of all my blockers for the rules
            if can_place_blocker(board,b_move[i][0],b_move[i][1]) and -3<=b_move[i][0][0]-pos_e[0]<=3 and -3<=b_move[i][0][1]-pos_e[1]<=3: #limitation of the possibility of blockers so we gain time
                b_move_a.append(b_move[i])
        all_moves=[p_moves_a,b_move_a]
    else : 
        all_moves = p_moves_a
    return all_moves
#function to find the distance between a pawn and his target
def distance(board, pawn):
    pos = evaluate_board(board, pawn)
    if pawn == 1.0:
        res = pos[0]
    elif pawn == 0.0:
        res = len(board)-1-pos[0]
    return res
#function to evaluate how many time i need to play to win
def evaluate_move(board, pawn):
    value = 0
    pos = evaluate_board(board,pawn)
    distance_objectif = distance(board, pawn)
    if distance_objectif != 0:
        value += distance_objectif
        if pawn ==PAWN1 :    
            if board[pos[0]+1][pos[1]] == BLOCKER :
                value+=1
        elif pawn == PAWN2:
            if board[pos[0]-1][pos[1]] == BLOCKER :
                value+=1
    elif distance_objectif == 0:
        value = 0
    
    return value
#function that evalute the best move with the strategy that we must do less play that the ennemy
def best_move(pawn1, pawn2, my_blocker, board) :
    best_move = []
    moves = generate_moves(board,pawn1,my_blocker,pawn2)
    my_value=evaluate_move(board,pawn1)
    if len(moves)==0:
        return "giveup"
    elif pawn1 == PAWN1 :
        for i in range(len(moves)) :
            for j in range(len(moves[i])):
                new_board = make_move(board,moves[i][j],pawn1)
                my_new_value=evaluate_move(new_board,pawn1)
                ennemy_new_value=evaluate_move(new_board,pawn2)
                if my_new_value <= my_value and my_new_value <= ennemy_new_value:
                    if is_winnable(new_board) :
                        best_move.append(moves[i][j])
        if len(best_move)==0 :
            res2 = chose_random(moves)
            return res2
    elif pawn1 == PAWN2 :
        for i in range(len(moves)) :
            for j in range(len(moves[i])):
                new_board = make_move(board,moves[i][j],pawn1)
                my_new_value=evaluate_move(new_board,pawn1)
                ennemy_new_value=evaluate_move(new_board,pawn2)
                if is_winnable(new_board) :
                        best_move.append(moves[i][j])
        if len(best_move)==0 :
            res2 = chose_random(moves)
            return res2
    res = random.choice(best_move)
    return res

def chose_random(liste):
    if len(liste) == 2:
        sous_liste_1 = liste[0]
        sous_liste_2 = liste[1]

        # Choix aléatoire de l'une des sous-listes
        sous_liste_choisie = random.choice([sous_liste_1, sous_liste_2])

         #Choix aléatoire d'un élément dans la sous-liste choisie
        element_choisi = random.choice(sous_liste_choisie)
    else:
        element_choisi = random.choice(liste)

    return element_choisi
def make_move(board, move, pawn) :
    old_position = evaluate_board(board, pawn)
    new_position = move
    if type(new_position[0]) == int :
        if len(new_position) ==2 :
            board[old_position[0]][old_position[1]]=2.0
            board[new_position[0]][new_position[1]]=pawn

    else :
        if len(move)==2:
            for i in range(len(move)):
                board[move[i][0]][move[i][1]]=BLOCKER
        else :    
            board[old_position[0]][old_position[1]]=2.0
            board[new_position[0][0]][new_position[0][1]]
    new_board = board
    return new_board
def is_winnable(board, pawn1, pawn2):
  """
  Checks if the current board state is winnable for both players.

  Args:
      board: A 2D list representing the Quoridor board.
      pawn1: The value representing Player 1's pawn (e.g., 0.0).
      pawn2: The value representing Player 2's pawn (e.g., 1.0).

  Returns:
      True if both players have a reachable winning position, False otherwise.
  """

  def check_reachable_winning_position(pawn, target_row):
    """
    Checks if the given pawn can reach the target row (winning position).

    Args:
        pawn: The value representing the pawn (pawn1 or pawn2).
        target_row: The row number of the winning position (0 for pawn1, len(board) - 1 for pawn2).

    Returns:
        True if the pawn can reach the target row, False otherwise.
    """

    pawn_pos = evaluate_board(board, pawn)  # Find pawn's current position

    # Check if pawn is already in the winning row
    if pawn_pos[0] == target_row:
      return True

    # Check if there are any empty spaces in the target row
    for col in range(len(board[0])):
      if board[target_row][col] == EMPTY_PAWN:
        return True  # Can reach target row if empty space exists

    # Recursively check if a reachable path exists for pawn movement
    # (This part can be optimized for performance if needed)
    for move in generate_moves(board, pawn, 0, pawn2 if pawn == pawn1 else pawn1):  # Consider all possible moves
      new_board = make_move(board.copy(), move[0], pawn)  # Simulate the move
      if check_reachable_winning_position(pawn, target_row, new_board):  # Check if winnable from this move
        return True

    return False  # No reachable path found for this pawn

  # Check winnability for both players
  return check_reachable_winning_position(pawn1, 0) and check_reachable_winning_position(pawn2, len(board) - 1)







# Fonction pour choisir le meilleur coup à jouer pour l'IA
def choose_move(board, pawn1, blocker, pawn2):
    good_moove = best_move(pawn1,pawn2, blocker,board)
    if len(good_moove)==2 :
        moove = {"type":"blocker",
                 "position":good_moove}
    elif type(good_moove)==str: #when we must giveup
        response = {"response":good_moove}
    else :
        moove = {"type":"pawn",
                 "position":good_moove}
    response = {"response":"move",
                "move":moove,
                "message": "j aime manger du chcolat"
                }
    return response




