import collections

from prueba_friedman import obtenerCaracteresN, LETRAS
from cifra_vigenere import traduciMensaje, TEXTO

#frecuencia de aparicion de las letras obtenido de wikipedia
FRECUENCIAS = { 'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
                'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
                'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
                'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
                'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
                'Z': 0.07 }

def buscarClave(texto, longitud_clave):
    clave = ""
    for i in range(0, longitud_clave):
        sub_texto = obtenerCaracteresN(texto, i, longitud_clave)
        mejor_frecuencia = -1
        mejor_letra = ""
        for j in range(0,len(LETRAS)):
            mov_cesar = traduciMensaje(LETRAS[j], sub_texto, 'd')
            frecuencia = compararFrecuencias(mov_cesar)
            if mejor_frecuencia == -1:
                mejor_letra = LETRAS[j]
                mejor_frecuencia = frecuencia
            if frecuencia < mejor_frecuencia:
                mejor_letra = LETRAS[j]
                mejor_frecuencia = frecuencia
        clave = clave+mejor_letra
    return clave

def compararFrecuencias(texto):
    coeficiente = 0
    frecuencias_texto = collections.Counter(texto)

    for letra in FRECUENCIAS:
        coeficiente += (frecuencias_texto[letra]-FRECUENCIAS[letra])**2
    return coeficiente

clave = buscarClave(TEXTO, 7)
print(f"la clave es \n{clave}\n")

encriptado = traduciMensaje(clave, TEXTO, "d")
print(f"el mensaje es \n{encriptado}\n")

