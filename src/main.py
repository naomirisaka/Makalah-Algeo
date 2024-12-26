import numpy as np
from input import *
from system_functions import *

def main():
    print("------- Dynamic System Stability Simulation -------")
    A = input_matrix()
    
    eigval, is_stable = check_stability(A)
    print("Eigenvalues:")
    for eig in eigval:
        if np.iscomplex(eig):
            print(f"{eig.real:.3f} + {eig.imag:.3f}j" if eig.imag >= 0 else f"{eig.real:.3f} - {abs(eig.imag):.3f}j")
        else:
            print(f"{eig.real:.3f} + 0j")
    
    if is_stable:
        print("System control is stable. No further action needed.")
        quit()
    else:
        print("System control is unstable. Adjustments may be needed.\n")
    
    x = input_initial_state(A.shape[0]) # initial state vector has to match the matrix size
    while True:
        print(f"\nCurrent state: {x}")
        if not np.all(np.abs(x) < 0.1):  # stability threshold
            print("System is unstable.")
            corr = recommend_correction(x)
            print(f"Correction recommendation: {corr}")
        
            apply_corr = input("Apply control corrections? (y/n): ").strip().lower() # asks about applying the correction
            if apply_corr == 'y':
                x = apply_correction(x, corr)
                print(f"State after corrections are applied: {x}")
            else:
                print("No corrections applied.")
        else:
            print("System is stable.")
            quit()
        
        cont = input("Continue simulation? (y/n): ").strip().lower() # asks about continuing the simulation
        if cont != 'y':
            print("Simulation ended.")
            break

if __name__ == "__main__":
    main()