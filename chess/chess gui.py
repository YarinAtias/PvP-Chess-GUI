import pygame
import chess_console

pygame.init()  # Initialize Pygame
WIDTH, HEIGHT = 700, 600  # Set the window dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
board_image = pygame.image.load("chess_board.png")  # Load the chessboard image
board = pygame.transform.scale(board_image, (WIDTH, HEIGHT))

# Define some constants and piece images
WHITE = (255, 255, 255)
PIECE_WIDTH, PIECE_HEIGHT = 57, 65

# Define the file paths to piece images
WHITE_PAWN_IMAGE = "white pawn.png"
WHITE_ROOK_IMAGE = "white rook.png"
WHITE_KNIGHT_IMAGE = "white knight.png"
WHITE_BISHOP_IMAGE = "white bishop.png"
WHITE_QUEEN_IMAGE = "white queen.png"
WHITE_KING_IMAGE = "white king.png"
BLACK_PAWN_IMAGE = "black pawn.png"
BLACK_ROOK_IMAGE = "black rook.png"
BLACK_KNIGHT_IMAGE = "black knight.png"
BLACK_BISHOP_IMAGE = "black bishop.png"
BLACK_QUEEN_IMAGE = "black queen.png"
BLACK_KING_IMAGE = "black king.png"
WHITE_PAWN_ID = chess_console.WHITE_PAWN
WHITE_ROOK_ID = chess_console.WHITE_ROOK
WHITE_KNIGHT_ID = chess_console.WHITE_KNIGHT
WHITE_BISHOP_ID = chess_console.WHITE_BISHOP
WHITE_QUEEN_ID = chess_console.WHITE_QUEEN
WHITE_KING_ID = chess_console.WHITE_KING
BLACK_PAWN_ID = chess_console.BLACK_PAWN
BLACK_ROOK_ID = chess_console.BLACK_ROOK
BLACK_KNIGHT_ID = chess_console.BLACK_KNIGHT
BLACK_BISHOP_ID = chess_console.BLACK_BISHOP
BLACK_QUEEN_ID = chess_console.BLACK_QUEEN
BLACK_KING_ID = chess_console.BLACK_KING
WHITE_PLAYER = chess_console.PLAYER_WHITE
BLACK_PLAYER = chess_console.PLAYER_BLACK

# Define the positions of the board squares
BOARD_SQUARES_POS = [
    (15, 10), (100, 10), (190, 10), (275, 10), (365, 10), (450, 10), (540, 10), (630, 10),
    (15, 80), (100, 80), (190, 80), (275, 80), (365, 80), (450, 80), (540, 80), (630, 80),
    (15, 160), (100, 160), (190, 160), (275, 160), (365, 160), (450, 160), (540, 160), (630, 160),
    (15, 230), (100, 230), (190, 230), (275, 230), (365, 230), (450, 230), (540, 230), (630, 230),
    (15, 310), (100, 310), (190, 310), (275, 310), (365, 310), (450, 310), (540, 310), (630, 310),
    (15, 380), (100, 380), (190, 380), (275, 380), (365, 380), (450, 380), (540, 380), (630, 380),
    (15, 450), (100, 450), (190, 450), (275, 450), (365, 450), (450, 450), (540, 450), (630, 450),
    (15, 530), (100, 530), (190, 530), (275, 530), (365, 530), (450, 530), (540, 530), (630, 530),
]


# Define a class to represent chess pieces
class Piece:
    # Constructor method
    def __init__(self, piece_id, color, image, pos):
        self.piece_id = piece_id
        self.color = color
        self.image = image
        self.pos = pos

    # Function that loads piece image when calling it
    def load_image(self):
        piece_image = pygame.image.load(self.image)
        piece_image = pygame.transform.scale(piece_image, (PIECE_WIDTH, PIECE_HEIGHT))
        screen.blit(piece_image, self.pos)


# Create instances of white chess pieces
w_pawn_1 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (15, 450))
w_pawn_2 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (100, 450))
w_pawn_3 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (190, 450))
w_pawn_4 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (275, 450))
w_pawn_5 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (365, 450))
w_pawn_6 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (450, 450))
w_pawn_7 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (540, 450))
w_pawn_8 = Piece(WHITE_PAWN_ID, WHITE_PLAYER, WHITE_PAWN_IMAGE, (630, 450))

w_rook_1 = Piece(WHITE_ROOK_ID, WHITE_PLAYER, WHITE_ROOK_IMAGE, (15, 530))
w_rook_2 = Piece(WHITE_ROOK_ID, WHITE_PLAYER, WHITE_ROOK_IMAGE, (630, 530))

w_knight_1 = Piece(WHITE_KNIGHT_ID, WHITE_PLAYER, WHITE_KNIGHT_IMAGE, (100, 530))
w_knight_2 = Piece(WHITE_KNIGHT_ID, WHITE_PLAYER, WHITE_KNIGHT_IMAGE, (540, 530))

w_bishop_1 = Piece(WHITE_BISHOP_ID, WHITE_PLAYER, WHITE_BISHOP_IMAGE, (190, 530))
w_bishop_2 = Piece(WHITE_BISHOP_ID, WHITE_PLAYER, WHITE_BISHOP_IMAGE, (450, 530))

w_queen = Piece(WHITE_QUEEN_ID, WHITE_PLAYER, WHITE_QUEEN_IMAGE, (275, 530))
w_king = Piece(WHITE_KING_ID, WHITE_PLAYER, WHITE_KING_IMAGE, (365, 530))
# ------------------------------------------------------------------
# Create instances for black chess pieces
b_pawn_1 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (15, 80))
b_pawn_2 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (100, 80))
b_pawn_3 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (190, 80))
b_pawn_4 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (275, 80))
b_pawn_5 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (365, 80))
b_pawn_6 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (450, 80))
b_pawn_7 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (540, 80))
b_pawn_8 = Piece(BLACK_PAWN_ID, BLACK_PLAYER, BLACK_PAWN_IMAGE, (630, 80))

b_rook_2 = Piece(BLACK_ROOK_ID, BLACK_PLAYER, BLACK_ROOK_IMAGE, (630, 10))
b_rook_1 = Piece(BLACK_ROOK_ID, BLACK_PLAYER, BLACK_ROOK_IMAGE, (15, 10))

b_knight_1 = Piece(BLACK_KNIGHT_ID, BLACK_PLAYER, BLACK_KNIGHT_IMAGE, (100, 10))
b_knight_2 = Piece(BLACK_KNIGHT_ID, BLACK_PLAYER, BLACK_KNIGHT_IMAGE, (540, 10))

b_bishop_1 = Piece(BLACK_BISHOP_ID, BLACK_PLAYER, BLACK_BISHOP_IMAGE, (190, 10))
b_bishop_2 = Piece(BLACK_BISHOP_ID, BLACK_PLAYER, BLACK_BISHOP_IMAGE, (450, 10))

b_queen = Piece(BLACK_QUEEN_ID, BLACK_PLAYER, BLACK_QUEEN_IMAGE, (275, 10))
b_king = Piece(BLACK_KING_ID, BLACK_PLAYER, BLACK_KING_IMAGE, (365, 10))

# Create a list of all chess pieces
ALL_PIECES = [w_pawn_1, w_pawn_2, w_pawn_3, w_pawn_4, w_pawn_5, w_pawn_6, w_pawn_7, w_pawn_8,
              w_rook_1, w_rook_2,
              w_knight_1, w_knight_2,
              w_bishop_1, w_bishop_2,
              w_queen, w_king,

              b_pawn_1, b_pawn_2, b_pawn_3, b_pawn_4, b_pawn_5, b_pawn_6, b_pawn_7, b_pawn_8,
              b_rook_1, b_rook_2,
              b_bishop_1, b_bishop_2,
              b_knight_1, b_knight_2,
              b_queen, b_king
              ]


# Function to convert the board state to a matrix
def convert_board_to_matrix() -> list[list]:
    # Creating a 8x8 matrix board
    help_matrix = [[chess_console.EMPTY_CELL for _ in range(8)] for _ in range(8)]
    for p_obj in ALL_PIECES:
        matrix_pos = square_to_matrix_pos(p_obj.pos)  # Convert the square coordinates into matrix coordinates: (1-8, 1-8)
        row, col = matrix_pos
        help_matrix[row][col] = p_obj.piece_id  # Assigns to every spot on the matrix board the current piece if there is
    return help_matrix


# Function to convert screen coordinates to matrix coordinates
def square_to_matrix_pos(board_position: tuple) -> tuple:
    row = 0
    col = 0
    for square in BOARD_SQUARES_POS:
        if square == board_position:
            return row, col
        col += 1
        if col == 8:
            row += 1
            col = 0


# Initialize the display
def init_board_display() -> None:
    screen.blit(board, (0, 0))
    pygame.display.update()


# Detect the square where the mouse was clicked
def detect_square(mouse_x: int, mouse_y: int):
    square_x = None
    square_y = None
    for x, y in BOARD_SQUARES_POS:
        if x - 10 <= mouse_x <= x + 60:
            square_x = x
        if y - 10 <= mouse_y <= y + 50:
            square_y = y
        if square_x is not None and square_y is not None:
            return square_x, square_y
    return None


# Function to draw the game window
def draw_window() -> None:
    screen.blit(board, (0, 0))  # Displays the new board every time it updates
    if check_mark:  # A condition which handles the appearance of the check mark
        current_king_square = b_king.pos if opponent_player_color == WHITE_PLAYER else w_king.pos
        rect_x = current_king_square[0] - 12
        rect_y = current_king_square[1]
        rect_height = 65
        rect_width = 80
        rect_color = (255, 0, 0)
        my_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, rect_color, my_rect)

    # Loading and showing all pieces images on the board
    for p_obj in ALL_PIECES:
        p_obj.load_image()

    # Handles the promotion display for player white
    if show_promotion_for_white:
        space = 0
        white_promotion_pieces_images = [WHITE_QUEEN_IMAGE, WHITE_KNIGHT_IMAGE, WHITE_BISHOP_IMAGE, WHITE_ROOK_IMAGE]
        border = pygame.Rect(250, 300, 150, 30)
        pygame.draw.rect(screen, (255, 0, 0), border)
        for image in white_promotion_pieces_images:
            image_to_load = pygame.image.load(image)
            image_to_load = pygame.transform.scale(image_to_load, (30, 30))
            screen.blit(image_to_load, (screen.get_width() / 2 - 100 + space, screen.get_height() / 2))
            space += 40

    # Handles the promotion display for player black
    elif show_promotion_for_black:
        space = 0
        black_promotion_pieces_images = [BLACK_QUEEN_IMAGE, BLACK_KNIGHT_IMAGE, BLACK_BISHOP_IMAGE, BLACK_ROOK_IMAGE]
        border = pygame.Rect(250, 300, 150, 30)
        pygame.draw.rect(screen, (255, 0, 0), border)
        for image in black_promotion_pieces_images:
            image_to_load = pygame.image.load(image)
            image_to_load = pygame.transform.scale(image_to_load, (30, 30))
            screen.blit(image_to_load, (screen.get_width() / 2 - 100 + space, screen.get_height() / 2))
            space += 40

    # Handles win scenario display
    if win:
        border = pygame.Rect(270, 275, 160, 50)
        pygame.draw.rect(screen, (0, 200, 0), border)
        if opponent_player_color == WHITE_PLAYER:
            text = f"White wins!"
        else:
            text = f"Black wins!"

        font = pygame.font.Font(None, 36)  # Choose a font and size
        text_surface = font.render(text, True, (255, 255, 255))  # Render the text to a Surface
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)  # Center the text on the screen
        screen.blit(text_surface, text_rect)

        time_text = f"Window closes in {time_count}"
        time_font = pygame.font.Font(None, 24)  # Choose a font and size for the time text
        time_surface = time_font.render(time_text, True, (255, 0, 0))  # Render the time text to a Surface
        time_rect = time_surface.get_rect()
        time_rect.center = (WIDTH // 2, (HEIGHT // 2) + 40)  # Position the time text below the win text
        screen.blit(time_surface, time_rect)

    pygame.display.update()  # Updates frames


# Main game loop
def main():
    # Declaring global variables
    global piece, start_pos, board_as_matrix, show_promotion_for_white, show_promotion_for_black, win, start_square
    global opponent_player_color, check_mark, time_count
    time_count = 30
    FPS = 120
    check_mark = False
    win = False
    show_promotion_for_black = False
    show_promotion_for_white = False
    selected_piece = False
    selected_square = True
    current_player_color = WHITE_PLAYER
    opponent_player_color = BLACK_PLAYER
    clock = pygame.time.Clock()
    init_board_display()
    run = True
    white_promoted_count = 0
    black_promoted_count = 0
    castling_occurred_for_white = False
    castling_occurred_for_black = False
    print("\nIn order to play just click on the piece that you want to move\n"
          "and afterwards click on the square that you want that the piece will be on. White starts!")
    while run:  # starts running the game/program
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if show_promotion_for_white:  # if Show promotion is happening for the white player
                    if 290 <= mouse_y <= 330:
                        if 240 <= mouse_x <= 280:
                            piece.image = WHITE_QUEEN_IMAGE
                            piece.piece_id = WHITE_QUEEN_ID
                        elif 290 <= mouse_x <= 320:
                            piece.image = WHITE_KNIGHT_IMAGE
                            piece.piece_id = WHITE_KNIGHT_ID
                        elif 330 <= mouse_x <= 360:
                            piece.image = WHITE_BISHOP_IMAGE
                            piece.piece_id = WHITE_BISHOP_ID
                        elif 360 <= mouse_x <= 400:
                            piece.image = WHITE_ROOK_IMAGE
                            piece.piece_id = WHITE_ROOK_ID
                        show_promotion_for_white = False

                elif show_promotion_for_black:  # If show promotion is happening for the black player
                    # Change the pawn to the desired piece
                    if 240 <= mouse_x <= 280:
                        piece.image = BLACK_QUEEN_IMAGE
                        piece.piece_id = BLACK_QUEEN_ID
                    elif 290 <= mouse_x <= 320:
                        piece.image = BLACK_KNIGHT_IMAGE
                        piece.piece_id = BLACK_KNIGHT_ID
                    elif 330 <= mouse_x <= 360:
                        piece.image = BLACK_BISHOP_IMAGE
                        piece.piece_id = BLACK_BISHOP_ID
                    elif 360 <= mouse_x <= 400:
                        piece.image = BLACK_ROOK_IMAGE
                        piece.piece_id = BLACK_ROOK_ID
                    show_promotion_for_black = False

                else:  # Else checks for the last click (If the click's purpose was to choose a piece or move it
                    clicked_square = detect_square(mouse_x, mouse_y)
                    if clicked_square is not None:
                        if not selected_square:  # If the 'selected square' has not been selected yet.
                            end_pos = square_to_matrix_pos(clicked_square)  # Tuple (row, col)
                            end_square = clicked_square
                            board_as_matrix = convert_board_to_matrix()
                            target_piece = board_as_matrix[end_pos[0]][end_pos[1]]

                            # Handles castling
                            if chess_console.valid_castling(start_pos, end_pos, board_as_matrix):
                                target_rook = None
                                # Finding the specific object of the rook
                                for p_obj in ALL_PIECES:
                                    if p_obj.pos == end_square:
                                        target_rook = p_obj
                                        break
                                if current_player_color == WHITE_PLAYER and not castling_occurred_for_white:  # Castling for white
                                    if target_rook.pos[0] > 200:
                                        piece.pos = (540, 530)
                                        target_rook.pos = (450, 530)
                                    else:
                                        piece.pos = (190, 530)
                                        target_rook.pos = (275, 530)

                                    current_player_color = BLACK_PLAYER
                                    opponent_player_color = WHITE_PLAYER
                                    castling_occurred_for_white = True

                                elif current_player_color == BLACK_PLAYER and not castling_occurred_for_black:  # Castling for black
                                    if target_rook.pos[0] > 200:
                                        piece.pos = (540, 10)
                                        target_rook.pos = (450, 10)
                                    else:
                                        piece.pos = (190, 10)
                                        target_rook.pos = (275, 10)
                                    current_player_color = WHITE_PLAYER
                                    opponent_player_color = BLACK_PLAYER
                                    castling_occurred_for_black = True

                            # switching between pieces of the same color if a mistake was occurred in selecting piece
                            elif (target_piece in chess_console.BLACK_PIECES and current_player_color == chess_console.PLAYER_BLACK) \
                                    or (target_piece in chess_console.WHITE_PIECES and current_player_color == chess_console.PLAYER_WHITE):
                                for p_obj in ALL_PIECES:
                                    if p_obj.pos == clicked_square:
                                        piece = p_obj
                                        break
                                start_pos = square_to_matrix_pos(clicked_square)  # Makes the last click as the start position
                                selected_square = False
                                selected_piece = True

                            # Handles the case of a regular movement on the board such as capturing or forwardness
                            elif chess_console.is_valid_move(start_pos, end_pos, board_as_matrix, current_player_color) and not \
                                    chess_console.is_current_king_in_check(start_pos, end_pos, board_as_matrix, current_player_color):
                                check_mark = False
                                if board_as_matrix[end_pos[0]][end_pos[1]] != chess_console.EMPTY_CELL:  # Checks the case of capturing opposite piece
                                    captured_piece = None
                                    for p_obj in ALL_PIECES:
                                        if p_obj.pos == clicked_square:
                                            captured_piece = p_obj
                                            break
                                    if captured_piece:
                                        ALL_PIECES.remove(captured_piece)  # Removing the captured piece off the board

                                piece.pos = clicked_square  # Moving the selected piece to the selected square
                                selected_square = True
                                selected_piece = False
                                board_as_matrix = convert_board_to_matrix()

                                current_player_moves = chess_console.all_possible_moves(board_as_matrix, current_player_color)
                                if chess_console.is_checkmate(current_player_moves, board_as_matrix, opponent_player_color):  # Checks for checkmate
                                    selected_piece = True
                                    selected_square = True
                                    win = True
                                    FPS = 1

                                # Change the player color after a move or promotion for white
                                if (piece.color == WHITE_PLAYER and piece.pos[1] == 10 and piece.piece_id == WHITE_PAWN_ID
                                        and white_promoted_count == 0):
                                    show_promotion_for_white = True
                                    white_promoted_count = 1
                                    if current_player_color == BLACK_PLAYER:
                                        current_player_color = WHITE_PLAYER
                                        opponent_player_color = BLACK_PLAYER
                                    else:
                                        current_player_color = BLACK_PLAYER
                                        opponent_player_color = WHITE_PLAYER

                                # Change the player color after a move or promotion for black
                                elif (piece.color == BLACK_PLAYER and piece.pos[1] == 530 and piece.piece_id == BLACK_PAWN_ID
                                      and black_promoted_count == 0):
                                    show_promotion_for_black = True
                                    black_promoted_count = 1
                                    if current_player_color == WHITE_PLAYER:
                                        current_player_color = BLACK_PLAYER
                                        opponent_player_color = WHITE_PLAYER
                                    else:
                                        current_player_color = WHITE_PLAYER
                                        opponent_player_color = BLACK_PLAYER

                                else:
                                    if current_player_color == WHITE_PLAYER:
                                        current_player_color = BLACK_PLAYER
                                        opponent_player_color = WHITE_PLAYER
                                    else:
                                        current_player_color = WHITE_PLAYER
                                        opponent_player_color = BLACK_PLAYER

                            elif chess_console.is_current_king_in_check(start_pos, end_pos, board_as_matrix, current_player_color):
                                check_mark = True

                        elif not selected_piece:  # If 'selected piece' has not been selected yet
                            for piece in ALL_PIECES:
                                if piece.pos == clicked_square and piece.color == current_player_color:
                                    start_square = clicked_square
                                    start_pos = square_to_matrix_pos(clicked_square)  # Tuple (row, col)
                                    selected_piece = True
                                    selected_square = False
                                    break
        draw_window()
        if win:
            time_count -= 1
            if time_count == -1:
                run = False


# Entry point of the program
if __name__ == "__main__":
    main()
