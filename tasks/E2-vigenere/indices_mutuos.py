import numpy as np
import collections

from cifra_vigenere import traduciMensaje, LETRAS, TEXTO
from prueba_friedman import obtenerCaracteresN

def calcularIndicesMutuos(texto, longitud_clave):
    eq = [0,0,0,0,0,0,0]
    A = []
    A_1 = []
    B_1 = []
    multi_ind_co=0
    for i in range(0, longitud_clave):
        sub_texto_i = obtenerCaracteresN(texto, i, longitud_clave)
        for j in range(i+1, longitud_clave):
            sub_texto_j = obtenerCaracteresN(texto, j, longitud_clave)
            for k in range(0,len(LETRAS)):
                mov_cesar_k = traduciMensaje(LETRAS[j], sub_texto_i, 'd')
                frecuencias_k = collections.Counter(mov_cesar_k)
                frecuencias_m = collections.Counter(sub_texto_i)
                for n in range(0, len(LETRAS)):
                    multi_ind_co += frecuencias_k[LETRAS[n]] * frecuencias_m[LETRAS[n]]  
                multi_ind_co = multi_ind_co/(len(sub_texto_i) * len(sub_texto_j))                
                eq[i] = 1
                eq[j] = 1
                A.append([eq[1:], k, multi_ind_co])
                eq = [0,0,0,0,0,0,0]

    A.sort(reverse=True, key=sortArray)
    while len(A_1) < longitud_clave-1:
        for j in range(0,len(A)):
            if A[j][0] not in A_1:
                A_1.append(A[j][0])
                B_1.append(A[j][1])

                break
  
    print(np.linalg.matrix_rank(A_1))
    print(f"A = {A_1}")
    print(f"B = {B_1}")
    return np.linalg.solve(A_1,B_1)

def sortArray(array):
    return array[2]

def calculaClave(inicio, desplazamientos):
    clave = ""
    letra_actual = inicio
    letras = np.array(list(LETRAS))
    for item in desplazamientos:
        letra_actual = LETRAS.find(inicio)
        letra_actual = int(letra_actual+item)
        clave += letras[letra_actual]
    return clave

desp = calcularIndicesMutuos(TEXTO, 7)
print(desp)
clave = calculaClave('C', desp)

print(clave)