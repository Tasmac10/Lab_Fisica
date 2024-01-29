### Criar um programa para analisar um lista de valores de medições de diametro de 5 canos e aplicar o desvio padrão em cada conjunto de valores

medidas = [[0.1367, 0.1354, 0.1354, 0.1287, 0.1344, 0.1338], [0.1972, 0.2019, 0.2016, 0.2044, 0.1972, 0.1951],
          [0.24830,0.2431,0.2411,0.2475,0.2419,0.2389],[0.2838,0.3041,0.2855,0.2811,0.2826,0.2848],
          [0.3207,0.3153,0.3135,0.3132,0.3129,0.3163], [0.3538,0.3529,0.3463,0.3581,0.3480,0.3453],
          [0.3738, 0.3742,0.3774,0.3753,0.3731,0.3744], [0.3938, 0.3872,0.3881,0.3886,0.4009,0.3959],
          [0.4032,0.4005,0.4019,0.4012,0.3976,0.3992]]

# valor medio = somatorio de todos os valores / quantidade de valores
def valormedio(medidas):
    conjunto_medias = []
    for conjunto_valores in range(len(medidas)):
        acc=0
        for valor in range(len(medidas[conjunto_valores])):
            acc = acc + medidas[conjunto_valores][valor]
        media = acc / len(medidas[conjunto_valores])
        conjunto_medias.append(media)
    return conjunto_medias

print("Valor medio")
print(valormedio(medidas))

# desvio padrao da amostra  = raiz quadrada da soma dos quadrados da diferenca entre o valor e a media dividido pela quantidade de valores - 1
def desviopadrao(medidas):
    conjunto_medias = valormedio(medidas)
    conjunto_desvio = []
    for conjunto_valores in range(len(medidas)):
        acc=0
        for valor in range(len(medidas[conjunto_valores])):
            acc = acc + (medidas[conjunto_valores][valor] - conjunto_medias[conjunto_valores])**2
        desvio = (acc / (len(medidas[conjunto_valores])-1))**0.5
        conjunto_desvio.append(desvio)
    return conjunto_desvio

print("Desvio padrao")
print(desviopadrao(medidas))

#incerteza tipo A = desvio padrao / raiz quadrada da quantidade de valores
def incertezaA(medidas):
    conjunto_desvio = desviopadrao(medidas)
    conjunto_incerteza = []
    for conjunto_valores in range(len(medidas)):
        incerteza = conjunto_desvio[conjunto_valores] / (len(medidas[conjunto_valores])**0.5)
        conjunto_incerteza.append(incerteza)
    return conjunto_incerteza

print("Incerteza A")
print(incertezaA(medidas))

#incerteza tipo B (paquimetro) = 0.05
def incertezaB(medidas):
    conjunto_incerteza = []
    for conjunto_valores in range(len(medidas)):
        incerteza = 0.0001
        conjunto_incerteza.append(incerteza)
    return conjunto_incerteza

print("Incerteza B")
print(incertezaB(medidas))

#incerteza combinada = raiz quadrada da soma dos quadrados das incertezas
def incertezacombinada(medidas):
    conjunto_incertezaA = incertezaA(medidas)
    conjunto_incertezaB = incertezaB(medidas)
    conjunto_incerteza = []
    for conjunto_valores in range(len(medidas)):
        incerteza = (conjunto_incertezaA[conjunto_valores]**2 + conjunto_incertezaB[conjunto_valores]**2)**0.5
        conjunto_incerteza.append(incerteza)
    return conjunto_incerteza

print("Incerteza combinada")
print(incertezacombinada(medidas))
