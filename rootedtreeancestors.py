# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 23:06:53 2024

@author: darca
"""
#Depth search first para revisar los nodos
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

def main():
    Vertices = {}
    nodos = set()
    NQ = input("Inserte valores 𝘯 y 𝘘: ").split()
    print("\n")
    NQ = tuple(map(int, NQ))
    
    #Primera serie de inputs, formando el árbol de acuerdo a la cantidad n insertada
    for i in range(NQ[0]-1):
        tinput = input("Inserte valores 𝘶 y 𝘷: ").split()
        tinput = tuple(map(int, tinput))       
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
    for i in range(NQ[1]):
        tinput = input("Inserte valores 𝘶 y 𝘷: ").split()
        tinput = tuple(map(int, tinput))
        if tinput[0] in Vertices:
            visited = set()
            if dfs(tinput[0], tinput[1], Vertices, visited):
                print("YES")
            else:
                print("NO")
        else:
            print(f"{tinput[0]} no es un nodo válido")

main()