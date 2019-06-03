# -*- coding: utf-8 -*-


from src import nutrient as nt
from src import foodlib as fdlib

# food component
class Food():
    # Las variables de clase son para atributos y métodos compartidos por todas las instancias de la clase  
    #f = foodlib.Foodlib()
    foodlib_obj = fdlib.Foodlib()

    def __init__(self,names_param,alias_param,nutrients_param,description_param,action_param,unit_param,value_param,proteins_param,carbo_param,fat_param,pc_param):
        # Variables de instancia: para datos únicos de cada instancia
        
        # - food name in one or more different languages
        self.multi_names = names_param
        # - food alias in one or more different languages
        self.multi_alias = alias_param
        # - one or more nutrient components. Considering all food has some nutritional value
        self.nutrients_list = nutrients_param        
        # - food description
        self.description = description_param
        # - food action
        self.action = action_param
        # - measure unit 
        self.unit = unit_param
        # - value
        self.value = value_param        
        # - % total Protein
        self.protein_percent = proteins_param
        # - % total Carbohydrates
        self.carbohydrates_percent = carbo_param
        # - % total Fat
        self.fat_percent = fat_param
        # - % total PC
        self.total_pc = pc_param       
        # - sum of total nutrient components weight value
        self.total_nutrients_weight = 0        
        self.total_kcal = 0
        # traverse each nutrient to sum the weights
        #for nutrient in self.nutrients_list:
            #if nutrient.value > 0:
                #self.total_nutrients_weight += nutrient.value
                #self.total_kcal += (self.foodlib.GetEnergyValue(nutrient))[0]
        
        # - other components
        self.other_components_value = self.value - self.total_nutrients_weight

    # Method to check if two foods are equal
    def EqualTo(self,food):            
        equal = False
        if isinstance(food,Food) and len(self.nutrients_list) == len(food.nutrients_list):
            if set(self.nutrients_list) == set(food.nutrients_list):
                equal = True
        return  equal

    
    # Method to check if the current food contains a specific nutrient
    def HasNutrient(self,nutrient):

        result = False        
       
        # Check if the parameter is a instance of Nutrient class
        if isinstance(nutrient,nt.Nutrient):

            # Traverse each nutrient in the current food
            for ntr in self.nutrients_list: 

                # First, check the scientific_name property  
                if nutrient.scientific_name.upper() ==  ntr.scientific_name.upper():
                    # This condition satisfied is enough to assure equality
                    result = True                    
                    
                # Traverse each parameter name
                for nutrient_name in nutrient.multi_names:   
                    # Check if the current parameter name is in some nutrient of nutrients_list
                    if nutrient_name.upper() in [x.upper() for x in ntr.multi_names]:
                        result = True

                if result:
                    break
        
                
        return result

    # Get the total weight of a specific nutrient name
    def GetNutrientQuantity(self,nutrient_name):

        result = 0
        if nutrient_name and isinstance(nutrient_name, str):
            # Traverse nutrient list
            for ntr in self.nutrients_list:
                # without distinction between uppercase and lowercase
                if (nutrient_name.upper() == ntr.scientific_name.upper()) or (nutrient_name.upper() in [x.upper() for x in ntr.multi_names]):
                    result = ntr.value
                    # the search ends
                    break
        
        return result

    def getTotalKcal():
        pass