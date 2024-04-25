""" Projet informatique
auteur: Nicolas Schell, Wilearts Nicolas
date : 6 fevrier 2024
entrée : 
sortie : 
"""
import copy
import random
import json



# Définition des constantes pour les valeurs du plateau
PAWN1 = 0.0
PAWN2 = 1.0
EMPTY_PAWN = 2.0
EMPTY_BLOCKER = 3.0
BLOCKER = 4.0
IMP = 5.0


# Fonction pour évaluer la position actuelle du plateau
def evaluate_board(board, pawn):
    position = [0,0]
    condition = False
    while condition == False :
        for i in range(len(board)):
            for j in range(len(board[i])) :
                if board[i][j] == pawn :
                    position = [i,j]
                    condition = True
    return position
def peut_passer(board, pos_depart, pos_final):
    case_a_checker_x = 0
    case_a_checker_y = 0
    for i in range(2) :
        if pos_final[i]-pos_depart[i]==0 or pos_final[i]-pos_depart[i] ==2 or pos_final[i]-pos_depart[i]==-2 :
            if i == 0 :
                case_a_checker_x = int((pos_final[i] - pos_depart[i])/2+pos_depart[i])
            else :
                case_a_checker_y = int((pos_final[i] - pos_depart[i])/2+pos_depart[i])
        else :
            return False
    if case_a_checker_x>=len(board) or case_a_checker_y>=len(board):
        return False
    elif board[case_a_checker_x][case_a_checker_y]== EMPTY_BLOCKER :
        return True 
    else :
        return False
def peut_mettre_blockeurs(board, pos_blocker1, pos_blocker2):
    case_mid_x = 0
    case_mid_y =0
    for i in range(len(pos_blocker1)) :
        if pos_blocker1[i]-pos_blocker2[i]==0 or pos_blocker1[i]-pos_blocker2[i] ==2 or pos_blocker1[i]-pos_blocker2[i]==-2 :
            res = True
        else :
            return False
    if board[pos_blocker1[0]][pos_blocker1[1]] == EMPTY_BLOCKER and board[pos_blocker2[0]][pos_blocker2[1]]== EMPTY_BLOCKER :
        case_mid_x = int((pos_blocker1[0]-pos_blocker2[0])/2+pos_blocker2[0])
        case_mid_y=int((pos_blocker1[1]-pos_blocker2[1])/2+pos_blocker2[1])
        if board[case_mid_x][case_mid_y]==EMPTY_PAWN or board[case_mid_x][case_mid_y] == PAWN1 or board[case_mid_x][case_mid_y] == PAWN2 or board[case_mid_x][case_mid_y] == BLOCKER :
            return False
        else :
            return True
    else :
        return False
# Fonction pour générer tous les coups possibles à partir d'une position donnée
def generate_moves(board, pawn):
    global My_Blockers
    b_move= []
    b_move_a=[]
    #part for the pawn:
    pos = evaluate_board(board, pawn)
    pos_up= [pos[0]-2,pos[1]]
    pos_down=[pos[0]+2,pos[1]]
    pos_left = [pos[0],pos[1]-2]
    pos_right=[pos[0],pos[1]+2]
    p_moves_b = [pos_up,pos_down,pos_left,pos_right]
    p_moves_a = []
    for i in range(len(p_moves_b)) :
        if peut_passer(board,pos,p_moves_b[i]):
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
            if peut_mettre_blockeurs(board,b_move[i][0],b_move[i][1]):
                b_move_a.append(b_move[i])
        all_moves=[p_moves_a,b_move_a]
    else : 
        all_moves = p_moves_a
    return all_moves


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

# Fonction pour effectuer un coup sur le plateau

# Algorithme minimax avec élagage alpha-bêta
def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate_board(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for move in generate_moves(board):
            new_board = make_move(board, move)
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in generate_moves(board):
            new_board = make_move(board, move)
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Fonction pour choisir le meilleur coup à jouer pour l'IA
def choose_move(board, pawn):
    #best_move = None
    #best_eval = float('-inf')
    #for move in generate_moves(board):
        #new_board = make_move(board, move)
        #eval = minimax(new_board, depth=3, maximizing_player=False)  # Profondeur de recherche limitée
        #if eval > best_eval:
            #best_eval = eval
            #best_move = move
    random_moove = chose_random(generate_moves(board, pawn))
    if len(random_moove)==2 :
        moove = {"type":"blocker",
                 "position":random_moove}
    else :
        moove = {"type":"Pawn",
                 "position":random_moove}
    return moove
#Principal code :

#print(generate_moves(board,PAWN2))
#d = generate_moves(board,PAWN2)
#print(len(d[0]))
#print(len(d[1]))
#s=choose_move(board, PAWN2)
#print(s)
#key = s.keys()
#if list(key)[0]=="Blocker":
#Blockers = Blockers-1
#print(Blockers)



