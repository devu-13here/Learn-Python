#8-puzzle using Best First Search/ Steepest Hill Climbing (Disply the no of steps required)
#using heuristic fxn

import heapq

initial_state = [[2,0,3], [1,8,4], [7,6,5]]
goal_state = [[1,2,3], [8,0,4], [7,6,5]]

#define operators to move tiles(up, down, left, right)
def move_blank(state, direction):
    blank_row, blank_col = find_blank(state)
    new_state = [row[:] for row in state]  #make a copy of the current state
    if direction == 'up' and blank_row>0:
        #This line simultaneously swaps the values of the blank space and the tile above it in the puzzle grid. It uses tuple unpacking to perform the swap
        new_state[blank_row][blank_col], new_state[blank_row-1][blank_col] = \
            new_state[blank_row-1][blank_col], new_state[blank_row][blank_col]
        
    elif direction == 'down' and blank_row<2:
        new_state[blank_row][blank_col], new_state[blank_row+1][blank_col] = \
            new_state[blank_row+1][blank_col], new_state[blank_row][blank_col]
        
    elif direction == 'left' and blank_col>0:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col-1] = \
            new_state[blank_row][blank_col-1], new_state[blank_row][blank_col]
        
    elif direction == 'right' and blank_col < 2:
        new_state[blank_row][blank_col], new_state[blank_row][blank_col+1] = \
            new_state[blank_row][blank_col+1], new_state[blank_row][blank_col]
        
    return new_state

def find_blank(state):
    # since 3*3 puzzle: loops iterate over indices [0 1 2] for both rows, col
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:   #indicates blank space
                return i,j

# Define the heuristic function H(n):
def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Best First Search Algo
def best_first_search(initial_state):
    heap = [(misplaced_tiles(initial_state), 0, initial_state)]  #Priority queue with H.Val(calculated using misplaces_tiles fxn), cost(means-moves taken), initial state
    visited = set()   #Set to store visited states
    moves  = 0  #Counter to keep track of total moves

    while heap:   #continue loop until priority queue(heap) is empty
        _, cost, current_state = heapq.heappop(heap)   # Pop the state with lowest H.V
                                                       # '-' is used to discard the H.Val since it's not needed here
        print_state(current_state)  #Print the current state

        if current_state == goal_state:
            return moves              # Return total moves if goal state is reached
        
        # Convert the current state to a tuple and add it to the visited set. This is done for hashability, so that we can efficiently check if a state has been visited before.
        visited.add(tuple(map(tuple,current_state)))   # Possible directions to move the blank space
        blank_row, blank_col = find_blank(current_state)    #  Find the row and column indices of the blank space in the current state.
        directions = ['up', 'down', 'left', 'right']  # Possible directions to move the blank space

        for direction in directions:
            new_state = move_blank(current_state, direction)    #Generate a new state by moving the blank space in the specified direction.
            if tuple(map(tuple,new_state)) not in visited:
                heapq.heappush(heap, (misplaced_tiles(new_state), cost + 1, new_state))  #Add new state to priority queue
        moves += 1  # Increment the move counter
    return -1  # Return -1 if no solution is found

def print_state(state):
    for row in state:
        print(row)
    print()

# Solve the puzzle
total_moves = best_first_search(initial_state)
print("Total number of moves used to achieve the goal state: ", total_moves)
