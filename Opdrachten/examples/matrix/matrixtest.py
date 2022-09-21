#!/usr/bin/env python

import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    vectorList1 = ([1, 2, 3], [4, 5, 6])
    vectorList2 = ([1, 1, 1], [1, 1, 1])   
    matrix1 = Matrix(vectorList1)
    matrix2 = Matrix(vectorList2)
    matrix3 = matrix1 + matrix2
    
    def test_addVectors(self):
        print("test_addVectors")
        self.assertEqual(self.matrix1.addVectors, ([1, 2, 3], [4, 5, 6]))
        self.assertEqual(self.matrix2.addVectors, ([1, 1, 1], [1, 1, 1]))
        self.assertEqual(self.matrix3.addVectors, matrix1 + matrix2)
        
if __name__ == '__main__':
    unittest.main()