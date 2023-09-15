import numpy as np
from numpy import cos
from numpy import sin


def Tv1v2():
    alpha = 30*np.pi/180
    beta = 0
    gamma = 0

    T = [[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma) - sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma)+sin(alpha)*sin(gamma), 0.1],
         [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma)-cos(alpha)*sin(gamma), 0],
         [-sin(beta), cos(beta)*sin(gamma), cos(beta)*cos(gamma), 0],
         [0, 0, 0, 1]]
    # print(np.array(T))
    return np.array(T)

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

def compute_Xc2():
    T_vc = Tvc()
    X_c1 = np.array([0.3, -0.1, 5.1, 1])

    Tv1c1 = T_vc.dot(X_c1)

    T_v1v2 = Tv1v2()
    # Tv2c1 = T_v1v2.dot(Tv1c1)
    T = T_v1v2.dot(Tv1c1)
    T = np.array([T[0],T[1],T[2]])
    
    return np.array(T)

def main():
	
    Xc2 = compute_Xc2()
    print(Xc2)

if __name__ == "__main__":
    main()