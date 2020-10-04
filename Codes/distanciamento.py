#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:57:56 2020

@author: erika
"""

# Bibliotecas usadas #

import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
from scipy.interpolate import make_interp_spline, BSpline
from scipy.ndimage.filters import gaussian_filter1d

# Regiao em especifico #

nome = 'Trairí'
regiao = 'TRAIR�'

label = ['Jaçanã', 'Serra de São Bento',"Lajes Pintadas", 'Campo Redondo', 'Boa Saúde']

# Importando os dados #

dataset_covid = pd.read_excel('Dados isolamento 3.xlsx')

# Funções Auxiliares #

def getMunicipios(casos):
    
    municipios = list(set(casos[:, 0]))
    
    return municipios

def getMuValue(casos, municipio):
    
    mu_values = []
    date = []
    
    for i in range(casos.shape[0]-1, -1, -1):
        
        if(casos[i][0] == municipio):
            
            if(casos[i][1] > 1.0):
                value = (casos[i+3][1] + casos[i-3][1])/2
            else:
                value = casos[i][1]
            
            mu_values = np.append(mu_values, value)
            k = casos[i][2]
            date = np.append(date, k)
    
    mu_values = gaussian_filter1d(mu_values, sigma=1.5)
    return mu_values, date

def getDataFrame(casos, listaMunicipios):

    frame1 = pd.DataFrame([])
    
    for i in listaMunicipios:
        
        value, date = getMuValue(casos, i)
        date = pd.to_datetime(date).strftime('%d/%m/%y')
        frame2 = pd.DataFrame(value, columns = [i])
        frame1 = pd.concat([frame1, frame2], axis = 1)
    
    dataframe = frame1
    
    return dataframe

def fourValues(data):
    
    teste = data.sort_values(axis = 1, by = [data.shape[0]-1], ascending = False)
    
    teste = teste.iloc[:, 0:5]
    
    return teste

def index(k):
    
    lista = np.array([])
    
    for i in range(0, k.shape[0]):
        
        if(i%3 == 0):
            lista = np.append(lista, k[i])
    
    return lista

# Pegando os dados apenas para a Região Especificada #
    
casos = dataset_covid.iloc[:, [False, True, True, True, True]].values

casos_regiao = []

for i in range(0, casos.shape[0]):
    
    if(casos[i][3] == regiao):
        casos_regiao = np.append(casos_regiao, casos[i])

casos_regiao = casos_regiao.reshape(
    (int(casos_regiao.shape[0]/casos.shape[1]), casos.shape[1]))

# Pegando os casos #

listaMunicipios = getMunicipios(casos_regiao)

#listaMunicipios = ['Serrinha', 'Arez', 'Passagem', 'Lagoa de Pedras', 'Tibau do Sul']

data = getDataFrame(casos_regiao, listaMunicipios)

data = fourValues(data)

dias = pd.date_range(start='2020-02-01', end='2020-07-06') # Array com os dias #
dias = pd.to_datetime(dias).strftime('%y/%m/%d')

data.index = dias

k2 = data.index.to_numpy(copy = True)

k = pd.to_datetime(k2).strftime('%y/%B')

k = index(k)

k1 = list(range(0, data.shape[0], 3))

# PLOTANDO OS GRAFICOS #

    # Usando Seaborn para fazer os graficos #

sns.set(style = 'whitegrid')

fig, ax = plt.subplots() 

plt.ylabel('Isolamento em cada Município')


#labels = pd.date_range(start='2020-02-01', end='2020-07-06', periods = 8)
#labels = pd.to_datetime(labels).strftime('%d/%m/%y')
x = list(range(0, 170, 20))
sns.color_palette("colorblind")
sns.despine(left=True, bottom=True)
plot = sns.lineplot(data=data, linewidth=1.7, markers = False, legend = False, dashes = False)
plt.xticks(rotation = 45, ticks = k1, labels = k, fontsize = 8.0, ha = 'right', weight='bold')
plt.yticks(ticks = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55],
           labels = ["25%", "30%", "35%", "40%", "45%", "50%", "55%"])
plt.legend(loc='upper left', labels = label)