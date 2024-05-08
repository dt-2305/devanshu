#!/usr/bin/env python
# coding: utf-8

# In[1]:


from queue import Queue

def water_jug_bfs(capacity_jug1, capacity_jug2, target_amount, target_jug):
    visited_states = set()
    q = Queue()
    q.put((0, 0))

    
    print("Initial state:", (0, 0))

    while not q.empty():
        current_state = q.get()

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        jug1, jug2 = current_state
        print("Current state:", current_state)

        if jug1 == target_amount and target_jug == 'A':
            print("Target reached! Goal state: Jug A =", jug1, "| Jug B =", jug2)
            return current_state
        elif jug2 == target_amount and target_jug == 'B':
            print("Target reached! Goal state: Jug A =", jug1, "| Jug B =", jug2)
            return current_state

        # Fill jug1
        new_state = (capacity_jug1, jug2)
        if new_state not in visited_states:
            q.put(new_state)
            print("Fill jug1:", new_state)

        # Fill jug2
        new_state = (jug1, capacity_jug2)
        if new_state not in visited_states:
            q.put(new_state)
            print("Fill jug2:", new_state)

        # Empty jug1
        new_state = (0, jug2)
        if new_state not in visited_states:
            q.put(new_state)
            print("Empty jug1:", new_state)

        # Empty jug2
        new_state = (jug1, 0)
        if new_state not in visited_states:
            q.put(new_state)
            print("Empty jug2:", new_state)

        # Pour jug1 to jug2
        pour_amount = min(jug1, capacity_jug2 - jug2)
        new_state = (jug1 - pour_amount, jug2 + pour_amount)
        if new_state not in visited_states:
            q.put(new_state)
            print("Pour jug1 to jug2:", new_state)

        # Pour jug2 to jug1
        pour_amount = min(jug2, capacity_jug1 - jug1)
        new_state = (jug1 + pour_amount, jug2 - pour_amount)
        if new_state not in visited_states:
            q.put(new_state)
            print("Pour jug2 to jug1:", new_state)

    print("No solution found!")
    return None

if __name__ == "__main__":
    capacity_jug1 = int(input("Enter capacity of jug 1: "))
    capacity_jug2 = int(input("Enter capacity of jug 2: "))
    target_amount = int(input("Enter target amount: "))
    target_jug = input("Enter target jug (A or B): ").upper()
    
    print("Starting Water Jug problem with capacities:", capacity_jug1, "and", capacity_jug2, "and target:", target_amount, "and target jug:", target_jug)
    result = water_jug_bfs(capacity_jug1, capacity_jug2, target_amount, target_jug)
    print("Water Jug Solution:", result)


# In[ ]:




