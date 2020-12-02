from cifra_vigenere import TEXTO

import collections

LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
k_p = 0.0685
k_r = 0.0385

    
def indice_coincidencia(texto):
    k_0 = 0
    longitud_texto = len(texto)
    frecuencias = collections.Counter(texto)
    for i in LETRAS:
        k_0 += frecuencias[i]*(frecuencias[i]-1)
    k_0 = k_0/(longitud_texto*(longitud_texto-1))
    return k_0

def prueba_friedman(texto):
    k_0 = indice_coincidencia(texto)
    longitud_clave = (k_p - k_r)/(k_0 - k_r)
    return(longitud_clave)

def promedio_coincidencia(texto, longitud):
    k_0 = 0
    for i in range(0, longitud):
        k_0 += indice_coincidencia(obtenerCaracteresN(texto, i, longitud))
    k_0 = k_0/longitud
    longitud_clave = (k_p - k_r)/(k_0 - k_r)
    return longitud_clave

def obtenerCaracteresN(texto, inicio, n):
    caracteres = ""
    for i in range(0,len(texto)):
        if i%n == inicio:
            caracteres = caracteres+texto[i]
    return caracteres


# print(f"prueba friedman longitud de la clave = {prueba_friedman(texto)}\n")
# for i in range (5,10):
#     print(f"test clave longitud {i} promedio de coincidencia = {promedio_coincidencia(texto,i)}\n")
