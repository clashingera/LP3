
class NQueens:
    def __init__(self) -> None:
        # Initialize chessboard size, board state, and solution count
        self.size = int(input("Enter size of chessboard: "))
        self.board = [[False] * self.size for _ in range(self.size)]
        self.count = 0

    def printBoard(self):
        # Display the current board state
        for row in self.board:
            print(" ".join("Q" if ele else "X" for ele in row))
        print()

    def isSafe(self, row: int, col: int) -> bool:
        # Check if placing a queen at (row, col) is safe
        
        # Check column for any queens
        for i in range(row):
            if self.board[i][col]:
                return False

        # Check top-left diagonal (\)
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1

        # Check top-right diagonal (/)
        i, j = row, col
        while i >= 0 and j < self.size:
            if self.board[i][j]:
                return False
            i -= 1
            j += 1

        return True  # Safe to place queen

    def set_position_first_queen(self):
        # User manually sets the initial queen's position
        print("Enter coordinates of first queen:")
        row = int(input(f"Enter row (1-{self.size}): ")) - 1
        col = int(input(f"Enter column (1-{self.size}): ")) - 1
        self.board[row][col] = True
        self.printBoard()

    def solve(self, row: int = 0):
        # Recursively try to place queens starting from the given row
        if row == self.size:
            self.count += 1
            self.printBoard()
            return

        # Skip the row if queen is already placed (first queen row)
        if any(self.board[row]):
            self.solve(row + 1)
            return

        for col in range(self.size):
            if self.isSafe(row, col):
                self.board[row][col] = True
                self.solve(row + 1)
                self.board[row][col] = False  # Backtrack

    def displayMessage(self):
        # Display the final message based on the count of solutions
        if self.count > 0:
            print("Solution exists for the given position of the queen.")
        else:
            print("Solution doesn't exist for the given position of the queen.")

# Main execution
solver = NQueens()
solver.set_position_first_queen()
solver.solve()
solver.displayMessage()

'''
### 2) Code Explanation

- **`__init__`**: Initializes the board size, creates a 2D list representing the board, and sets the count of solutions to 0.
- **`printBoard`**: Prints the current state of the board, with `Q` for queens and `X` for empty spots.
- **`isSafe`**: Checks if a queen can be safely placed at `(row, col)` by verifying there are no other queens in the same column or diagonals (above the current position).
- **`set_position_first_queen`**: Takes user input to place the first queen at a specified location on the board.
- **`solve`**: Uses backtracking to attempt to place queens row by row. If it reaches the last row (`row == size`), it prints a solution. Otherwise, it recursively tries to place queens in the current row.
- **`displayMessage`**: Outputs whether solutions exist given the first queen's initial position.

---

### 3) Explanation of Input and Output

- **Input**:
  - `Enter size of chessboard`: User specifies the board size (e.g., `4` for a 4x4 board).
  - `Enter coordinates of first queen`: User specifies the initial position of the first queen as two integers (row and column).

- **Output**:
  - The program will print all valid board configurations (solutions) with queens placed safely. Each solution shows `Q` for queens and `X` for empty spots.
  - If there are any solutions, it displays `"Solution exists for the given position of the queen."` Otherwise, it shows `"Solution doesn't exist for the given position of the queen."`

---

### 4) Time and Space Complexity

- **Time Complexity**: \( O(N!) \)
  - The algorithm checks all possible placements for `N` queens. For each queen, it tries `N` columns, leading to an exponential complexity.
  
- **Space Complexity**: \( O(N^2) \)
  - The program stores the board as an `N x N` matrix. Additionally, the recursive calls have a space complexity of \( O(N) \) for the call stack, but the overall space complexity is dominated by the board.
'''