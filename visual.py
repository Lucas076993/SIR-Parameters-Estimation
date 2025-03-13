import pandas as pd
from matplotlib import pyplot as plt

# plotando casos
data = pd.read_csv("data/tratados/casos_srag_2024.csv", sep=",")
data.plot.scatter(x="DT_NOTIFIC", y="CASO_SRAG",  s=1)
plt.savefig("data/graficos/casos.png")

# plotando média móvel
data = pd.read_csv("data/tratados/media_movel_srag_2024.csv", sep=",")
data.plot.scatter(x="DT_NOTIFIC", y="CASO_SRAG",  s=1, label="data")
plt.savefig("data/graficos/media_movel.png")


# plotando increasing e media movel juntos
increasing = pd.read_csv("data/tratados/increasing.csv", sep=",")
decreasing = pd.read_csv("data/tratados/decreasing.csv", sep=",", index_col=0)


plt.scatter(increasing.index, increasing["Estimativa"], label="Estimado Crescendo", s=1)
plt.scatter(decreasing.index, decreasing["Estimativa"], label="Estimado Decaindo", s=1)
plt.scatter(data.index, data["CASO_SRAG"], label="Dados", s=1)

plt.savefig("data/graficos/estimado.png")

