import pandas as pd
import numpy as np

pd.read_csv()          # ler o arquivo (com sep=';' e decimal=',' no seu caso)
df.info()               # tipos de dados, valores faltantes
df.describe()           # estatística descritiva
df.isnull().sum()       # contagem de valores faltantes por coluna
df.duplicated()         # checar duplicatas
