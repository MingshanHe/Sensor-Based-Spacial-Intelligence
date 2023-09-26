import numpy as np
from scipy.stats import norm
from scipy.linalg import expm
from scipy.linalg import logm
from numpy.random import rand

np.random.seed(seed=0)

def gaussian_distribution(x, mean, sigma):
    gd = (1/(sigma*np.sqrt(2*np.pi))) *  np.exp(-(x - mean)**2 / (2*sigma**2))
    return gd

def lie_vee(A):
    """
    Converts a skew-symmetric matrix A to a vector w.
    """
    w = np.array([A[2, 1], A[0, 2], A[1, 0]])
    return w

def lie_hat(phi):
    """
    Converts a vector phi to a skew-symmetric matrix.
    """
    A = np.array([[0, -phi[2], phi[1]],
                  [phi[2], 0, -phi[0]],
                  [-phi[1], phi[0], 0]])
    return A
    
def gen_phi():

    # Defining the matrix R
    R = np.array([[0,0,1],[1,0,0],[0,1,0]])

    # Computing the matrix logarithm of R
    A = logm(R)

    # Converting the matrix A to a vector
    phi = lie_vee(A)

    return phi
    
def gen_phi_prime(phi):

    # Generate random vector e from a normal distribution
    e = np.array(gaussian_distribution(rand(3), 0, 0.1*0.1))

    # Update phi with e
    # print(e)
    # print(phi)
    phi_prime = phi+e

    return phi_prime
    
def gen_rprime(phi_prime):

    # Convert phi_prime to skew-symmetric matrix
    # print(phi_prime)
    A_prime = lie_hat(phi_prime)
    # print(A_prime)
    # Compute the matrix exponential of A_prime
    R_prime = expm(A_prime)

    return R_prime
    
def main():
    phi = gen_phi()
    phi_prime = gen_phi_prime(phi)
    R_prime = gen_rprime(phi_prime)
    
    print(R_prime)
    
if __name__ == "__main__":
    main()