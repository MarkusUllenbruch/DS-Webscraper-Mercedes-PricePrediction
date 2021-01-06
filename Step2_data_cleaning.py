# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:23:41 2021

Data Cleaning & Wrangling of Raw Data

@author: Markus Ullenbruch
"""

import numpy as np
import pandas as pd
import glob
import os
import math

path_raw_data = r'./data_raw'  #Path to raw data
all_files = glob.glob(os.path.join(path_raw_data, "*.csv"))  #List of all files ending with .csv
df_from_each_file = (pd.read_csv(file) for file in all_files)  #Make pandas dataframe from all files
data = pd.concat(df_from_each_file, ignore_index=True)  # Concatenate them together to single dataframe

# Drop row when price is -1 (not available)
data = data[data['price'] != '-1']

# Remove '.', '€' and '(Brutto)' in price and make numeric
data['price'] = data['price'].apply(lambda x: float(x.lower().replace('(brutto)', '').replace('.','').replace('€','')))

# Make Age of car in [years] from 'first_registration'
def make_car_age(x):
    '''Parse first_registration string into age in years'''
    year = float(x.split('/')[1])
    month = float(x.split('/')[0])
    age = 2020.0 - year - month/12.0
    return age

data['age'] = data['first_registration'].apply(make_car_age)

# delete oldtimer (we do not want to predict oldtimer bc they are too specific)
data = data[data.age < 30.0]

# Remove '.' and 'km' and '(Brutto)' in milage and make numeric
data['milage'] = data['milage'].apply(lambda x: float(x.lower().replace('km', '').replace('.','')))
milage_max = 0.8*1e6
data['milage'] = data['milage'].apply(lambda x: milage_max if x > milage_max else x)

# Make power_ps
data['power_ps'] = data['power'].apply(lambda x: float(x.lower().replace('(', '').replace(')', '').split()[2]) if x != '-1' else None)

# Make power_kw
data['power_kw'] = data['power'].apply(lambda x: float(x.lower().replace('(', '').replace(')', '').split()[0]) if x != '-1' else None)

# Unfallschaden
def make_damage(x):
    xl = x.lower()
    if 'repariert' in xl:
        return 'repaired'
    elif 'unfallfrei' in xl:
        return 'without'
    else:
        return 'na'
data['Schaden'] = data['damage'].apply(make_damage)

# number of owners make categorical strings
data['num_owners'] = data['num_owners'].apply(lambda x: str(x) if x != -1 else 'na')

# cartype simplification
def simplify_cartype(x):
    xl = x.lower()
    xl = xl.replace(',','')
    xl = xl.replace('tageszulassung', '').replace('vorführfahrzeug', '')
    if 'suv' in xl:
        return 'suv'
    elif 'van' in xl or 'minibus' in xl:
        return 'van'
    elif 'cabrio' in xl or 'roadster' in xl:
        return 'cabrio'
    elif 'sportwagen' in xl or 'coup' in xl:
        return 'sport'
    elif 'limousine' in xl:
        return 'limousine'
    elif 'kombi' in xl:
        return 'kombi'
    elif 'kleinwagen' in xl:
        return 'kleinwagen'
    elif 'andere' in xl:
        return 'andere'
    else:
        return xl

data['car_type'] = data['car_type'].apply(simplify_cartype)


# make a row for 'Model' and parse carmodel from carname
def make_car_model(x):
    xl = x.lower()
    if 'a-klasse' in xl or 'a klasse' in xl or ' A ' in x or 'A1' in x or 'A2' in x or 'A4' in x:
        return 'A-Klasse'
    
    elif 'b-klasse' in xl or 'b klasse' in xl or ' B ' in x or 'B1' in x or 'B2' in x:
        return 'B-Klasse'
    
    elif 'c-klasse' in xl or 'c klasse' in xl or ' c ' in xl or 'c1' in xl or 'c2' in xl or 'c3' in xl:
        return 'C-Klasse'
    
    elif 'e-klasse' in xl or 'e klasse' in xl or ' E ' in x or 'e2' in xl or 'e3' in xl:
        return 'E-Klasse'
    
    elif 's-klasse' in xl or 's klasse' in xl or ' S ' in x:
        return 'S-Klasse'
    
    elif 'g-klasse' in xl or 'g klasse' in xl or ' G ' in x:
        return 'G-Klasse'
    
    elif 'm-klasse' in xl or 'm klasse' in xl or 'ML' in x or 'ml' in xl:
        return 'M-Klasse'
    
    elif 'x-klasse' in xl or 'x klasse' in xl:
        return 'X-Klasse'
    
    elif 'r-klasse' in xl or 'r klasse' in xl or ' r ' in xl:
        return 'R-Klasse'
    
    elif 'v-klasse' in xl or 'v klasse' in xl or ' v ' in xl or 'viano' in xl:
        return 'V-Klasse'
    
    elif 'marco polo' in xl or 'marco' in xl or 'polo' in xl:
        return 'MarcoPolo'
    
    elif 'cla' in xl:
        return 'CLA'
    
    elif 'clc' in xl:
        return 'CLC'
    
    elif 'clk' in xl:
        return 'CLK'
    
    elif 'cl' in xl:
        return 'CL'
    
    elif 'cls' in xl:
        return 'CLS'
    
    elif 'sl' in xl:
        return 'SL'
    
    elif 'slc' in xl:
        return 'SLC'
    
    elif 'slk' in xl:
        return 'SLK'
    
    elif 'slr' in xl:
        return 'SLR'
    
    elif 'sls' in xl:
        return 'SLS'
    
    elif 'gla' in xl:
        return 'GLA'
    
    elif 'glb' in xl:
        return 'GLB'
    
    elif 'glc' in xl:
        return 'GLC'
    
    elif 'glk' in xl:
        return 'GLK'
    
    elif 'gle' in xl:
        return 'GLE'
    
    elif 'gls' in xl:
        return 'GLS'
    
    elif 'gl' in xl:
        return 'GL'
    
    elif 'GT' in x:
        return 'GT'
    
    elif 'vaneo' in xl or 'citan' in xl:
        return 'Vaneo'
    
    elif 'vito' in xl:
        return 'Vito'
    
    elif 'sprinter' in xl:
        return 'Sprinter'
    
    else:
        return 'OTHER'
    
data['Model'] = data['carname'].apply(make_car_model)


# feature engineering/ creating new features out of existing ones

# AMG
data['amg'] = data['carname'].apply(lambda x: 1 if 'amg' in x.lower() else 0)
# McLaren
data['mc_laren'] = data['carname'].apply(lambda x: 1 if 'laren' in x.lower() else 0)
# Black-Series
data['blk_series'] = data['carname'].apply(lambda x: 1 if 'black series' in x.lower() or 'black-series' in x.lower() else 0)
# Blue Efficiency
data['blue_eff'] = data['carname'].apply(lambda x: 1 if 'blue' in x.lower() else 0)
# G-Power
data['g_pow'] = data['carname'].apply(lambda x: 1 if 'g power' in x.lower() or 'g-power' in x.lower() else 0)
# Brabus
data['brabus'] = data['carname'].apply(lambda x: 1 if 'brabus' in x.lower() else 0)
# Avantgarde
data['avantgarde'] = data['carname'].apply(lambda x: 1 if 'avantgarde' in x.lower() else 0)
# Elegance
data['elegance'] = data['carname'].apply(lambda x: 1 if 'elegance' in x.lower() else 0)
# Tag 63
data['tag_63'] = data['carname'].apply(lambda x: 1 if '63' in x.lower() else 0)
# Tag 65
data['tag_65'] = data['carname'].apply(lambda x: 1 if '65' in x.lower() or ' 65 ' in x.lower() else 0)
# Tag 55
data['tag_55'] = data['carname'].apply(lambda x: 1 if '55' in x.lower() or ' 55 ' in x.lower() else 0)
# TÜV AU
data['tüv'] = data['carname'].apply(lambda x: 1 if 'tüv' in x.lower() else 0)
# E10 geignet
data['E10'] = data['fuel_type'].apply(lambda x: 1 if 'e10' in x.lower() else 0)
# Biodiesel geignet
data['biodiesel'] = data['fuel_type'].apply(lambda x: 1 if 'biodiesel' in x.lower() else 0)
# Pflanzenöl geignet
data['pflanzenöl'] = data['fuel_type'].apply(lambda x: 1 if 'pflanzenöl' in x.lower() else 0)
# electric
data['electric'] = data['fuel_type'].apply(lambda x: 1 if 'elektr' in x.lower() else 0)

## Fill in missing values of power_ps with the mean of existing values of the same car Model
data["power_ps"] = data.groupby("Model")["power_ps"].transform(lambda x: x.fillna(x.mean()))

## Fill in missing values of power_kw with the mean of existing values of the same car Model
data["power_kw"] = data.groupby("Model")["power_kw"].transform(lambda x: x.fillna(x.mean()))

## make Hubraum numeric and make '-1' entries NaN
data['hubraum'] = data['hubraum'].apply(lambda x: float(x.replace('.','').split()[0]) if x != '-1' else None)
data['hubraum'] = data['hubraum'].apply(lambda x: x if isinstance(x, float) else None)
## Fill in missing values (NaNs) of hubraum with the mean of existing hubraum values grouped by the same car Model
data["hubraum"] = data.groupby("Model")["hubraum"].transform(lambda x: x.fillna(x.mean()))

# make num_seats categorical
data['num_seats'] = data['num_seats'].apply(lambda x: str(x) if x != -1 else 'na')

# make num_doors categorical
data['num_doors'] = data['num_doors'].apply(lambda x: x if x != '-1' else 'na')

# make emission_class categorical
data['emission_class'] = data['emission_class'].apply(lambda x: x if x != '-1' else 'na')

# clean fuel_type
def fueltype(x):
    if x == '-1':
        return 'na'
    else:
        return x.split()[0].replace(',', '')

data['fueltype'] = data['fuel_type'].apply(fueltype)

# drop columns that give no further information or are already further feature engineered
data_cleaned = data.drop(['construction_year', 'power', 'fuel_type', 'first_registration', 'damage'], axis=1)

## Save cleaned dataset
data_cleaned.to_csv('data_cleaned.csv')


#### To-Do
# Age verfeinern, nicht nur jahre, sondern auch Monate berücksichtigen
# "Oldtimer" entfernen (oder drinlassen?)