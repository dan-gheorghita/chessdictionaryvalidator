Here is the commented code:

```python
# Dictionary of chess pieces with their positions on the board
chess_pieces = {'1h': 'bking', '6c': 'wqueen', 
                '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', 
                '1f': 'bpawn', '2f': 'bpawn', '3f': 'bpawn', '4f': 'bpawn',
                '5f': 'bpawn', '6f': 'bpawn', '7f': 'bpawn', '8f': 'bpawn',
                '2h': 'bpawn',}

# Dictionary of incorrect chess pieces with their positions
wrong_pieces = {'0A':'bpawn', '3F':'wpawn', '5d':'Dknight', '8g':'wping'}

# Dictionary of maximum number of each type of piece on the board
maxpiece_dictionary = {'black': 16, 'white': 16, 
                       'bking': 1, 'wking': 1, 'bpawn': 8, 'wpawn': 8}

# Dictionary to keep track of the actual number of each type of piece on the board
actual_pieces = {'black': 0, 'white': 0, 
                  'bking': 0, 'wking': 0, 'bpawn': 0, 'wpawn': 0}

# List of valid chess piece types
valid_pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']

# Function to check if a position on the board is valid
def valid_position(position):
    # Check if the row number is between 1 and 8 (inclusive)
    if(int(position[0]) > 0 and int(position[0]) < 9):
        # Check if the column letter is between 'a' and 'i' (inclusive)
        if(position[1] >= 'a' and position[1] < 'i'):
            return True
        else:
            return False

# Function to determine if a piece is black or white
def black_or_white(piece):
    # If the piece starts with 'w', increment the white count
    if(piece[0] == 'w'):
        actual_pieces['white'] += 1
    # If the piece starts with 'b', increment the black count
    elif(piece[0] == 'b'):
        actual_pieces['black'] += 1
    # If the piece does not start with 'w' or 'b', return False
    else:
        return False

# Function to check if a piece is in the maxpiece_dictionary
def in_maxpieces(piece):
    # If the piece is in the maxpiece_dictionary, increment its count
    if piece in maxpiece_dictionary.keys():
        actual_pieces[piece] += 1

# Function to check if there are too many pieces of a certain type
def over_limit():
    # Iterate over the actual_pieces dictionary
    for piece in actual_pieces.keys():
        # If the count of a piece exceeds its maximum limit, return the piece type
        if(actual_pieces[piece] > maxpiece_dictionary[piece]):
            return piece

# Function to check if a piece is valid (i.e., it is one of the valid_pieces types)
def valid_piece(piece):
    # Extract the piece type from the piece string
    the_slice = piece[1:len(piece)]
    # If the piece type is in the valid_pieces list, return True
    if(the_slice in valid_pieces):
        return True
    else:
        return False

# Iterate over the chess_pieces dictionary
for square, piece in chess_pieces.items():
    # Check if the position is valid
    if valid_position(str(square)) is True:
        # Determine if the piece is black or white
        valid_color = black_or_white(piece)
        # If the piece color is invalid, print an error message and break
        if(valid_color is False):
            print('Format for piece is incorrect. Start with \'b\' or \'w\'')
            break
        # Check if the piece is valid
        if(valid_piece(piece) is False):
            print('Format for piece is incorrect. Only: ' + ', '.join(valid_pieces))
            break
        # Increment the count of the piece in the actual_pieces dictionary
        in_maxpieces(piece)
        # Check if there are too many pieces of a certain type
        over_piece = over_limit()
        # If there are too many pieces, print an error message and break
        if(over_piece is not None):
            print('Too many ' + over_piece + ' pieces')
            break
    else:
        # If the position is invalid, print an error message and break
        print('Invalid position of ' + str(piece) +' on '+ str(square))
        break

# Print the actual number of each type of piece on the board
print(actual_pieces)
```