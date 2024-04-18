""" Projet informatique
auteur: Nicolas Schell, Wilearts Nicolas
date : 6 fevrier 2024
entrée : 
sortie : 
"""
import copy

# Définition des constantes pour les valeurs du plateau
PAWN1 = 0
PAWN2 = 1
EMPTY_PAWN = 2
EMPTY_BLOCKER = 3
BLOCKER = 4
IMP = 5

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
        if i == 0 :
            case_a_checker_x = (pos_depart[i] - pos_final[i])/2+pos_depart[i]
        else :
            case_a_checker_y = (pos_depart[i] - pos_final[i])/2+pos_depart[i]
    if board[case_a_checker_x][case_a_checker_y]==3.0 :
        return True 
    else : 
        return False

# Fonction pour générer tous les coups possibles à partir d'une position donnée
def generate_moves(board, pos, pawn):
    moves = []
    for 
    return moves

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
board = init_board()
print_board(board)
ai_move = choose_move(board)
print("AI's move:", ai_move)
