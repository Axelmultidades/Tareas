"""
Title: Implementar el ADT Arboles Binarios
Autor: Axel Jes Aguilar Ribera
Date: 10/04/25
Version: v3.0
"""
"""
creacion de clase ArbolBinario
"""
from Nodo import Nodo
from collections import deque
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

    #Actualizacion de implementacion de metodos
    
    #verificacion si el arbol esta vacío
    def esta_vacio(self):
        return self.__raiz is None
    
    #verificacion si es hoja
    def es_hoja(self, nodo):
        return nodo.get_hijo_izquierdo() is None and nodo.get_hijo_derecho() is None
    
    #Metodo para recorrer en pre_orden
    def pre_orden(self):
        self.__pre_orden_rec(self.__raiz)
        print()

    def __pre_orden_rec(self, nodo):
        if nodo:
            print(nodo.get_data(), end=" ")
            self.__pre_orden_rec(nodo.get_hijo_izquierdo())
            self.__pre_orden_rec(nodo.get_hijo_derecho())
    
    #Metodo para recorrer en post orden
    def post_orden(self):
        self.__post_orden_rec(self.__raiz)
        print()

    def __post_orden_rec(self, nodo):
        if nodo:
            self.__post_orden_rec(nodo.get_hijo_izquierdo())
            self.__post_orden_rec(nodo.get_hijo_derecho())
            print(nodo.get_data(), end=" ")

    #implementacion de metodos DFS y BFS
    # DFS Preorden
    def dfs_preorden(self):
        """Devuelve lista del recorrido en preorden (DFS)."""
        resultado = []
        self.__dfs_preorden_rec(self.__raiz, resultado)
        return resultado

    def __dfs_preorden_rec(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.get_data())  # Nodo
            self.__dfs_preorden_rec(nodo.get_hijo_izquierdo(), resultado)  # Izquierda
            self.__dfs_preorden_rec(nodo.get_hijo_derecho(), resultado)  # Derecha

    # DFS Inorden
    def dfs_inorden(self):
        """Devuelve lista del recorrido en inorden (DFS)."""
        resultado = []
        self.__dfs_inorden_rec(self.__raiz, resultado)
        return resultado

    def __dfs_inorden_rec(self, nodo, resultado):
        if nodo:
            self.__dfs_inorden_rec(nodo.get_hijo_izquierdo(), resultado)  # Izquierda
            resultado.append(nodo.get_data())  # Nodo
            self.__dfs_inorden_rec(nodo.get_hijo_derecho(), resultado)  # Derecha

    # DFS Postorden
    def dfs_postorden(self):
        """Devuelve lista del recorrido en postorden (DFS)."""
        resultado = []
        self.__dfs_postorden_rec(self.__raiz, resultado)
        return resultado

    def __dfs_postorden_rec(self, nodo, resultado):
        if nodo:
            self.__dfs_postorden_rec(nodo.get_hijo_izquierdo(), resultado)  # Izquierda
            self.__dfs_postorden_rec(nodo.get_hijo_derecho(), resultado)  # Derecha
            resultado.append(nodo.get_data())  # Nodo
                  
    # Método para recorrido por niveles (BFS)
    def recorrido_por_niveles(self):
        """Realiza un recorrido por niveles (BFS) del ABB."""
        if self.__raiz is None:
            print("El árbol está vacío.")
            return

        cola = deque()
        cola.append(self.__raiz)

        while cola:
            nodo_actual = cola.popleft()
            print(nodo_actual.get_data(), end=" ")

            if nodo_actual.get_hijo_izquierdo() is not None:
                cola.append(nodo_actual.get_hijo_izquierdo())
            if nodo_actual.get_hijo_derecho() is not None:
                cola.append(nodo_actual.get_hijo_derecho())
