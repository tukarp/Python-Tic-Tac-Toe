# Simple Tic-Tac-Toe Game
# Made by github.com/tukarp


# Move class
class Move(object):
    # Define constructor
    def __init__(self, row, column, sign):
        self.row = row          # Row coordinate
        self.column = column    # Column coordinate
        self.sign = sign        # Sign of the player


# Player class
class Player(object):
    # Define constructor
    def __init__(self, name, sign):
        self.name = name  # Name of the player
        self.sign = sign  # Sign of the player

    # Get player move
    def get_move(self):
        # Choose coordinates message
        print("Choose coordinates ([0-2] [0-2]):")

        # Get correct input from player loop
        while True:
            # Try block
            try:
                # Get row and column from input
                row, column = input(f"{self.name}: ").split()

                # Check if row and column are digits
                if row.isdigit() and column.isdigit():
                    # Check if both row and column are in range [0-2]
                    if int(row) in [0, 1, 2] and int(column) in [0, 1, 2]:
                        # Return move
                        return Move(int(row), int(column), self.sign)
                    else:
                        # Print error message
                        print("Wrong coordinates!")
                else:
                    # Print error message
                    print("You should enter numbers!")
            # Raise ValueError exception
            except ValueError:
                # Print error message
                print("Value Error!")


# Grid class
class Grid(object):
    # Define constructor
    def __init__(self):
        # Create grid
        self.grid = [["█", "█", "█"] for i in range(3)]

    # Print grid
    def __str__(self):
        # Create grid state
        return self.get_state()

    # Get grid state
    def get_state(self):
        # Initialize state
        state = ""

        # Iterate over rows
        for row in self.grid:
            # Add row to state
            state += "".join(row) + "\n"
        # Return state
        return state

    # Get grid field
    def get_field(self, row, y):
        # Return field in grid
        return self.grid[row][y]

    # Set grid field
    def set_field(self, move):
        # Check if field is empty
        if self.get_field(move.row, move.column) != "█":
            # Print error message
            print("This field is taken!")
            # Return False
            return False
        # Set field
        self.grid[move.row][move.column] = move.sign
        # Return True
        return True

    # Print grid
    def print_grid(self):
        print(f"""
          ◪ X 0 1 2
          Y ─────────
          0 │ {self.grid[0][0]} {self.grid[0][1]} {self.grid[0][2]} │
          1 │ {self.grid[1][0]} {self.grid[1][1]} {self.grid[1][2]} │
          2 │ {self.grid[2][0]} {self.grid[2][1]} {self.grid[2][2]} │
            ────────
            """)


# Game class
class Game(object):
    # Define constructor
    def __init__(self):
        # Initialize name of the game
        self.name = "Tic-Tac-Toe"
        # Create grid
        self.grid = Grid()
        # Initialize winning sign
        self.winning_sign = None


    # Play game
    def play(self, player_one, player_two):
        # Print welcome message
        print(f"Welcome to {self.name} Game!")
        # Create players tuple
        players = (player_one, player_two)
        # Initialize current player
        current_player = 0

        # While game is not over
        while not self.game_over():
            # Print grid
            self.grid.print_grid()
            # While move is not possible
            while not self.grid.set_field(
                    players[current_player].get_move()):
                # Pass
                pass
            # Switch current player
            current_player ^= 1
        # If winning sign is None
        if self.winning_sign is None:
            # Print grid
            self.grid.print_grid()
            # Print draw message
            print("Draw!")
        # If winning sign is player one sign
        elif self.winning_sign == player_one.sign:
            # Print grid
            self.grid.print_grid()
            # Print player one won message
            print(f"{player_one.name} ({player_one.sign}) has won!")
        # If winning sign is player two sign
        elif self.winning_sign == player_two.sign:
            # Print grid
            self.grid.print_grid()
            # Print player two won message
            print(f"{player_two.name} ({player_two.sign}) has won!")

    # Check if game is over
    def game_over(self):
        # For each row
        for row in range(3):
            # If signs in row are the same
            if self.grid.get_field(row, 0) == \
                    self.grid.get_field(row, 1) == \
                    self.grid.get_field(row, 2) and \
                    self.grid.get_field(row, 0) != '█':
                # Set winning sign
                self.winning_sign = self.grid.get_field(row, 0)
                # Return True
                return True
        # For each column
        for column in range(3):
            # If signs in columns are the same
            if self.grid.get_field(0, column) == \
                    self.grid.get_field(1, column) == \
                    self.grid.get_field(2, column) and \
                    self.grid.get_field(0, column) != '█':
                # Set winning sign
                self.winning_sign = self.grid.get_field(0, column)
                # Return True
                return True
        # if signs on diagonal from left top are the same
        if self.grid.get_field(0, 0) == \
                self.grid.get_field(1, 1) == \
                self.grid.get_field(2, 2) and \
                self.grid.get_field(0, 0) != '█':
            # Set winning sign
            self.winning_sign = self.grid.get_field(0, 0)
            # Return True
            return True
        # if signs on diagonal from left bottom are the same
        if self.grid.get_field(2, 0) == \
                self.grid.get_field(1, 1) == \
                self.grid.get_field(0, 2) and \
                self.grid.get_field(2, 0) != '█':
            # Set winning sign
            self.winning_sign = self.grid.get_field(2, 0)
            # Return True
            return True
        # If next move is not possible
        if not self.is_next_move_possible():
            # Set winning sign to None
            self.winning_sign = None
            # Return True
            return True
        # Return False
        return False

    # Check if next move is possible
    def is_next_move_possible(self):
        # Return True if "█" is in grid state
        return "█" in self.grid.get_state()


# Define main function
def main():
    # Create game object
    game = Game()

    # Create player one
    player_one = Player("Player One", "X")
    # Create player two
    player_two = Player("Player Two", "O")

    # Start game with given players
    game.play(player_one, player_two)


# Main function
if __name__ == "__main__":
    # Call main function
    main()
