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