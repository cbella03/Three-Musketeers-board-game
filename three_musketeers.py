# The Three Musketeers Game
\
# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board


def all_locations():
    """Returns a list of all 25 locations on the board."""
    return [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)]


def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    all_loc = all_locations()
    letters = list('ABCDE')
    numbers = [i for i in range(1, 6)]
    locs = [x+str(y) for x in letters for y in numbers]
    list_loc = dict(zip(locs, all_loc))
    if s not in list_loc:
        raise ValueError
    else:
        return list_loc[s]

#def string_to_location(s):
    
 #   all_locations_ = all_locations()
  #  list_locations = [[all_locations_[0], 'A1'], [all_locations_[1], 'A2'], [all_locations_[2], 'A3'], [all_locations_[3], 'A4'], [all_locations_[4], 'A5'], [all_locations_[5], 'B1'], [all_locations_[6], 'B2'], [all_locations_[7], 'B3'], [all_locations_[8], 'B4'], [all_locations_[9], 'B5'], [all_locations_[10], 'C1'], [all_locations_[11], 'C2'], [all_locations_[12], 'C3'], [all_locations_[13], 'C4'], [all_locations_[14], 'C5'], [all_locations_[15], 'D1'], [all_locations_[16], 'D2'], [all_locations_[17], 'D3'], [all_locations_[18], 'D4'], [all_locations_[19], 'D5'], [all_locations_[20], 'E1'], [all_locations_[21], 'E2'], [all_locations_[22], 'E3'], [all_locations_[23], 'E4'], [all_locations_[24], 'E5']]  
   # strings = [x[1] for x in list_locations]
    #if all(x!=s for x in strings)== True:
     #   raise ValueError
    #for i in range(len(list_locations)):
     #   if list_locations[i][1] == s:
      #      return list_locations[i][0]
    
def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    all_loc = all_locations()
    letters = list('ABCDE')
    numbers = [i for i in range(1, 6)]
    locs = [x+str(y) for x in letters for y in numbers]
    list_loc = dict(zip(all_loc, locs))
    if location not in list_loc:
        raise ValueError
    else:
        return list_loc[location]

#def location_to_string(location):
 #   """Returns the string representation of a location.
  #  Similarly to the previous function, this function should raise
   # ValueError exception if the input is outside of the correct range
   # """  
   # all_locations_ = all_locations()
   # list_locations = [[all_locations_[0], 'A1'], [all_locations_[1], 'A2'], [all_locations_[2], 'A3'], [all_locations_[3], 'A4'], [all_locations_[4], 'A5'], [all_locations_[5], 'B1'], [all_locations_[6], 'B2'], [all_locations_[7], 'B3'], [all_locations_[8], 'B4'], [all_locations_[9], 'B5'], [all_locations_[10], 'C1'], [all_locations_[11], 'C2'], [all_locations_[12], 'C3'], [all_locations_[13], 'C4'], [all_locations_[14], 'C5'], [all_locations_[15], 'D1'], [all_locations_[16], 'D2'], [all_locations_[17], 'D3'], [all_locations_[18], 'D4'], [all_locations_[19], 'D5'], [all_locations_[20], 'E1'], [all_locations_[21], 'E2'], [all_locations_[22], 'E3'], [all_locations_[23], 'E4'], [all_locations_[24], 'E5']]  
   # if all(x!=location for x in all_locations_):
    #    raise ValueError
    #for i in range(len(list_locations)):
     #   if list_locations[i][0] == location:
      #      return list_locations[i][1]

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    try:
        return board[location[0]][location[1]]
    except Exception:
        return "None"
    

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    if direction == "right":
        tup = (location[0], location[1]+1)
        return tup
    elif direction == "left":
        tup = (location[0], location[1]-1)
        return tup
    elif direction == "up":
        tup = (location[0]-1, location[1])
        return tup
    elif direction == "down":
        tup = (location[0]+1, location[1])
        return tup

#def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
 #   if at(location) != 'M':
  #      raise ValueError
   # if at(location) == 'M' and at(adjacent_location(location, direction)) == 'R'
   # and 0 <= adjacent_location(location, direction)[0] <= 4
   # and 0 <= adjacent_location(location, direction)[1] <= 4:
    #    return True
    #else:
     #   return False
 
def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    if at(location) != 'M':
        raise ValueError
    else:
        return at(adjacent_location(location, direction)) == 'R' and 0 <= adjacent_location(location, direction)[0] <= 4 and 0 <= adjacent_location(location, direction)[1] <= 4



def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    if at(location) != 'R':
        raise ValueError
    else:
        return at(adjacent_location(location, direction)) == '-' and 0 <= adjacent_location(location, direction)[0] <= 4 and 0 <= adjacent_location(location, direction)[1] <= 4
    

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if at(location) == 'R':
        return at(adjacent_location(location, direction)) == '-' and 0 <= adjacent_location(location, direction)[0] <= 4 and 0 <= adjacent_location(location, direction)[1] <= 4
    elif at(location) == 'M':
        return at(adjacent_location(location, direction)) == 'R' and 0 <= adjacent_location(location, direction)[0] <= 4 and 0 <= adjacent_location(location, direction)[1] <= 4
    

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range.
    You can assume that input will always be in correct range."""
    directions = ["right", "left", "up", "down"]
    for i in directions:
        if is_legal_move(location, i):
            return True
    return False
        


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    var = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == who and can_move_piece_at((i,j)):
                return True
    return False

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    directions = ["up", "right", "down", "left"]
    right_directions = []
    for i in directions:
        if is_legal_move(location, i):
            right_directions.append(i)
    return right_directions

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    return 0 <= location[0] < 5 and 0 <= location[1] < 5
    
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    return is_legal_location(adjacent_location(location, direction))

    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    directions = ["up", "right", "down", "left"]
    possible_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in directions:
                if board[i][j] == player and is_legal_move((i,j), k):
                    possible_moves.append([(i,j),k])
    return possible_moves

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    player = board[location[0]][location[1]]
    board[adjacent_location(location, direction)[0]][adjacent_location(location, direction)[1]] = player
    board[location[0]][location[1]] = '-'

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    from random import randint
    all_possible_moves = all_possible_moves_for(who)
    i = randint(0, len(all_possible_moves)-1)
    return (all_possible_moves[i][0], all_possible_moves[i][1])
    

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    row_positions = []
    column_positions = []
    for i in range(len(board)):
                       for j in range(len(board[i])):
                           if board[i][j] == 'M':
                               row_positions.append(i)
                               column_positions.append(j)
    return all(x==row_positions[0] for x in row_positions) or all(x==column_positions[0] for x in column_positions)
    
               

#---------- Communicating with the user ----------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
        
if __name__ == "__main__":
    start()

