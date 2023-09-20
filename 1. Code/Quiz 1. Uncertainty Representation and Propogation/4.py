import numpy as np

R1 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=np.float32)
R2 = np.array([[0,-0.39894228,0.39894228], [1,0,0.39894228], [0.39894228,1,0]], dtype=np.float32)

print(R1@R2)