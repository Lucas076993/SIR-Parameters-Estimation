import pandas as pd
from cvt_data import cvt_data_fra
from matplotlib import pyplot as plt

franca = pd.read_csv("data/bruto/covid-hospit-incid-2023-03-31-18h01.csv", sep=";")
franca["jour"] = franca["jour"].apply(lambda x: cvt_data_fra(x))
franca = franca[franca.index <= 100]

columns = franca.columns
columns = columns.drop("incid_hosp")
columns = columns.drop("jour")

franca = franca.drop(columns=columns, axis=1)


franca.index = pd.DatetimeIndex(franca["jour"])
franca = franca.drop(columns=["jour"], axis=1)

print(franca.head())

franca.to_csv("data/tratados/franca.csv")

medias_ano = franca.rolling("7D", min_periods=1).mean()
medias_ano.to_csv("data/tratados/media_movel_franca.csv")

print(medias_ano)