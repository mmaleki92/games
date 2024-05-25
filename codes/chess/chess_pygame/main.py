import pygame
import chess
import sys

# Initialize Pygame
pygame.init()

# Set the size of the window
screen_size = 800
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Chess Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
highlight_color = (50, 50, 250)  # Color for highlighting selected square

# Initialize the chess board
board = chess.Board()

def draw_board(screen):
    tile_size = screen_size // 8
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, white, pygame.Rect(col*tile_size, row*tile_size, tile_size, tile_size))
            else:
                pygame.draw.rect(screen, black, pygame.Rect(col*tile_size, row*tile_size, tile_size, tile_size))

# Assuming each square's size is determined by dividing the screen size by 8
tile_size = screen_size // 8

piece_images = {}
for piece in chess.PIECE_TYPES:
    for color in (chess.WHITE, chess.BLACK):
        piece_name = f'{chess.piece_name(piece).capitalize()}{"W" if color == chess.WHITE else "B"}'
        # Load the image
        image = pygame.image.load(f'images/{piece_name}.svg').convert_alpha()
        # Resize the image to fit the tile size
        piece_images[f'{piece}_{color}'] = pygame.transform.scale(image, (tile_size, tile_size))

def draw_pieces(screen, board):
    tile_size = screen_size // 8
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            image = piece_images[f'{piece.piece_type}_{piece.color}']
            # Calculate the position based on the square
            col = square % 8
            row = square // 8
            screen.blit(image, (col * tile_size, (7 - row) * tile_size))

selected_square = None  # Stores the currently selected square

def screen_to_board_pos(x, y):
    """Convert screen coordinates to chess board coordinates."""
    row = y // (screen_size // 8)
    col = x // (screen_size // 8)
    return chess.square(col, 7-row)

# Function to highlight selected square
def highlight_square(screen, square):
    if square is not None:
        s = pygame.Surface((tile_size, tile_size))  # Create a surface for highlighting
        s.set_alpha(100)  # Transparency (0-255)
        s.fill(highlight_color)
        screen.blit(s, ((square % 8) * tile_size, (7 - square // 8) * tile_size))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // tile_size
            row = 7 - (pos[1] // tile_size)
            square = chess.square(col, row)

            if selected_square is None:
                # Select the square if it has a piece and it's the correct turn
                piece = board.piece_at(square)
                if piece and ((piece.color == chess.WHITE and board.turn == chess.WHITE) or 
                            (piece.color == chess.BLACK and board.turn == chess.BLACK)):
                    selected_square = square
            else:
                # Determine if the move is a promotion
                is_promotion = board.piece_at(selected_square) == chess.Piece(chess.PAWN, board.turn) and \
                            (row == 0 or row == 7)

                # Create the move, specifying promotion to a queen if applicable
                move = chess.Move(selected_square, square, promotion=chess.QUEEN if is_promotion else None)
                
                if move in board.legal_moves:
                    board.push(move)
                selected_square = None



    screen.fill(white)
    draw_board(screen)
    highlight_square(screen, selected_square)
    draw_pieces(screen, board)
    pygame.display.flip()

pygame.quit()