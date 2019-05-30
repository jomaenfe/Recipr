# -*- coding: utf-8 -*-


import sys


# nutrient component
class Nutrient:
    # Las variables de clase son para atributos y métodos compartidos por todas las instancias de la clase  
    
    #CATEGORIES = list(Foodlib.CATEGORY_VALUES.keys()) 

    # 'nutrient_category': kcal|kJ. https://www.boe.es/doue/2011/304/L00018-00063.pdf pág.45
    ENERGY_VALUES = { "carbohydrate": (4,17), "polyalcohol": (2.4,10), "protein": (4,17), "fat": (9,37), "salatrim": (6,25),
                "alcohol": (7,29), "etanol": (7,29), "organic-acid": (3,13), "dietary-fiber": (2,8), "eritritol": (0,0),
                "mineral": (0,0), "vitamin": (0,0), "water": (0,0)

    }
    

    def __init__(self,scientific_param,names_param,unit_param,value_param,range_param1,range_param2,category_param):
        # Variables de instancia: son para datos únicos de cada instancia

        # - cientific name in english language.
        self.scientific_name = scientific_param
        # - nutrient component name in one or more different languages
        self.multi_names = names_param
        # - measure unit
        self.unit = unit_param
        # - the value
        self.value = value_param
        # - control range for the nutrient component value
        self.control_range = (range_param1,range_param2)
        # - nutrient component by a specific category fiel, (animal,vegetal,liquid,gas,other)
        self.category = category_param
        

    
    # Check if the current nutrient is in the control range
    def InControlRange(self):

        return self.value >= self.control_range[0] and self.value <= self.control_range[1]


    