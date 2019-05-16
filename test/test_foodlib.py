# -*- coding: utf-8 -*-


import unittest
import sys

from foodlib import Foodlib
from nutrient import Nutrient

class FoodlibTestCase(unittest.TestCase):

    foodlib = Foodlib()

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_ToGrams(self):
       
        self.assertEqual(self.foodlib.ToGrams(1000,"mg"), 1, "Incorrect unit")
        self.assertEqual(self.foodlib.ToGrams(1000,"mG"), 1, "Incorrect unit")
        self.assertEqual(self.foodlib.ToGrams(300,"MG"), 0.3, "Incorrect unit")
        self.assertEqual(self.foodlib.ToGrams(100,"hg"), 10000, "Incorrect unit")

    def test_Conversor(self):
        
        self.assertEqual(self.foodlib.Conversor(10,"hg","g"), 1000, "Incorrect unit")

    def test_GetEnergyValue(self):        
      
        # scientific_param,names_param,unit_param,value_param,range_param1,range_param2,category_param
        nutrient = Nutrient("potassium",["potasio","pottasche"],"g",5,3.5,5.3,"mineral")
        self.assertEqual(self.foodlib.GetEnergyValue(nutrient), (0,0), "Incorrect value")
        nutrient = Nutrient("inulin",["inulina","inuline"],"g",5,3.5,5.3,"carbohydrate")
        self.assertEqual(self.foodlib.GetEnergyValue(nutrient), (20,85), "Incorrect value")


test = FoodlibTestCase()

test.test_ToGrams()
test.test_Conversor()
test.test_GetEnergyValue()