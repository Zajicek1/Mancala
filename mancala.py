STARTING_SEEDS = 4

STARTING_STORES = 0


class Player:
    """A class representing a player in Mancala. Also,
    creates the individual player boards for the game.
    Designated with their own pits and store."""

    # Constructor to initialize the parameters/data members
    def __init__(self, name):
        self._name = name

    # Method to return the player's name
    def return_player(self):
        return self._name


class Board:
    """A class representing the board in Mancala"""

    # Constructor to initialize parameters/data members
    def __init__(self):
        seed = STARTING_SEEDS
        store = STARTING_STORES
        self._board = [seed, seed, seed, seed, seed, seed, store,
                       store, seed, seed, seed, seed, seed, seed]
        self._side1 = self._board[0:7]
        self._side2 = self._board[7:14]

    # Returns the sides and full board of the players
    # for the game
    def return_board(self):
        return self._board

    # Returns the index range for player1
    def return_side1(self):
        return self._side1
    # Returns the index range for player2

    def return_side2(self):
        return self._side2


class Mancala:
    """A class representing the Mancala game. This class

    means the game is played between two players."""

    # Constructor to initialize parameters/data members

    def __init__(self):
        self._name = None
        self._updated_board = []
        self._board = []
        self._player1_side_empty = [0, 0, 0, 0, 0, 0]
        self._player2_side_empty = [0, 0, 0, 0, 0, 0]
        self._player1_side = Board().return_side1()
        self._player2_side = Board().return_side2()

    # Takes one parameter: name. Then returns
    # the object of that player by creating a
    # variable which calls from the Player()
    # class
    def create_player(self, player_name):
        if self._name is None:
            return Player(player_name)

    # Takes no parameters and prints the current
    # board information in a designated format
    def print_board(self):
        if self._board is not None:
            print(f'player1:')
            print(f'store: {self._updated_board[6]}')
            print(f'{self._updated_board[:6]}')
            print(f'player2:')
            print(f'store: {self._updated_board[13]}')
            print(f'{self._updated_board[7:13]}')

    # Takes no parameters and returns if the winner
    # of the game. Can also return a tie or unfinished
    # if the game is not over yet.
    def return_winner(self):
        if self._updated_board[:6] == self._player1_side_empty and self._updated_board[7:13] == self._player2_side_empty:
            if self._updated_board[6] > self._updated_board[13]:
                return f'Winner is player 1: {player1.return_player()}'
            elif self._updated_board[6] < self._updated_board[13]:
                return f'Winner is player 2: {player2.return_player()}'
            elif self._updated_board[6] == self._updated_board[13]:
                return f"It's a tie"
            else:
                return 'ERROR'
        if self._player1_side[:6] != self._player1_side_empty or self._player2_side[7:13] != self._player2_side_empty:
            return f'Game has not ended'

    # Takes two parameters: player index and pit index.
    # This method starts the playing of the game and
    # should follow the ruleset of Mancala. It should
    # also check the ending state of the game if it
    # is reached
    def play_game(self, player, pit):
        if player == 1:
            j = 6
            pointer = pit
            if pit <= 0 or pit > 6:
                return 'Invalid number for pit index'
            else:
                i = 0
                seed = self._player1_side[pit - 1]
                self._player1_side[pit - 1] = 0
                while seed > 0:
                    if seed == 1 and pointer == 6:
                        self._player1_side[pit + i] += 1
                        print('player 1 take another turn')
                        seed -= 1
                    if seed == 0:
                        self._board = []
                        for num in self._player1_side:
                            self._board.append(num)
                        for num in reversed(self._player2_side):
                            self._board.append(num)
                        self._updated_board = self._board
                        return self._updated_board
                    if seed > 0 and pointer >= len(self._player1_side):
                        i = 6
                        while seed > 0:
                            self._player2_side[i] += 1
                            seed -= 1
                            i -= 1
                            if seed > 0 and i == 0:
                                pit = 0
                                if seed == 1 and self._player1_side[pit] == 0 and self._player2_side[pit + 1] >= 1:
                                    player1_seed = seed
                                    player2_seed = self._player2_side[pit + 1]
                                    total_seeds = player1_seed + player2_seed
                                    self._player2_side[pit + 1] = 0
                                    self._player1_side[pit] = 0
                                    self._player1_side[6] += total_seeds
                                    seed -= 1
                                    while seed == 0 and self._player1_side[0:6] == self._player1_side_empty:
                                        self._player2_side[0] += self._player2_side[j]
                                        self._player2_side[j] = 0
                                        j -= 1
                                        if j == 1:
                                            self._board = []
                                            for num in self._player1_side:
                                                self._board.append(num)
                                            for num in reversed(self._player2_side):
                                                self._board.append(num)
                                            self._updated_board = self._board
                                            return self._updated_board
                                    if seed == 0:
                                        self._board = []
                                        for num in self._player1_side:
                                            self._board.append(num)
                                        for num in reversed(self._player2_side):
                                            self._board.append(num)
                                        self._updated_board = self._board
                                        return self._updated_board
                                self._player1_side[pit + i] += 1
                                i += 1
                            if seed == 0:
                                self._board = []
                                for num in self._player1_side:
                                    self._board.append(num)
                                for num in reversed(self._player2_side):
                                    self._board.append(num)
                                self._updated_board = self._board
                                return self._updated_board
                    if seed == 1 and self._player1_side[pit] == 0 and self._player2_side[pit] >= 1:
                        player1_seed = seed
                        player2_seed = self._player2_side[pit + 1]
                        total_seeds = player1_seed + player2_seed
                        self._player2_side[pit + 1] = 0
                        self._player1_side[pit] = 0
                        self._player1_side[6] += total_seeds
                        seed -= 1
                        if seed == 0:
                            self._board = []
                            for num in self._player1_side:
                                self._board.append(num)
                            for num in reversed(self._player2_side):
                                self._board.append(num)
                            self._updated_board = self._board
                            return self._updated_board
                    self._player1_side[pit + i] += 1
                    seed -= 1
                    i += 1
                    pointer += 1
                    while seed == 0 and self._player1_side[0:5] == self._player1_side_empty:
                        self._player2_side[pointer] += self._player2_side[0]
                        if self._player2_side[1:6] == self._player2_side_empty:
                            continue
                    if seed == 0:
                        self._board = []
                        for num in self._player1_side:
                            self._board.append(num)
                        for num in reversed(self._player2_side):
                            self._board.append(num)
                        self._updated_board = self._board
                        return self._updated_board
        if player == 2:
            pointer = pit
            j = 0
            if pit <= 0 or pit > 6:
                return 'Invalid number for pit index'
            else:
                i = 7
                seed = self._player2_side[i - pit]
                self._player2_side[i - pit] = 0
                while seed > 0:
                    if seed == 1 and pointer == 6:
                        self._player2_side[i - pit - 1] += 1
                        print('player 2 take another turn')
                        seed -= 1
                    if seed == 0:
                        self._board = []
                        for num in self._player1_side:
                            self._board.append(num)
                        for num in reversed(self._player2_side):
                            self._board.append(num)
                        self._updated_board = self._board
                        return self._updated_board
                    if seed > 0 and pointer >= len(self._player2_side):
                        i = 0
                        while seed > 0:
                            self._player1_side[i] += 1
                            seed -= 1
                            i += 1
                            if seed > 0 and i == 6:
                                pit = 6
                                if seed >= 1 and len(self._player1_side) == pointer:
                                    while seed > 0:
                                        self._player2_side[i] += seed
                                        seed -= 1
                                        i -= 1
                                        if seed == 0:
                                            self._board = []
                                            for num in self._player1_side:
                                                self._board.append(num)
                                            for num in reversed(self._player2_side):
                                                self._board.append(num)
                                            self._updated_board = self._board
                                            return self._updated_board
                                if seed == 1 and self._player2_side[pit] == 0 and self._player1_side[pit - 1] >= 1:
                                    player2_seed = seed
                                    player1_seed = self._player1_side[pit - 1]
                                    total_seeds = player1_seed + player2_seed
                                    self._player2_side[pit] = 0
                                    self._player1_side[pit - 1] = 0
                                    self._player2_side[0] += total_seeds
                                    seed -= 1
                                    while seed == 0 and self._player2_side[1:7] == self._player2_side_empty:
                                        self._player1_side[6] += self._player1_side[j]
                                        self._player1_side[j] = 0
                                        j += 1
                                        if j == 6:
                                            self._board = []
                                            for num in self._player1_side:
                                                self._board.append(num)
                                            for num in reversed(self._player2_side):
                                                self._board.append(num)
                                            self._updated_board = self._board
                                            return self._updated_board
                                    if seed == 0:
                                        self._board = []
                                        for num in self._player1_side:
                                            self._board.append(num)
                                        for num in reversed(self._player2_side):
                                            self._board.append(num)
                                        self._updated_board = self._board
                                        return self._updated_board
                                self._player1_side[pit + i] += 1
                                i += 1
                            if seed == 0:
                                self._board = []
                                for num in self._player1_side:
                                    self._board.append(num)
                                for num in reversed(self._player2_side):
                                    self._board.append(num)
                                self._updated_board = self._board
                                return self._updated_board
                    if seed == 1 and self._player2_side[pit] == 0 and self._player1_side[pit] >= 1:
                        player2_seed = seed
                        player1_seed = self._player2_side[pit - 1]
                        total_seeds = player1_seed + player2_seed
                        self._player2_side[pit] = 0
                        self._player1_side[pit - 1] = 0
                        self._player2_side[0] += total_seeds
                        seed -= 1
                        if seed == 0:
                            self._board = []
                            for num in self._player1_side:
                                self._updated_board.append(num)
                            for num in reversed(self._player2_side):
                                self._updated_board.append(num)
                            self._updated_board = self._board
                            return self._updated_board
                    self._player2_side[i - pit - 1] += 1
                    seed -= 1
                    i -= 1
                    pointer += 1
                    if seed == 0:
                        self._board = []
                        for num in self._player1_side:
                            self._board.append(num)
                        for num in reversed(self._player2_side):
                            self._board.append(num)
                        self._updated_board = self._board
                        return self._updated_board