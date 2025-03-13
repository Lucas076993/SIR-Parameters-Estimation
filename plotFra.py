import pandas as pd
from matplotlib import pyplot as plt

# simulação
simulacaoRK4 = pd.read_csv("data/tratados/simulacao_fra.csv", sep=",")
simulacaoMickens = pd.read_csv("data/tratados/SIRMickens_fra.csv", sep=",")
data = pd.read_csv("data/tratados/franca.csv", sep=",")

plt.scatter(simulacaoRK4.index, simulacaoRK4["Infectados"], label="Estimado RK4", s=1)
plt.scatter(simulacaoMickens.index, simulacaoMickens["Infectados"], label="Estimado Mickens", s=1)
plt.scatter(data.index, data["incid_hosp"], label="Dados", s=1)
plt.legend()

plt.xlabel("Dias")
plt.ylabel("Casos")

plt.savefig("data/graficos/simulacao2020_fra.png")