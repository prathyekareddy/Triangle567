# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 should be a Right triangle')
        self.assertEqual(classify_triangle(6, 8, 10),'Right','6, 8, 10 should be a Right triangle')
        self.assertEqual(classify_triangle(15, 20, 25),'Right','15, 20, 25 should be a Right triangle')
        
    
    def testInput(self):
        self.assertEqual(classify_triangle(-2,-3,-4),"InvalidInput","-2,-3,-4 are Invalid Inputs")
        self.assertEqual(classify_triangle(200,300,400),"InvalidInput","200,300,400 are Invalid Inputs")
        self.assertEqual(classify_triangle(7,9,16),'NotATriangle','7,9,16 are Invalid Inputs')


    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(6,6,6),"Equilateral","6,6,- is a Equilateral")
        self.assertEqual(classify_triangle(40,40,40),"Equilateral","40,40,40 is a Equilateral")

    def testScaleneTriangles(self): 
        self.assertEqual(classify_triangle(4,9,8),'Scalene','4,9,2 should be Scalene')
        self.assertEqual(classify_triangle(10,13,21),'Scalene','10,13,21 should be Scalene')
        self.assertEqual(classify_triangle(40,90,100),'Scalene','40,90,100 should be Scalene')
        
    def testIsocelesTriangles(self): 
        self.assertEqual(classify_triangle(33,9,33),'Isosceles','33,9,33 should be an Isosceles')  
        self.assertEqual(classify_triangle(33,33,9),"Isosceles","33,33,9 should be an Triangle")
        self.assertEqual(classify_triangle(9,33,33),"Isosceles","9,33,33 should be an Triangle")
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
