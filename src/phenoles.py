# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:55:36 2019

@author: andreamorgar
"""


import pyexcel as pe
import numpy as np
import pandas as pd



# CONVERSIÓN A MATRIZ

def get_polyphenols(filename):

    sheet = pe.get_sheet(file_name = filename)

    # Por eficiencia, vamos a trabajar con numpy, así que tenemos que pasar de una
    # hoja de cálculo a una matriz con la que si que sepamos trabajar
    npsheet = np.array([[i for i in j] for j in sheet])


    # CONVERSIÓN A DATAFRAME

    # Para realizar agrupaciones de manera eficiente, podemos usar el paquete pandas,
    # por lo que vamos a convertir la matriz en un dataframe. La fila 1 tiene los
    # nombres de las columnas, pero para trabajar de una forma más cómoda nos
    # interesa tener esos nombres como nombres de columna del dataframe (ahora
    # mismo tenemos como nombre de columna, el índice de la misma)

    # Por tanto, obtenemos un dataframe excluyendo la primera fila (nombres de las
    # columnas)
    phenoles_df = pd.DataFrame(npsheet[1:,:])

    # Ponemos el nombre correcto a las columnas del dataframe
    phenoles_df.columns = sheet.row[0]


    # -------------------- OBTENER POLIFENOLES TOTALES ----------------------------------
    totals = phenoles_df[phenoles_df['compound'] == 'Polyphenols, total']
    polyphenol_total_values = totals[['food','mean']].groupby('food')['mean'].agg(
        lambda x: pd.to_numeric(x, errors='coerce').sum())


    # -------------------- OBTENER POLIFENOLES B ------------------------------------------

    # Ahora agrupamos por nombre de alimento. Queremos obtener la suma de los
    # valores de los fenoles individuales. Para ello:

    # 1. No nos interesa el valor de los polifenoles totales, ya que precisamente,
    # es el valor que intentamos obtener calculando la suma de las medias de los
    # valores de los polifenoles individuales, por lo que los excluimos de nuestro
    # dataset.

    # Para ello tenemos que quitarle todas las columnas que tengan compound = polifenoles totales.
    individuals = phenoles_df[phenoles_df['compound'] != 'Polyphenols, total']

    # 2. Para ello, aplicamos groupby, pero solo a las columnas del dataframe que
    # nos interesan.(food y mean)

    # 3. Agrupamos el dataframe en función de la comida. De esta forma tendremos
    # una serie de valores agrupados por el valor que toma la columna "food" del
    # dataframe.


    agrupacion = individuals[['food','mean']].groupby('food')['mean'].agg(
        lambda x: pd.to_numeric(x, errors='coerce').sum())



    # Queremos por cada comida,la suma de los polifenoles implicados

    res = individuals[['food','mean','compound_sub_group']].groupby(['food','compound_sub_group'])['mean'].agg(
        lambda x: pd.to_numeric(x, errors='coerce').sum()).reset_index()

    #res.to_excel("polifenoles-compound-sub-group.xlsx")


    # ----------------------------- SUBFAMILIAS----------------------------------------------------

    res_compound_subgroup = res.pivot_table(index=['food'], columns=['compound_sub_group'],
                         values='mean', aggfunc='first', fill_value='')


    # Problema: al juntar se tiene que tener en cuenta que existen comidas que no tienen especificados
    # el valor para todos los subgrupos de componentes. Al rellenar la tabla, ocurre que les pone un 0 automati
    #camente. Pensamos que en nuestro caso debemos especificar que este valor es un nan, puesto que no está
    # en nuestra tabla, y no un cero.


    # ------------------------------- FAMILIAS -------------------------------------------------
    res_group = individuals[['food','mean','compound_group']].groupby(['food','compound_group'])['mean'].agg(
        lambda x: pd.to_numeric(x, errors='coerce').sum()).reset_index()

    res_compound_group = res_group.pivot_table(index=['food'], columns=['compound_group'],
                         values='mean', aggfunc='first', fill_value='')

    # problema: existe Lignans en compound group y en compound sub group (mismo valor). Le cambiamos el nombre
    # para distinguirlo.
    res_compound_group.rename(index=str,columns={"Lignans":"Lignans Group", "Flavonoids":"Flavonoids Group",
                                                 "Other polyphenols":"Other polyphenols Group", "Phenolic acids":
                                                     "Phenolic acids Group", "Stilbenes": "Stilbenes Group"},inplace=True)


    # Obtenemos todos los polifenoles individuales para cada uno de los alimentos
    res_individuals = individuals[['food','mean','compound']].groupby(['food','compound'])['mean'].agg(
        lambda x: pd.to_numeric(x, errors='coerce').sum()).reset_index()

    # Para poder juntarlo después, necesitamos reorganizar la tabla. Para ello, necesitamos tener en cada fila
    # las comidas y en cada columna los polifenoles individuales.
    res_compound_individual = res_individuals.pivot_table(index=['food'], columns=['compound'],
                         values='mean', aggfunc='first', fill_value='')


    # ----------------- CONCATENACIÓN -----------------------------------------------------------------

    # Ahora tenemosque montar la tabla, teniendo en cuenta dos cosas:
    # a) No todos los alimentos tienen el valor de polifenoles totales calculado.
    # b) Hay alimentos que solo tienen el valor de polifenoles totales.

#    # 1. Obtenemos un dataframe con nombre,grupo y subgrupo
    polifenoles = phenoles_df[['food_group','food_sub_group', 'food']].groupby('food').min()

#    df_polifenoles_totales['polyphenols, total'] = df_polifenoles_totales['polyphenols, total'].apply(pd.to_numeric, errors = 'coerce')

    # Concatenamos el valor de polifenoles totales
    result = pd.concat([polifenoles, polyphenol_total_values], axis=1, join_axes=[polifenoles.index])
    result.rename(index=str,columns={"mean":"Polifenoles Totales Programa"},inplace=True)

    # Concatenamos el valor de polifenoles B
    result = pd.concat([result, agrupacion], axis=1, join_axes=[result.index])
    # Tiene de nombre mean -> lo cambiamos
    result.rename(index=str,columns={"mean":"Polifenoles B (calculados)"},inplace=True)


    # concatenamos lo anterior con los resultados de los grupos de polifenoles para cada comida
    result = pd.concat([result, res_compound_group], axis=1, join_axes=[result.index])

    # concatenamos lo anterior con los resultados de los subgrupos de polifenoles para cada comida
    result = pd.concat([result, res_compound_subgroup], axis=1, join_axes=[result.index])
    #nota: recordar qe hay alimentos que solo tienen polifenoles totales definidos

    # concatenamos lo anterior con los resultados de los grupos de polifenoles para cada comida
    result = pd.concat([result, res_compound_individual], axis=1, join_axes=[result.index])



    return result

# result = get_polyphenols("phenol-explorer-all.xlsx")
# # Guardamos resultados
# result.to_excel("result.xlsx")
