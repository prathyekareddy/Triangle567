# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 should be a Right triangle')
        self.assertEqual(classifyTriangle(6, 8, 10),'Right','6, 8, 10 should be a Right triangle')
        self.assertEqual(classifyTriangle(15, 20, 25),'Right','15, 20, 25 should be a Right triangle')
        
    
    def testInput(self):
        self.assertEqual(classifyTriangle(-2,-3,-4),"InvalidInput","-2,-3,-4 are Invalid Inputs")
        self.assertEqual(classifyTriangle(200,300,400),"InvalidInput","200,300,400 are Invalid Inputs")
        self.assertEqual(classifyTriangle(7,9,16),'NotATriangle','7,9,16 are Invalid Inputs')


    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(6,6,6),"Equilateral","6,6,- is a Equilateral")
        self.assertEqual(classifyTriangle(40,40,40),"Equilateral","40,40,40 is a Equilateral")

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(4,9,8),'Scalene','4,9,2 should be Scalene')
        self.assertEqual(classifyTriangle(10,13,21),'Scalene','10,13,21 should be Scalene')
        self.assertEqual(classifyTriangle(40,90,100),'Scalene','40,90,100 should be Scalene')
        
    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(33,9,33),'Isosceles','33,9,33 should be an Isosceles')  
        self.assertEqual(classifyTriangle(33,33,9),"Isosceles","33,33,9 should be an Triangle")
        self.assertEqual(classifyTriangle(9,33,33),"Isosceles","9,33,33 should be an Triangle")
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()