#!/bin/python3

import math
import os
import random
import re
import sys
import copy
# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    '''obstacles.append([r_q,n+1])
    obstacles.append([r_q,0])
    obstacles.append([n+1,c_q])
    obstacles.append([n+1,0])
    
    if(r_q >= c_q):
        obstacles.append([n+1,c_q + (n - r_q +1)])
        obstacles.append([r_q -(n - r_q +1),c_q -(n - r_q +1)])
    else:
        obstacles.append([r_q + (n-c_q+1),n+1])
        obstacles.append([r_q - (n-c_q +1),c_q-(n-c_q +1)])
    print (obstacles)'''
    
    it, count = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)], 0

    for m in it:
        r, c = r_q, c_q
        while (r + m[0] >= 1 and r + m[0] <= n) and (c + m[1] >= 1 and c + m[1] <= n):
            r += m[0]
            c += m[1]
            if [r, c] in obstacles:break
            count += 1

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
