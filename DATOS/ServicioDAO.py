# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN

from datetime import datetime
from DATOS.conexion import Conexion
from DOMINIO.Servicio import ServicioBancario
from DOMINIO.cliente import Cliente
import pyodbc as bd


class ServicioBancarioDAO:
    # Consultas SQL
    _INSERT = ("INSERT INTO Transacciones (IdTransaccion, Monto, FechaTramite, Estado, IdCliente,"
               "Nombres, Apellidos)"
               "VALUES (?, ?, ?, ?, ?, ?, ?)")
    _UPDATE = ("UPDATE Transacciones SET Monto=?, FechaTramite=?, Estado=?, IdCliente=?, Nombres=?, Apellidos=?"
               " WHERE IdTransaccion=?")
    _DELETE = "DELETE FROM Transacciones WHERE IdTransaccion=?"
    _SELECT = "SELECT * FROM Transacciones WHERE IdTransaccion=?"

    @classmethod
    def insertar_servicio(cls, servicio):
        try:
            if cls.existe_id_transaccion(servicio.cod_transaccion):
                return {'ejecuto': False, 'mensaje': 'El ID de Transacción ya existe.'}

            try:
                fecha = datetime.strptime(servicio.fecha, "%d/%m/%Y").strftime("%Y-%m-%d")
                with Conexion.obtenerCursor() as cursor:
                    datos = (servicio.cod_transaccion, servicio.monto, fecha, servicio.estado,
                             servicio.cliente.id, servicio.cliente.nombres, servicio.cliente.apellidos)
                    cursor.execute(cls._INSERT, datos)
                    Conexion.obtenerConexion().commit()
                    respuesta = cursor.rowcount
                    if respuesta == 1:
                        return {'ejecuto': True, 'mensaje': 'Se guardó con éxito.'}
            except bd.IntegrityError as e_bb:
                print(f"Error en el servicio: {e_bb}")
                if 'IdTransaccion' in e_bb.__str__():
                    return {'ejecuto': False, 'mensaje': 'ID Transacción ya existe.'}
                elif 'IdCliente' in e_bb.__str__():
                    return {'ejecuto': False, 'mensaje': 'Cédula cliente ya existe.'}
        except Exception as e:
            print(f"Error General: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al guardar los datos, Comunicarse con Sistemas.'}

    @classmethod
    def actualizar_servicio(cls, servicio):
        try:
            fecha = datetime.strptime(servicio.fecha, "%d/%m/%Y").strftime("%Y-%m-%d")
            with Conexion.obtenerCursor() as cursor:
                datos = (servicio.monto, fecha, servicio.estado, servicio.cliente.id,
                         servicio.cliente.nombres, servicio.cliente.apellidos, servicio.cod_transaccion)
                cursor.execute(cls._UPDATE, datos)
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Servicio actualizado con éxito.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'No se encontró el servicio para actualizar.'}
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al actualizar los datos.'}

    @classmethod
    def eliminar_servicio(cls, cod_transaccion):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._DELETE, (cod_transaccion,))
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Servicio eliminado correctamente.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'El código de transacción no existe.'}
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al intentar eliminar el servicio.'}

    @classmethod
    def seleccionar_servicio(cls, cod_transaccion):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECT, (cod_transaccion,))
                registro = cursor.fetchone()

                if registro:
                    cliente = Cliente(
                        id=registro[4],
                        nombres=registro[5],
                        apellidos=registro[6]
                    )
                    return ServicioBancario(
                        cod_transaccion=registro[0],
                        cliente=cliente,
                        monto=registro[1],
                        fecha=registro[2],
                        estado=registro[3]
                    )
                return None
        except Exception as e:
            print(f"Error al seleccionar: {e}")
            return None

    @classmethod
    def existe_id_transaccion(cls, id_transaccion):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Banco WHERE IdTransaccion = ?", (id_transaccion,))
                resultado = cursor.fetchone()
                return resultado[0] > 0
        except Exception as e:
            print(f"Error al validar existencia de ID: {e}")
            return False