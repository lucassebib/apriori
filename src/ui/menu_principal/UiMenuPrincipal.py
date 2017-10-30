# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuPrincipal.ui'
#
# Created: Sun Oct 29 20:25:57 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

#---------------------------------------------------
#-------------AGREGADO #1 IMPORTACIONES-------------
#---------------------------------------------------
from PyQt4.QtCore import QFileInfo
from PyQt4.QtGui import *

from apriori import EjecutarCorrida
#----------------------FIN #1-----------------------

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    #-----------------------------------------------
    #-------------AGREGADO #2 VARIABLES-------------
    #-----------------------------------------------
    fichero_actual = ''
    ruta = ''
    nombre_archivo = ''
    #-------------FIN #2-------------
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(712, 636)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_ver_reglas = QtGui.QPushButton(self.centralwidget)
        self.btn_ver_reglas.setGeometry(QtCore.QRect(440, 520, 111, 41))
        self.btn_ver_reglas.setObjectName(_fromUtf8("btn_ver_reglas"))
        self.btn_salir = QtGui.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(560, 520, 101, 41))
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 601, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.l_archivo = QtGui.QLabel(self.groupBox)
        self.l_archivo.setGeometry(QtCore.QRect(70, 40, 53, 16))
        self.l_archivo.setObjectName(_fromUtf8("l_archivo"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(210, 70, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.l_soporte = QtGui.QLabel(self.groupBox)
        self.l_soporte.setGeometry(QtCore.QRect(40, 70, 91, 20))
        self.l_soporte.setObjectName(_fromUtf8("l_soporte"))
        self.btn_procesar = QtGui.QPushButton(self.groupBox)
        self.btn_procesar.setGeometry(QtCore.QRect(470, 120, 101, 41))
        self.btn_procesar.setObjectName(_fromUtf8("btn_procesar"))
        self.dsb_soporte = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_soporte.setGeometry(QtCore.QRect(130, 70, 61, 21))
        self.dsb_soporte.setObjectName(_fromUtf8("dsb_soporte"))
        self.dsb_confianza = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_confianza.setGeometry(QtCore.QRect(340, 70, 61, 21))
        self.dsb_confianza.setObjectName(_fromUtf8("dsb_confianza"))
        self.btn_examinar = QtGui.QPushButton(self.groupBox)
        self.btn_examinar.setGeometry(QtCore.QRect(470, 30, 93, 28))
        self.btn_examinar.setObjectName(_fromUtf8("btn_examinar"))
        self.le_examinar = QtGui.QLineEdit(self.groupBox)
        self.le_examinar.setGeometry(QtCore.QRect(130, 31, 281, 31))
        self.le_examinar.setText(_fromUtf8(""))
        self.le_examinar.setPlaceholderText(_fromUtf8(""))
        self.le_examinar.setObjectName(_fromUtf8("le_examinar"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(20, 100, 561, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.barra_progreso = QtGui.QProgressBar(self.groupBox)
        self.barra_progreso.setEnabled(True)
        self.barra_progreso.setGeometry(QtCore.QRect(30, 130, 431, 23))
        self.barra_progreso.setMinimum(0)
        self.barra_progreso.setProperty("value", 0)
        self.barra_progreso.setTextVisible(True)
        self.barra_progreso.setObjectName(_fromUtf8("barra_progreso"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuInicio = QtGui.QMenu(self.menubar)
        self.menuInicio.setObjectName(_fromUtf8("menuInicio"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionInstrucciones_de_Uso = QtGui.QAction(MainWindow)
        self.actionInstrucciones_de_Uso.setObjectName(_fromUtf8("actionInstrucciones_de_Uso"))
        self.actionAcerca_de = QtGui.QAction(MainWindow)
        self.actionAcerca_de.setObjectName(_fromUtf8("actionAcerca_de"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionDesde_Archivo = QtGui.QAction(MainWindow)
        self.actionDesde_Archivo.setObjectName(_fromUtf8("actionDesde_Archivo"))
        self.actionIngreso_Manual = QtGui.QAction(MainWindow)
        self.actionIngreso_Manual.setObjectName(_fromUtf8("actionIngreso_Manual"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setCheckable(False)
        self.actionReset.setEnabled(True)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.menuInicio.addAction(self.actionReset)
        self.menuInicio.addSeparator()
        self.menuInicio.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionInstrucciones_de_Uso)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        #---------------------------------------------
        #--------AGREGADO #4 INICIALIZACIONES#--------
        #---------------------------------------------
        self.barra_progreso.hide()
        #--------------------FIN #4-------------------

        #---------------------------------------------
        #-------------AGREGADO #5 EVENTOS-------------
        #---------------------------------------------
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_salir, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.btn_examinar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.abrir)
        QtCore.QObject.connect(self.btn_procesar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.procesar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #-------------FIN #5-------------

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Algoritmo Apriori", None))
        self.btn_ver_reglas.setText(_translate("MainWindow", "Ver Reglas", None))
        self.btn_salir.setText(_translate("MainWindow", "Salir", None))
        self.groupBox.setTitle(_translate("MainWindow", "Parametros", None))
        self.l_archivo.setText(_translate("MainWindow", "Archivo:", None))
        self.label_2.setText(_translate("MainWindow", "Confianza (%):", None))
        self.l_soporte.setText(_translate("MainWindow", "Soporte (%):", None))
        self.btn_procesar.setText(_translate("MainWindow", "Procesar", None))
        self.btn_examinar.setText(_translate("MainWindow", "Examinar", None))
        self.menuInicio.setTitle(_translate("MainWindow", "Inicio", None))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda", None))
        self.actionInstrucciones_de_Uso.setText(_translate("MainWindow", "Instrucciones de Uso", None))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionDesde_Archivo.setText(_translate("MainWindow", "Desde Archivo", None))
        self.actionIngreso_Manual.setText(_translate("MainWindow", "Ingreso Manual", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))

    #-----------------------------------------------
    #-------------AGREGADO #6 FUNCIONES-------------
    #-----------------------------------------------
    def abrir(self):
        nombre_fichero = QFileDialog.getOpenFileName(None, "Abrir fichero", self.ruta)
        if nombre_fichero:
            self.fichero_actual = nombre_fichero
            self.ruta = QFileInfo(nombre_fichero).path()
            self.le_examinar.setText(_translate("MainWindow", nombre_fichero, None))
            
            self.nombre_archivo = str(nombre_fichero)
            self.nombre_archivo = self.nombre_archivo.split('/')
            self.nombre_archivo = self.nombre_archivo[len(self.nombre_archivo) - 1]

    def procesar(self):
        self.barra_progreso.show()
        value = self.barra_progreso.value()
        print('parametros:')
        confianza = float(self.dsb_confianza.value())
        soporte = float(self.dsb_soporte.value())
        print(self.nombre_archivo)
        print(self.ruta)
        print(self.fichero_actual)
        print('-------------------------------')
        EjecutarCorrida(self.fichero_actual, soporte, confianza )

        while value <= 1000000:
            self.barra_progreso.setValue(value/10000)
            value = value + 1


        self.barra_progreso.hide()


    #--------------------FIN #6---------------------