import collections

from prueba_friedman import obtenerCaracteresN, LETRAS
from cifra_vigenere import traduciMensaje, TEXTO

#frecuencia de aparicion de las letras obtenido de wikipedia
FRECUENCIAS = { 'E': 12.181, 'T': 4.632, 'A': 11.525, 'O': 8.683, 'I': 6.247,
                'N': 6.712, 'S': 7.977, 'H': 0.703, 'R': 6.871, 'D': 5.010,
                'L': 4.967, 'C': 4.019, 'U': 2.927, 'M': 3.157, 'W': 0.017,
                'F': 0.692, 'G': 1.768, 'Y': 1.008, 'P': 2.510, 'B': 2.215,
                'V': 1.138, 'K': 0.011, 'J': 0.493, 'X': 0.215, 'Q': 0.877,
                'Z': 0.467 }

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

