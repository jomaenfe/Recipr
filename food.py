# -*- coding: utf-8 -*-

from enum import Enum

from nutrient import *
from foodlib import *

# food component
class Food:
    # Las variables de clase son para atributos y métodos compartidos por todas las instancias de la clase  
       
    def __init__(self,names_param,alias_param,nutrients_param,description_param,action_param,unit_param,proteins_param,carbo_param,fat_param,pc_param):
        # Variables de instancia: para datos únicos de cada instancia

        # - food name in one or more different languages
        self.multi_names = names_param
        # - food name in one or more different languages
        self.multi_alias = alias_param
        # - one or more nutrient components. Considering all food has some nutritional value
        self.nutrients_list = nutrients_param        
        # - food description
        self.description = description_param
        # - food action
        self.action = action_param
        # - unit measure
        self.unit = unit_param
        # - % total Protein
        self.protein_percent = proteins_param
        # - % total Carbohydrates
        self.carbohydrates_percent = carbo_param
        # - % total Fat
        self.fat_percent = fat_param
        # - % total PC
        self.total_pc = pc_param       
        # - sum of total nutrient components weight value
        self.total_weight = 0        
        self.total_kcal = 0
        # traverse each nutrient to sum the weights
        for nutrient in nutrients_list:
            if nutrient.value > 0:
                self.total_weight += nutrient.value
            self.total_kcal += (Foodlib.GetEnergyValue(nutrient))[0]
        
        

        
        # Method to check if the current food contains a specific nutrient
        def HasNutrient(self,nutrient):

            result = False
            
            # Check if the parameter is a instance of Nutrient class
            if isinstance(nutrient,Nutrient):
                # Traverse each nutrient in the current food
                for ntr in self.nutrients_list:               
                    # First, check the scientific_name property  
                    if nutrient.scientific_name ==  ntr.scientific_name:
                        # This condition satisfied is enough to assure equality
                        result = True
                        break
                    # Traverse each parameter name
                    for nutrient_name in nutrient.multi_names:   
                        # Check if the current parameter name is in some nutrient of nutrients_list
                        if nutrient_name.upper() in [x.upper() for x in ntr.multi_names]:
                            result = True
                        break
                    break   
                    
            return result

        # Get the total weight of a specific nutrient name
        def GetNutrientQuantity(self,nutrient_name):

            result = 0
            if nutrient_name:
                # Traverse nutrient list
                for ntr in self.nutrients_list:
                    # without distinction between uppercase and lowercase
                    if (nutrient_name.upper() == scientific_name.upper()) or (nutrient_name.upper() in [x.upper() for x in ntr.multi_names]):
                        result = ntr.value
                        # the search ends
                        break
            
            return result

        

        

