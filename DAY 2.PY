#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(mc, tip_percent, tax_percent):
    x=(tip_percent*mc)/100
    y=(tax_percent*mc)/100
    k=x+y+mc
    s=int(k)+0.5
    if(k>=s):
        print(int(k)+1)
    else:
        print(int(k))
    

if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    solve(meal_cost, tip_percent, tax_percent)
