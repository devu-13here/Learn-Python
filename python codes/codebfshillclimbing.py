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
        # Generate neighboring states based on possible moves
        neighbors = []
        empty_index = self.board.index(0)  # Find the index of the empty tile

        for move in legal_moves[empty_index]:
            new_board = self.board[:]
            new_board[empty_index], new_board[move] = new_board[move], new_board[empty_index]
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
initial_state = [2,8,3,1,5,4,7,6,0]
goal_state = [1, 2, 3,8,0,4,7,6,5]

# Possible moves for each tile index
legal_moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

initial_state = PuzzleState(initial_state)
final_state = hill_climbing(initial_state)

# Print the final state
print("Final State:", final_state.board)
print("Heuristic:", final_state.heuristic)
