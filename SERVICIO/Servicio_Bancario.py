# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN

from PySide6.QtCore import QDate
from PySide6.QtWidgets import QMainWindow, QMessageBox
from UI.vtnPrincipal import Ui_vtnPrincipal
from DATOS.ServicioDAO import ServicioBancarioDAO
from DOMINIO.Servicio import ServicioBancario
from DOMINIO.cliente import Cliente


class ServicioBancarioServicio(QMainWindow, Ui_vtnPrincipal):
    '''
    Clase que genera la lógica de los objetos de tipo ServicioBancario
    '''
    def __init__(self):
        super(ServicioBancarioServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.setCalendarPopup(True)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnCrear.clicked.connect(self.crear)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.limpiar()

    def validaciones(self):
        # Captura de datos del formulario - SERVICIO BANCARIO
        cod_transaccion = self.ui.TxTBuscar.text().strip()
        monto = self.ui.TxTMonto.text().strip()
        fecha = self.ui.dateEdit.text().strip()
        estado = self.ui.comboBox.currentText()

        # Captura de datos del formulario - CLIENTE
        cedula = self.ui.TxTCedula.text().strip()
        nombres = self.ui.TxTNombres.text().strip()
        apellidos = self.ui.TxTApellidos.text().strip()

        if cod_transaccion == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el Código de Transacción")
            return None
        elif monto == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el monto")
            return None
        else:
            try:
                monto_float = float(monto)
                if monto_float <= 0:
                    QMessageBox.warning(self, "Advertencia", "El monto debe ser mayor a 0")
                    return None
            except ValueError:
                QMessageBox.warning(self, "Advertencia", "El monto debe ser un número válido")
                return None

        if len(cedula) < 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la cédula del cliente (10 dígitos)")
            return None
        elif nombres == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar los nombres del cliente")
            return None
        elif apellidos == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar los apellidos del cliente")
            return None

        cliente = Cliente(id=cedula, nombres=nombres, apellidos=apellidos)
        return ServicioBancario(cod_transaccion=cod_transaccion, cliente=cliente,
                                monto=monto_float, fecha=fecha, estado=estado)
    def guardar(self):
        servicio = self.validaciones()
        if servicio:
            respuesta_dict = ServicioBancarioDAO.insertar_servicio(servicio)
            if respuesta_dict.get('ejecuto'):
                QMessageBox.information(self, "Éxito", respuesta_dict['mensaje'])
                self.statusBar().showMessage("Se guardó la información", 5000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', respuesta_dict['mensaje'])

    def limpiar(self):
        self.ui.TxTBuscar.clear()
        self.ui.TxTMonto.clear()
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.TxTCedula.clear()
        self.ui.TxTNombres.clear()
        self.ui.TxTApellidos.clear()

    def crear(self):
        self.limpiar()
        self.statusBar().showMessage("Campos listos para nuevo servicio.", 3000)

    def buscar(self):
        cod = self.ui.TxTBuscar.text().strip()
        if not cod:
            QMessageBox.warning(self, "Advertencia", "Ingrese un código para buscar.")
            return

        servicio = ServicioBancarioDAO.seleccionar_servicio(cod)
        if servicio:
            self.ui.TxTMonto.setText(str(servicio.monto))
            fecha_str = str(servicio.fecha)[:10]
            self.ui.dateEdit.setDate(QDate.fromString(fecha_str, "yyyy-MM-dd"))
            self.ui.comboBox.setCurrentText(servicio.estado)
            self.ui.TxTCedula.setText(servicio.cliente.id)
            self.ui.TxTNombres.setText(servicio.cliente.nombres)
            self.ui.TxTApellidos.setText(servicio.cliente.apellidos)
            self.statusBar().showMessage("Servicio cargado con éxito.", 3000)
        else:
            QMessageBox.information(self, "Búsqueda", "No se encontró el servicio.")

    def actualizar(self):
        servicio_nuevo = self.validaciones()

        if servicio_nuevo:
            servicio_existente = ServicioBancarioDAO.seleccionar_servicio(servicio_nuevo.cod_transaccion)

            if servicio_existente:
                # Confirmación del usuario mediante botones
                mensaje = f"¿Desea actualizar la información del servicio {servicio_nuevo.cod_transaccion}?"
                confirmar = QMessageBox.question(self, "Confirmar", mensaje,
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                if confirmar == QMessageBox.StandardButton.Yes:
                    # Ejecutar la actualización en el DAO
                    respuesta = ServicioBancarioDAO.actualizar_servicio(servicio_nuevo)
                    if respuesta.get('ejecuto'):
                        QMessageBox.information(self, "Éxito", "Datos actualizados correctamente.")
                        self.buscar()  # Refresca la información en pantalla
                    else:
                        QMessageBox.critical(self, "Error", respuesta.get('mensaje'))
            else:
                QMessageBox.warning(self, "Advertencia", "El código de transacción no existe en la base de datos.")

    def eliminar(self):
        cod = self.ui.TxTBuscar.text().strip()
        if not cod:
            QMessageBox.warning(self, "Advertencia", "Seleccione un servicio para eliminar.")
            return

        confirmar = QMessageBox.question(self, "Confirmar", f"¿Eliminar servicio {cod}?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirmar == QMessageBox.StandardButton.Yes:
            respuesta = ServicioBancarioDAO.eliminar_servicio(cod)
            if respuesta.get('ejecuto'):
                QMessageBox.information(self, "Éxito", respuesta.get('mensaje'))
                self.statusBar().showMessage(respuesta.get('mensaje'), 5000)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", respuesta.get('mensaje'))