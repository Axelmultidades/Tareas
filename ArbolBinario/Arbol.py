"""
Title: Implementar el ADT Arboles Binarios
Autor: Axel Jes Aguilar Ribera
Date: 03/04/25
Version: v1.0
"""
"""
creacion de clase ArbolBinario
"""
from Nodo import Nodo
class ArbolBinarioBusqueda:
    def __init__(self):
        """Inicializa el árbol binario de búsqueda vacío."""
        self.__raiz = None
        self.__num_nodos = 0

    # Método para insertar un valor en el ABB
    def insertar(self, data):
        self.__raiz = self.__insertar_rec(self.__raiz, data)
        self.__num_nodos += 1

    def __insertar_rec(self, nodo, data):
        """Función recursiva para insertar un nodo en el ABB."""
        if nodo is None:
            return Nodo(data)

        if data < nodo.get_data():
            nodo.set_hijo_izquierdo(self.__insertar_rec(nodo.get_hijo_izquierdo(), data))
        else:
            nodo.set_hijo_derecho(self.__insertar_rec(nodo.get_hijo_derecho(), data))

        return nodo

    # Método para realizar un recorrido inorden
    def in_orden(self):
        """Realiza un recorrido inorden del ABB."""
        self.__in_orden_rec(self.__raiz)
        print()

    def __in_orden_rec(self, nodo):
        if nodo:
            self.__in_orden_rec(nodo.get_hijo_izquierdo())
            print(nodo.get_data(), end=" ")
            self.__in_orden_rec(nodo.get_hijo_derecho())

    # Método para buscar un valor en el ABB
    def buscar(self, data):
        """Verifica si un valor está en el ABB."""
        return self.__buscar_rec(self.__raiz, data) is not None

    def __buscar_rec(self, nodo, data):
        if nodo is None or nodo.get_data() == data:
            return nodo

        if data < nodo.get_data():
            return self.__buscar_rec(nodo.get_hijo_izquierdo(), data)
        return self.__buscar_rec(nodo.get_hijo_derecho(), data)

    # Método para encontrar el valor mínimo en el ABB
    def minimo(self):
        """Devuelve el valor mínimo en el ABB."""
        nodo = self.__raiz
        while nodo.get_hijo_izquierdo():
            nodo = nodo.get_hijo_izquierdo()
        return nodo.get_data()

    # Método para encontrar el valor máximo en el ABB
    def maximo(self):
        """Devuelve el valor máximo en el ABB."""
        nodo = self.__raiz
        while nodo.get_hijo_derecho():
            nodo = nodo.get_hijo_derecho()
        return nodo.get_data()

    # Método para calcular la altura del ABB
    def altura(self):
        """Devuelve la altura del ABB."""
        return self.__altura_rec(self.__raiz)

    def __altura_rec(self, nodo):
        if nodo is None:
            return -1  # Altura de un árbol vacío
        return 1 + max(self.__altura_rec(nodo.get_hijo_izquierdo()), self.__altura_rec(nodo.get_hijo_derecho()))

    # Método para contar el número total de nodos en el ABB
    def get_num_nodos(self):
        """Devuelve la cantidad total de nodos en el ABB."""
        return self.__num_nodos



