#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def initial_state(size):
    state = random.sample(range(size), size)
    while not is_valid_state(state):
        random.shuffle(state)
    return state

def is_valid_state(state):
    size = len(state)
    for i in range(size):
        for j in range(i + 1, size):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                return False
    return True

def compute_attacks(state):
    attacks = 0
    size = len(state)
    for i in range(size):
        for j in range(i + 1, size):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def heuristic(state):
    return -compute_attacks(state)

def hill_climbing(size, max_iter=1000):
    current_state = initial_state(size)
    for _ in range(max_iter):
        if compute_attacks(current_state) == 0:
            return current_state  # Found a solution
        neighbors = []
        for col in range(size):
            for row in range(size):
                if row != current_state[col]:
                    neighbor = list(current_state)
                    neighbor[col] = row
                    neighbors.append(neighbor)
        best_neighbor = max(neighbors, key=heuristic)
        if heuristic(best_neighbor) <= heuristic(current_state):
            return current_state  # Local minimum, return current state
        current_state = best_neighbor
    return None  # Failed to find a solution within max iterations

def print_board(state):
    size = len(state)
    for row in range(size):
        queens_positions = [str(col + 1) if state[row] == col else "-" for col in range(size)]
        print(" ".join("Q" if state[row] == col else "-" for col in range(size)))
    print("-".join(str(col + 1) for col in state))

def main():
    try:
        num_queens = int(input("Enter the number of queens: "))
        if num_queens <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a positive integer for the number of queens.")
        return

    solution = hill_climbing(num_queens)
    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("Failed to find a solution within the maximum number of iterations.")

if __name__ == "__main__":
    main()


# In[ ]:




