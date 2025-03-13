import pandas as pd
from matplotlib import pyplot as plt

# simulação
simulacaoRK4 = pd.read_csv("data/tratados/simulacao.csv", sep=",")
simulacaoMickens = pd.read_csv("data/tratados/SIRMickens.csv", sep=",")
data2025 = pd.read_csv("data/tratados/casos_srag_total.csv", sep=",")

plt.scatter(simulacaoRK4.index, simulacaoRK4["Infectados"], label="Estimado RK4", s=1)
plt.scatter(simulacaoMickens.index, simulacaoMickens["Infectados"], label="Estimado Mickens", s=1)
plt.scatter(data2025.index, data2025["CASO_SRAG"], label="Dados", s=1)
plt.legend()

plt.xlabel("Dias")
plt.ylabel("Casos")

plt.savefig("data/graficos/simulacaoCasos.png")