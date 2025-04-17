"""
Title: Implementar el ADT Arboles Binarios
Autor: Axel Jes Aguilar Ribera
Date: 17/04/25
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

abb.eliminar(20)  
abb.eliminar(30)  
abb.eliminar(50)  

abb.in_orden()  # Verifica el resultado después de eliminar
