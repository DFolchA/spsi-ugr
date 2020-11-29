import re

NONLETTERS_PATTERN = re.compile('[^A-Z]')
MAX_KEY_LENGTH = 16

def examenKasiski(texto):
    secuenciasRepetidas = encontrarSecuenciasRepetidas(texto)
    print(secuenciasRepetidas)
    factores = {}
    for secuencia in secuenciasRepetidas:
        factores[secuencia] = []
        for espacio in secuenciasRepetidas[secuencia]:
            factores[secuencia].extend(encontrarFactoresEnteros(espacio))

    factoresByCount = ordenarFactoresComunes(factores)

    allLikelyKeyLengths = []
    for twoIntTuple in factoresByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])

    return allLikelyKeyLengths

def encontrarSecuenciasRepetidas(msg):
    espacioEntreSec = {}
    for longitud in range(3, 10):
        for inicio in range(len(msg) - longitud):
            secuencia = msg[inicio:inicio + longitud]

            for i in range(inicio + longitud, len(msg) - longitud):
                if msg[i:i + longitud] == secuencia:
                    if secuencia not in espacioEntreSec:
                        espacioEntreSec[secuencia] = [] # initialize blank list

                    espacioEntreSec[secuencia].append(i - inicio)
    return espacioEntreSec

def encontrarFactoresEnteros(num):
    if num < 2:
        return []

    factores = []

    for i in range(2, MAX_KEY_LENGTH + 1): # don't test 1
        if num % i == 0:
            factores.append(i)
            factores.append(int(num / i))
    if 1 in factores:
        factores.remove(1)
    return list(set(factores))

def ordenarFactoresComunes(secuenciaFactores):
    cuenta = {} 

    for secuencia in secuenciaFactores:
        listaFactores = secuenciaFactores[secuencia]
        for factor in listaFactores:
            if factor not in cuenta:
                cuenta[factor] = 0
            cuenta[factor] += 1

    factoresByCount = []
    for factor in cuenta:
        if factor <= MAX_KEY_LENGTH:
            factoresByCount.append( (factor, cuenta[factor]) )

    factoresByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factoresByCount

def getItemAtIndexOne(x):
    return x[1]

