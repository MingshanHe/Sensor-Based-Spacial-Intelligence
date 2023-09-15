import numpy as np
from numpy import cos
from numpy import sin

def T01():
    alpha = 180*np.pi/180
    beta = 0
    gamma = 0

    T = [[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma) - sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma)+sin(alpha)*sin(gamma), 2],
         [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma)-cos(alpha)*sin(gamma), 0],
         [-sin(beta), cos(beta)*sin(gamma), cos(beta)*cos(gamma), 0],
         [0, 0, 0, 1]]
    # print(np.array(T))
    return np.array(T)

def T12():
    alpha = -150*np.pi/180
    beta = 90*np.pi/180
    gamma = 0

    T = [[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma) - sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma)+sin(alpha)*sin(gamma), 0],
         [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma)-cos(alpha)*sin(gamma), 0],
         [-sin(beta), cos(beta)*sin(gamma), cos(beta)*cos(gamma), 1],
         [0, 0, 0, 1]]
    # print(np.array(T))
    return np.array(T)

def compute_T02():
    # TODO
    # Replace below with the correct T02
    # T_01 = T01()
    # T_12 = T12()
    T = T01().dot(T12())
    
    return np.array(T)

def main():
	
    T02 = compute_T02()
    print(T02)

if __name__ == "__main__":
    main()