#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 00:34:40 2020

@author: erika
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# Regiao em especifico #

regiao = 'Trairí' # Região que queremos #
nome = 'Trairí'

# Importando os dados #

dataset_covid = pd.read_excel('02_07.xlsx')

# FUNÇÕES AUXILIARES #

def getMediaMu(casos_positivos, territorio):
    
    counter = 0
    contaminados = 0
    
    for i in range(0, casos_positivos.shape[0]):
        
        if(casos_positivos[i][1] == territorio):
            
            contaminados += 1
            
            if(casos_positivos[i][2] == 'Sim'):
                counter += 1
            if(casos_positivos[i][3] == 'Sim'):
                counter += 1
            if(casos_positivos[i][4] == 'Sim'):
                counter += 1
            if(casos_positivos[i][5] == 'Sim'):
                counter += 1
            if(casos_positivos[i][6] == 'Sim'):
                counter += 1
                
    if(contaminados == 0):
        media = 0
    else:
        media = counter/contaminados
    
    return media

def getDataFrame(casos_positivos, listaTerritorios):
  
    medias = []
    
    for i in listaTerritorios:
        
        media = getMediaMu(casos_positivos, i)
        medias = np.append(medias, media)

    
    dataframe = pd.DataFrame({'Territorios' : listaTerritorios,
                              'Medias' : medias})
    
    # Sort #
    
    dataframe = dataframe.sort_values(by=['Medias'], ascending = False)
    
    return dataframe

# Pegando os valores que queremos, no caso queremos os Resultados, os Territorios de Cidadânia, e  #
# os Diferentes sintomas que queremos saber                                                        #

casos = dataset_covid.loc[:, ['ResultadodoTeste', 'TERRITÓRIO DE CIDADANIA', 'Febre', 'Tosse', 'Outros',
                              'Dispneia', 'DordeGarganta']].values

# Agora precisamos selecionar apenas os casos que deram como Positivos                             #

casos_positivos = []

for i in range(0, casos.shape[0]):
    
    if(casos[i][0] == 'Positivo'):
        
        casos_positivos = np.append(casos_positivos, casos[i])

casos_positivos = casos_positivos.reshape(
    (int(casos_positivos.shape[0]/casos.shape[1]), casos.shape[1]))

# Agora iremos pegar a media de sintomas de cada Territorio de Cidadânia                           #

    # Usamos uma função para pegar os valores unicos da coluna de 'Territórios de Cidadânia' #

listaTerritorios = list(set(casos_positivos[:, 1]))

    # Pegando a media de sintomas #

data = getDataFrame(casos_positivos, listaTerritorios)

# PLotando os graficos para a Media de sintomas por Territorio de Cidadânia #

    # Usaremos a BIblioteca Seaborn para isso #

sns.set(style = 'whitegrid')

f, ax = plt.subplots()

ax.grid(True)
# ax.set_xticklabels(labels)

# Antes de continaurmos precisamos ajeitar alguns erros nos nomes #

data = data.replace('Terras Potiguares', 'Terra dos Potiguaras')
data = data.replace('Sertão, Cabugi e Litoral Norte', 'Sertão Central, Cabugi e Litoral Norte')
listaTerritorios = data.loc[:, ['Territorios']].values

# Continuando #

color = ['maroon' if (x == nome) else 'steelblue' for x in listaTerritorios]
sns.set_palette(color)
bar_plot = sns.barplot(x='Medias', y='Territorios', data=data)

# Colocando os vlaores nas Barras #

for i, j in enumerate(data.loc[:, 'Medias'].values):
    
    ax.text(j, i, str(round(j, 1)), va='center', ha = 'right', fontweight='bold',
                    color='white')

bar_plot.set(xlabel="Média de sintomas", ylabel="Territórios de Cidadania")
sns.despine(left=True, bottom=True)

