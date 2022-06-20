
import numpy as np

def solution(a, b):
    a = np.array((1, 2, 3))
    b = np.array((4, 5, 6))
    dist = np.linalg.norm(a-b)

    print(dist)

a = 'ab'
b = 'abcbcb'
print(solution(a,b))