# Winning combinations: rows, columns, diagonals
LINES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def print_board(board):
    """Display 3x3 grid"""
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("---+---+---")
    print("\n")

def winner(board):
    """Return winner ('X'/'O') or None"""
    for a, b, c in LINES:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return None

def moves(board):
    """Return list of empty positions"""
    return [i for i, v in enumerate(board) if v == ' ']

def terminal(board):
    """Check if game is over"""
    return winner(board) is not None or not moves(board)

def utility(board, me='O'):
    """Score: +1 win, -1 loss, 0 draw"""
    w = winner(board)
    return 1 if w == me else -1 if w else 0

# Global counters for node exploration
minimax_nodes = 0
alphabeta_nodes = 0

def minimax(board, player, me='O'):
    """Minimax algorithm: returns (value, move)"""
    global minimax_nodes
    minimax_nodes += 1
    
    if terminal(board):
        return utility(board, me), None
    
    best_val = -2 if player == me else 2  # MAX vs MIN
    best_move = None
    
    for m in moves(board):
        b2 = board[:]
        b2[m] = player
        val, _ = minimax(b2, 'X' if player == 'O' else 'O', me)
        
        if (player == me and val > best_val) or (player != me and val < best_val):
            best_val, best_move = val, m
    
    return best_val, best_move

def alphabeta(board, player, alpha=-2, beta=2, me='O'):
    """Alpha-beta pruning optimization"""
    global alphabeta_nodes
    alphabeta_nodes += 1
    
    if terminal(board):
        return utility(board, me), None
    
    if player == me:  # MAX player
        best_val, best_move = -2, None
        for m in moves(board):
            b2 = board[:]; b2[m] = player
            val, _ = alphabeta(b2, 'X', alpha, beta, me)
            if val > best_val:
                best_val, best_move = val, m
            alpha = max(alpha, val)
            if alpha >= beta: 
                break  # Prune
        return best_val, best_move
    else:  # MIN player
        best_val, best_move = 2, None
        for m in moves(board):
            b2 = board[:]; b2[m] = player
            val, _ = alphabeta(b2, 'O', alpha, beta, me)
            if val < best_val:
                best_val, best_move = val, m
            beta = min(beta, val)
            if alpha >= beta: 
                break  # Prune
        return best_val, best_move

def play_game():
    """Main game loop"""
    global alphabeta_nodes  # make sure we can reset inside loop
    
    board = [' '] * 9
    human, ai = 'X', 'O'
    
    print("Tic-Tac-Toe (You: X, AI: O)")
    print_board(board)
    current = human if input("Go first? (y/n): ").lower().startswith('y') else ai
    
    while not terminal(board):
        if current == human:
            try:
                pos = int(input("Move (1-9): ")) - 1
                if pos not in moves(board):
                    print("Invalid move")
                    continue
                board[pos] = human
            except ValueError:
                print("Enter 1-9")
                continue
        else:
            print("AI thinking...")
            alphabeta_nodes = 0  # Reset counter
            _, m = alphabeta(board, ai, me=ai)
            board[m] = ai
            print(f"AI chose {m+1} (explored {alphabeta_nodes} nodes)")
        
        print_board(board)
        current = ai if current == human else human
    
    w = winner(board)
    print("You win!" if w == human else "AI wins!" if w == ai else "Draw!")

def compare_algorithms():
    """Compare minimax vs alphabeta efficiency"""
    global minimax_nodes, alphabeta_nodes
    
    board = [' '] * 9  # Empty board test
    
    # Test Minimax
    minimax_nodes = 0
    _, move1 = minimax(board, 'O', me='O')
    print(f"Minimax: {minimax_nodes} nodes explored, chose position {move1+1}")
    
    # Test Alpha-Beta
    alphabeta_nodes = 0
    _, move2 = alphabeta(board, 'O', me='O')
    print(f"Alpha-Beta: {alphabeta_nodes} nodes explored, chose position {move2+1}")
    
    efficiency = ((minimax_nodes - alphabeta_nodes) / minimax_nodes) * 100
    print(f"Alpha-Beta is {efficiency:.1f}% more efficient!")

if __name__ == "__main__":
    # Compare algorithms first
    compare_algorithms()
    # Then play the game
    play_game()
