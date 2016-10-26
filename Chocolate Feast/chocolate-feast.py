#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    
    money_chocolates = n//c
    wrappers = money_chocolates
    
    wrapper_chocolates = 0
    
    while float(wrappers)/m >= 1.0:
        wrapper_chocolates = wrapper_chocolates + float(wrappers)//m
        wrappers = wrappers - (float(wrappers)//m)*m + float(wrappers)//m

    total_chocolates = money_chocolates + wrapper_chocolates
    
    print(int(total_chocolates))