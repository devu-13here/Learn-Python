class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Implement the heuristic function H(n)
        misplaced_tiles = sum([1 for i, j in zip(self.board, goal_state) if i != j])
        return misplaced_tiles

    def is_goal(self):
        return self.board == goal_state

    def generate_neighbors(self):
        # Generate neighboring states based on possible moves (up, down, left, right)
        neighbors = []
        empty_index = self.board.index(0)  # Find the index of the empty tile
        row, col = empty_index // 3, empty_index % 3

        # Define possible moves: up, down, left, right
        moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        for move_row, move_col in moves:
            if 0 <= move_row < 3 and 0 <= move_col < 3:
                move_index = move_row * 3 + move_col
                new_board = self.board[:]
                new_board[empty_index], new_board[move_index] = new_board[move_index], new_board[empty_index]
                neighbors.append(PuzzleState(new_board))

        return neighbors

def hill_climbing(initial_state):
    current_state = initial_state

    while True:
        neighbors = current_state.generate_neighbors()
        best_neighbor = min(neighbors, key=lambda x: x.heuristic)

        if best_neighbor.heuristic >= current_state.heuristic:
            break  # Stop if no better neighbor is found

        current_state = best_neighbor

    return current_state

# Specific initial and goal states
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

initial_state = PuzzleState(initial_state)
final_state = hill_climbing(initial_state)

# Print the final state
print("Final State:", final_state.board)
print("Heuristic:", final_state.heuristic)
