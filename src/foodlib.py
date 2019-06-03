# -*- coding: utf-8 -*-

from src import nutrient as nt
from src import food as fd


#from food import *
#from nutrient import *
import re
#from nutrient import Nutrient

# Measure list has to be in ascendent order
# TODO añadir otros nombres a cada 
MASS_UNITS = ["ug","mg","cg","dg","g","dag","hg","kg"]    
CAPACITY_UNITS = ["ul","ml","cl","dl","l","dal","hl","kl"]

MEASURES_LIST = [MASS_UNITS,CAPACITY_UNITS]




# Main class, tools to operate with food
class Foodlib(): 

    def __init__(self):
        pass  # do something
        
    # Grams converter to normalize operations
    # Añadir otro parametro, la otra unidad a convertir, y asi vale cualquiera => Conversor
    def ToGrams(self,value,unit):
        
        if unit and len(unit) < 5 and unit.upper != "G":
            if unit.upper() in [x.upper() for x in MASS_UNITS]:
                position = [x.upper() for x in MASS_UNITS].index(unit.upper())                
                if position < MASS_UNITS.index("g"):
                    # We have to divide the value 
                    for i in range(0,MASS_UNITS.index("g")-position):                        
                        value /= 10                    
                elif position > MASS_UNITS.index("g"):
                    # We have to multiplicate the value
                    for i in range(0,position-MASS_UNITS.index("g")):
                        value *= 10
        return value    

    # General Conversor of value units based on MASS_UNITS and CAPACITY_UNITS lists
    # Parameters: value_to_convert, from_unit, to_unit
    def Conversor(self,value,unit,tounit):

        # To avoid errors, remove posible multi whitespaces, and whitespace in the sides.
        unit = re.sub(' +', ' ', unit).lstrip().rstrip()
        tounit = re.sub(' +', ' ', tounit).lstrip().rstrip()

        # tratamos el tipo de las variables?
        # First, prove the parameters
        #
        # Check if the value is at least positive and different from zero
        # Check if the unit of the value exist
        # Check if tounit parameter exist
        # Evaluate the last two parameters to check if they are differents, . Check whitesapce in the middle?
        # Have to check if unit and tounit are str and value is a double?
        #        
        
        if value > 0 and unit and tounit and (unit.upper() != tounit.upper()):
            # Traverse the measures list
            for measures in MEASURES_LIST:
                # Check if unit and tounit are in the current sublist
                if unit.upper() in [x.upper() for x in measures] and tounit.upper() in [x.upper() for x in measures]:
                    # reference position
                    ref_pos = [x.upper() for x in MASS_UNITS].index(unit.upper())
                    # unit we want
                    param_pos = [x.upper() for x in MASS_UNITS].index(tounit.upper())

                    if ref_pos < param_pos:
                        # We have to divide the value (param_pos-ref_pos) times
                        for i in range(0,param_pos-ref_pos):
                            value %= 10  
                    elif ref_pos > param_pos:
                        # We have to multiplicate the value (ref_pos-param_pos) times
                        for i in range(0,ref_pos-param_pos):
                            value *= 10
                else:
                    # Return the value with no changes
                    pass            

        return value  

    # Calculator kcal from a specific nutrient
    def GetEnergyValue(self,nutrient):

        result = (0,0)
        # Check if the parameter is a nutrient (Contains the category and the total weight)
        if isinstance(nutrient,nt.Nutrient):
            # Get the parameter category values from the ENERGY_VALUES list.
            # ENERGY_values = [entry[0].upper() for entry in ENERGY_VALUES.items()][nutrient.category.lstrip().rstrip().replace(' ','-').upper()]
            for energy_value,x in nt.Nutrient.ENERGY_VALUES.items():
                
                if (nutrient.category.lstrip().rstrip().replace(' ','-').upper() == energy_value.upper()):                    
                    # Calculate the total energy value based on the total grams of the nutrient
                    kcal = self.ToGrams(nutrient.value,nutrient.unit)*x[0]
                    kJ = self.ToGrams(nutrient.value,nutrient.unit)*x[1]
                    result = (kcal,kJ)             
                    break   
            
            

        return result
