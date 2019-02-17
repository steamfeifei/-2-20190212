import numpy as np

data = [[1, 1, 1, 0, 0],
        [2, 2, 2, 0, 0],
        [3, 3, 3, 0, 0],
        [5, 5, 3, 2, 2],
        [0, 0, 0, 3, 3],
        [0, 0, 0, 6, 6]]
data = np.array(data)
U, S, V = np.linalg.svd(data)
S = [
    [S[0], 0, 0],
    [0, S[1], 0],
    [0, 0, S[2]]
]
import  pandas as pd

