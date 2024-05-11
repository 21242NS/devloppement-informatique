""" Projet informatique
auteur: Nicolas Schell, Wilearts Nicolas
date : 6 fevrier 2024
entrée : 
sortie : 
"""
import copy
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
    elif board[box_to_check_x][box_to_check_y]== EMPTY_BLOCKER :
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
        else :
            return True
    else :
        return False
# Function which generates all possible moves
def generate_moves(board, pawn, My_Blockers):
    
    b_move= [] # Creation of a list of positions of my blockers
    b_move_a=[] # Creation of a list of positions of my blockers that i can place
    #part for the pawn:
    pos = evaluate_board(board, pawn) # Finding my position
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
    if My_Blockers > 0:
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
        for i in range(len(b_move)):
            if can_place_blocker(board,b_move[i][0],b_move[i][1]):
                b_move_a.append(b_move[i])
        all_moves=[p_moves_a,b_move_a]
    else : 
        all_moves = p_moves_a
    return all_moves
def distance(board, pawn):
    pos = evaluate_board(board, pawn)
    if pawn == 1.0:
        res = pos[0]
    elif pawn == 0.0:
        res = len(board)-1-pos[0]
    return res
def evaluate_move(board, pawn):
    value = 0
    distance_objectif = distance(board, pawn)
    if distance_objectif == 0:
        value += distance_objectif
    return value

def minimax(node, depht, pawn1, pawn2,alpha, beta) :
    
    
    
    return random.choice(best_move) 

def chose_random(liste):
    if len(liste) == 2:
        sous_liste_1 = liste[0]
        sous_liste_2 = liste[1]

        # Choix aléatoire de l'une des sous-listes
        sous_liste_choisie = random.choice([sous_liste_1, sous_liste_2])

        # Choix aléatoire d'un élément dans la sous-liste choisie
        element_choisi = random.choice(sous_liste_choisie)
    else:
        element_choisi = random.choice(liste)

    return element_choisi
def make_move(board, move, pawn) :
    old_position = evaluate_board(board, pawn)
    new_poition = move
    board[old_position[0]][old_position[1]]=2.0
    board[new_poition[0]][new_poition[1]]=pawn
    new_board = board
    return new_board





# Fonction pour choisir le meilleur coup à jouer pour l'IA
def choose_move(board, pawn, blocker):
    #best_move = None
    #best_eval = float('-inf')
    #for move in generate_moves(board):
        #new_board = make_move(board, move)
        #eval = minimax(new_board, depth=3, maximizing_player=False)  # Profondeur de recherche limitée
        #if eval > best_eval:
            #best_eval = eval
            #best_move = move
    random_moove = chose_random(generate_moves(board, pawn, blocker))
    if len(random_moove)==2 :
        moove = {"type":"blocker",
                 "position":random_moove}
    else :
        moove = {"type":"Pawn",
                 "position":random_moove}
    response = {"respone":"move",
                "move":moove,
                "message": "j'aime manger du chcolat"
                }
    return response



