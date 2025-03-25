"""
Title: Representacion de una clase usando los estandares PEP8
Autor: Axel Jes Aguilar Ribera
Date: 24/03/25
Version: v1.0
"""

class Coche:
    """Clase que representa un coche con sus características básicas"""

    def __init__(self, marca: str, modelo: str, año: int, velocidad: float = 0.0):
        """
        Inicializa un objeto Coche con los atributos dados

        parametro marca: Marca del coche
        parametro modelo: Modelo del coche
        parametro año: Año de fabricación del coche
        parametro velocidad: Velocidad actual del coche (por defecto 0.0)
        """
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._velocidad = velocidad

    # Métodos getter
    def get_marca(self) -> str:
        """Devuelve la marca del coche"""
        return self._marca

    def get_modelo(self) -> str:
        """Devuelve el modelo del coche"""
        return self._modelo

    def get_año(self) -> int:
        """Devuelve el año de fabricación del coche"""
        return self._año

    def get_velocidad(self) -> float:
        """Devuelve la velocidad actual del coche"""
        return self._velocidad

    # Métodos setter
    def set_marca(self, marca: str):
        """Establece la marca del coche"""
        self._marca = marca

    def set_modelo(self, modelo: str):
        """Establece el modelo del coche"""
        self._modelo = modelo

    def set_año(self, año: int):
        """Establece el año de fabricación del coche"""
        if año > 1885:  # Primer automóvil fabricado en 1886
            self._año = año
        else:
            raise ValueError("El año debe ser mayor a 1885")

    def set_velocidad(self, velocidad: float):
        """Establece la velocidad del coche."""
        if velocidad >= 0:
            self._velocidad = velocidad
        else:
            raise ValueError("La velocidad no puede ser negativa")

    def acelerar(self, incremento: float):
        """Aumenta la velocidad del coche en el valor especificado"""
        if incremento > 0:
            self._velocidad += incremento
        else:
            raise ValueError("El incremento debe ser un valor positivo")

    def frenar(self, decremento: float):
        """Disminuye la velocidad del coche en el valor especificado"""
        if 0 <= decremento <= self._velocidad:
            self._velocidad -= decremento
        else:
            raise ValueError("El decremento debe ser un valor positivo y no mayor que la velocidad actual")


#Ejemplo
coche1 = Coche("toyota","Corolla","2020")
print("La marca es", coche1.get_marca())
print(f"Velocidad actual: {coche1.get_velocidad()}")
coche1.acelerar(50)
print(f"Velocidad con la aceleracion: {coche1.get_velocidad()}")