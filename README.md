[![Build Status](https://www.travis-ci.org/Stance4Health-Dev/common.svg?branch=master)](https://www.travis-ci.org/Stance4Health-Dev/common)
[![Coverage Status](https://coveralls.io/repos/github/Stance4Health-Dev/common/badge.svg?branch=master)](https://coveralls.io/github/Stance4Health-Dev/common?branch=master)

# Requirements development

## Behaviors based on Personas:

- Store a nutrient component.  
    - Store the nutrient component name in one or more different languages.
    - Store scientific name of the nutrient component in english language.
    - Set the unit of the nutrient component.  
    - Set a control range of the nutrient component value.
    - Get the food components that contain a specific nutrient component.
    - Get the nutrient components by a specific category field(animal,vegetal,liquid,gas).
- Store a food component.
    - Set the food name in one or more different languages.
    - Set one or more alias name in one or more different languages.
    - Include one or more nutrient components. Considering all food has some nutritional value.
    - Get the quantity of each nutrient component.
    - Check if a food has a specific nutrient component.        
    - Alert of a specific value of a nutrient component. 
    - Get the total number of different nutrient components in the food.
    - Calculate the total nutrient value of the food. Based on the sum of all nutrient components.    
    - Get % total Protein.
    - Get % total Carbohydrates.
    - Get % total Fat.
    - Get % total PC.        
    - Set a description*.
    - Set an action*. 
- Store a recipe.
    - Store the recipe name in one or more different languages.
    - Include one or more food components. Considering all recipes has some food component.
    - Set the cooking methods to get/cook the final recipe.    
    - Find recipes based on food components and/or cooking methods.
    - Suggest similar recipes based in the adding or removing a food component or cooking methods.
    - Get recipe recommendations.
- Store a user profile
    - Set an unique email identificator.
    - Set a password.
    - Set basic healthy attributes (age, weight, height).
- Store a diet.    
    - Get balanced diet based on a user profile.
    - Set zero or more goals of the user diet. Feel better, weight loss, eat just vegetables, gain muscle mass.
    - Get a diet based on restrictions.
    - Recompute diet if something unexpected happens. For example, the quantity of a determinated food changed, and that implies less or more calories.



*(based on https://github.com/Stance4Health-Dev/common/blob/master/values.md)

Others behaviors not considered for now:

- Store a restaurante/local profile.
    - Alert new free gluten recipes.
    - Get available recipes of a specific restaurant.
- Real time monitor.
    - Monitor for data when is access.
    - Monitor when an user eats.
    - Monitor top food consumed.
- Storage history of used data.
    - Get food most accessed.

Some food variables in https://github.com/Stance4Health-Dev/docs/blob/master/data-representation/fields.md
description-household-weigh
Percent refuse