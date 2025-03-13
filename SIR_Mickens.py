import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error


def SIR_Mickens(S0, I0, R0, deltaT, beta, alpha, N, length, file_path):
    # valores iniciais
    Sk = S0
    Ik = I0
    Rk = R0

    # multiplicando as constantes pra otimizar as contas
    a = alpha * deltaT
    b = beta * deltaT / N
    #denI = 1 + a

    with open(file_path, "w") as f:
        f.write("Suscetiveis,Infectados,Recuperados\n")

        for k in range(length):
            # salvando no arquivo
            f.write("{},{},{}\n".format(Sk, Ik, Rk))
            
            # calculando os valores
            #Sk_old = Sk
            Sk = Sk / (1 + b * Ik)
            Ik = Ik * (1 + b * Sk - a)
            Rk = a * Ik + Rk

if __name__ == "__main__":
    R0 = 0
    N = 2.460354382325183e+18
    alpha = 471322.66044314916
    beta = 471322.67475319497
    I0 = 136.75083214945124
    S0 = N - I0
    #I0 = 8.0
    dias = 402
    #I0 = 8
    file_path = "data/tratados/SIRMickens.csv"


    delta_t_domain = np.linspace(start=0, stop=1, num=50)
    dados = pd.read_csv("data/tratados/casos_srag_total.csv")
    mae = 0

    for deltaT in delta_t_domain:
        SIR_Mickens(S0, I0, R0, deltaT, beta, alpha, S0, dias, file_path)
        simulado = pd.read_csv("data/tratados/SIRMickens.csv")

        new_mae = mean_squared_error(simulado["Infectados"], dados["CASO_SRAG"])
        if(new_mae < mae or mae == 0):
            mae = new_mae
            best = deltaT
    
    print("Best deltaT:", best)
    print("MSE:", mae)

    SIR_Mickens(S0, I0, R0, best, beta, alpha, S0, dias, file_path)


