import numpy as np
from scipy.optimize import fsolve

def estimate_R0(gamma, Gamma, I_max):
    rho = gamma / Gamma

    # Função para resolver S_e/N em função de R0
    def SeN_equation(x, R0):
        return x - (1/R0)*np.log(x) - 1

    # Função para calcular rho teórico
    def rho_equation(R0):
        x_guess = 0.1  # Chute inicial para S_e/N
        SeN = fsolve(SeN_equation, x_guess, args=(R0))[0]
        rho_calculado = (R0 - 1) / (1 - R0 * SeN)
        return rho_calculado - rho

    # Resolver R0 usando fsolve
    R0_initial_guess = 1  # Chute inicial para R0
    R0 = fsolve(rho_equation, R0_initial_guess)[0]

    # Calcular beta, alpha e N
    beta = gamma / (1 - 1/R0)
    alpha = beta / R0
    N = (R0 * I_max) / (R0 - 1 - np.log(R0))

    return R0, beta, alpha, N


if __name__ == "__main__":
    I0 = 136.75083214945124
    gamma_inc = 0.014310045798493598
    C = 5304.717319017966
    gamma_dec = 0.01065553513437767
    Imax = 1134

    
    R0, beta, alpha, N = estimate_R0(gamma_inc, gamma_dec, Imax)

    print("R0 = {}".format(R0))
    print("N = {}".format(N))
    print("alpha = {}".format(alpha))
    print("beta = {}".format(beta))
    print("I0 = {}".format(I0))