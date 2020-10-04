#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 08:44:40 2020

@author: erika
"""

regiao = 'Açu-Mossoró'

# Bibliotecas Utilizadas #

import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# Pegando os dados #

letalidade = [0.185465556396669,
              0.338235294117647,
0.168831168831169,
0.256474519632414,
0.269922879177378,
0.211608222490931,
0.105947955,
0.337868480725624,
0.237962053065235,
0.348780487804878]
municipios = ['Açu-Mossoró', 'Agreste Litoral Sul', 'Alto Oeste', 'Mato Grande', 'Potengi', 'Seridó',
              'Sertão do Apodi', 'Sertão, Cabugi e Litoral Norte', 'Terra dos Potiguaras', 'Trairí']

data = pd.DataFrame([letalidade], columns = municipios)

data = data.sort_values(axis = 1, by = [0], ascending = False)

sns.set(style='whitegrid')

f, ax = plt.subplots()

color = ['maroon' if (x == regiao) else 'steelblue' for x in data.columns.values]
barplot = sns.barplot(x = data.iloc[0,:],y = data.columns.values, palette=color)

# Colocando os vlaores nas Barras #

for i, j in enumerate(data.iloc[0,:].values):
    
    ax.text(j, i, str(round(j, 1)), va='center', ha = 'right', fontweight='bold',
                    color='white')

labels = ['0%', '0.05%', '0.1%', '0.15%', '0.2%', '0.25%', '0.3%', '0.35%']
ax.set_xticklabels(labels)

barplot.set(xlabel="Média dos fatores de risco", ylabel="Território de Cidadania")
sns.despine(left=True, bottom=True)