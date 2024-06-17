# Define the initial state and the goal state
initial_state_hill_climbing = [[2, 0, 3],
                                [1, 8, 4],
                                [7, 6, 5]]  # Initial state of the puzzle

goal_state_hill_climbing = [[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]]  # Goal state of the puzzle

# Define operators to move tiles (up, down, left, right)
def move_blank_hill_climbing(state, direction):
    blank_row, blank_col = find_blank_hill_climbing(state)
    new_state = [row[:] for row in state]  # Make a copy of the current state
    # Move the blank space in the specified direction
    if direction == 'up' and blank_row > 0:
        new_state[blank_row][blank_col], new_state[blank_row - 1][blank_col] = \
            new_state[blank_row - 1][blank_col], new_state[blank_row][blank_col]
    elif direction == 'down' and blank_row < 2:
        new_state[blank_row][blank_col], new_state[blank_row + 1][blank_col] = \
            new_state[blank_row + 1][blank_col], new_state[blank_row][blank_col]
    elif direction == 'left' and blank_col > 0:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col - 1] = \
            new_state[blank_row][blank_col - 1], new_state[blank_row][blank_col]
    elif direction == 'right' and blank_col < 2:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col + 1] = \
            new_state[blank_row][blank_col + 1], new_state[blank_row][blank_col]
    return new_state

def find_blank_hill_climbing(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def misplaced_tiles_hill_climbing(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state_hill_climbing[i][j]:
                count += 1
    return count

def hill_climbing(initial_state):
    current_state = initial_state

    while True:
        neighbors = [move_blank_hill_climbing(current_state, direction) for direction in ['up', 'down', 'left', 'right']]
        best_neighbor = min(neighbors, key=lambda x: misplaced_tiles_hill_climbing(x))

        if misplaced_tiles_hill_climbing(best_neighbor) >= misplaced_tiles_hill_climbing(current_state):
            break  # Stop if no better neighbor is found

        current_state = best_neighbor

    return current_state

# Solve the puzzle using Hill Climbing
final_state_hill_climbing = hill_climbing(initial_state_hill_climbing)

# Print the final state
print("Final State (Hill Climbing):", final_state_hill_climbing)
print("Heuristic (Hill Climbing):", misplaced_tiles_hill_climbing(final_state_hill_climbing))
