import numpy as np

from slam_utils import SlamUtils
slam = SlamUtils()
    
def prob():

    # Constants
    DTOR = np.pi / 180
    RTOD = 180 / np.pi

    # Robot starts at the origin = world frame
    xr = np.array([0, 0, 0])
    Sr = np.zeros((3, 3))

    # Robot sees object #1
    x1 = np.array([-1, 1, 0])
    R = np.diag([0.1**2, 0.2**2, (1 * DTOR)**2])

    X = np.concatenate((xr, x1))
    Cov = np.block([
        [Sr, np.zeros((3, 3))],
        [np.zeros((3, 3)), R]
    ])

    # Robot moves
    u = np.array([1, 1, 0])
    Q = np.diag([0.15**2, 0.05**2, (1 * DTOR)**2])
    yr, J = slam.head2tail_2d(xr, u) #(hint: you can use head2tail_2d in slam_utils)
    Sy = J@np.block([
        [Sr, np.zeros((3,3))],
        [np.zeros((3,3)), Q]
    ])@np.transpose(J)

    X = np.concatenate((yr, x1))
    Cov = np.block([
        [Sy, np.zeros((3, 3))],
        [np.zeros((3, 3)), R]
    ])

    # Robot sees #2
    z2 = np.array([-1, 1, 0])
    x2, J = slam.head2tail_2d(yr, z2)
    S2 = J@np.block([
        [Sy, np.zeros((3,3))],
        [np.zeros((3,3)), R]
    ])@np.transpose(J)

    X = np.concatenate((yr, x1, x2))
    Cov = np.block([
        [Sy, np.zeros((3, 3)), Sy],
        [np.zeros((3, 3)), R, np.zeros((3,3))],
        [Sy, np.zeros((3,3)), S2]
    ])

    # see the results
    slam.plot_pose_with_cov_ellipse(X, Cov)
    
    return xr, x1, yr

def main():
    
    xr, x1, yr = prob()

    print("xr:")
    print(xr)
    print("x1:")
    print(x1)
    print("yr:")
    print(yr)

if __name__ == "__main__":
    main()