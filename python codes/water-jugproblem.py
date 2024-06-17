target_quantity=2
capacity_jug1=4
capacity_jug2=3



def water_jug_problem(capacity_jug1, capacity_jug2, target_quantity):
    jug1 = 0
    jug2 = 0

while jug1 != target_quantity and jug2 != target_quantity:
        # Fill jug 1
        jug1 = capacity_jug1 if jug1 == 0 else jug1

        # Transfer water from jug 1 to jug 2
        transfer_amount = min(jug1, capacity_jug2 - jug2)
        jug1 -= transfer_amount
        jug2 += transfer_amount

        # Check if target quantity is reached
        if jug1 == target_quantity or jug2 == target_quantity:
            break

        # Empty jug 2
        jug2 = 0

if jug1 == target_quantity or jug2 == target_quantity:
        print("Target quantity {target_quantity} can be measured.")
else:
        print("Target quantity {target_quantity} cannot be measured with the given jug capacities.")

# Example usage:
water_jug_problem(4,3,2)
