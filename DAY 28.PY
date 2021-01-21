#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    n=[]
    e=[]
    for N_itr in range(N):
        fname,email = input().split()
        if email.endswith("@gmail.com"):
            if email not in e:
                n.append(fname)
                e.append(email)
    n.sort()
    for i in n:
        print(i)

