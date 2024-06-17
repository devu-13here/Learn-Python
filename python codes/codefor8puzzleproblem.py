import heapq

class PuzzleState:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.cost = 0  # Cost from the initial state to this state
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

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
            neighbors.append(PuzzleState(new_board, parent=self))

        return neighbors

def best_first_search(initial_state):
    heap = [initial_state]
    visited = set()

    while heap:
        current_state = heapq.heappop(heap)

        if current_state.is_goal():
            # Print intermediate steps
            print_intermediate_steps(current_state)
            return current_state.cost

        visited.add(tuple(current_state.board))

        for neighbor in current_state.generate_neighbors():
            if tuple(neighbor.board) not in visited:
                neighbor.cost = current_state.cost + 1
                heapq.heappush(heap, neighbor)

    return float('inf')  # If no solution is found

def print_intermediate_steps(state):
    steps = []
    while state:
        steps.append(state.board)
        state = state.parent

    steps.reverse()
    for step in steps:
        print(step)

# Specific initial and goal states
initial_state = [2,0,3,1,8,4,7,6,5]
goal_state = [1,2,3,8,0,4,7,6,5]

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
total_moves = best_first_search(initial_state)
print("Total number of moves:", total_moves)
