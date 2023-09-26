import numpy as np
from scipy.linalg import logm
 
def lie_vee(A):
    """
    Converts a skew-symmetric matrix A to a vector w.
    """
    w = np.array([A[2, 1], A[0, 2], A[1, 0]])
    return w
        
def gen_phi():

    # Defining the matrix R
    R = np.array([[0,0,1],[1,0,0],[0,1,0]])

    # Computing the matrix logarithm of R
    A = logm(R)

    # Converting the matrix A to a vector
    phi = lie_vee(A)

    return phi
    
def main():
    
    phi = gen_phi()
    print(phi)

if __name__ == "__main__":
    main()