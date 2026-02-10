create table Transacciones(
IdTransaccion VARCHAR(10) PRIMARY KEY,
Monto DECIMAL (15,2) NOT NULL,
FechaTramite DATE NOT NULL,
Estado VARCHAR(11) NOT NULL,
IdCliente VARCHAR(10) NOT NULL,
Nombres VARCHAR(60) NOT NULL,
Apellidos VARCHAR(60) NOT NULL
)