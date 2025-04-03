"""
Title: Implementar el ADT Arboles Binarios
Autor: Axel Jes Aguilar Ribera
Date: 03/04/25
Version: v1.0
"""
"""
Principal utilizado para pruebas
"""
from Arbol import ArbolBinarioBusqueda
abb = ArbolBinarioBusqueda()

abb.insertar(50)
abb.insertar(30)
abb.insertar(70)
abb.insertar(20)
abb.insertar(40)
abb.insertar(60)
abb.insertar(80)

# Recorrido en orden
print("Recorrido en orden:")
abb.in_orden()

# Buscar valores en el árbol
valores_a_buscar = [40, 90]
for valor in valores_a_buscar:
    if abb.buscar(valor):
        print(f"El valor {valor} se encuentra en el árbol.")
    else:
        print(f"El valor {valor} no está en el árbol.")

# Encontrar valores mínimo y máximo
print(f"Valor mínimo: {abb.minimo()}")
print(f"Valor máximo: {abb.maximo()}")

# Obtener la altura del árbol
print(f"Altura del árbol: {abb.altura()}")

# Contar nodos
print(f"Número total de nodos: {abb.get_num_nodos()}")

