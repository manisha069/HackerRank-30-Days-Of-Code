import math
import os
import random
import re
import sys

def toBinary(n):
    ls=list()
    rem=n
    while rem>0:
        x=rem%2
        ls.append(x)
        rem=rem//2
    ls.reverse()
    return ls
        

if __name__ == '__main__':
    n = int(input())
    ls=toBinary(n)
    c=list()
    
    for i in range(len(ls)-1):
        count=0
        if ls[i]==1:
            j=i
            count=1
            while(ls[j+1]==1):
                count+=1
                j+=1
                if j>=len(ls)-1:
                    break
        c.append(count)
    print(max(c))
