def waterJugSolver(jug1_capacity, jug2_capacity):
    from collections import deque

    # Initialize visited dictionary to keep track of visited states
    visited = {}
    
    # Initialize the queue for BFS and the initial state
    queue = deque()
    queue.append((0, 0))  # Start with both jugs empty
    
    while queue:
        amt1, amt2 = queue.popleft()
        
        # Check if the goal is reached
        if amt1 == 4 or amt2 == 4:
            print(f"Solution found: Jug1: {amt1}, Jug2: {amt2}")
            return
        
        # Check if the current state has been visited
        if (amt1, amt2) in visited:
            continue
        
        # Mark the current state as visited
        visited[(amt1, amt2)] = True
        
        # Generate all possible moves and add them to the queue
        # Fill Jug1
        if (jug1_capacity, amt2) not in visited:
            queue.append((jug1_capacity, amt2))
        # Fill Jug2
        if (amt1, jug2_capacity) not in visited:
            queue.append((amt1, jug2_capacity))
        # Empty Jug1
        if (0, amt2) not in visited:
            queue.append((0, amt2))
        # Empty Jug2
        if (amt1, 0) not in visited:
            queue.append((amt1, 0))
        # Pour Jug1 into Jug2
        pour_amt = min(amt1, jug2_capacity - amt2)
        new_amt1 = amt1 - pour_amt
        new_amt2 = amt2 + pour_amt
        if (new_amt1, new_amt2) not in visited:
            queue.append((new_amt1, new_amt2))
        # Pour Jug2 into Jug1
        pour_amt = min(amt2, jug1_capacity - amt1)
        new_amt1 = amt1 + pour_amt
        new_amt2 = amt2 - pour_amt
        if (new_amt1, new_amt2) not in visited:
            queue.append((new_amt1, new_amt2))
    
    print("No solution found")

# Example usage
waterJugSolver(6, 5)
