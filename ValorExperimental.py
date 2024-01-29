#Encontrar o valor experimental de g com incertezas usando a fórmula g = 2h/t^2
import math
Tempos = [[0.1367, 0.1354, 0.1354, 0.1287, 0.1344, 0.1338], [0.1972, 0.2019, 0.2016, 0.2044, 0.1972, 0.1951],
          [0.24830,0.2431,0.2411,0.2475,0.2419,0.2389],[0.2838,0.3041,0.2855,0.2811,0.2826,0.2848],
          [0.3207,0.3153,0.3135,0.3132,0.3129,0.3163], [0.3538,0.3529,0.3463,0.3581,0.3480,0.3453],
          [0.3738, 0.3742,0.3774,0.3753,0.3731,0.3744], [0.3938, 0.3872,0.3881,0.3886,0.4009,0.3959],
          [0.4032,0.4005,0.4019,0.4012,0.3976,0.3992]]

Alturas = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8]

def Valor_Medio(Tempos):
    #Calcula o valor médio de cada conjunto de tempos
    Medias = []
    for i in range(len(Tempos)):
        soma = 0
        for j in range(len(Tempos[i])):
            soma += Tempos[i][j]
        media = soma/len(Tempos[i])
        Medias.append(media)
    return Medias
print(Valor_Medio(Tempos))

def Incerteza_Tempo(Tempos):
    #Calcula a incerteza de cada conjunto de tempos
    Incerteza = []
    for i in range(len(Tempos)):
        soma = 0
        for j in range(len(Tempos[i])):
            soma += (Tempos[i][j] - Valor_Medio(Tempos)[i])**2
        incerteza = (soma/(len(Tempos[i])*(len(Tempos[i])-1)))**(1/2)
        Incerteza.append(incerteza)
    return Incerteza
print(Incerteza_Tempo(Tempos))

def Incerteza_Tempo_Quadrado(Tempos):
    #Calcula a incerteza de cada conjunto de tempos ao quadrado
    Incerteza = []
    for i in range(len(Tempos)):
        soma = 0
        for j in range(len(Tempos[i])):
            soma += (Tempos[i][j] - Valor_Medio(Tempos)[i])**2
        incerteza = (soma/(len(Tempos[i])*(len(Tempos[i])-1)))**(1/2)
        Incerteza.append(incerteza**2)
    return Incerteza
print(Incerteza_Tempo_Quadrado(Tempos))

def Incerteza_Altura(Alturas):
    #Calcula a incerteza de cada altura
    Incerteza = []
    for i in range(len(Alturas)):
        Incerteza.append(0.005)
    return Incerteza
print(Incerteza_Altura(Alturas))

def Propagacao_Incerteza(Alturas, Tempos):
    #Calcula a incerteza de cada valor experimental de g
    Incerteza = []
    for i in range(len(Alturas)):
        Incerteza.append(((2*Alturas[i])/(Valor_Medio(Tempos)[i]**2))*Incerteza_Tempo(Tempos)[i])
    return Incerteza
print(Propagacao_Incerteza(Alturas, Tempos))

def Valor_Experimental(Alturas, Tempos):
    #Calcula o valor experimental de g
    Valores = []
    for i in range(len(Alturas)):
        Valores.append(2*Alturas[i]/(Valor_Medio(Tempos)[i]**2))
    return Valores
print(Valor_Experimental(Alturas, Tempos))

def Incerteza_Experimental(Alturas, Tempos):
    #Calcula a incerteza experimental de g
    Incerteza = []
    for i in range(len(Alturas)):
        Incerteza.append(math.sqrt((Propagacao_Incerteza(Alturas, Tempos)[i])**2))
    return Incerteza
print(Incerteza_Experimental(Alturas, Tempos))

def Erro_Percentual(Alturas, Tempos):
    #Calcula o erro percentual de cada valor experimental de g
    Erro = []
    for i in range(len(Alturas)):
        Erro.append((Incerteza_Experimental(Alturas, Tempos)[i]/Valor_Experimental(Alturas, Tempos)[i])*100)
    return Erro
print(Erro_Percentual(Alturas, Tempos))




