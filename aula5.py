# -*- coding: utf-8 -*-
#Aula5.ipynb

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd

from scipy.stats import binom

from scipy.stats import norm

enem_sp = pd.read_csv('/content/drive/MyDrive/Arquivos/AtividadeEstatistica/aula5/enem_2019_tratado.csv',
                      sep=',', encoding='iso-8859-1')

#QUAL A PROBABILIDADE DE RETIRAR MAIS DO QUE 8 MULHERES NUM TOTAL DE 10 AMOSTRAS NO ENEM 2019?

mulher_enem = enem_sp.loc[enem_sp.SEXO == 'F']

p = len(mulher_enem) / len(enem_sp)
p

p1 = 1 - (binom.pmf(0,10,p)+binom.pmf(1,10,p)+binom.pmf(2,10,p)+binom.pmf(3,10,p)+binom.pmf(4,10,p)+binom.pmf(5,10,p)+binom.pmf(6,10,p)+binom.pmf(7,10,p)+binom.pmf(8,10,p))
p1

#Qual a probabilidade de sortear uma pessoa com idade entre 20 e 30 anos no Enem 2019?

norm.cdf(4.5, loc=4.8, scale=0.5)

enem_sp.IDADE.mean()

sup = 1 - (norm.cdf(20, loc=enem_sp.IDADE.mean(), scale=enem_sp.IDADE.std()))
sup

inf = 1 - (norm.cdf(30, loc=enem_sp.IDADE.mean(), scale=enem_sp.IDADE.std()))
inf

total = sup - inf
total