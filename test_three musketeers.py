import pytest

from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'



board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 = [ [_, _, _, _, M],
            [_, _, R, _, _],
            [_, R, M, R, _],
            [M, R, _, _, _],
            [R, _, _, R, _] ]



def test_create_board():
    create_board()
    assert at((0,0)) == 'R'
    assert at((0,4)) == 'M'
    assert at((1,1)) == 'R'
    assert at((2,2)) == 'M'
    assert at((4,0)) == 'M'
    

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    assert at((4,3)) == R
    set_board(board2)
    assert at((0,0)) == _
    assert at((0,4)) == M
    assert at((1,3)) == _    
    assert at((4,3)) == R

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    set_board(board2)
    assert board2 == get_board()

def test_all_locations():
    assert all_locations() == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]
  

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
        string_to_location('F3')
        string_to_location('X6')
        string_to_location('A6')
    assert string_to_location('A1') == (0,0)
    assert string_to_location('A2') == (0,1)
    assert string_to_location('A5') == (0,4)
    assert string_to_location('B5') == (1,4)
    

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((6,0))
        location_to_string((10,0))
        location_to_string((6,7))
        location_to_string((2,7))
        location_to_string((1,8))
    assert location_to_string((0,0)) == 'A1'
    assert location_to_string((0,1)) == 'A2'
    assert location_to_string((0,4)) == 'A5'
    assert location_to_string((1,4)) == 'B5'
    assert location_to_string((2,0)) == 'C1'
    assert location_to_string((3,3)) == 'D4'
    assert location_to_string((4,0)) == 'E1'
    assert location_to_string((4,2)) == 'E3'

def test_at():
    set_board(board1)
    assert at((0,0)) == '-'
    
  

def test_adjacent_location():
    assert adjacent_location((0,0),'right') == (0,1)
    assert adjacent_location((0,4),'left') == (0,3)
    assert adjacent_location((0,3),'down') == (1,3)
    assert adjacent_location((2,2),'up') == (1,2)
    assert adjacent_location((4,4),'left') == (4,3)
    assert adjacent_location((3,2),'right') == (3,3)
    assert adjacent_location((1,2),'down') == (2,2)
    
    
def test_is_legal_move_by_musketeer():
    create_board()
    with pytest.raises(ValueError):
        is_legal_move_by_musketeer((0,0), 'right')
        is_legal_move_by_musketeer((2,2), 'right')
        is_legal_move_by_musketeer((5,6), 'right')
    assert is_legal_move_by_musketeer((0,4), 'right') == False
    assert is_legal_move_by_musketeer((0,4), 'down') == True
    assert is_legal_move_by_musketeer((0,4), 'left') == True
    assert is_legal_move_by_musketeer((0,4), 'up') == False
    assert is_legal_move_by_musketeer((2,2), 'up') == True
    assert is_legal_move_by_musketeer((2,2), 'right') == True
    assert is_legal_move_by_musketeer((4,0), 'right') == True
    assert is_legal_move_by_musketeer((4,0), 'left') == False
    
    
def test_is_legal_move_by_enemy():
    create_board()
    with pytest.raises(ValueError):
        is_legal_move_by_enemy((0,4), 'left')
        is_legal_move_by_enemy((2,2), 'right')
        is_legal_move_by_enemy((4,0), 'up')
        is_legal_move_by_enemy((5,0), 'down')
    assert is_legal_move_by_enemy((1,2), 'right') == False
    assert is_legal_move_by_enemy((1,2), 'left') == False
    set_board(board1)
    assert is_legal_move_by_enemy((1,2), 'up') == True
    assert is_legal_move_by_enemy((1,2), 'left') == True
    assert is_legal_move_by_enemy((1,2), 'right') == False
    assert is_legal_move_by_enemy((1,2), 'down') == False

def test_is_legal_move():
    create_board()
    assert is_legal_move((0,0), 'right') == False
    assert is_legal_move((0,0), 'left') == False
    assert is_legal_move((0,0), 'down') == False
    assert is_legal_move((4,4), 'right') == False
    assert is_legal_move((4,4), 'up') == False
    assert is_legal_move((4,4), 'left') == False

    assert is_legal_move((0,4), 'right') == False
    assert is_legal_move((0,4), 'down') == True
    assert is_legal_move((0,4), 'left') == True
    assert is_legal_move((0,4), 'up') == False
    assert is_legal_move((2,2), 'up') == True
    assert is_legal_move((2,2), 'right') == True
    assert is_legal_move((4,0), 'right') == True
    assert is_legal_move((4,0), 'left') == False

def test_can_move_piece_at():
    create_board()
    assert can_move_piece_at((0,0)) == False
    assert can_move_piece_at((0,1)) == False
    assert can_move_piece_at((0,2)) == False
    assert can_move_piece_at((0,3)) == False
    assert can_move_piece_at((0,4)) == True
    assert can_move_piece_at((1,0)) == False
    assert can_move_piece_at((1,1)) == False
    assert can_move_piece_at((2,2)) == True
    assert can_move_piece_at((4,0)) == True
    assert can_move_piece_at((4,1)) == False
    set_board(board1)
    assert can_move_piece_at((2,1)) == True
    assert can_move_piece_at((1,2)) == True

def test_has_some_legal_move_somewhere():
    create_board()
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    board3 =[ [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, M, M],
            [_, _, _, M, R] ]
    set_board(board3)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == False
    board4 =[ [_, _, _, _, _],
            [_, _, R, _, _],
            [M, _, _, _, _],
            [_, _, _, _, M],
            [_, _, _, M, _] ]
    set_board(board4)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True 

def test_possible_moves_from():
    create_board()
    assert possible_moves_from((0,4)) == ['down', 'left']
    assert possible_moves_from((2,2)) == ['up', 'right', 'down', 'left']
    assert possible_moves_from((4,0)) == ['up', 'right']
    assert possible_moves_from((1,4)) == []
    assert possible_moves_from((4,4)) == []
    

def test_is_legal_location():
    assert is_legal_location((0,0)) == True
    assert is_legal_location((4,0)) == True
    assert is_legal_location((2,2)) == True
    assert is_legal_location((3,1)) == True
    assert is_legal_location((0,5)) == False
    assert is_legal_location((2,6)) == False
    assert is_legal_location((6,6)) == False
    assert is_legal_location((5,6)) == False
    assert is_legal_location((6,4)) == False
    assert is_legal_location((5,2)) == False

def test_is_within_board():
    create_board()
    assert is_within_board((0,0), 'right') == True
    assert is_within_board((0,0), 'left') == False
    assert is_within_board((0,0), 'up') == False
    assert is_within_board((4,0), 'up') == True
    assert is_within_board((4,0), 'left') == False
    assert is_within_board((4,0), 'down') == False
    assert is_within_board((4,4), 'down') == False
    assert is_within_board((4,4), 'right') == False
    assert is_within_board((4,4), 'up') == True
    assert is_within_board((6,4), 'up') == False
    assert is_within_board((5,5), 'up') == False
    assert is_within_board((4,5), 'up') == False

def test_all_possible_moves_for():
    board5 =[ [_, _, _, _, _],
            [_, _, R, _, _],
            [M, _, _, _, _],
            [_, _, _, _, M],
            [_, _, _, M, _] ]
    set_board(board5)
    assert all_possible_moves_for('M') == []
    assert all_possible_moves_for('R') == [[(1,2),"up"], [(1,2),"right"], [(1,2),"down"],[(1,2),"left"]]


    
def test_make_move():
    create_board()
    make_move((0,4), "left")
    get_board() == [ ['R', 'R', 'R', 'M', '-'],
      ['R', 'R', 'R', 'R', 'R'],
      ['R', 'R', 'M', 'R', 'R'],
      ['R', 'R', 'R', 'R', 'R'],
      ['M', 'R', 'R', 'R', 'R'] ]


def test_is_enemy_win():
    board6 = [ [_, _, _, _, _], [_, _, M, M, M],[_, R, _, R, _],[_, _, _, _, _],[_, _, _, R, _] ]
    set_board(board6)
    assert is_enemy_win() == True
    board7 = [ [_, _, M, _, _], [_, _, M, _, _],[_, R, M, R, _],[_, _, _, _, _],[_, _, _, R, _] ]
    set_board(board7)
    assert is_enemy_win() == True
    board8 = [ [_, _, M, _, _], [_, _, M, M, _],[_, R, _, R, _],[_, _, _, _, _],[_, _, _, R, _] ]
    set_board(board8)
    assert is_enemy_win() == False
