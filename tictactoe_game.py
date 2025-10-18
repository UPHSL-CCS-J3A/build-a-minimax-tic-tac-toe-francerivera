LINES = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("---+---+---")
    print("\n")

def winner(board):
    for a, b, c in LINES:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return None

def moves(board):
    return [i for i, v in enumerate(board) if v == ' ']

def terminal(board):
    return winner(board) is not None or not moves(board)

def utility(board, me='O'):
    w = winner(board)
    return 1 if w == me else -1 if w else 0

def minimax(board, player, me='O'):
    if terminal(board):
        return utility(board, me), None
    
    best_val = -2 if player == me else 2
    best_move = None
    
    for m in moves(board):
        b2 = board[:]
        b2[m] = player
        val, _ = minimax(b2, 'X' if player == 'O' else 'O', me)
        
        if (player == me and val > best_val) or (player != me and val < best_val):
            best_val, best_move = val, m
    
    return best_val, best_move

def alphabeta(board, player, alpha=-2, beta=2, me='O'):
    if terminal(board):
        return utility(board, me), None
    
    if player == me:
        best_val, best_move = -2, None
        for m in moves(board):
            b2 = board[:]; b2[m] = player
            val, _ = alphabeta(b2, 'X', alpha, beta, me)
            if val > best_val:
                best_val, best_move = val, m
            alpha = max(alpha, val)
            if alpha >= beta: break
        return best_val, best_move
    else:
        best_val, best_move = 2, None
        for m in moves(board):
            b2 = board[:]; b2[m] = player
            val, _ = alphabeta(b2, 'O', alpha, beta, me)
            if val < best_val:
                best_val, best_move = val, m
            beta = min(beta, val)
            if alpha >= beta: break
        return best_val, best_move

def play_game():
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
            _, m = alphabeta(board, ai, me=ai)
            board[m] = ai
            print(f"AI chose {m+1}")
        
        print_board(board)
        current = ai if current == human else human
    
    w = winner(board)
    print("You win!" if w == human else "AI wins!" if w == ai else "Draw!")

if __name__ == "__main__":
    play_game()