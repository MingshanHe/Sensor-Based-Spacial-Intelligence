import numpy as np
from scipy.stats import norm
from scipy.linalg import logm
from scipy.linalg import expm
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
    
def gen_rprime(phi,e):

    # Compute the magnitude of phi
    # magphi = np.sqrt(phi[0]**2+phi[1]**2+phi[2]**2)
    magphi = np.linalg.norm(phi)
    # phi3 = phi*phi*phi

    # magphi3 = np.sqrt(phi3[0]**2+phi3[1]**2+phi3[2]**2)
    # Get skew-symmetric matrix A from phi and compute R
    A = lie_hat(phi)
    R = expm(A)
    
    # Compute the Jacobian matrix Jr
    # You should consider two cases
    if magphi != 0:
        Jr = np.eye(3) - A*(1-np.cos(magphi))/(magphi**2) + A@A*(magphi-np.sin(magphi))/(magphi**3)
    else:
        Jr = np.eye(3)

    # Calculate R_prime2 using the provided relationship
    R_prime = R@expm(lie_hat(Jr@e))
    
    return R_prime
        
def main():
   
    # Generate random vector e from a normal distribution
    e = norm.rvs(loc=0, scale=0.1,size=(1,3))
    e = e[0]

    phi = gen_phi()
    R_prime2 = gen_rprime(phi,e)
    print(R_prime2)

if __name__ == "__main__":
    main()