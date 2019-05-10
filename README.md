[![Build Status](https://www.travis-ci.org/Stance4Health-Dev/common.svg?branch=master)](https://www.travis-ci.org/Stance4Health-Dev/common)
[![Coverage Status](https://coveralls.io/repos/github/Stance4Health-Dev/common/badge.svg?branch=master)](https://coveralls.io/github/Stance4Health-Dev/common?branch=master)

# common

# Requeriments development


## Behaviors based on Personas:

x.Store a nutrient component.  
    x.Store the nutrient component name in one or more different languages.
    x.Store scientific name of the nutrient component in english language.
    x.Set the unit of the nutrient component.  
    x.Set a control range of the nutrient component value.
    x.Get the food components that contain a specific nutrient component.
    x.Get the nutrient components by a specific category field(animal,vegetal,liquid,gas).
x.Store a food component.
    x.Set the food name in one or more different languages.
    x.Set one or more alias name in one or more different languages.
    x.Include one or more nutrient components. Considering all food has some nutritional value.
    x.Get the quantity of each nutrient component.
    x.Check if a food has a specific nutrient component.        
    x.Alert of a specific value of a nutrient component. 
    x.Get the total number of different nutrient components in the food.
    x.Calculate the total nutrient value of the food. Based on the sum of all nutrient components.    
    x.Get % total Protein.
    x.Get % total Carbohydrates.
    x.Get % total Fat.
    x.Get % total PC.        
    x.Set a description*.
    x.Set an action*. 
x.Store a recipe.
    x.Store the recipe name in one or more different languages.
    x.Include one or more food components. Considering all recipes has some food component.
    x.Set the cooking methods to get/cook the final recipe.    
    x.Find recipes based on food components and/or cooking methods.
    x.Suggest similar recipes based in the adding or removing a food component or cooking methods.
    x.Get recipe recommendations.
x.Store a user profile
    x.Set an unique email identificator.
    x.Set a password.
    x.Set basic healthy attributes (age, weight, height).
x.Store a diet.    
    x.Get balanced diet based on a user profile.
    x.Set zero or more goals of the user diet. Feel better, weight loss, eat just vegetables, gain muscle mass.
    x.Get a diet based on restrictions.
    x.Recompute diet if something unexpected happens. For example, the quantity of a determinated food changed, and that implies less or more calories.



*(based on https://github.com/Stance4Health-Dev/common/blob/master/values.md)

Others behaviors not considered for now:

x.Store a restaurante/local profile.
    x.Alert new free gluten recipes.
    x.Get available recipes of a specific restaurant.
x.Real time monitor.
    x.Monitor for data when is access.
    x.Monitor when an user eats.
    x.Monitor top food consumed.
x.Storage history of used data.
    x.Get food most accessed.

Some food variables in https://github.com/Stance4Health-Dev/docs/blob/master/data-representation/fields.md
description-household-weigh
Percent refuse