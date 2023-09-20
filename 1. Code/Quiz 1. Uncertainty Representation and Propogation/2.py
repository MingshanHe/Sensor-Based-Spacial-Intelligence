import numpy as np
def NearZero(z):
    return abs(z) < 1e-6

def skew_symmetric_matrix(vec):
    mat =  np.array([[0,      -vec[2],  vec[1]],
                     [vec[2],       0, -vec[0]],
                     [-vec[1], vec[0],       0]])
    
    return mat

def to_SO3(vec):

    so3mat = skew_symmetric_matrix(vec)
    omgtheta = vec
    if NearZero(np.linalg.norm(omgtheta)):
        rot =  np.eye(3)
    else:
        theta = np.linalg.norm(omgtheta)
        omgmat = so3mat / theta
        rot =  np.eye(3) + np.sin(theta) * omgmat + (1 - np.cos(theta)) * np.dot(omgmat, omgmat)

    return rot
    
def to_so3(rot):

    acosinput = (np.trace(rot) - 1) / 2.0
    if acosinput >= 1:
        so3mat = np.zeros((3, 3))
    elif acosinput <= -1:
        if not NearZero(1 + rot[2][2]):
            omg = (1.0 / np.sqrt(2 * (1 + rot[2][2]))) * np.array([rot[0][2], rot[1][2], 1 + rot[2][2]])
        elif not NearZero(1 + rot[1][1]):
            omg = (1.0 / np.sqrt(2 * (1 + rot[1][1]))) * np.array([rot[0][1], 1 + rot[1][1], rot[2][1]])
        else:
            omg = (1.0 / np.sqrt(2 * (1 + rot[0][0]))) * np.array([1 + rot[0][0], rot[1][0], rot[2][0]])
        so3mat = skew_symmetric_matrix(np.pi * omg)
    else:
        theta = np.arccos(acosinput)
        so3mat = theta / 2.0 / np.sin(theta) * (rot - np.array(rot).T)

    vec = np.array([so3mat[2][1], so3mat[0][2], so3mat[1][0]])
    return vec   
    
def main():

    rot = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32)
    so3 = to_so3(rot)
    SO3 = to_SO3(so3)
    
    print("so3:")
    print(so3)    
    print("SO3:")
    print(SO3)
    

if __name__ == "__main__":
    main()