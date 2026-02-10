# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN


from DOMINIO.cliente import Cliente

class ServicioBancario:
    """
    Clase que permite crear objetos de tipo serivicio
    """
    def __init__(self, cod_transaccion, cliente, monto, fecha, estado):
        self._cod_transaccion = cod_transaccion
        self._cliente = cliente
        self._monto = monto
        self._fecha = fecha
        self._estado = estado

    # Property & Setter
    @property
    def cod_transaccion(self):
        return self._cod_transaccion
    @cod_transaccion.setter
    def cod_transaccion(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El número de transacción no puede estar vacío")
        self._cod_transaccion = valor.strip()

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if not isinstance(valor, Cliente):
            raise ValueError("El campo cliente debe ser una instancia de Cliente")
        self._cliente = valor

    @property
    def monto(self):
        return self._monto
    @monto.setter
    def monto(self, valor):
        if not isinstance(valor, float) or valor <= 0:
            raise ValueError("El monto no puede ser 0")
        self._monto = float(valor)

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("La fecha no puede estar vacía")
        self._fecha = valor

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, valor):
        estados_validos = ["Procesando", "Finalizado", "Cancelado",]
        if valor not in estados_validos:
            raise ValueError(f"Estado debe ser un estado válido: {estados_validos}")
        self._estado = valor
