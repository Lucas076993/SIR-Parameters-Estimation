import pandas as pd
from matplotlib import pyplot as plt

simulacaoRK4 = pd.read_csv("data/tratados/simulacao.csv", sep=",")
simulacaoMickens = pd.read_csv("data/tratados/SIRMickens.csv", sep=",")
data2025 = pd.read_csv("data/tratados/media_movel_srag_total.csv", sep=",")

erroRK4 = pow(simulacaoRK4["Infectados"] - data2025["CASO_SRAG"], 2) / len(data2025["CASO_SRAG"])
erroMickens = pow(simulacaoMickens["Infectados"] - data2025["CASO_SRAG"], 2) / len(data2025["CASO_SRAG"])

plt.scatter(simulacaoRK4.index, erroRK4, label="Erro RK4", s=1)
plt.scatter(simulacaoMickens.index, erroMickens, label="Erro Mickens", s=1)
plt.legend()

plt.xlabel("Dias")
plt.ylabel("Erro Relativo")

plt.savefig("data/graficos/erro.png")