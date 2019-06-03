# -*- coding: utf-8 -*-


import unittest
import sys

from src import nutrient as nt
from src import food as fd

class foodTestCase(unittest.TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_Equal(self):

        #scientific_param,names_param,unit_param,value_param,range_param1,range_param2,category_param
        nutrient1 = nt.Nutrient("potassium",["potasio","pottasche"],"mg",126,125,127,"mineral")
        nutrient2 = nt.Nutrient("magnesium",["magnesio","magnésium"],"mg",10,9,11,"mineral")
        nutrient3 = nt.Nutrient("cholesterol",[],"g",373,370,375,"carbohydrate")

        nutrient2 = nt.Nutrient("sucrose",["sacarosa","saccharose"],"g",6,3.5,5.3,"carbohydrate")
        
        nutrient4 = nt.Nutrient("lactose",["lactosa"],"g",6,3.5,5.3,"mineral")
        nutrient5 = nt.Nutrient("vitamin-b1-tiamina",["vitamina-A-IU"],"mg",6,3.5,5.3,"vitamin")
        
        
        desctiption = "They are protected by a shell and rich in proteins"
        action = ""
        unit = "g"
        value = 100
        #names_param,alias_param,nutrients_param,description_param,action_param,unit_param,proteins_param,carbo_param,fat_param,pc_param
        food_object1 = fd.Food(["chicken-egg","huevo-de-gallina","Oeuf-de-poule"],[],[nutrient1,nutrient2,nutrient3],desctiption,action,unit,value,0,0,0,0)
        food_object2 = fd.Food(["chicken-egg","ovo-de-pollo","Oeuf-de-poule"],[],[nutrient1,nutrient2,nutrient3],desctiption,action,unit,value,0,0,0,0)
        
        self.assertEqual(food_object1.EqualTo(food_object2), True, "Incorrect value")
        food_object1 = fd.Food(["chicken-egg","huevo-de-gallina","Oeuf-de-poule"],[],[nutrient1,nutrient5,nutrient3],desctiption,action,unit,value,0,0,0,0)
        self.assertEqual(food_object1.EqualTo(food_object2), False, "Incorrect value")

    def test_HasNutrient(self):
        nutrient1 = nt.Nutrient("potassium",["potasio","pottasche"],"mg",126,125,127,"mineral")
        nutrient2 = nt.Nutrient("magnesium",["magnesio","magnésium"],"mg",10,9,11,"mineral")
        nutrient3 = nt.Nutrient("cholesterol",[],"g",373,370,375,"carbohydrate")                     
        desctiption = "They are protected by a shell and rich in proteins"
        action = ""
        unit = "g"
        value = 100
        #names_param,alias_param,nutrients_param,description_param,action_param,unit_param,proteins_param,carbo_param,fat_param,pc_param
        food_object1 = fd.Food(["chicken-egg","huevo-de-gallina","Oeuf-de-poule"],[],[nutrient1,nutrient2,nutrient3],desctiption,action,unit,value,0,0,0,0)
        self.assertEqual(food_object1.HasNutrient(nutrient2), True, "Incorrect nutrient")
        
        # Removing the scientific name and alias
        nutrient2 = nt.Nutrient("",["magnesio",""],"mg",10,9,11,"mineral")
        self.assertEqual(food_object1.HasNutrient(nutrient2), True, "Incorrect nutrient")

        nutrient2 = nt.Nutrient("",["majnesio",""],"mg",10,9,11,"mineral")
        self.assertEqual(food_object1.HasNutrient(nutrient2), False, "Incorrect nutrient")

        nutrient2 = nt.Nutrient("",["",""],"mg",10,9,11,"mineral")
        self.assertEqual(food_object1.HasNutrient(nutrient2), False, "Incorrect nutrient")

        self.assertEqual(food_object1.HasNutrient("nutrient2"), False, "Incorrect nutrient")


    def test_GetNutrientQuantity(self):

        nutrient1 = nt.Nutrient("potassium",["potasio","pottasche"],"mg",126,125,127,"mineral")
        nutrient2 = nt.Nutrient("magnesium",["magnesio","magnésium"],"mg",10,9,11,"mineral")
        nutrient3 = nt.Nutrient("cholesterol",[],"g",373,370,375,"carbohydrate")                     
        desctiption = "They are protected by a shell and rich in proteins"
        action = ""
        unit = "g"
        value = 100
        #names_param,alias_param,nutrients_param,description_param,action_param,unit_param,proteins_param,carbo_param,fat_param,pc_param
        food_object1 = fd.Food(["chicken-egg","huevo-de-gallina","Oeuf-de-poule"],[],[nutrient1,nutrient2,nutrient3],desctiption,action,unit,value,0,0,0,0)
        self.assertEqual(food_object1.GetNutrientQuantity("cholesterol"), 373, "Incorrect nutrient")
        
        self.assertEqual(food_object1.GetNutrientQuantity("cHolesterol"), 373, "Incorrect nutrient")
        self.assertEqual(food_object1.GetNutrientQuantity("cHol esterol"), 0, "Incorrect nutrient")
        self.assertEqual(food_object1.GetNutrientQuantity(""), 0, "Incorrect nutrient")
        self.assertEqual(food_object1.GetNutrientQuantity(777), 0, "Incorrect nutrient")
        self.assertEqual(food_object1.GetNutrientQuantity("magnésium"), 10, "Incorrect nutrient")
        







#test = foodTestCase()
#test.test_Equal()
#test.test_HasNutrient()
#test.test_GetNutrientQuantity()
        