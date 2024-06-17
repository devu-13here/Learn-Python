import heapq

# Define the initial state and the goal state
initial_state = [[2, 0, 3],
                 [1, 8, 4],
                 [7, 6, 5]]  # Initial state of the puzzle

goal_state = [[1, 2, 3],
              [8,0, 4],
              [7, 6,5]]  # Goal state of the puzzle

# Define operators to move tiles (up, down, left, right)
def move_blank(state, direction):
    blank_row, blank_col = find_blank(state)
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

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

def best_first_search(initial_state):
    heap = [(misplaced_tiles(initial_state), 0, initial_state)]  # Priority queue with heuristic value, cost, and state
    visited = set()  # Set to store visited states
    moves = 0  # Counter for total moves
    
    while heap:
        _, cost, current_state = heapq.heappop(heap)  # Pop the state with the lowest heuristic value
        if current_state == goal_state:
            print("Goal state reached!")
            return moves  # Return total moves if goal state is reached
        visited.add(tuple(map(tuple, current_state)))  # Convert state to tuple for hashability
        blank_row, blank_col = find_blank(current_state)
        directions = ['up', 'down', 'left', 'right']  # Possible directions to move the blank space
        for direction in directions:
            new_state = move_blank(current_state, direction)
            if tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(heap, (misplaced_tiles(new_state), cost + 1, new_state))  # Add new state to the priority queue
        moves += 1  # Increment move counter
        print(f"\nAfter Iteration {moves}:\n", current_state)

    return -1  # Return -1 if no solution is found
def print_state(state):
  for row in state:
      print(row)
  print()

# Solve the puzzle
total_moves = best_first_search(initial_state)
print("Total number of moves used to achieve the goal state:", total_moves)
