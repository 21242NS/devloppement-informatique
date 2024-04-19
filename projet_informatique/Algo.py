""" Projet informatique
auteur: Nicolas Schell, Wilearts Nicolas
date : 6 fevrier 2024
entrée : 
sortie : 
"""
import copy

# Définition des constantes pour les valeurs du plateau
PAWN1 = 0.0
PAWN2 = 1.0
EMPTY_PAWN = 2.0
EMPTY_BLOCKER = 3.0
BLOCKER = 4.0
IMP = 5.0
Blockers = 10
class Blocker():
    def __init__(self, position):
        self.position = position
    def space1(self):
        pos1=self.position[0]
        return pos1
    def space2(self):
        pos2 =self.position[1]
        return pos2
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
            p_moves_a.append(p_moves_b[i])
    #part for the blockers :
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
    
    return all_moves

# Fonction pour effectuer un coup sur le plateau
def make_move(board, move):
    # Ici, vous devez implémenter la mise à jour du plateau après avoir effectué un coup
    return new_board

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
def choose_move(board):
    best_move = None
    best_eval = float('-inf')
    for move in generate_moves(board):
        new_board = make_move(board, move)
        eval = minimax(new_board, depth=3, maximizing_player=False)  # Profondeur de recherche limitée
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Exemple d'utilisation
#board = init_board()
#print_board(board)
#ai_move = choose_move(board)
#print("AI's move:", ai_move)
board =     [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]
print(generate_moves(board,PAWN2))
s = generate_moves(board,PAWN2)
print(len(s[0]))
print(len(s[1]))
