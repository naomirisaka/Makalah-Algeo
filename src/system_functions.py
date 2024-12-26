import numpy as np

def check_stability(A): # checks if the system is stable
    eigval = np.linalg.eigvals(A)
    is_stable = all(np.real(e) < 0 for e in eigval) # if all real parts are negative, system is stable
    return eigval, is_stable

def recommend_correction(status): # recommends a control correction based on the current status
    max_corr_limit = 10  # fixed maximum correction limit
    needed_corr = -status 
    max_corr = np.maximum(0.1 * np.abs(status), max_corr_limit) # maximum correction limit as 10%
    corr = np.sign(needed_corr) * np.minimum(np.abs(needed_corr), max_corr) # compares the corrections
    return corr

def apply_correction(status, corr): # applies the correction to the status
    updated_status = status + corr
    return updated_status