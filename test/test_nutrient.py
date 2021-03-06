# -*- coding: utf-8 -*-


import unittest

from src import nutrient as nt

class nutrientTestCase(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_InControlRange(self):
        nutrient = nt.Nutrient("potassium",["potasio","pottasche"],"g",7,3.5,5.3,"mineral")
        self.assertEqual(nutrient.InControlRange(), False, "Incorrect values")
        nutrient = nt.Nutrient("potassium",["potasio","pottasche"],"g",5,3.5,5.3,"mineral")
        self.assertEqual(nutrient.InControlRange(), True, "Incorrect values")

   
# Testing
#test_nutrient = nutrientTestCase()
#test_nutrient.test_InControlRange()