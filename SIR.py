import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sklearn.metrics import mean_squared_error


def resultado_para_dataframe(solucao):
    """
    Converte o objeto de solução do modelo SIR em um DataFrame.
    """
    # Cria um DataFrame com as colunas S, I, R
    df = pd.DataFrame({
        'Dia': solucao.t,
        'Suscetiveis': solucao.y[0],
        'Infectados': solucao.y[1],
        'Recuperados': solucao.y[2]
    })
    
    return df

def modelo_sir(t, y, beta, alpha, N):
    """
    Define as equações diferenciais do modelo SIR.
    y[0] = S (suscetíveis)
    y[1] = I (infectados)
    y[2] = R (recuperados)
    """
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - alpha * I
    dRdt = alpha * I
    return [dSdt, dIdt, dRdt]

def simular_sir(S0, I0, R0, beta, alpha, dias, N):
    """
    Simula o modelo SIR e retorna os resultados.
    """
    t_span = (0, dias)
    t_eval = np.linspace(0, dias, dias)  # Pontos de tempo para avaliação

    # Resolve as equações diferenciais
    solucao = solve_ivp(
        fun=lambda t, y: modelo_sir(t, y, beta, alpha, N),
        t_span=t_span,
        y0=[S0, I0, R0],
        t_eval=t_eval,
        method='RK45'  # Método de Runge-Kutta de ordem 4
    )

    return solucao

def plotar_resultados(solucao):
    """
    Plota as curvas S(t), I(t) e R(t).
    """
    plt.figure(figsize=(10, 6))
    plt.plot(solucao.t, solucao.y[0], label='Suscetíveis (S)')
    plt.plot(solucao.t, solucao.y[1], label='Infectados (I)', color='red')
    plt.plot(solucao.t, solucao.y[2], label='Recuperados (R)', color='green')
    plt.xlabel('Dias')
    plt.ylabel('Número de indivíduos')
    plt.title('Modelo SIR')
    plt.legend()
    plt.grid(True)
    plt.savefig("data/graficos/Simulação.png")




R0 = 0
N = 2.460354382325183e+18
alpha = 471322.66044314916
beta = 471322.67475319497
I0 = 136.75083214945124
S0 = N - I0
#I0 = 8.0
dias = 402

dados = pd.read_csv("data/tratados/casos_srag_total.csv")

# Executa a simulação
resultado = simular_sir(S0, I0, R0, beta, alpha, dias, N)
data = resultado_para_dataframe(resultado)

# Mede o erro absoluto médio
mse = mean_squared_error(data["Infectados"], dados["CASO_SRAG"])
print("MSE: {}".format(mse))

# Plota os resultados
plotar_resultados(resultado)


data.to_csv("data/tratados/simulacao.csv", sep=",")