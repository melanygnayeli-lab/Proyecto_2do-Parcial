# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(527, 568)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblBuscar = QLabel(self.centralwidget)
        self.lblBuscar.setObjectName(u"lblBuscar")
        self.lblBuscar.setGeometry(QRect(50, 30, 111, 16))
        self.TxTBuscar = QLineEdit(self.centralwidget)
        self.TxTBuscar.setObjectName(u"TxTBuscar")
        self.TxTBuscar.setGeometry(QRect(210, 20, 141, 31))
        self.TxTBuscar.setMaxLength(10)
        self.lblMonto = QLabel(self.centralwidget)
        self.lblMonto.setObjectName(u"lblMonto")
        self.lblMonto.setGeometry(QRect(110, 80, 71, 16))
        self.TxTMonto = QLineEdit(self.centralwidget)
        self.TxTMonto.setObjectName(u"TxTMonto")
        self.TxTMonto.setGeometry(QRect(210, 70, 141, 31))
        self.TxTMonto.setMaxLength(15)
        self.lblFecha = QLabel(self.centralwidget)
        self.lblFecha.setObjectName(u"lblFecha")
        self.lblFecha.setGeometry(QRect(110, 130, 71, 16))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(210, 120, 141, 31))
        self.lblEstado = QLabel(self.centralwidget)
        self.lblEstado.setObjectName(u"lblEstado")
        self.lblEstado.setGeometry(QRect(110, 180, 61, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 170, 141, 31))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 220, 341, 201))
        self.lblCedula = QLabel(self.groupBox)
        self.lblCedula.setObjectName(u"lblCedula")
        self.lblCedula.setGeometry(QRect(60, 40, 71, 16))
        self.TxTCedula = QLineEdit(self.groupBox)
        self.TxTCedula.setObjectName(u"TxTCedula")
        self.TxTCedula.setGeometry(QRect(160, 29, 151, 31))
        self.TxTCedula.setMaxLength(10)
        self.lblNombres = QLabel(self.groupBox)
        self.lblNombres.setObjectName(u"lblNombres")
        self.lblNombres.setGeometry(QRect(50, 90, 61, 16))
        self.TxTNombres = QLineEdit(self.groupBox)
        self.TxTNombres.setObjectName(u"TxTNombres")
        self.TxTNombres.setGeometry(QRect(160, 80, 151, 31))
        self.TxTNombres.setMaxLength(60)
        self.lblApellidos = QLabel(self.groupBox)
        self.lblApellidos.setObjectName(u"lblApellidos")
        self.lblApellidos.setGeometry(QRect(50, 140, 61, 16))
        self.TxTApellidos = QLineEdit(self.groupBox)
        self.TxTApellidos.setObjectName(u"TxTApellidos")
        self.TxTApellidos.setGeometry(QRect(160, 130, 151, 31))
        self.TxTApellidos.setMaxLength(60)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(40, 460, 121, 41))
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(260, 460, 121, 41))
        self.btnBuscar = QPushButton(self.centralwidget)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(390, 20, 91, 31))
        self.btnCrear = QPushButton(self.centralwidget)
        self.btnCrear.setObjectName(u"btnCrear")
        self.btnCrear.setGeometry(QRect(390, 70, 91, 31))
        self.btnActualizar = QPushButton(self.centralwidget)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(390, 120, 91, 31))
        self.btnEliminar = QPushButton(self.centralwidget)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(390, 170, 91, 31))
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 527, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"SISTEMA BANCARIO", None))
        self.lblBuscar.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00f3digo Transacci\u00f3n", None))
        self.lblMonto.setText(QCoreApplication.translate("vtnPrincipal", u"Monto", None))
        self.lblFecha.setText(QCoreApplication.translate("vtnPrincipal", u"Fecha", None))
        self.lblEstado.setText(QCoreApplication.translate("vtnPrincipal", u"Estado", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Procesando", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Finalizado", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Cancelado", None))

        self.groupBox.setTitle(QCoreApplication.translate("vtnPrincipal", u"GroupBox", None))
        self.lblCedula.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula", None))
        self.lblNombres.setText(QCoreApplication.translate("vtnPrincipal", u"Nombres", None))
        self.lblApellidos.setText(QCoreApplication.translate("vtnPrincipal", u"Apellidos", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.btnBuscar.setText(QCoreApplication.translate("vtnPrincipal", u"Buscar", None))
        self.btnCrear.setText(QCoreApplication.translate("vtnPrincipal", u"Crear", None))
        self.btnActualizar.setText(QCoreApplication.translate("vtnPrincipal", u"Actualizar", None))
        self.btnEliminar.setText(QCoreApplication.translate("vtnPrincipal", u"Eliminar", None))
    # retranslateUi

