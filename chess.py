import chess
import chess.svg

def display_board(board):
    print(board)

def make_move(board, move):
    try:
        board.push_san(move)
    except ValueError as e:
        print(f"Invalid move: {e}")

def main():
    board = chess.Board()

    while not board.is_game_over():
        display_board(board)
        move = input("Enter your move: ")
        make_move(board, move)

    print("Game over.")
    print(f"Result: {board.result()}")

if __name__ == "__main__":
    main()