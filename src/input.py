import numpy as np

def input_matrix(): # matrix input and validation
    dim = int(input("Amount of control variables: "))
    print(f"Input the influence (-1 to 1) between control variables in {dim} x {dim} matrix form.") # negative indicates negative correlation
    
    mat = []
    for i in range(dim):
        while True:
            row = list(map(float, input(f"Row {i+1}: ").split()))

            if len(row) != dim:
                print(f"The row must contain exactly {dim} elements. Please try again.")
                continue

            if all(0 <= abs(x) <= 1 for x in row):
                mat.append(row)
                break 

            else:
                print("All elements must be between -1 and 1 (inclusive). Please try again.")

    return np.array(mat)

def input_initial_state(dim): # vector input and validation
    while True:
        x = list(map(float, input(f"Input the initial control state vector for each variable ({dim} elements): ").split()))
        if len(x) != dim:
            print(f"The vector must contain exactly {dim} elements. Please try again.")
            continue
        return np.array(x)