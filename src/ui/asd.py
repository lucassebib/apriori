# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuPrincipal.ui'
#
# Created: Sat Dec 02 20:16:25 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(884, 694)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(884, 694))
        MainWindow.setMaximumSize(QtCore.QSize(884, 694))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/regla.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn_salir = QtGui.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(780, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_salir.setFont(font)
        self.btn_salir.setObjectName(_fromUtf8("btn_salir"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 861, 591))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 310, 831, 91))
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
        self.groupBox_4.setGeometry(QtCore.QRect(10, 170, 831, 121))
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
        self.sb_max_consecuentes.setGeometry(QtCore.QRect(700, 240, 61, 22))
        self.sb_max_consecuentes.setMinimum(1)
        self.sb_max_consecuentes.setProperty("value", 5)
        self.sb_max_consecuentes.setObjectName(_fromUtf8("sb_max_consecuentes"))
        self.cb_max_antecedentes = QtGui.QCheckBox(self.tab)
        self.cb_max_antecedentes.setGeometry(QtCore.QRect(480, 200, 231, 20))
        self.cb_max_antecedentes.setObjectName(_fromUtf8("cb_max_antecedentes"))
        self.cb_max_consecuentes = QtGui.QCheckBox(self.tab)
        self.cb_max_consecuentes.setGeometry(QtCore.QRect(480, 240, 221, 20))
        self.cb_max_consecuentes.setObjectName(_fromUtf8("cb_max_consecuentes"))
        self.sb_max_antecedentes = QtGui.QSpinBox(self.tab)
        self.sb_max_antecedentes.setEnabled(False)
        self.sb_max_antecedentes.setGeometry(QtCore.QRect(700, 200, 61, 22))
        self.sb_max_antecedentes.setMinimum(1)
        self.sb_max_antecedentes.setProperty("value", 5)
        self.sb_max_antecedentes.setObjectName(_fromUtf8("sb_max_antecedentes"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 831, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.l_archivo = QtGui.QLabel(self.groupBox)
        self.l_archivo.setGeometry(QtCore.QRect(70, 30, 71, 16))
        self.l_archivo.setObjectName(_fromUtf8("l_archivo"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 70, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.l_soporte = QtGui.QLabel(self.groupBox)
        self.l_soporte.setGeometry(QtCore.QRect(70, 70, 101, 20))
        self.l_soporte.setObjectName(_fromUtf8("l_soporte"))
        self.dsb_soporte = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_soporte.setGeometry(QtCore.QRect(190, 60, 81, 31))
        self.dsb_soporte.setMaximum(100.0)
        self.dsb_soporte.setProperty("value", 30.0)
        self.dsb_soporte.setObjectName(_fromUtf8("dsb_soporte"))
        self.dsb_confianza = QtGui.QDoubleSpinBox(self.groupBox)
        self.dsb_confianza.setGeometry(QtCore.QRect(410, 60, 81, 31))
        self.dsb_confianza.setMaximum(100.0)
        self.dsb_confianza.setProperty("value", 80.0)
        self.dsb_confianza.setObjectName(_fromUtf8("dsb_confianza"))
        self.btn_examinar = QtGui.QPushButton(self.groupBox)
        self.btn_examinar.setGeometry(QtCore.QRect(720, 20, 101, 31))
        self.btn_examinar.setObjectName(_fromUtf8("btn_examinar"))
        self.le_examinar = QtGui.QLineEdit(self.groupBox)
        self.le_examinar.setGeometry(QtCore.QRect(150, 21, 561, 31))
        self.le_examinar.setText(_fromUtf8(""))
        self.le_examinar.setPlaceholderText(_fromUtf8(""))
        self.le_examinar.setObjectName(_fromUtf8("le_examinar"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(20, 90, 801, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.barra_progreso = QtGui.QProgressBar(self.groupBox)
        self.barra_progreso.setEnabled(True)
        self.barra_progreso.setGeometry(QtCore.QRect(20, 110, 801, 23))
        self.barra_progreso.setMinimum(0)
        self.barra_progreso.setProperty("value", 0)
        self.barra_progreso.setTextVisible(True)
        self.barra_progreso.setObjectName(_fromUtf8("barra_progreso"))
        self.btn_procesar = QtGui.QPushButton(self.tab)
        self.btn_procesar.setGeometry(QtCore.QRect(750, 500, 91, 31))
        self.btn_procesar.setObjectName(_fromUtf8("btn_procesar"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 831, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 30, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.le_cant_transacciones = QtGui.QLineEdit(self.groupBox_2)
        self.le_cant_transacciones.setEnabled(True)
        self.le_cant_transacciones.setGeometry(QtCore.QRect(240, 30, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_cant_transacciones.setFont(font)
        self.le_cant_transacciones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_cant_transacciones.setReadOnly(True)
        self.le_cant_transacciones.setObjectName(_fromUtf8("le_cant_transacciones"))
        self.le_cant_productos = QtGui.QLineEdit(self.groupBox_2)
        self.le_cant_productos.setEnabled(True)
        self.le_cant_productos.setGeometry(QtCore.QRect(240, 60, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_cant_productos.setFont(font)
        self.le_cant_productos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_cant_productos.setEchoMode(QtGui.QLineEdit.Normal)
        self.le_cant_productos.setReadOnly(True)
        self.le_cant_productos.setPlaceholderText(_fromUtf8(""))
        self.le_cant_productos.setObjectName(_fromUtf8("le_cant_productos"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(360, 30, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.le_cant_reglas = QtGui.QLineEdit(self.groupBox_2)
        self.le_cant_reglas.setEnabled(True)
        self.le_cant_reglas.setGeometry(QtCore.QRect(580, 30, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_cant_reglas.setFont(font)
        self.le_cant_reglas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.le_cant_reglas.setReadOnly(True)
        self.le_cant_reglas.setObjectName(_fromUtf8("le_cant_reglas"))
        self.btn_pdf = QtGui.QPushButton(self.groupBox_2)
        self.btn_pdf.setGeometry(QtCore.QRect(750, 20, 31, 41))
        self.btn_pdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pdf.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pdf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pdf.setIcon(icon1)
        self.btn_pdf.setIconSize(QtCore.QSize(40, 40))
        self.btn_pdf.setObjectName(_fromUtf8("btn_pdf"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(720, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tw_rules = QtGui.QTableWidget(self.tab_3)
        self.tw_rules.setGeometry(QtCore.QRect(10, 140, 841, 281))
        self.tw_rules.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tw_rules.setColumnCount(4)
        self.tw_rules.setObjectName(_fromUtf8("tw_rules"))
        self.tw_rules.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tw_rules.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_rules.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_rules.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tw_rules.setHorizontalHeaderItem(3, item)
        self.te_observaciones = QtGui.QTextEdit(self.tab_3)
        self.te_observaciones.setGeometry(QtCore.QRect(10, 450, 841, 101))
        self.te_observaciones.setObjectName(_fromUtf8("te_observaciones"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 430, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cb_aplicar_restricc = QtGui.QCheckBox(self.tab_3)
        self.cb_aplicar_restricc.setGeometry(QtCore.QRect(690, 420, 161, 20))
        self.cb_aplicar_restricc.setObjectName(_fromUtf8("cb_aplicar_restricc"))
        self.l_titulo = QtGui.QLabel(self.tab_3)
        self.l_titulo.setGeometry(QtCore.QRect(20, 110, 831, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.l_titulo.setFont(font)
        self.l_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.l_titulo.setObjectName(_fromUtf8("l_titulo"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 29))
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
        font.setPointSize(9)
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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.btn_salir, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.dsb_confianza, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.dsb_confianza.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
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
        MainWindow.setTabOrder(self.btn_procesar, self.le_cant_transacciones)
        MainWindow.setTabOrder(self.le_cant_transacciones, self.le_cant_reglas)
        MainWindow.setTabOrder(self.le_cant_reglas, self.le_cant_productos)
        MainWindow.setTabOrder(self.le_cant_productos, self.tw_rules)
        MainWindow.setTabOrder(self.tw_rules, self.cb_aplicar_restricc)
        MainWindow.setTabOrder(self.cb_aplicar_restricc, self.te_observaciones)
        MainWindow.setTabOrder(self.te_observaciones, self.btn_salir)

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Parametros Generales", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Resultados Parciales", None))
        self.label.setText(_translate("MainWindow", "Cantidad de Transacciones:", None))
        self.label_3.setText(_translate("MainWindow", "Cantidad de Items:", None))
        self.le_cant_transacciones.setText(_translate("MainWindow", "0", None))
        self.le_cant_productos.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "Cantidad de Reglas Generadas:", None))
        self.le_cant_reglas.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "Exportar Reglas", None))
        self.tw_rules.setSortingEnabled(True)
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

import imagenes_rc
