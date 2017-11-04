# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuPrincipal.ui'
#
# Created: Sat Nov 04 12:08:27 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

#---------------------------------------------------
#-------------AGREGADO #1 IMPORTACIONES-------------
#---------------------------------------------------
import os
import webbrowser
import time
import images_rc
import threading

from PyQt4.QtCore import QFileInfo
from PyQt4.QtGui import *

from apriori import EjecutarCorrida, obtenerDatos
from funciones import generar_restricciones
from clasesUI import WAcercaDe


RUTA_BASE = os.path.dirname(os.path.dirname(__file__))
RUTA_REGLAS = os.path.join(RUTA_BASE, 'reglas')
RUTA_AYUDA = os.path.join(RUTA_BASE, 'help')
archivo_ayuda = RUTA_AYUDA + '/index.html'
NOMBRE_ARCHIVO_REGLAS_RESTRICCIONES = 'reglas_con_restricciones'

global cant_transacc, cant_reglas
cant_transacc = 0
cant_reglas = 0
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
        MainWindow.resize(1117, 736)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1117, 736))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/regla.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_salir = QtGui.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(980, 640, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_salir.setFont(font)
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1081, 611))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 380, 1031, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.cb_soporte = QtGui.QCheckBox(self.groupBox_3)
        self.cb_soporte.setEnabled(False)
        self.cb_soporte.setGeometry(QtCore.QRect(40, 40, 101, 20))
        self.cb_soporte.setCheckable(True)
        self.cb_soporte.setChecked(True)
        self.cb_soporte.setObjectName(_fromUtf8("cb_soporte"))
        self.cb_confianza = QtGui.QCheckBox(self.groupBox_3)
        self.cb_confianza.setEnabled(False)
        self.cb_confianza.setGeometry(QtCore.QRect(210, 40, 111, 20))
        self.cb_confianza.setChecked(True)
        self.cb_confianza.setObjectName(_fromUtf8("cb_confianza"))
        self.cb_sustentacion = QtGui.QCheckBox(self.groupBox_3)
        self.cb_sustentacion.setGeometry(QtCore.QRect(390, 40, 161, 20))
        self.cb_sustentacion.setObjectName(_fromUtf8("cb_sustentacion"))
        self.cb_lift = QtGui.QCheckBox(self.groupBox_3)
        self.cb_lift.setGeometry(QtCore.QRect(560, 40, 191, 20))
        self.cb_lift.setObjectName(_fromUtf8("cb_lift"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 230, 1041, 121))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.cb_min_consecuentes = QtGui.QCheckBox(self.groupBox_4)
        self.cb_min_consecuentes.setGeometry(QtCore.QRect(80, 70, 221, 20))
        self.cb_min_consecuentes.setObjectName(_fromUtf8("cb_min_consecuentes"))
        self.sb_min_consecuentes = QtGui.QSpinBox(self.groupBox_4)
        self.sb_min_consecuentes.setEnabled(False)
        self.sb_min_consecuentes.setGeometry(QtCore.QRect(300, 70, 61, 22))
        self.sb_min_consecuentes.setMinimum(1)
        self.sb_min_consecuentes.setProperty("value", 1)
        self.sb_min_consecuentes.setObjectName(_fromUtf8("sb_min_consecuentes"))
        self.cb_min_antecedentes = QtGui.QCheckBox(self.groupBox_4)
        self.cb_min_antecedentes.setGeometry(QtCore.QRect(80, 30, 231, 20))
        self.cb_min_antecedentes.setObjectName(_fromUtf8("cb_min_antecedentes"))
        self.sb_min_antecedentes = QtGui.QSpinBox(self.groupBox_4)
        self.sb_min_antecedentes.setEnabled(False)
        self.sb_min_antecedentes.setGeometry(QtCore.QRect(300, 30, 61, 22))
        self.sb_min_antecedentes.setMinimum(1)
        self.sb_min_antecedentes.setProperty("value", 1)
        self.sb_min_antecedentes.setObjectName(_fromUtf8("sb_min_antecedentes"))
        self.sb_max_consecuentes = QtGui.QSpinBox(self.tab)
        self.sb_max_consecuentes.setEnabled(False)
        self.sb_max_consecuentes.setGeometry(QtCore.QRect(700, 300, 61, 22))
        self.sb_max_consecuentes.setMinimum(1)
        self.sb_max_consecuentes.setProperty("value", 5)
        self.sb_max_consecuentes.setObjectName(_fromUtf8("sb_max_consecuentes"))
        self.cb_max_antecedentes = QtGui.QCheckBox(self.tab)
        self.cb_max_antecedentes.setGeometry(QtCore.QRect(480, 260, 231, 20))
        self.cb_max_antecedentes.setObjectName(_fromUtf8("cb_max_antecedentes"))
        self.cb_max_consecuentes = QtGui.QCheckBox(self.tab)
        self.cb_max_consecuentes.setGeometry(QtCore.QRect(480, 300, 221, 20))
        self.cb_max_consecuentes.setObjectName(_fromUtf8("cb_max_consecuentes"))
        self.sb_max_antecedentes = QtGui.QSpinBox(self.tab)
        self.sb_max_antecedentes.setEnabled(False)
        self.sb_max_antecedentes.setGeometry(QtCore.QRect(700, 260, 61, 22))
        self.sb_max_antecedentes.setMinimum(1)
        self.sb_max_antecedentes.setProperty("value", 5)
        self.sb_max_antecedentes.setObjectName(_fromUtf8("sb_max_antecedentes"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 1041, 191))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.l_archivo = QtGui.QLabel(self.groupBox)
        self.l_archivo.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.l_archivo.setObjectName(_fromUtf8("l_archivo"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 80, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.l_soporte = QtGui.QLabel(self.groupBox)
        self.l_soporte.setGeometry(QtCore.QRect(70, 80, 101, 20))
        self.l_soporte.setObjectName(_fromUtf8("l_soporte"))
        self.dsb_soporte = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_soporte.setGeometry(QtCore.QRect(190, 70, 81, 31))
        self.dsb_soporte.setMaximum(100.0)
        self.dsb_soporte.setProperty("value", 30.0)
        self.dsb_soporte.setObjectName(_fromUtf8("dsb_soporte"))
        self.dsb_confianza = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_confianza.setGeometry(QtCore.QRect(410, 70, 81, 31))
        self.dsb_confianza.setMaximum(100.0)
        self.dsb_confianza.setProperty("value", 80.0)
        self.dsb_confianza.setObjectName(_fromUtf8("dsb_confianza"))
        self.btn_examinar = QtGui.QPushButton(self.groupBox)
        self.btn_examinar.setGeometry(QtCore.QRect(720, 30, 101, 31))
        self.btn_examinar.setObjectName(_fromUtf8("btn_examinar"))
        self.le_examinar = QtGui.QLineEdit(self.groupBox)
        self.le_examinar.setGeometry(QtCore.QRect(150, 31, 561, 31))
        self.le_examinar.setText(_fromUtf8(""))
        self.le_examinar.setPlaceholderText(_fromUtf8(""))
        self.le_examinar.setObjectName(_fromUtf8("le_examinar"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(20, 110, 1001, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.barra_progreso = QtGui.QProgressBar(self.groupBox)
        self.barra_progreso.setEnabled(True)
        self.barra_progreso.setGeometry(QtCore.QRect(20, 140, 801, 23))
        self.barra_progreso.setMinimum(0)
        self.barra_progreso.setProperty("value", 0)
        self.barra_progreso.setTextVisible(True)
        self.barra_progreso.setObjectName(_fromUtf8("barra_progreso"))
        self.btn_procesar = QtGui.QPushButton(self.tab)
        self.btn_procesar.setGeometry(QtCore.QRect(940, 520, 101, 41))
        self.btn_procesar.setObjectName(_fromUtf8("btn_procesar"))
        self.btn_detener = QtGui.QPushButton(self.tab)
        self.btn_detener.setGeometry(QtCore.QRect(810, 520, 101, 41))
        self.btn_detener.setObjectName(_fromUtf8("btn_detener"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 1041, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 30, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.le_cant_transacciones = QtGui.QLineEdit(self.groupBox_2)
        self.le_cant_transacciones.setEnabled(True)
        self.le_cant_transacciones.setGeometry(QtCore.QRect(270, 30, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cant_transacciones.setFont(font)
        self.le_cant_transacciones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_cant_transacciones.setReadOnly(True)
        self.le_cant_transacciones.setObjectName(_fromUtf8("le_cant_transacciones"))
        self.le_cant_productos = QtGui.QLineEdit(self.groupBox_2)
        self.le_cant_productos.setEnabled(True)
        self.le_cant_productos.setGeometry(QtCore.QRect(270, 60, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cant_productos.setFont(font)
        self.le_cant_productos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_cant_productos.setEchoMode(QtGui.QLineEdit.Normal)
        self.le_cant_productos.setReadOnly(True)
        self.le_cant_productos.setPlaceholderText(_fromUtf8(""))
        self.le_cant_productos.setObjectName(_fromUtf8("le_cant_productos"))
        self.btn_ver_reglas = QtGui.QPushButton(self.groupBox_2)
        self.btn_ver_reglas.setEnabled(True)
        self.btn_ver_reglas.setGeometry(QtCore.QRect(850, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_ver_reglas.setFont(font)
        self.btn_ver_reglas.setMouseTracking(False)
        self.btn_ver_reglas.setStyleSheet(_fromUtf8(""))
        self.btn_ver_reglas.setInputMethodHints(QtCore.Qt.ImhNone)
        self.btn_ver_reglas.setAutoDefault(False)
        self.btn_ver_reglas.setDefault(False)
        self.btn_ver_reglas.setFlat(False)
        self.btn_ver_reglas.setObjectName(_fromUtf8("btn_ver_reglas"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(390, 30, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.le_cant_reglas = QtGui.QLineEdit(self.groupBox_2)
        self.le_cant_reglas.setEnabled(True)
        self.le_cant_reglas.setGeometry(QtCore.QRect(650, 30, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cant_reglas.setFont(font)
        self.le_cant_reglas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_cant_reglas.setReadOnly(True)
        self.le_cant_reglas.setObjectName(_fromUtf8("le_cant_reglas"))
        self.tw_rules = QtGui.QTableWidget(self.tab_3)
        self.tw_rules.setGeometry(QtCore.QRect(10, 140, 1061, 291))
        self.tw_rules.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tw_rules.setColumnCount(4)
        self.tw_rules.setObjectName(_fromUtf8("tw_rules"))
        self.tw_rules.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tw_rules.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_rules.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_rules.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_rules.setHorizontalHeaderItem(3, item)
        self.te_observaciones = QtGui.QTextEdit(self.tab_3)
        self.te_observaciones.setGeometry(QtCore.QRect(10, 470, 1061, 101))
        self.te_observaciones.setObjectName(_fromUtf8("te_observaciones"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 450, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cb_aplicar_restricc = QtGui.QCheckBox(self.tab_3)
        self.cb_aplicar_restricc.setGeometry(QtCore.QRect(890, 440, 181, 20))
        self.cb_aplicar_restricc.setObjectName(_fromUtf8("cb_aplicar_restricc"))
        self.l_titulo = QtGui.QLabel(self.tab_3)
        self.l_titulo.setGeometry(QtCore.QRect(20, 110, 1041, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l_titulo.setFont(font)
        self.l_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_titulo.setObjectName(_fromUtf8("l_titulo"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionSalir.setFont(font)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionDesde_Archivo = QtGui.QAction(MainWindow)
        self.actionDesde_Archivo.setObjectName(_fromUtf8("actionDesde_Archivo"))
        self.actionIngreso_Manual = QtGui.QAction(MainWindow)
        self.actionIngreso_Manual.setObjectName(_fromUtf8("actionIngreso_Manual"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setCheckable(False)
        self.actionReset.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionReset.setFont(font)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.menuInicio.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionInstrucciones_de_Uso)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuInicio.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())


        #---------------------------------------------
        #--------AGREGADO #4 INICIALIZACIONES#--------
        #---------------------------------------------
        MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

        #self.tw_rules.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        #self.tw_rules.resizeColumnsToContents()
        self.tw_rules.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #header = self.table.horizontalHeader()
        #header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)


        self.barra_progreso.hide()
        self.btn_ver_reglas.hide()
        #--------------------FIN #4-------------------

        #---------------------------------------------
        #-------------AGREGADO #5 EVENTOS-------------
        #---------------------------------------------
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_salir, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.btn_examinar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.abrir)
        QtCore.QObject.connect(self.btn_procesar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.procesar)
        QtCore.QObject.connect(self.cb_min_consecuentes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ckeckStatus)
        QtCore.QObject.connect(self.cb_min_antecedentes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ckeckStatus)
        QtCore.QObject.connect(self.cb_max_antecedentes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ckeckStatus)
        QtCore.QObject.connect(self.cb_max_consecuentes, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ckeckStatus)

        QtCore.QObject.connect(self.cb_aplicar_restricc, QtCore.SIGNAL(_fromUtf8("clicked()")), self.mostrar_restricciones)

        QtCore.QObject.connect(self.btn_ver_reglas, QtCore.SIGNAL(_fromUtf8("clicked()")), self.obtenerReglas)

        QtCore.QObject.connect(self.actionAcerca_de, QtCore.SIGNAL(_fromUtf8("triggered()")), self.showAcercaDe)
        QtCore.QObject.connect(self.actionInstrucciones_de_Uso, QtCore.SIGNAL(_fromUtf8("triggered()")), self.abrirAyuda)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #-------------FIN #5-------------


        MainWindow.setTabOrder(self.tabWidget, self.le_examinar)
        MainWindow.setTabOrder(self.le_examinar, self.btn_examinar)
        MainWindow.setTabOrder(self.btn_examinar, self.dsb_soporte)
        MainWindow.setTabOrder(self.dsb_soporte, self.dsb_confianza)
        MainWindow.setTabOrder(self.dsb_confianza, self.cb_min_antecedentes)
        MainWindow.setTabOrder(self.cb_min_antecedentes, self.sb_min_antecedentes)
        MainWindow.setTabOrder(self.sb_min_antecedentes, self.cb_max_antecedentes)
        MainWindow.setTabOrder(self.cb_max_antecedentes, self.sb_max_antecedentes)
        MainWindow.setTabOrder(self.sb_max_antecedentes, self.cb_min_consecuentes)
        MainWindow.setTabOrder(self.cb_min_consecuentes, self.sb_min_consecuentes)
        MainWindow.setTabOrder(self.sb_min_consecuentes, self.cb_max_consecuentes)
        MainWindow.setTabOrder(self.cb_max_consecuentes, self.sb_max_consecuentes)
        MainWindow.setTabOrder(self.sb_max_consecuentes, self.cb_soporte)
        MainWindow.setTabOrder(self.cb_soporte, self.cb_confianza)
        MainWindow.setTabOrder(self.cb_confianza, self.cb_sustentacion)
        MainWindow.setTabOrder(self.cb_sustentacion, self.cb_lift)
        MainWindow.setTabOrder(self.cb_lift, self.btn_procesar)
        MainWindow.setTabOrder(self.btn_procesar, self.btn_ver_reglas)
        MainWindow.setTabOrder(self.btn_ver_reglas, self.le_cant_transacciones)
        MainWindow.setTabOrder(self.le_cant_transacciones, self.le_cant_reglas)
        MainWindow.setTabOrder(self.le_cant_reglas, self.le_cant_productos)
        MainWindow.setTabOrder(self.le_cant_productos, self.tw_rules)
        MainWindow.setTabOrder(self.tw_rules, self.cb_aplicar_restricc)
        MainWindow.setTabOrder(self.cb_aplicar_restricc, self.te_observaciones)
        MainWindow.setTabOrder(self.te_observaciones, self.btn_salir)
        MainWindow.setTabOrder(self.btn_salir, self.btn_detener)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AppRules", None))
        self.btn_salir.setToolTip(_translate("MainWindow", "<html><head/><body><p>Salir de la Aplicacion</p></body></html>", None))
        self.btn_salir.setText(_translate("MainWindow", "Salir", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Parametros de Poda", None))
        self.cb_soporte.setText(_translate("MainWindow", "Soporte", None))
        self.cb_confianza.setText(_translate("MainWindow", "Confianza", None))
        self.cb_sustentacion.setText(_translate("MainWindow", "Conviccion ", None))
        self.cb_lift.setText(_translate("MainWindow", "Sustentacion (Lift)", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Restriciones", None))
        self.cb_min_consecuentes.setText(_translate("MainWindow", "Minimo de Consecuentes:", None))
        self.cb_min_antecedentes.setText(_translate("MainWindow", "Minimo de Antecedentes:", None))
        self.cb_max_antecedentes.setText(_translate("MainWindow", "Maximo de Antecedentes:", None))
        self.cb_max_consecuentes.setText(_translate("MainWindow", "Maximo de Consecuentes:", None))
        self.groupBox.setTitle(_translate("MainWindow", "Parametros", None))
        self.l_archivo.setText(_translate("MainWindow", "Archivo:", None))
        self.label_2.setText(_translate("MainWindow", "Confianza (%):", None))
        self.l_soporte.setText(_translate("MainWindow", "Soporte (%):", None))
        self.btn_examinar.setText(_translate("MainWindow", "Examinar", None))
        self.btn_procesar.setText(_translate("MainWindow", "Procesar", None))
        self.btn_detener.setText(_translate("MainWindow", "Detener", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Parametros Generales", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Resultados Parciales", None))
        self.label.setText(_translate("MainWindow", "Cantidad de Transacciones:", None))
        self.label_3.setText(_translate("MainWindow", "Cantidad de Items:", None))
        self.le_cant_transacciones.setText(_translate("MainWindow", "0", None))
        self.le_cant_productos.setText(_translate("MainWindow", "0", None))
        self.btn_ver_reglas.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ver Reglas Generadas</p></body></html>", None))
        self.btn_ver_reglas.setText(_translate("MainWindow", "Ver Reglas", None))
        self.label_5.setText(_translate("MainWindow", "Cantidad de Reglas Generadas:", None))
        self.le_cant_reglas.setText(_translate("MainWindow", "0", None))
        item = self.tw_rules.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Regla", None))
        item = self.tw_rules.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Soporte", None))
        item = self.tw_rules.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Confianza", None))
        item = self.tw_rules.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Interpretacion", None))
        self.label_4.setText(_translate("MainWindow", "OBSERVACIONES:", None))
        self.cb_aplicar_restricc.setText(_translate("MainWindow", "Aplicar Restricciones", None))
        self.l_titulo.setText(_translate("MainWindow", "REGLAS SIN RESTRICCIONES", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Resultados", None))
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
        global cant_transacc, cant_reglas

        try:
            self.fichero_actual.close()
        except Exception as e:
            pass
        
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.barra_progreso.show()
        self.barra_progreso.setValue(20)
        time.sleep(0.3)
     
        confianza = float(self.dsb_confianza.value())
        soporte = float(self.dsb_soporte.value())
        self.statusbar.showMessage("Leyendo archivo...")
        self.barra_progreso.setValue(35)
        time.sleep(0.2)
        self.barra_progreso.setValue(48)
        EjecutarCorrida(self.fichero_actual, soporte, confianza) 
        
        cant_transacc, cant_prod, cant_reglas = obtenerDatos()
        self.le_cant_productos.setText(_translate("MainWindow", str(cant_prod), None))
        self.le_cant_transacciones.setText(_translate("MainWindow", str(cant_transacc), None))
        self.le_cant_reglas.setText(_translate("MainWindow", str(cant_reglas), None))
        self.barra_progreso.hide()

        self.statusbar.showMessage("Gerando Reglas...")
        self.barra_progreso.setValue(62)
        time.sleep(0.1)
        self.obtenerReglas()

        self.statusbar.showMessage("Leyendo Restricciones...")
        self.barra_progreso.setValue(75)
        time.sleep(0.1)
        
        #Obtengo Parametros de Restricciones
        conviccion = False
        lift = False
        min_anteced = False
        min_conse = False
        max_anteced = False
        max_conse = False
        valor_min_ant = long(self.sb_min_antecedentes.value())
        valor_max_ant = long(self.sb_max_antecedentes.value())
        valor_min_cons = long(self.sb_min_consecuentes.value())
        valor_max_cons = long(self.sb_max_consecuentes.value())

        if self.cb_sustentacion.isChecked():
            conviccion = True
        
        if self.cb_lift.isChecked():
            lift = True
        
        if self.cb_min_antecedentes.isChecked():
            min_anteced = True
        
        if self.cb_min_consecuentes.isChecked():
            min_conse = True
        
        if self.cb_max_antecedentes.isChecked():
            max_anteced = True
        
        if self.cb_max_consecuentes.isChecked():
            max_conse = True
        
        self.statusbar.showMessage("Genreando Restricciones...")
        generar_restricciones(conviccion, lift ,min_anteced, min_conse, max_anteced, max_conse, valor_min_ant, valor_max_ant, valor_min_cons, valor_max_cons)
        self.barra_progreso.setValue(82)
        time.sleep(0.1)
        #self.tw_rules.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        #self.tw_rules.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)

        self.barra_progreso.setValue(100)
        time.sleep(0.4)
        self.statusbar.showMessage("Gerenacion Exitosa (100%)")

        QtGui.QApplication.restoreOverrideCursor()

        self.tabWidget.setCurrentIndex(1)

    def ckeckStatus(self):
        if self.cb_min_consecuentes.isChecked():
            self.sb_min_consecuentes.setEnabled(True)
        else:
            self.sb_min_consecuentes.setEnabled(False)

        if self.cb_min_antecedentes.isChecked():
            self.sb_min_antecedentes.setEnabled(True)
        else:
            self.sb_min_antecedentes.setEnabled(False)

        if self.cb_max_consecuentes.isChecked():
            self.sb_max_consecuentes.setEnabled(True)
        else:
            self.sb_max_consecuentes.setEnabled(False)

        if self.cb_max_antecedentes.isChecked():
            self.sb_max_antecedentes.setEnabled(True)
        else:
            self.sb_max_antecedentes.setEnabled(False)

    def obtenerReglas(self):
        global cant_transacc
        self.limpiarTabla()
        
        archivo_reglas = open(RUTA_REGLAS + '/reglas' + '.dat', 'r')

        for i, linea in enumerate(archivo_reglas):
            l = linea.split()
            self.tw_rules.insertRow(i)
            print("el valor de L es: "+ str(l))
            self.tw_rules.setItem(i, 1, QtGui.QTableWidgetItem(str(format(100*(float(l[len(l)-4])/float(cant_transacc)),'.2f'))+"%"))
            self.tw_rules.setItem(i, 2, QtGui.QTableWidgetItem(str(format(float(l[len(l)-3]), '.2f'))+"%"))
            self.tw_rules.setItem(i, 3, QtGui.QTableWidgetItem("asdadasdasdasdasdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"))

            item = str()
            for k, j in enumerate(l):
                if k < len(l) - 4:
                    item = item + " " + j
                else: 
                    break;
            self.tw_rules.setItem(i, 0, QtGui.QTableWidgetItem(str(item)))

        archivo_reglas.close()

    def showAcercaDe(self):
        modal = WAcercaDe()
        modal.exec_()

    def abrirAyuda(self):
        webbrowser.open_new_tab(archivo_ayuda)

    def limpiarTabla(self):
        for i in reversed(range(self.tw_rules.rowCount())):
            self.tw_rules.removeRow(i)

    def cargar_con_restricciones(self):
        global cant_transacc
        self.limpiarTabla()

        archivo_con_restricciones= open(RUTA_REGLAS + '/' + NOMBRE_ARCHIVO_REGLAS_RESTRICCIONES + '.dat', 'r')

        for i, linea in enumerate(archivo_con_restricciones):
            l = linea.split()
            self.tw_rules.insertRow(i)
        
            self.tw_rules.setItem(i, 1, QtGui.QTableWidgetItem(str(format(100*float(l[len(l) - 4])/float(cant_transacc),'.2f'))+"%"))
            self.tw_rules.setItem(i, 2, QtGui.QTableWidgetItem(str(format(float(l[len(l) - 3]), '.2f'))+"%"))
            self.tw_rules.setItem(i, 3, QtGui.QTableWidgetItem("asdadasdasdasdasdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"))

            item = str()
            for k, j in enumerate(l):
                if k < len(l) - 4:
                    item = item + " " + j
                else: 
                    break;
            self.tw_rules.setItem(i, 0, QtGui.QTableWidgetItem(str(item)))

        archivo_con_restricciones.close()

    def mostrar_restricciones(self):
        self.limpiarTabla()

        if self.cb_aplicar_restricc.isChecked():
            self.cargar_con_restricciones()
            self.l_titulo.setText(_translate("MainWindow", "REGLAS CON RESTRICCIONES", None))
    
        else:
            self.obtenerReglas()
            self.l_titulo.setText(_translate("MainWindow", "REGLAS SIN RESTRICCIONES", None))

        

    #--------------------FIN #6---------------------
