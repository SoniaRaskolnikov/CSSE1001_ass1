# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name: Zachariah Jones
# Student Number: 48775467
# ----------------

def num_hours() -> float:
    """Returns number of hours worked on this assignment.
    
    Returns:
        Float of how many hours this assignment has been worked on."""
    return 2.

def generate_initial_board() -> list[str]:
    """Generates an empty board full of BLANK_PIECE.

    Returns:
        An empty board as a list of strings.
    """
    return [BLANK_PIECE * BOARD_SIZE] * BOARD_SIZE

def is_column_full(column: str) -> bool:
    """Checks if a given column is full.

    Args:
        column (str): The given column to check

    Returns:
        Whether the column is full or not as a bool
    """
    return not BLANK_PIECE in column

def is_column_empty(column: str) -> bool:
    """Checks if a given column is empty.

    Args:
        column (str): The given column to check

    Returns:
        Whether the column is empty or not as a bool
    """
    return column == BLANK_PIECE * BOARD_SIZE

def display_board(board: list[str]) -> None:
    """Prints the board.

    Each column is enumerated and are seperated by COLUMN_SEPERATOR.

    Args:
        board (list[str]): Board to be displayed
    """
    for row_number in range(BOARD_SIZE):
        row = ""
        for column in board:
            row += column[row_number]
        
        print("|" + "|".join(row) + "|")

    for i in range(BOARD_SIZE):
        print(end=f" {i+1}")

    print(" ")
    
def check_input(command: str) -> bool:
    """Checks command for errors as specified in the first two rows of Table 2.

    (prints the relevant error message)

    Args:
        command (str): Command to be inspected.

    Returns:
        Whether or not an error was identified as a bool.
    """
    if len(command) == 0:
        print(INVALID_FORMAT_MESSAGE)
        return False
    
    action = command[0].lower()
    if action not in "arhq":
        print(INVALID_FORMAT_MESSAGE)
        return False
    
    # Check format errors for adding and removing a piece
    if action in "ar":
        # Check for superfluous characters
        if command[2:]:
            print(INVALID_FORMAT_MESSAGE)
            return False
        # "Not followed by a single digit integer"
        # Assuming that doesn't include negative numbers
        if not command[1:] or command[1] not in "0123456789":
            print(INVALID_FORMAT_MESSAGE)
            return False
        
        column_number = int(command[1:]) # typecast can't fail ?
        if column_number < 1 or BOARD_SIZE < column_number:
            print(INVALID_COLUMN_MESSAGE)
            return False

    # Check format errors for help and quit commands
    if action in "hq":
        if command[1:]:
            print(INVALID_FORMAT_MESSAGE)
            return False
    
    return True

def get_action() -> str:
    """Repeatedly prompts user for command, until a valid one is given.

    (Valid according to check_input())

    Returns:
        Valid action.
    """
    while True:
        action = input(ENTER_COMMAND_MESSAGE)
        if check_input(action):
            return action

def add_piece(board: list[str], piece: str, column_index: int) -> bool:
    """Adds a piece to a specified column on the board, if there is space.

    (Prints error message and returns false, if there is not space)

    Args:
        board (list[str]): The board in play.
        piece (str): The piece character to be placed.
        column_index (int): The index of which column to place the piece in.

    Returns:
        Whether or not the column was full as a bool.
    """
    selected_column = board[column_index]
    if is_column_full(selected_column):
        print(FULL_COLUMN_MESSAGE)
        return False

    row_idx = BOARD_SIZE - selected_column[::-1].index(BLANK_PIECE) - 1
    board[column_index] = selected_column[:row_idx] + piece + selected_column[row_idx + 1:]
    return True

def remove_piece(board: list[str], column_index: int) -> bool:
    """Removes a piece from a specified column, if it isn't empty.

    (Prints error message and returns false, if the column is empty)

    Args:
        board (list[str]): The board in play.
        column_index (int): The index of the column to remove a piece from.

    Returns:
        Whether or not the column is empty as a bool.
    """
    selected_column = board[column_index]
    if is_column_empty(selected_column):
        print(EMPTY_COLUMN_MESSAGE)
        return False
    
    new_column = BLANK_PIECE + selected_column[:-1]
    board[column_index] = new_column
    return True

def check_win(board: list[str]) -> Optional[str]:
    """Checks the board for 4 connected pieces, either horizontally, vertically, or diagonally.

    Args:
        board (list[str]): The board in play.

    Returns:
        Returns the character of whichever piece has won.
        Returns BLANK_PIECE, if it's a draw.
        Returns None, if no win is found.
    """
    PLAYER_1_WIN = False
    PLAYER_2_WIN = False

    full_columns = 0
    for column in board:
        if is_column_full(column):
            full_columns += 1

    if full_columns == BOARD_SIZE:
        return BLANK_PIECE

    # Downward vertical scan
    for i in range(BOARD_SIZE - 3):
        for j in range(BOARD_SIZE - 3):
            # create diagonal from board[i][j]
            scan = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3]
            #scan = [board[i + n][j + n] for n in range(4)]
            if scan == PLAYER_1_PIECE * 4:
                PLAYER_1_WIN = True
            if scan == PLAYER_2_PIECE * 4:
                PLAYER_2_WIN = True

    # Upward vertical scan
    for i in range(BOARD_SIZE - 3):
        for j in range(3, BOARD_SIZE):
            # create diagonal from board[i][j]
            scan = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3]
            #scan = [board[i - n][j - n] for n in range(4)]
            if scan == PLAYER_1_PIECE * 4:
                PLAYER_1_WIN = True
            if scan == PLAYER_2_PIECE * 4:
                PLAYER_2_WIN = True

    # horizontal and vertical scan 
    for i in range(BOARD_SIZE - 3):
        for j in range(BOARD_SIZE):
            horizontal_scan = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j] 
            vertical_scan = board[j][i:i + 4]
            if horizontal_scan == PLAYER_1_PIECE * 4 or vertical_scan == PLAYER_1_PIECE * 4:
                PLAYER_1_WIN = True
            if horizontal_scan == PLAYER_2_PIECE * 4 or vertical_scan == PLAYER_2_PIECE * 4:
                PLAYER_2_WIN = True

    if PLAYER_1_WIN and PLAYER_2_WIN:
        return BLANK_PIECE
    elif PLAYER_1_WIN:
        return PLAYER_1_PIECE
    elif PLAYER_2_WIN:
        return PLAYER_2_PIECE

def get_opposite_peice(piece: str) -> str:
    """Returns other player's piece.

    (Helper function not required for assignment)

    Args:
        piece (str): piece to be switched

    Returns:
        The piece opposite to the one passed in.
        If piece is not either player's piece, PLAYER_1_PIECE will be returned.
    """
    if piece == PLAYER_1_PIECE:
        return PLAYER_2_PIECE
    else: 
        return PLAYER_1_PIECE

def play_game() -> None:
    """Implementation of game logic (Steps 1-7)"""
    winner = ""

    board = generate_initial_board()
    move = PLAYER_1_PIECE
    # Steps 1-6 repeat until someone wins or draws
    while not winner:
        # Step 1
        display_board(board)
        # Step 2
        if move == PLAYER_1_PIECE:
            print(PLAYER_1_MOVE_MESSAGE)
        else:
            print(PLAYER_2_MOVE_MESSAGE)
        
        moved = False
        # User is prompted for a move until a valid one is given
        while not moved:
            # Prompt user for input
            action = get_action()
            command = action[0].lower()
            # checks for type of command
            if command == "h":
                print(HELP_MESSAGE)
            elif command == "q":
                winner = get_opposite_peice(move)
                moved = True
            elif command == "a":
                column_idx = int(action[1]) - 1
                # only exits the loop if move is valid
                if add_piece(board, move, column_idx):
                    moved = True
            elif command == "r":
                column_idx = int(action[1]) - 1
                # only exits the loop if move is valid
                if remove_piece(board, column_idx):
                    moved = True
        
        move = get_opposite_peice(move)
        # this doesn't happen only when a player quits
        if not winner:
            winner = check_win(board)
    
    display_board(board)
    # Step 7
    if winner == BLANK_PIECE:
        print(DRAW_MESSAGE)
    elif winner == PLAYER_1_PIECE:
        print(PLAYER_1_VICTORY_MESSAGE)
    elif winner == PLAYER_2_PIECE:
        print(PLAYER_2_VICTORY_MESSAGE)


def main() -> None:
    """The main function"""
    while True:
        play_game()
        if input(CONTINUE_MESSAGE).lower() != "y":
            break

if __name__ == "__main__":
    main()
