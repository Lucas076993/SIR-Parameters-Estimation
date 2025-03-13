import pandas as pd
import numpy as np
from train import train
from matplotlib import pyplot as plt

# definindo funções a serem ajustadas
def logI(t, gamma, b):
    return gamma * t + b

def dlogI(t, GAMMA, b):
    return - GAMMA * t + b

def dI(t, GAMMA, b):
    return np.exp(- GAMMA * t) * np.exp(b)

def I(t, gamma, b):
    return np.exp(gamma * t) * np.exp(b)

# lendo o dataset
data = pd.read_csv("data/tratados/media_movel_srag_2024.csv", sep=",")


maximum = data["CASO_SRAG"].max()
max_point = data["CASO_SRAG"].idxmax()
increasing = data[data.index <= max_point]
decreasing = data[data.index > max_point]


# fitting increasing
result_increasing = train(logI, increasing.index, increasing["CASO_SRAG"])
print(result_increasing[-2])

# fitting decreasing
result_decreasing = train(dlogI, decreasing.index, decreasing["CASO_SRAG"])
print(result_decreasing[-2])

# reajustando os dados
estimado_increasing = I(result_increasing[-1], *result_increasing[0])
estimado_decreasing = dI(result_decreasing[-1], *result_decreasing[0])

print(increasing.head())
print(decreasing.head())