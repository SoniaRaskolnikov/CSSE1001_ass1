from a1 import (
    generate_initial_board,
    is_column_full,
    is_column_empty,
    display_board,
    add_piece,
    remove_piece,
    check_win,
    )


def generate_initial_board_test():
    assert generate_initial_board() == ['--------', '--------', '--------', '--------', '--------', '--------', '--------', '--------']
generate_initial_board_test()

def is_column_full_test():
    assert not is_column_full("---XOXXX") 
    assert is_column_full("OXXOOXOO") 
is_column_full_test()

def is_column_empty_test():
    assert (not is_column_empty("---XOXXX"))
    assert (not is_column_empty("OXXOOXOO"))
    assert is_column_empty("--------") 
is_column_empty_test()

def display_board_test():
    display_board(['--------', '----OOOO', 'XXXXXXXX', '--------', '------XO', '--------', '---XXOXO', '--------'])
    display_board(['Ashleigh', '        ', '-----W--', 'B----i--', '-r---l--', '--a--s--', '---e-o--', '-----n--'])
display_board_test()

# test check_input() manually
# test get_action() manually

def add_piece_test():
    board = ['--------', 'O---OOOO', 'XXXXXXXX', '--------', '------XO','--------', '---XXOXO', '--------']
    assert add_piece(board, "X", 1)
    display_board(board)
    assert not add_piece(board, "O", 2)
    display_board(board)
add_piece_test()

def remove_piece_test():
    board = ['--------', '----OOOO', 'XXOOOXXX', '--------', '------XO','--------', '---XXOXO', '--------']
    assert remove_piece(board, 2)
    assert not remove_piece(board, 0)
remove_piece_test()

def check_win_test():
    board = ['------XO', '-------O', '--------', '--------', '-------O','--------', '--------', '------XX']
    assert check_win(board) is None
    # diagonal
    board = ['-------O', '------OX', '-----OXO', '---XOOXX', '--------','--------', '--------', '--------']
    #board.reverse()
    assert check_win(board) == "O"
    # horizontal
    board = ['-------X', '-------X', '------OX', '---OOOXX', '--------','--------', '--------', '--------']
    assert check_win(board) == "X"
    # both win and vertical and horizontal
    board = ['---XXXXO', '-------O', '-------O', '-------O', '--------','--------', '--------', '--------']
    assert check_win(board) == "-"
check_win_test()