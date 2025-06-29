# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CD3fufNFFk15cim06a5Of6InvbUFctb4
"""

def es_par_o_impar(n):
    """
    Determina si un número es par o impar.

    Parámetros:
    n (int): Número entero.

    Retorna:
    str: 'par' si es par, 'impar' si es impar.
    """
    return "par" if n % 2 == 0 else "impar"

def cuenta_regresiva(n):
    """
    Función recursiva que imprime los números desde n hasta 0,
    indicando para cada uno si es par o impar.

    Parámetros:
    n (int): Número entero desde donde comenzar la cuenta regresiva.
    """
    if n < 0:
        return
    print(f"{n} - {es_par_o_impar(n)}")
    if n == 0:
        print("¡Despegue completado! Fin de la cuenta regresiva.")
    else:
        cuenta_regresiva(n - 1)