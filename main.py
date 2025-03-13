import pandas as pd
from cvt_data import cvt_data

data = pd.read_csv("data/bruto/INFLUD24-10-02-2025.csv", sep=";")
data = data[data["CASO_SRAG"] == 1]

# limpeza das colunas indesejadas
columns = data.columns
columns = columns.drop("DT_NOTIFIC")
columns = columns.drop("CASO_SRAG")
data = data.drop(columns=columns, axis=1)

# tratamento dde dados (agrupando casos de SRAG)
data = data.groupby(["DT_NOTIFIC"], as_index=False).count()
num_total_ano = data["CASO_SRAG"].sum()

data["DT_NOTIFIC"] = data["DT_NOTIFIC"].apply(lambda x: cvt_data(x))
data.index = pd.DatetimeIndex(data["DT_NOTIFIC"])
data = data.drop(columns=["DT_NOTIFIC"], axis=1)


dia_final = "28/12/2024"
dia_final = cvt_data(dia_final)

dia_inicial_2025 = "29/12/2024"
dia_inicial_2025 = cvt_data(dia_inicial_2025)

# ordenando conforme as datas
data = data.sort_index()
data_total = data.copy()
data2025 = data[data.index >= dia_inicial_2025]
data = data[data.index <= dia_final]

data.to_csv("data/tratados/casos_srag_2024.csv")
data2025.to_csv("data/tratados/casos_srag_2025.csv")
data_total.to_csv("data/tratados/casos_srag_total.csv")


# calculo media movel
medias_ano = data.rolling('7D', min_periods=1).mean()
medias_ano.to_csv("data/tratados/media_movel_srag_2024.csv")
medias_ano = medias_ano["CASO_SRAG"]

medias_2025 = data2025.rolling('7D', min_periods=1).mean()
medias_2025.to_csv("data/tratados/media_movel_srag_2025.csv")

medias_total = data_total.rolling('7D', min_periods=1).mean()
medias_total.to_csv("data/tratados/media_movel_srag_total.csv")

print("Quantidade total de casos em 2024: {}".format(num_total_ano))
print("Médias Móveis:", medias_ano, end="\n")