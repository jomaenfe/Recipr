# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:55:36 2019

@author: andreamorgar
"""


import unittest
import pyexcel as pe
from src import phenoles as phs



class correspondencesTestCase(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_polyphenols(self):
        # Get the resulting database (same values as example of the documentation)
        self.result = phs.get_polyphenols("test/example-test2.xlsx")
        # self.result.to_excel("prueba.xlsx")

        # Now we are going to check that values are correct

        # Check if shape is correct
        self.assertEqual(self.result.shape[0], 4, "Number of rows doesn't match")
        self.assertEqual(self.result.shape[1], 15, "Number of columns doesn't match")

        # We randomly choose some cells, to check if they have or not the correct values
        self.assertEqual(self.result['G2'].values[1],0.7,"The value of the cell is not correct")
        self.assertEqual(self.result['S3'].values[1],0.7,"The value of the cell is not correct")
        self.assertEqual(self.result['S3'].values[2],'',"The value of the cell is not correct")
        self.assertEqual(self.result['C1'].values[0],1.5,"The value of the cell is not correct")
        self.assertEqual(self.result['food_group'].values[3],'B',"The value of the cell is not correct")
        self.assertEqual(self.result['Polifenoles B (calculados)'].values[2],1.2,"The value of the cell is not correct")
