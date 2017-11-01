import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from UiAcercaDe import Ui_Dialog as AcercaDe

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class WAcercaDe(QtGui.QDialog):
	
	def __init__(self):
		QtGui.QDialog.__init__(self, parent=None)
		
		self.ventana = AcercaDe()
		self.ventana.setupUi(self)

