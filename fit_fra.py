import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# funções
def logI(t, gamma, b):
    return gamma * t + b

def dlogI(t, GAMMA, b):
    return - GAMMA * t + b

def I(t, gamma, b):
    return np.exp(b) * np.exp(gamma * t)

def dI(t, GAMMA, b):
    return np.exp(b) * np.exp(- GAMMA * t)

# lendo o dataset
data = pd.read_csv("data/tratados/franca.csv", sep=",")

# transformação dos dados
maximum = data["incid_hosp"].max()
data["incid_hosp"] = np.log(data["incid_hosp"])


# separando os dados de aumento e decaimento
max_point = data["incid_hosp"].idxmax()
increasing = data[data.index <= max_point]
decreasing = data[data.index > max_point]

# cross-validation
iX_train, iX_test, iy_train, iy_test, = train_test_split(increasing.index, increasing["incid_hosp"], random_state=0)
dX_train, dX_test, dy_train, dy_test, = train_test_split(decreasing.index, decreasing["incid_hosp"], random_state=0)


# fitting increasing
parameters_increasing, covariance = curve_fit(logI, iX_train, iy_train)
predict_i = logI(iy_test, *parameters_increasing)
mae_in = mean_squared_error(predict_i, iy_test)

# fitting decreasing
parameters_decreasing, covariance = curve_fit(dlogI, dX_train, dy_train)
predict_d = logI(dy_test, *parameters_decreasing)
mae_de = mean_squared_error(predict_d, dy_test)

print("MSE increasing: {}".format(mae_in))
print("MSE decreasing: {}".format(mae_de))



increasing["Estimativa"] = I(increasing.index, *parameters_increasing)
increasing["incid_hosp"] = np.exp(increasing["incid_hosp"])

increasing.to_csv("data/tratados/increasing_fra.csv")

# fitting decreasing
parameters_decreasing, covariance = curve_fit(dI, decreasing.index, decreasing["incid_hosp"])
decreasing["Estimativa"] = dI(decreasing.index, parameters_decreasing[0], parameters_decreasing[1])
decreasing["incid_hosp"] = np.exp(decreasing["incid_hosp"])

decreasing.to_csv("data/tratados/decreasing_fra.csv")

# salvando parametros nos arquivos
with open("data/params.txt", "w") as f:
    msg = "I0 = {}\n".format(np.exp(parameters_increasing[1]))
    msg = msg + "gamma_inc = {}\n".format(parameters_increasing[0])
    msg = msg + "C = {}\n".format(np.exp(parameters_decreasing[1]))
    msg = msg + "gamma_dec = {}\n".format(parameters_decreasing[0])
    msg = msg + "Imax = {}\n".format(maximum)
    f.write(msg)