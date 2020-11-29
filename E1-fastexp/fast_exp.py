# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:13:05 2020

@author: dfolch
"""

def fast_exp_n(a, b):
    if b==0: return 1
    elif b>0:
        exp=(fast_exp_e(a*a,(b/2)) if b%2==0 else fast_exp_e(a*a,((b-1)/2))*a)
    return exp

def fast_exp_e(a, b):
    if b==0: return 1
    a,b=(1/a, abs(b)) if b < 0 else (a, b)
    exp=(fast_exp_e(a*a,(b/2)) if b%2==0 else fast_exp_e(a*a,((b-1)/2))*a)
    return exp


