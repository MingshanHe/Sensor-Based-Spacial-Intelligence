import numpy as np
from numpy import cos
from numpy import sin

def Tvc():
    alpha = 90*np.pi/180
    beta = 0
    gamma = 90*np.pi/180

    T = [[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma) - sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma)+sin(alpha)*sin(gamma), 0.1],
         [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma)-cos(alpha)*sin(gamma), 0],
         [-sin(beta), cos(beta)*sin(gamma), cos(beta)*cos(gamma), -0.25],
         [0, 0, 0, 1]]
    # print(np.array(T))
    return np.array(T)

def compute_Xv1():
    # TODO
    # Replace below with the correct Xv1
    T_vc = Tvc()
    X_c1 = np.array([0.3, -0.1, 5.1, 1])

    T = T_vc.dot(X_c1)
    T = np.array([T[0],T[1],T[2]])
    # T = [5.20, -0.1, 0.55]

    
    return np.array(T)

def main():
	
    Xv1 = compute_Xv1()
    print(Xv1)

if __name__ == "__main__":
    main()