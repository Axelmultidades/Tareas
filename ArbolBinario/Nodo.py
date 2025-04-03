"""
Title: Implementar el ADT Arboles Binarios
Autor: Axel Jes Aguilar Ribera
Date: 03/04/25
Version: v1.0
"""
"""
creacion de clase nodo 
"""
class Nodo:
    __data__ = 0
    __HijoIzquierdo__ = None
    __HijoDerecho__ = None

    def __init__(self,data):
        """Inicializa un nodo con un valor y sin hijos."""
        self.__HijoIzquierdo__ = None
        self.__HijoDerecho__ = None
        self.__data__ = data
    #Metodo de obtencion de dato
    def get_data(self):
        return self.__data__    
    #Metodo de poner dato
    def set_data(self,data):
        self.__data__ = data
    #Metodo de obtencion de hijo izquierdo del nodo
    def get_hijo_izquierdo(self):
        return self.__HijoIzquierdo__
    #Metodo de poner hijo izquierdo del nodo
    def set_hijo_izquierdo(self,HijoIzquierdo):
        self.__HijoIzquierdo__ = HijoIzquierdo 
    #Metodo de obtencion de hijo derecho del nodo
    def get_hijo_derecho(self):
        return self.__HijoDerecho__
    #Metodo de poner hijo derecho del nodo
    def set_hijo_derecho(self,HijoDerecho):
        self.__HijoDerecho__ = HijoDerecho 
