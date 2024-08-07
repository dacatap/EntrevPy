# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 23:06:53 2024

@author: darca
"""
#Depth-first search para revisar los nodos
def dfs(u, v, graph, visited):
    if u == v:
        return True
    visited.add(u)
    if u in graph:
        for neighbor in graph[u]:
            if neighbor not in visited:
                if dfs(neighbor, v, graph, visited):
                    return True
    return False

#Validación de inputs
def getTwoIntegers(a, b):
    while True:
        finput = input(f"Inserte valores {a} y {b}: ").split()
        if len(finput) != 2:
            print("\nError: Por favor inserte 2 números enteros separados por un espacio\n")
            continue
        try:
            finput = tuple(map(int, finput))
            return finput
        except ValueError:
            print("\nError: Ambos valores deben ser enteros. Por favor intente de nuevo\n")

def main():
    Vertices = {}
    nodos = set()
    
            
    NQ = getTwoIntegers("n", "Q")
    #Primera serie de inputs, formando el árbol de acuerdo a la cantidad n insertada
    print("\nConstrucción de árbol")
    for i in range(NQ[0]-1):
        tinput = getTwoIntegers("u", "v")    
        if tinput[0] in Vertices:
            if isinstance(Vertices[tinput[0]], list):
                Vertices[tinput[0]].append(tinput[1])
            else:
                Vertices[tinput[0]] = [Vertices[tinput[0]], tinput[1]]
        else:
            Vertices[tinput[0]] = [tinput[1]]
        nodos.add(tinput[0])
        nodos.add(tinput[1])
    
    #Loop usado para crear entradas en el arbol, creando los nodos finales sin sucesores
    for i in nodos:
        if i not in Vertices:
            Vertices[i] = []
    print(Vertices)
    
    #Segunda serie de inputs, realizando querys de acuerdo al valor Q insertado
    print("\nConsulta de ancestros")
    for i in range(NQ[1]):
        tinput = getTwoIntegers("u", "v")   
        if tinput[0] in Vertices:
            visited = set()
            if dfs(tinput[0], tinput[1], Vertices, visited):
                print("YES")
            else:
                print("NO")
        else:
            print(f"{tinput[0]} no es un nodo válido")

main()