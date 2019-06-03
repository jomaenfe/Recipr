# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:55:36 2019

@author: andreamorgar
"""


import unittest

import pandas as pd
import pyexcel as pe

from src import phenoles as phs



class correspondencesTestCase(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_polyphenols(self):
        # Obtenemos la base de datos resultante
        result = phs.get_polyphenols("test/example-test2.xlsx")

        # Ahora vamos a comprobar que tiene los valores correctos

        # Primero comprobamos número de filas y de columnas
        self.assertEqual(result.shape[0], 4, "Number of rows doesn't match")
        self.assertEqual(result.shape[1], 15, "Number of columns doesn't match")


        self.assertEqual(result['G2'].values[1],0.7,"The value of the cell is not correct")

        #self.assertEqual(result['C1'].values[3],0.7,"The value of the cell is not correct")

        #self.assertEqual(result['C1'].values[0],3.3,"The value of the cell is not correct")


        self.assertEqual(result['food_group'].values[3],'B',"The value of the cell is not correct")

        #self.assertEqual(result['Polifenoles B (calculados) '].values[2],0.9,"The value of the cell is not correct")







# result = get_polyphenols("example-test2.xlsx")

# result.to_excel("test_example.xlsx")
