# -*- coding: utf-8 -*-
import numpy as np
import io


def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,-0.7
    tmp = x1 * w1 + x2 * w2
    if tmp + theta < 0:
        return 0
    elif tmp > theta:
        return 1

def NAND (x1,x2):
    w1,w2,theta = -0.5,-0.5,0.7
    tmp = x1 * w1 + x2 * w2
    if tmp + theta <= 0:
        return 0
    elif tmp + theta > 0:
        return 1

def OR (x1,x2):
    w1,w2,theta = 0.5,0.5,-0.2
    tmp = x1 * w1 + x2 * w2
    if tmp + theta <= 0:
        return 0
    elif tmp + theta > 0:
        return 1

def XOR(x1,x2): 
    s1 = OR(x1,x2)
    s2 = NAND(x1,x2)
    y = AND(s1,s2)
    return y

def main(x,y):
    ans =XOR(x,y)
    print(ans)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    main(x,y)
