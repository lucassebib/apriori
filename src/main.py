import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from UiMenuPrincipal import Ui_MainWindow as MenuPrincipal

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class WMenuPrincipal(QtGui.QMainWindow):
	
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		
		self.ventana = MenuPrincipal()
		self.ventana.setupUi(self)

def main():
	app =QtGui.QApplication(sys.argv)
	ventana = WMenuPrincipal()
	ventana.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()	