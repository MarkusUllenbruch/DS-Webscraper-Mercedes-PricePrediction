# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:23:41 2021

Data Cleaning & Wrangling of Raw Data

@author: Markus Ullenbruch
"""

import numpy as np
import pandas as pd

path_dataset = './Data/mobile_data_6000_8000.csv'

data = pd.read_csv(path_dataset)

# Drop row when price is -1 (not available)
data = data[data['price'] != '-1']

# Remove '.', '€' and '(Brutto)' in price and make numeric
data['price'] = data['price'].apply(lambda x: float(x.lower().replace('(brutto)', '').replace('.','').replace('€','')))

# Remove '.' and 'km' and '(Brutto)' in milage and make numeric
data['milage'] = data['milage'].apply(lambda x: float(x.lower().replace('km', '').replace('.','')))

# Make power_ps
data['power_ps'] = data['power'].apply(lambda x: float(x.lower().replace('(', '').replace(')', '').split()[2]) if x != '-1' else None)

# Make power_kw
data['power_kw'] = data['power'].apply(lambda x: float(x.lower().replace('(', '').replace(')', '').split()[0]) if x != '-1' else None)

# Unfallschaden
def make_damage(x):
    xl = x.lower()
    if 'reparierter unfallschaden' in xl:
        return 'repaired'
    elif 'unfallfrei' in xl:
        return 'no_damage'
    elif '-1' in xl:
        return 'damage_unknown'
data['Schaden'] = data['damage'].apply(make_damage)

# number of owners make categorical strings
data['num_owners'] = data['num_owners'].apply(lambda x: str(x) if x != -1 else 'na')

# cartype simplification
def simplify_cartype(x):
    xl = x.lower()
    if 'suv' in xl:
        return 'suv'
    elif 'van' in xl or 'minibus' in xl:
        return 'van'
    elif 'cabrio' in xl or 'roadster' in xl:
        return 'cabrio'
    elif 'sportwagen' in xl or 'coup' in xl:
        return 'sport'
    else:
        return xl

data['car_type'] = data['car_type'].apply(simplify_cartype)

# Age of car from 'first_registration'
data['age'] = data['first_registration'].apply(lambda x: 2020 - float(x.split('/')[1]))


# make a row for 'Model' and parse carmodel from carname
def make_car_model(x):
    xl = x.lower()
    if 'a-klasse' in xl or 'a klasse' in xl or ' A ' in x or 'A1' in x or 'A2' in x:
        return 'A-Klasse'
    
    elif 'b-klasse' in xl or 'b klasse' in xl or ' B ' in x or 'B1' in x or 'B2' in x:
        return 'B-Klasse'
    
    elif 'c-klasse' in xl or 'c klasse' in xl or ' c ' in xl or 'C1' in x or 'C2' in x:
        return 'C-Klasse'
    
    elif 'e-klasse' in xl or 'e klasse' in xl or ' E ' in x or 'E2' in x or 'E3' in x:
        return 'E-Klasse'
    
    elif 's-klasse' in xl or 's klasse' in xl or ' S ' in x:
        return 'S-Klasse'
    
    elif 'g-klasse' in xl or 'g klasse' in xl:
        return 'G-Klasse'
    
    elif 'm-klasse' in xl or 'm klasse' in xl or 'ML' in x or 'ml' in xl:
        return 'M-Klasse'
    
    elif 'x-klasse' in xl or 'x klasse' in xl:
        return 'X-Klasse'
    
    elif 'r-klasse' in xl or 'r klasse' in xl or ' r ' in xl:
        return 'R-Klasse'
    
    elif 'v-klasse' in xl or 'v klasse' in xl:
        return 'V-Klasse'
    
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
    
    elif 'vaneo' in xl or 'citan' in xl:
        return 'Vaneo'
    
    elif 'viano' in xl:
        return 'Viano'
    
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
# Tag 63
data['tag_63'] = data['carname'].apply(lambda x: 1 if ' 63 ' in x.lower() else 0)
# Tag 65
data['tag_65'] = data['carname'].apply(lambda x: 1 if '65' in x.lower() or ' 65 ' in x.lower() else 0)
# Tag 55
data['tag_55'] = data['carname'].apply(lambda x: 1 if '55' in x.lower() or ' 55 ' in x.lower() else 0)

## Fill in missing values of power_ps with the mean of existing values of the same car Model
data["power_ps"] = data.groupby("Model")["power_ps"].transform(lambda x: x.fillna(x.mean()))

## Fill in missing values of power_kw with the mean of existing values of the same car Model
data["power_kw"] = data.groupby("Model")["power_kw"].transform(lambda x: x.fillna(x.mean()))

## Hubraum
data['hubraum'] = data['hubraum'].apply(lambda x: float(x.replace('.','').split()[0]) if x != '-1' else None)
## Fill in missing values of hubraum with the mean of existing values of the same car Model
data["hubraum"] = data.groupby("Model")["hubraum"].transform(lambda x: x.fillna(x.mean()))

# num_seats
data['num_seats'] = data['num_seats'].apply(lambda x: str(x) if x != -1 else 'na')

# num_doors
data['num_doors'] = data['num_doors'].apply(lambda x: x if x != '-1' else 'na')

# emission_class
data['emission_class'] = data['emission_class'].apply(lambda x: x if x != '-1' else 'na')