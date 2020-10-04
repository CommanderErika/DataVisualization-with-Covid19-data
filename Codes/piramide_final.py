#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:14:38 2020

@author: erika
"""

# Iportando as bibliotecas #

from array import array
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import cycle

# Regiao #

regiao = 'Trairí'
nome = 'Trairí'

# Importando os dados #

dataset_covid = pd.read_excel('02_07.xlsx')

# FUNÇÕES AUXILIARES #

     # Função para pegar os dados confirmados e separar por Faixa Etaria e Sexo #

def getCasos(casos_positivos):
    
    lista = ['Óbito', 'ÓBITO', 'óbito']
    sexos = ['MASCULINO', 'Masculino', 'FEMININO', 'Feminino']
    faixa_et = ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 29', '30 a 39', '40 a 49', '50 a 59',
                '60 a 69', '70 a 79', '80 a 89', '> 89']
    masculino_n = [0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0]
    feminino_n = [0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0]
    counter = 0
    for i in range(0, casos_positivos.shape[0]):
    
        if(casos_positivos[i][2] != lista[0] or casos_positivos[i][2] != lista[1] or casos_positivos[i][2] != lista[2]):
            counter += 1
            if(casos_positivos[i][4] == sexos[0] or casos_positivos[i][4] == sexos[1]):
                if(casos_positivos[i][3] == faixa_et[0]):
                    masculino_n[0] += 1
                elif(casos_positivos[i][3] == faixa_et[1]):
                    masculino_n[1] += 1
                elif(casos_positivos[i][3] == faixa_et[2]):
                    masculino_n[2] += 1
                elif(casos_positivos[i][3] == faixa_et[3]):
                    masculino_n[3] += 1
                elif(casos_positivos[i][3] == faixa_et[4]):
                    masculino_n[4] += 1
                elif(casos_positivos[i][3] == faixa_et[5]):
                    masculino_n[5] += 1
                elif(casos_positivos[i][3] == faixa_et[6]):
                    masculino_n[6] += 1
                elif(casos_positivos[i][3] == faixa_et[7]):
                    masculino_n[7] += 1
                elif(casos_positivos[i][3] == faixa_et[8]):
                    masculino_n[8] += 1
                elif(casos_positivos[i][3] == faixa_et[9]):
                    masculino_n[9] += 1
                elif(casos_positivos[i][3] == faixa_et[10]):
                    masculino_n[10] += 1
                elif(casos_positivos[i][3] == faixa_et[11]):
                    masculino_n[11] += 1
            elif(casos_positivos[i][4] == sexos[2] or casos_positivos[i][4] == sexos[3]):
                if(casos_positivos[i][3] == faixa_et[0]):
                    feminino_n[0] += 1
                elif(casos_positivos[i][3] == faixa_et[1]):
                    feminino_n[1] += 1
                elif(casos_positivos[i][3] == faixa_et[2]):
                    feminino_n[2] += 1
                elif(casos_positivos[i][3] == faixa_et[3]):
                    feminino_n[3] += 1
                elif(casos_positivos[i][3] == faixa_et[4]):
                    feminino_n[4] += 1
                elif(casos_positivos[i][3] == faixa_et[5]):
                    feminino_n[5] += 1
                elif(casos_positivos[i][3] == faixa_et[6]):
                    feminino_n[6] += 1
                elif(casos_positivos[i][3] == faixa_et[7]):
                    feminino_n[7] += 1
                elif(casos_positivos[i][3] == faixa_et[8]):
                    feminino_n[8] += 1
                elif(casos_positivos[i][3] == faixa_et[9]):
                    feminino_n[9] += 1
                elif(casos_positivos[i][3] == faixa_et[10]):
                    feminino_n[10] += 1
                elif(casos_positivos[i][3] == faixa_et[11]):
                    feminino_n[11] += 1
             
    masculino_n = [i * (-1) for i in masculino_n] # colocando os valores de masculino_n como engativo #

    masculino_n = [i / casos_positivos.shape[0] * 100 for i in masculino_n] # colocando em percentuais #
    feminino_n = [i / casos_positivos.shape[0] * 100 for i in feminino_n]

    dataframe = pd.DataFrame({ 'Age' : ['0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 29 anos',
                               '30 a 39 anos', '40 a 49 anos', '50 a 59 anos',
                '60 a 69 anos', '70 a 79 anos', '80 a 89 anos', '90+'],
                     'Masculino' : masculino_n,
                     'Feminino' : feminino_n
                    })
    
    return dataframe

def getCasosRN(casos_positivos):
    
    lista = ['Óbito', 'ÓBITO', 'óbito']
    sexos = ['MASCULINO', 'Masculino', 'FEMININO', 'Feminino']
    faixa_et = ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 29', '30 a 39', '40 a 49', '50 a 59',
                '60 a 69', '70 a 79', '80 a 89', '> 89']
    masculino_n = [0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0]
    feminino_n = [0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0]
    counter = 0
    for i in range(0, casos_positivos.shape[0]):
    
        if(casos_positivos[i][2] != lista[0] or casos_positivos[i][2] != lista[1] or casos_positivos[i][2] != lista[2]):
            counter +=1
            if(casos_positivos[i][4] == sexos[0] or casos_positivos[i][4] == sexos[1]):
                if(casos_positivos[i][3] == faixa_et[0]):
                    masculino_n[0] += 1
                elif(casos_positivos[i][3] == faixa_et[1]):
                    masculino_n[1] += 1
                elif(casos_positivos[i][3] == faixa_et[2]):
                    masculino_n[2] += 1
                elif(casos_positivos[i][3] == faixa_et[3]):
                    masculino_n[3] += 1
                elif(casos_positivos[i][3] == faixa_et[4]):
                    masculino_n[4] += 1
                elif(casos_positivos[i][3] == faixa_et[5]):
                    masculino_n[5] += 1
                elif(casos_positivos[i][3] == faixa_et[6]):
                    masculino_n[6] += 1
                elif(casos_positivos[i][3] == faixa_et[7]):
                    masculino_n[7] += 1
                elif(casos_positivos[i][3] == faixa_et[8]):
                    masculino_n[8] += 1
                elif(casos_positivos[i][3] == faixa_et[9]):
                    masculino_n[9] += 1
                elif(casos_positivos[i][3] == faixa_et[10]):
                    masculino_n[10] += 1
                elif(casos_positivos[i][3] == faixa_et[11]):
                    masculino_n[11] += 1
            elif(casos_positivos[i][4] == sexos[2] or casos_positivos[i][4] == sexos[3]):
                if(casos_positivos[i][3] == faixa_et[0]):
                    feminino_n[0] += 1
                elif(casos_positivos[i][3] == faixa_et[1]):
                    feminino_n[1] += 1
                elif(casos_positivos[i][3] == faixa_et[2]):
                    feminino_n[2] += 1
                elif(casos_positivos[i][3] == faixa_et[3]):
                    feminino_n[3] += 1
                elif(casos_positivos[i][3] == faixa_et[4]):
                    feminino_n[4] += 1
                elif(casos_positivos[i][3] == faixa_et[5]):
                    feminino_n[5] += 1
                elif(casos_positivos[i][3] == faixa_et[6]):
                    feminino_n[6] += 1
                elif(casos_positivos[i][3] == faixa_et[7]):
                    feminino_n[7] += 1
                elif(casos_positivos[i][3] == faixa_et[8]):
                    feminino_n[8] += 1
                elif(casos_positivos[i][3] == faixa_et[9]):
                    feminino_n[9] += 1
                elif(casos_positivos[i][3] == faixa_et[10]):
                    feminino_n[10] += 1
                elif(casos_positivos[i][3] == faixa_et[11]):
                    feminino_n[11] += 1
             
    masculino_n = [i * (-1) for i in masculino_n] # colocando os valores de masculino_n como engativo #

    masculino_n = [i / counter * 100 for i in masculino_n] # colocando em percentuais #
    feminino_n = [i / counter * 100 for i in feminino_n]

    dataframe = pd.DataFrame({ 'Age' : ['0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 29 anos',
                               '30 a 39 anos', '40 a 49 anos', '50 a 59 anos',
                '60 a 69 anos', '70 a 79 anos', '80 a 89 anos', '90+'],
                     'Masculino' : masculino_n,
                     'Feminino' : feminino_n
                    })
    
    return dataframe

casos = dataset_covid.loc[:, ['ResultadodoTeste', 'TERRITÓRIO DE CIDADANIA', 'ÓBITO', 'FAIXAETÁRIA', 'Sexo']].values

# Entretando queremos apenas os casos positivos que sejam de Terras Potiguares #
# Também queremos que não tenha os dados com datas absurdas                    #

    # Casos Apenas do territorio Especificado #

casos_positivos = []

for i in range(0, casos.shape[0]):
    
    if(casos[i][0] == 'Positivo' and casos[i][1] == regiao):
        casos_positivos = np.append(casos_positivos, casos[i])
        
casos_positivos = casos_positivos.reshape(
    (int(casos_positivos.shape[0]/casos.shape[1]), casos.shape[1]))


    # De todo o Estado #

casos_estado = []

for i in range(0, casos.shape[0]):
    
    if(casos[i][0] == 'Positivo'):
        casos_estado = np.append(casos_estado, casos[i])

casos_estado = casos_estado.reshape(
    (int(casos_estado.shape[0]/casos.shape[1]), casos.shape[1]))

# Pegando os valores #

    # Pegando os dados sobre sexo e Faixa Etária #

data = getCasos(casos_positivos)

dataRN = getCasosRN(casos_estado)
 

# PLOTANDO A PIRAMIDE ETARIA #

    # Usando SEABORN para criar o grafico #

faixa_et = ['90+', '80 a 89 anos', '70 a 79 anos', '60 a 69 anos', '50 a 59 anos', '40 a 49 anos',
            '30 a 39 anos', '20 a 29 anos',
            '15 a 19 anos', '10 a 14 anos', '5 a 9 anos', '0 a 4 anos']

sns.set(style = 'whitegrid')


f, ax = plt.subplots()

plt.style.use('bmh')

ax.grid(True)  

sns.set_color_codes("deep")
sns.barplot(x='Masculino', y='Age', data=dataRN, order=faixa_et,
                       color = 'r', label = 'Masculino Estado'
                       )

sns.barplot(x='Feminino', y='Age', data=dataRN, order=faixa_et,
                       color = 'b', label = 'Feminino Estado')

bar = sns.barplot(x='Masculino', y='Age', data=data, order=faixa_et, facecolor=(1, 1, 1, 0),
                        errcolor=".2", edgecolor="0.2", label = 'Masculino ' + nome, linewidth = 1.5)

bar = sns.barplot(x='Feminino', y='Age', data=data, order=faixa_et, facecolor=(1, 1, 1, 0),
                        errcolor="0.2", edgecolor="0.2",  label = 'Feminino ' + nome, linewidth = 1.5)

hatches = cycle([' ', ' ', '///', '++'])

num_locations = len(data.Feminino)
for i, patch in enumerate(bar.patches):
    if i % num_locations == 0:
        hatch = next(hatches)
    patch.set_hatch(hatch)

labels = ['15%', '10%', '5%', '0%' , '5%', '10%', '15%']
plt.xticks(ticks = [-15, -10, -5, 0, 5, 10, 15], labels = labels)
ax.legend(ncol=4, loc="upper right", frameon=True)
ax.legend(title = 'Sexo')
bar.set(xlabel="", ylabel="Faixa Etária")
sns.despine(left=True, bottom=True)