# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:04:40 2024

@author: darca
"""

from collections import Counter

def mostrepNum(list1):
    if not list1: #Solo para asegurarse que la lista no está vacía
            return 0
    count = Counter(list1)
    mostRepeated = count.most_common(1) 
    """
    count.most_common retorna una tupla, por lo que en la siguiente linea se retorna
    mostRepeated[0][1], donde el [0] accede a la tupla, y el [1] al segundo valor de esta, la cual es la cantidad de veces
    que se repitió el número más repetido en la lista
    """
    return mostRepeated[0][1]

def main():
    listaDiametros = []
    #Se le pide al usuario la N cantidad de Ollas
    temp = int(input("Inserte cantidad de Ollas: "))
    
    #Se le pide al usuario ingresar N cantidad de Diametros, los cuales se agregan a la listaDiametros
    for i in range(temp):
        diametro = int(input(f"Inserte diametro de olla n°{i+1}: "))
        listaDiametros.append(diametro)  
        
    """
    Se busca el número más veces repetido en la lista de diametros, y se retorna cuantas veces este se repitió
    Esto debido a que la cantidad de pilas en las que se pueden apilar las ollas, 
    si o si depende de las veces que se repita un diametro en especifico
    """
    nrepetido = mostrepNum(listaDiametros)
    print(nrepetido)

main()