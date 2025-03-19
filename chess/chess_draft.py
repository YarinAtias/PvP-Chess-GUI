"""
   If you are seeing this code, you probably wanted to see what's behind the amazing, sophisticated and marvelous thing
   that my friend and I have created. Follow us on our Instagrams if you'd like to, _yarin_atias and ofir_luski.

   Special thanks to our smart, handsome and amazing teacher, Daniel Ayzenshteyn. Appreciating a lot.
   Have fun observing our code.
"""

import copy
from colorama import Fore

SECTIONS_COLOR = Fore.LIGHTCYAN_EX
PLAYER_WHITE = "White"
PLAYER_BLACK = "Black"
EMPTY_CELL = ' '

BLACK_PLAYER_COLOR = Fore.RED
BLACK_PAWN = f"{BLACK_PLAYER_COLOR + 'P' + Fore.RESET}"
BLACK_ROOK = f"{BLACK_PLAYER_COLOR + 'R' + Fore.RESET}"
BLACK_KNIGHT = f"{BLACK_PLAYER_COLOR + 'N' + Fore.RESET}"
BLACK_BISHOP = f"{BLACK_PLAYER_COLOR + 'B' + Fore.RESET}"
BLACK_QUEEN = f"{BLACK_PLAYER_COLOR + 'Q' + Fore.RESET}"
BLACK_KING = f"{BLACK_PLAYER_COLOR + 'K' + Fore.RESET}"

WHITE_PAWN = 'P'
WHITE_ROOK = 'R'
WHITE_KNIGHT = 'N'
WHITE_BISHOP = 'B'
WHITE_QUEEN = 'Q'
WHITE_KING = 'K'

WHITE_PIECES = [WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING]
BLACK_PIECES = [BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING]

GAME_INFO = f"""
Here's a few things that you need to know before start playing.
----------------------------------------------------------------
*  For your attention, the game is built for 2 physical players instead of 1 because my partner and I don't have the energy to
   develop an AI simulator, so deal with the existed.

{SECTIONS_COLOR + '1' + Fore.RESET}. The chess pieces are shown by their letters. 'R' indicates the Rook, 'N' indicates the Knight,
   'B' indicates the Bishop, 'Q' indicates the Queen and last but not least, 'K' indicates the King.

{SECTIONS_COLOR + '2' + Fore.RESET}. For convenience, instead of black pieces, we decided to change it into red,
   so it doesn't matter as long as you see the difference.

{SECTIONS_COLOR + '3' + Fore.RESET}. In order to move pieces on the board, you need to mark the initialized 
   dot in its algebraic notation and the desired dot on the board (Exp: e2/E2 -> e4/E4).

{SECTIONS_COLOR + '4' + Fore.RESET}. In order to execute castling, you need to mark your king and then the
   desired rook in their algebraic notation (Exp: e1/E1 -> h1/H1).

{SECTIONS_COLOR + '5' + Fore.RESET}. If you accidentally mark a dot on the board as your start point and you want to return, you can simply
   just press '1' and enter. This will restart the process.
"""


# Initializing the board
def board_creation() -> list[list]:
    board = [
[BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK],
    [BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN, BLACK_PAWN],
      [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
      [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
      [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
      [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
    [WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN, WHITE_PAWN],
[WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK],
    ]
    return board


# A function that prints the board on the screen
def print_board(board) -> None:
    print()
    print('   -------------------------------')
    for i, row in enumerate(board):
        print(str(8 - i) + ' |', end='')
        for piece in row:
            print(' ' + piece + ' ', end='|')
        print('\n   -------------------------------')
    print('    A   B   C   D   E   F   G   H')
    print()


# A function that takes care of the user's input and makes sure it is valid
def spots_input() -> tuple:
    rows_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    columns_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

    start_pos = input("Enter start position: ").strip()
    while start_pos == "" or start_pos[0].strip().upper() not in rows_letters or start_pos[1:] not in columns_numbers:
        print()
        start_pos = input("Error has occurred. Try again: ").strip()

    end_pos = input("Enter end position: ").strip()
    if end_pos == '1'.strip():
        return spots_input()
    while end_pos == "" or end_pos[0].strip().upper() not in rows_letters or end_pos[1:] not in columns_numbers:
        print()
        end_pos = input("Error has occurred. Try again: ").strip()
        if end_pos == '1'.strip():
            return spots_input()

    return start_pos, end_pos


# A function that makes user a player doesn't capture his own pieces
def can_capture(main_piece, target_piece) -> bool:
    if target_piece == EMPTY_CELL:
        return True
    main_piece_color = "white" if main_piece in WHITE_PIECES else "black"
    target_piece_color = "white" if target_piece in WHITE_PIECES else "black"
    if main_piece_color != target_piece_color:
        return True
    return False


# A function that checks if a move that comes as an input from the user is a legal move
def is_valid_move(start, end, game_board, player_color) -> bool:
    start_row, start_col = start[0], start[-1]
    end_row, end_col = end[0], end[-1]
    piece = game_board[start_row][start_col]
    target = game_board[end_row][end_col]
    row_dir = -1 if end_row < start_row else 1
    col_dir = -1 if end_col < start_col else 1
    if piece == EMPTY_CELL:
        return False
    if player_color == PLAYER_WHITE and piece not in WHITE_PIECES:
        return False
    if player_color == PLAYER_BLACK and piece not in BLACK_PIECES:
        return False

    if piece == WHITE_PAWN or piece == BLACK_PAWN:
        # Checks if a pawn can eat an opponent piece
        if (piece == BLACK_PAWN and end_row - start_row == 1 and abs(end_col - start_col) == 1 and target != EMPTY_CELL) or \
                (end_row - start_row == -1 and piece == WHITE_PAWN and abs(end_col - start_col) == 1 and target != EMPTY_CELL):
            if can_capture(piece, target):
                return True

        # Checks if the pawn can move 2 squares
        elif (start_row == 1 and piece == BLACK_PAWN) or (start_row == 6 and piece == WHITE_PAWN):
            if 1 <= abs(end_row - start_row) <= 2 and start_col == end_col and (target == EMPTY_CELL):
                pass
            else:
                return False

        # Checks if a pawn can move 1 square as a legal move
        elif (start_row - end_row if player_color == PLAYER_BLACK else end_row - start_row) == -1 and \
                start_col == end_col and target == EMPTY_CELL:
            pass
        else:
            return False

        # A loop that iterates through all the lines between the rows and checks that there's nothing in the pawn's way
        for line in range(start_row + row_dir, end_row + row_dir, row_dir):
            if target != EMPTY_CELL:
                return False
        else:
            return True


    # Checking a valid way for the rook.
    elif piece == WHITE_ROOK or piece == BLACK_ROOK:
        if (start_row == end_row or start_col == end_col) and (target == EMPTY_CELL or can_capture(piece, target)):
            if start_row == end_row:
                for col in range(start_col + col_dir, end_col + col_dir, col_dir):
                    if col == end_col:
                        break
                    if game_board[start_row][col] != EMPTY_CELL:
                        return False
                if can_capture(piece, target):
                    return True
                return False

            for row in range(start_row + row_dir, end_row + row_dir, row_dir):
                if row == end_row:
                    break
                if game_board[row][start_col] != EMPTY_CELL:
                    return False
            if can_capture(piece, target):
                return True
            return False


    # Checking a valid way for the knight
    elif piece == WHITE_KNIGHT or piece == BLACK_KNIGHT:
        if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1:
            if target == EMPTY_CELL:
                return True
            elif can_capture(piece, target):
                return True
        if abs(start_col - end_col) == 2 and abs(start_row - end_row) == 1:
            if target == EMPTY_CELL:
                return True
            elif can_capture(piece, target):
                return True
        return False


    # Checking a valid way for the bishop
    elif piece == WHITE_BISHOP or piece == BLACK_BISHOP:
        if abs(start_row - end_row) == abs(start_col - end_col):
            curr_row, curr_col = start_row, start_col
            while True:
                curr_row += row_dir
                curr_col += col_dir
                if curr_row == end_row and curr_col == end_col:
                    if can_capture(piece, target):
                        return True
                    return False
                try:
                    if game_board[curr_row][curr_col] != EMPTY_CELL:
                        return False
                except IndexError:
                    return False


    # Checking a valid way for Freddie Mercury
    elif piece == WHITE_QUEEN or piece == BLACK_QUEEN:
        if target == EMPTY_CELL or can_capture(piece, target):
            if (start_row == end_row or start_col == end_col) or abs(start_row - end_row) == abs(start_col - end_col):
                if start_row == end_row:
                    for col in range(start_col + col_dir, end_col + col_dir, col_dir):
                        if col == end_col:
                            return True
                        if game_board[start_row][col] != EMPTY_CELL:
                            return False
                if start_col == end_col:
                    for row in range(start_row + row_dir, end_row + row_dir, row_dir):
                        if can_capture(piece, target):
                            if game_board[row][start_col] == target:
                                return True
                        if game_board[row][start_col] != EMPTY_CELL:
                            return False
                    else:
                        return True
            if abs(start_row - end_row) == abs(start_col - end_col):
                curr_row, curr_col = start_row, start_col
                while True:
                    curr_row += row_dir
                    curr_col += col_dir
                    if curr_row == end_row and curr_col == end_col:
                        if can_capture(piece, target):
                            return True
                        return False
                    if game_board[curr_row][curr_col] != EMPTY_CELL:
                        return False
            return False


    # Checking a valid way for Cristiano Ronaldo
    elif piece == WHITE_KING or piece == BLACK_KING:
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1 and can_capture(piece, target):
            return True
    return False


# A function that checks for a checkmate and returns True only when nothing can prevent the checkmate
def is_checkmate(player_possible_moves: list[tuple], game_board: list[list], opponent_player_color: str) -> bool:
    opponent_king_in_check = False
    temp_game_board = copy.deepcopy(game_board)
    opponent_king_color = BLACK_KING if opponent_player_color == PLAYER_BLACK else WHITE_KING
    # Spotting the opponent king inside a tuple
    king_location = king_location_finder(game_board, opponent_king_color)
    # Checks if the king is indeed in a check
    for move in player_possible_moves:
        if move == king_location:
            opponent_king_in_check = True
            break
    if opponent_king_in_check:
        # Generating all the opponent's possible moves
        """Iterates through all the opponent's king possible moves and checks if no
        matter where the king will go it will still be a checkmate"""
        if can_block_checkmate(temp_game_board, opponent_player_color):
            return False
        else:
            return True
    return False


# A function that checks if a certain player can block the checkmate that being executed on him
def can_block_checkmate(game_board, opponent_color) -> bool:
    temp_game_board = copy.deepcopy(game_board)
    opponent_pieces = WHITE_PIECES if opponent_color == PLAYER_WHITE else BLACK_PIECES
    opponent_player_possible_moves = all_possible_moves(temp_game_board, opponent_color)

    for row in range(8):
        for col in range(8):
            obj = game_board[row][col]
            if obj in opponent_pieces:
                piece_row, piece_col = row, col
                for move in opponent_player_possible_moves:
                    if is_valid_move((piece_row, piece_col), move, game_board, opponent_color):
                        if not is_opponent_king_still_in_check((piece_row, piece_col), move, temp_game_board, opponent_color):
                            return True
    return False


# Generates all the desired king's possible moves
def king_possible_moves(king_color, game_board) -> list[tuple]:
    possible_moves = []
    king_pos = king_location_finder(game_board, king_color)
    for board_line in range(8):
        for board_column in range(8):
            if (is_valid_move(king_pos, (board_line, board_column), game_board, king_color)) and \
                    (board_line, board_column) not in possible_moves:
                possible_moves.append((board_line, board_column))
    return possible_moves


# Receives every time another move for the opponent king and checks if the king is still in check after the movement
def is_opponent_king_still_in_check(start_pos, end_pos, game_board: list[list], opponent_player_color) -> bool:
    temp_game_board = piece_movement_help(start_pos, end_pos, game_board)
    opponent_king_color = BLACK_KING if opponent_player_color == PLAYER_BLACK else WHITE_KING
    current_player_color = PLAYER_BLACK if opponent_player_color == PLAYER_WHITE else PLAYER_WHITE
    king_location = king_location_finder(temp_game_board, opponent_king_color)
    current_player_possible_moves = all_possible_moves(temp_game_board, current_player_color)
    for move in current_player_possible_moves:
        if move == king_location:
            return True
    return False


# Checks if the current king is in check in a case to prevent the player to move illegal pieces while their king is in check
def is_current_king_in_check(start_pos, end_pos, game_board, current_player_color) -> bool:
    help_board = copy.deepcopy(game_board)
    temp_game_board = piece_movement_help(start_pos, end_pos, help_board)
    current_king_color = BLACK_KING if current_player_color == PLAYER_BLACK else WHITE_KING
    opponent_player_color = PLAYER_WHITE if current_player_color == PLAYER_BLACK else PLAYER_BLACK
    king_location = king_location_finder(temp_game_board, current_king_color)
    opponent_player_possible_moves = all_possible_moves(temp_game_board, opponent_player_color)
    if king_location in opponent_player_possible_moves:
        return True
    return False


# A function that checks for a stalemate and return True only when there is a stalemate
def is_there_stalemate(king_all_possible_moves, opponent_king_color, game_board) -> bool:
    current_player_color = PLAYER_BLACK if opponent_king_color == WHITE_KING else PLAYER_WHITE
    opponent_player_color = PLAYER_WHITE if current_player_color == PLAYER_BLACK else PLAYER_BLACK
    temp_game_board = copy.deepcopy(game_board)
    current_player_all_possible_moves = all_possible_moves(temp_game_board, current_player_color)
    king_location = king_location_finder(temp_game_board, opponent_king_color)
    if not king_all_possible_moves:
        return False
    values_list = []
    shard_moves = []
    for move in king_all_possible_moves:
        if move in current_player_all_possible_moves:
            shard_moves.append(move)
    for move in king_all_possible_moves:
        if is_current_king_in_check(king_location, move, temp_game_board, opponent_player_color) \
                and not can_block_checkmate(temp_game_board, opponent_player_color):
            values_list.append(True)
        else:
            values_list.append(False)
    if all(values_list) and values_list != []:
        return True
    for row in game_board:
        for piece in row:
            if piece != EMPTY_CELL:
                if piece != BLACK_KING and piece != WHITE_KING:
                    return False
    else:
        return True


# A function a finds the spot of a desired king
def king_location_finder(game_board, king_color) -> tuple:
    found_king = False
    king_location = ()
    for row in game_board:
        for piece in row:
            if piece == king_color:
                king_location = (game_board.index(row), row.index(piece))
                found_king = True
                break
        if found_king:
            break
    return king_location


# Generates all the possible moves for the desired player
def all_possible_moves(game_board: list, player_color) -> list[tuple]:
    pieces_color = WHITE_PIECES if player_color == PLAYER_WHITE else BLACK_PIECES
    possible_moves = []
    for row in range(8):
        for col in range(8):
            curr_piece = (row, col)
            piece_row, piece_col = curr_piece[0], curr_piece[1]
            if game_board[piece_row][piece_col] not in pieces_color:
                continue
            for board_line in range(8):
                for board_column in range(8):
                    if is_valid_move(curr_piece, (board_line, board_column), game_board, player_color) and (board_line, board_column) not in possible_moves:
                        possible_moves.append((board_line, board_column))
    return possible_moves


# A function that moves the pieces on the board
def move_pieces_on_board(start, end, game_board) -> None:
    start_col, start_row = start[-1], start[0]
    end_col, end_row = end[-1], end[0]
    game_board[end_row][end_col] = game_board[start_row][start_col]
    game_board[start_row][start_col] = EMPTY_CELL


# Returns a new board which contains a copy of the actual board after a movement that is called in 2 of the functions above
def piece_movement_help(start, end, game_board) -> list[list]:
    temp_game_board = copy.deepcopy(game_board)
    start_col, start_row = start[-1], start[0]
    end_col, end_row = end[-1], end[0]
    temp_game_board[end_row][end_col] = temp_game_board[start_row][start_col]
    temp_game_board[start_row][start_col] = EMPTY_CELL
    return temp_game_board


# Checks if there is a valid castling
def valid_castling(start, end, game_board) -> bool:
    start_row, start_col = start[0], start[-1]
    end_row, end_col = end[0], end[-1]
    col_dir = -1 if end_col < start_col else 1
    piece = game_board[start_row][start_col]
    target = game_board[end_row][end_col]
    is_valid = True
    if (piece == WHITE_KING and target == WHITE_ROOK) or (piece == BLACK_KING and target == BLACK_ROOK):
        for col in range(start_col + col_dir, end_col + col_dir, col_dir):
            if col == end_col:
                break
            if game_board[start_row][col] != EMPTY_CELL:
                is_valid = False
    else:
        return False
    if is_valid:
        if col_dir == 1:
            game_board[start_row][6] = piece
            game_board[start_row][5] = target
            game_board[start_row][7] = EMPTY_CELL
            game_board[start_row][4] = EMPTY_CELL
        else:
            game_board[start_row][2] = piece
            game_board[start_row][3] = target
            game_board[start_row][0] = EMPTY_CELL
            game_board[start_row][4] = EMPTY_CELL
        return True
    return False


# Checks for a valid En passant capture
def is_valid_en_passant(start, end, game_board):
    start_row, start_col = start[0], start[-1]
    end_row, end_col = end[0], end[-1]
    piece = game_board[start_row][start_col]
    opponent_pawn = BLACK_PAWN if piece == WHITE_PAWN else WHITE_PAWN
    current_pawn = WHITE_PAWN if opponent_pawn == BLACK_PAWN else BLACK_PAWN
    if piece != current_pawn:
        return False
    if game_board[end_row][end_col] == EMPTY_CELL and (start_row == 4 if piece == BLACK_PAWN else start_row == 3):
        if start_col == 7:
            if game_board[start_row][start_col - 1] == opponent_pawn:
                game_board[start_row][start_col - 1] = EMPTY_CELL
                return True
        elif start_col == 0:
            if game_board[start_row][start_col + 1] == opponent_pawn:
                game_board[start_row][start_col + 1] = EMPTY_CELL
                return True
        else:
            if game_board[start_row][start_col + 1] == opponent_pawn:
                game_board[start_row][start_col + 1] = EMPTY_CELL
                return True
            if game_board[start_row][start_col - 1] == opponent_pawn:
                game_board[start_row][start_col - 1] = EMPTY_CELL
                return True
    else:
        return False


# A function that takes care of the pawn's promotion
def can_pawn_promotion(start, end, game_board, player_color) -> None:
    promotion_options = ("Q", 'R', 'N', 'B')
    start_row, start_col = start[0], start[-1]
    end_row, end_col = end[0], end[-1]
    piece = game_board[start_row][start_col]
    if (piece == WHITE_PAWN and end_row == 0) or (piece == BLACK_PAWN and end_row == 7):
        piece_promotion = input(f"Choose the promotion for your pawn {promotion_options}: ")
        while piece_promotion.strip().upper() not in promotion_options:
            print()
            print(f"{piece_promotion} is not available")
            piece_promotion = input(f"Choose the promotion for your pawn {promotion_options}: ")
        if player_color == PLAYER_BLACK:
            game_board[start_row][start_col] = f"{BLACK_PLAYER_COLOR + piece_promotion.strip().upper() + Fore.RESET}"
        else:
            game_board[start_row][start_col] = piece_promotion.strip().upper()


# Returns the user input move as a tuple of (row, col)
def pieces_move(start, end) -> tuple:
    board_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    start_col, start_row = start[0], int(start[-1])
    end_col, end_row = end[0], int(end[-1])
    start_pos = (7 - start_row + 1, board_dict[start_col.upper()])
    end_pos = (7 - end_row + 1, board_dict[end_col.upper()])
    return start_pos, end_pos


# The visual player turn
def player_turn(game_board, player_color) -> None:
    temp_board = copy.deepcopy(game_board)
    castling_executed = False
    while True:
        print()
        print(f"Current player: {player_color}")
        user_input = spots_input()
        start_pos = user_input[0]
        end_pos = user_input[-1]
        move1, move2 = pieces_move(start_pos, end_pos)
        if valid_castling(move1, move2, game_board):
            castling_executed = True
            break
        elif is_valid_en_passant(move1, move2, game_board):
            break
        if is_valid_move(move1, move2, game_board, player_color) and not is_current_king_in_check(move1, move2, temp_board, player_color):
            can_pawn_promotion(move1, move2, game_board, player_color)
            break
        elif is_current_king_in_check(move1, move2, temp_board, player_color) and is_valid_move(move1, move2, game_board, player_color):
            print("This move is not allowed. Your king is in check or will be in check.\n")
        else:
            print("This move is not allowed.")
    if castling_executed:
        pass
    else:
        move_pieces_on_board(move1, move2, game_board)
    print_board(game_board)


# A main loop
def main():
    see_game_info = input("Before playing, do you want to get some info about the game and learn how to play (y/n)?\n").upper().strip()
    if see_game_info == "Y":
        print(GAME_INFO)
        input("Press enter to continue")

    curr_player_color = PLAYER_WHITE
    opponent_color = PLAYER_BLACK
    game_board = board_creation()
    print_board(game_board)
    while True:
        player_turn(game_board, curr_player_color)
        current_player_moves = all_possible_moves(game_board, curr_player_color)
        opponent_king = WHITE_KING if curr_player_color == PLAYER_BLACK else BLACK_KING
        current_king_moves = king_possible_moves(opponent_king, game_board)

        if is_checkmate(current_player_moves, game_board, opponent_color):
            print(f"{curr_player_color} wins!")
            break
        if is_there_stalemate(current_king_moves, opponent_king, game_board):
            print("Draw!")
            break
        if curr_player_color == PLAYER_WHITE:
            curr_player_color = PLAYER_BLACK
            opponent_color = PLAYER_WHITE
        else:
            curr_player_color = PLAYER_WHITE
            opponent_color = PLAYER_BLACK


if __name__ == '__main__':
    main()
