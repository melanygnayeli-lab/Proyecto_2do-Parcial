# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN

class Cliente:
    """
    Clase que permite crear objetos de tipo serivicio
    """
    def __init__(self, id, nombres, apellidos):
        self._id = id
        self._nombres = nombres
        self._apellidos = apellidos

    #Property & Setter
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El número de transacción no puede estar vacío")
        self._id = valor.strip()

    @property
    def nombres(self):
        return self._nombres
    @nombres.setter
    def nombres(self, valor):
        if not isinstance(valor,str):
            raise ValueError("Los nombres no pueden estar vacíos")
        self._nombres = valor.strip()

    @property
    def apellidos(self):
        return self._apellidos
    @apellidos.setter
    def apellidos(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Los apellidos no pueden estar vacíos")
        self._apellidos.strip()

