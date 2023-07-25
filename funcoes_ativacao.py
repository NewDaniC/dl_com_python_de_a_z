import numpy as np
# transfer function


def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0


def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))


def tahnFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))


def reluFunction(soma):
    if soma >= 0:
        return soma
    return 0


def linearFunction(soma):
    return soma


def softmaxFunction(x): # Retorna a probabilidade de cada classe
    ex = np.exp(x)
    return ex / ex.sum()


teste = stepFunction(-1)
print(teste)
teste = sigmoidFunction(-0.358)
print(teste)
teste = tahnFunction(-0.358)
print(teste)
teste = reluFunction(0.358)
print(teste)
teste = linearFunction(-0.358)
print(teste)
valores = [7.0, 2.0, 1.3]
print(softmaxFunction(valores))
