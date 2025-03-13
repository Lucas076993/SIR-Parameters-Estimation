from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from scipy.optimize import curve_fit
import numpy as np

def train(func, X, y):
    result = []
    X_copy = X.copy()
    y_copy = y.copy()

    # separa os dados e faz o ajuste na curva
    X_train, X_test, y_train, y_test = train_test_split(X_copy, y_copy, random_state=0)
    parameters, covariance = curve_fit(func, X_train, y_train)

    # junta os resultados
    result.append(parameters)
    result.append(covariance)

    # estimando erro total
    estimado_teste = func(np.array(X_test), *parameters)
    score = mean_absolute_error(estimado_teste, y_test)
    result.append(score)
    result.append(func(np.array(X), *parameters))

    return result

if __name__ == "__main__":
    def reta(t, a, b):
        return a + b * t
    
    testeX = np.array([0, 1, 2, 3, 4])
    testeY = np.array([1, 4, 7, 10, 13])

    resultados = train(reta, testeX, testeY)
    print("Teste em todo o domínio: ", reta(testeX, *resultados[0]), sep="\t")
    print("Parâmetros Encontrados: {}\nCovariância: {}\nErro médio absoluto: {}".format(*resultados))
    