#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:16:46 2020

@author: erika
"""

# Iportando as bibliotecas #

import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import math
import matplotlib.pyplot as plt

# Região que iremos fazer os graficos #

regiao = 'Sertão, Cabugi e Litoral Norte'
nome = 'Sertão Central, Cabugi e Litoral Norte'

labels = ['Casos acumulados no '+nome, 'Guamaré', 'Macau', 'Angicos', 'Afonso Bezerra', 'Caiçara do Rio do Vento']
# Importando os dados #

dataset_covid = pd.read_excel('02_07.xlsx')

dataset_covid['TERRITÓRIO DE CIDADANIA'] = dataset_covid['TERRITÓRIO DE CIDADANIA'].astype(str)

# FUNÇÕES AUXILIARES #

def getMunicipios(casos):
    
    municipios = np.unique(casos[:, 4])
    
    return municipios

def ajeitar(casos):
    
    casos_positivos = []

    for i in range(0, casos.shape[0]):
    
        if(casos[i][0] == 'Positivo' and casos[i][3].year >= 2020 and casos[i][1] == regiao):
            casos_positivos = np.append(casos_positivos, casos[i])
        
       
    casos_positivos = casos_positivos.reshape((int(casos_positivos.shape[0]/casos.shape[1]),
                                                   casos.shape[1]))
    
    return casos_positivos

    # Pegar os dados do Territorio em Especifico #

def getValue(casos, dias, municipio):
    
    counters = [0] * dias.shape[0]
    
    flag = False
    
    counter = 0
    
    for y, i in enumerate(dias):
        
        for j in range(0, casos.shape[0]):
            
            if(casos[j][3] == i):
                if(casos[j][4] == municipio):
                    counter += 1
                    flag = True
                
        if(flag == True): 
            counters[y] = counter
            flag = False
        else:
            continue
    
    return counters

def getValueT(casos, dias):
    
    counters = [0] * dias.shape[0]
    
    flag = False
    
    counter = 0
    
    for y, i in enumerate(dias):
        
        for j in range(0, casos.shape[0]):
            
            if(casos[j][3] == i):
                counter += 1
                flag = True
                
        if(flag == True): 
            counters[y] = counter
            flag = False
        else:
            continue
    
    return counters

    # Pegar o Data Frame #

def getDataframe(casos, dias, listaMunicipios):
    
    frame1 = pd.DataFrame(getValueT(casos, dias), columns = ['Casos acumulados de' + str(nome)])
    
    for i in listaMunicipios:
        
        frame2 = pd.DataFrame(getValue(casos, dias, i), columns = [i])
        frame1 = pd.concat([frame1, frame2], axis = 1)
    
    dataframe = frame1
    
    return dataframe

def fourValues(data):
    
    teste = data.sort_values(axis = 1, by = [data.shape[0]-1], ascending = False)
    
    teste = teste.iloc[:, 0:6]
    
    return teste

def getFix(data, listaMunicipios1):

    frame1 = pd.DataFrame(data.iloc[:, 0].values, columns = ['Obitos acumulados em '+nome])
    
    for i in listaMunicipios1:
        
        casos = data.loc[:, i].values
        
        for j in range(1, casos.shape[0]):
        
            if(casos[j] == 0):
                casos[j] = casos[j-1]
            else:
                continue
            
        frame2 = pd.DataFrame(casos, columns = [i])
        frame1 = pd.concat([frame1, frame2], axis = 1)
    
    dataframe = frame1
    
    return dataframe

def index(k):
    
    lista = np.array([])
    
    for i in range(0, k.shape[0]):
        
        if(i%2 == 0):
            lista = np.append(lista, k[i])
    
    return lista

# Pegando os dados que queremos, no caso queremos casos e obitos e os territorios de cidadania #

casos = dataset_covid.loc[:, ['ResultadodoTeste', 'TERRITÓRIO DE CIDADANIA', 'ÓBITO', 'DatadaNotificação','MunicípiodeResidência', 'POP TOTAL 2020']].values

casos = ajeitar(casos) # Deixas apenas as datas validas e os casos Positivos e o Territorio #

listaMunicipios = getMunicipios(casos) # Cria uma lista dos Territorios #

# Alterando o formato das datas para facilitar #

casos[:, 3] = pd.to_datetime(casos[:, 3]).strftime('%y/%m/%d')

dias = pd.date_range(start='2020-03-09', end='2020-07-02') # Array com os dias #
dias = pd.to_datetime(dias).strftime('%y/%m/%d')

data = getDataframe(casos, dias, listaMunicipios)

# Ajeitando a questão das datas #

data.index = dias

data = data[(data.T != 0).any()]

dataFinal = getFix(data, listaMunicipios) # Ajeitando os dias para ficar apenas os que tiveram casos #

# Ajeitando a questão de pegar os 5 maiores valores #

dataFinal = fourValues(dataFinal) # Pegar os 5 maiores valores #

listaMunicipios = dataFinal.columns.values

# Fazendo as labels #

k2 = data.index.to_numpy(copy = True)

k = pd.to_datetime(k2).strftime('%y/%B')

k = index(k)

k1 = list(range(0, dataFinal.shape[0], 2))

# PLOTANDO OS GRAFICOS #

    # Usando Seaborn para fazer os graficos 

sns.set(style = 'whitegrid')

plt.ylabel('Nº de casos acumulados')
plt.xlabel('Dias')


sns.despine(left=True, bottom=True)
sns.lineplot(data=dataFinal, linewidth=2.5,palette = "colorblind", markers = False, dashes = True)
plt.legend(labels = labels)
plt.xticks(rotation = 45, ticks = k1, labels = k, fontsize = 8.0, ha = 'right', weight='bold')