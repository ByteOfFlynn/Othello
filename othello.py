class Player:
    """Manages a player in the Othello Game"""

    def __init__(self, name, color):
        """Initialize a player with name and color"""
        self._name = name
        self._color = color

    def get_name(self):
        """Get method for name"""
        return self._name

    def get_color(self):
        """Get method for color"""
        return self._color

class Othello:
    """Manages the Othello game"""

    def __init__(self):
        """Initialize the game board with pieces"""
        self._board = []
        self._players = []
        for i in range(10):
            row = ['.'] * 10
            self._board.append(row)
        for i in range(10):
            self._board[0][i] = '*'
            self._board[9][i] = '*'
            self._board[i][0] = '*'
            self._board[i][9] = '*'
        self._board[4][4] = 'O'
        self._board[5][5] = 'O'
        self._board[4][5] = 'X'
        self._board[5][4] = 'X'
        self._current_piece = 'X'

    def print_board(self):
        """Print the current state of the game board"""
        for row in self._board:
            print(' '.join(row))

    def create_player(self, player_name, color):
        """Create a player and add it to the game"""
        player = Player(player_name, color)
        self._players.append(player)
        if color == 'black':
            self._board[4][5] = 'X'
            self._board[5][4] = 'X'
        elif color == 'white':
            self._board[4][4] = 'O'
            self._board[5][5] = 'O'

    def return_winner(self):
        """Return the winner of the game"""
        black_count = sum(row.count('X') for row in self._board)
        white_count = sum(row.count('O') for row in self._board)
        if black_count > white_count:
            return "Winner is black player: " + self._players[1].get_name()
        elif black_count < white_count:
            return "Winner is white player: " + self._players[0].get_name()
        else:
            return "It's a tie"

    def return_available_positions(self, color):
        """Return a list of possible positions for a player to move"""
        available_positions = []
        if color == 'black':
            opponent_color = 'O'
            player_color = 'X'
        else:
            opponent_color = 'X'
            player_color = 'O'
        for row in range(1, 9):
            for col in range(1, 9):
                if self._board[row][col] == '.':
                    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                    for dx, dy in directions:  # Manages the directions a player can move
                        x, y = row + dx, col + dy
                        if self._board[x][y] == opponent_color:
                            x += dx
                            y += dy
                            while 0 <= x < 10 and 0 <= y < 10:
                                if self._board[x][y] == player_color:
                                    available_positions.append((row, col))
                                    break
                                if self._board[x][y] == '.' or self._board[x][y] == '*':
                                    break
                                x += dx
                                y += dy
        return available_positions

    def make_move(self, player_color, piece_position):
        """Make a move and update the game board"""
        row, col = piece_position
        player = self._players[0] if player_color == 'black' else self._players[1]
        self._board[row][col] = self._current_piece
        opponent_piece = 'O' if self._current_piece == 'X' else 'X'
        self._flip_pieces(row, col, self._current_piece, opponent_piece)
        self._current_piece = 'O' if self._current_piece == 'X' else 'X'  # Swaps the current piece
        return self._board[1:9]

    def _flip_pieces(self, row, col, color, opponent_color):
        """Flip the opponent's pieces after a move"""
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            i, j = row + dx, col + dy
            if self._board[i][j] == opponent_color:
                pieces_to_flip = []
                while self._board[i][j] == opponent_color:
                    pieces_to_flip.append((i, j))
                    i += dx
                    j += dy
                    if not (0 <= i < 10 and 0 <= j < 10):
                        break
                if 0 <= i < 10 and 0 <= j < 10 and self._board[i][j] == color:
                    for piece_row, piece_col in pieces_to_flip:
                        self._board[piece_row][piece_col] = color

    def play_game(self, player_color, piece_position):
        """Play the game and make a move for a player"""
        player = self._players[0] if player_color == 'white' else self._players[1]
        positions = self.return_available_positions(player_color)
        if piece_position not in positions:    # On invalid move
            print("Invalid move")
            print("Here are the valid moves:")
            for position in positions:
                print(position)
            return
        else:
            self.make_move(player_color[0].upper(), piece_position)
        black_positions = self.return_available_positions("black")
        white_positions = self.return_available_positions("white")
        if not black_positions or not white_positions:   # On the win of a game
            print("Game is ended")
            black_count = sum(row.count('X') for row in self._board)
            white_count = sum(row.count('O') for row in self._board)
            print(f"White Piece: {white_count} Black Piece: {black_count}")
            print(self.return_winner())
