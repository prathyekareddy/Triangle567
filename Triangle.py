# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a,b,c):   
    if a > 200 or b > 200 or c > 200:
        return "InvalidInput"
    if (a <= 0) or (b <= 0) or (c <= 0):
        return "InvalidInput"
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return "InvalidInput"
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return "NotATriangle"

    if a == b and b == c and a == c:
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return "Isosceles"
