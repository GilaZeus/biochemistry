from PyQt5 import QtWidgets, QtCore
from logic.gui.dialogue import Ui_MainWindow
import shutil
import sys
import importlib
import chain_to_import


def open_chain(path):
    '''Help to import and open a chain.'''
    shutil.copyfile(path, 'chain_to_import.py')

def restore():
    '''Restore the file to import before closing.'''
    shutil.copyfile('logic\\chain_to_import.py', 'chain_to_import.py')
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_program)
    

    def start_program(self):
        open_chain(self.ui.lineEdit.text())
        self.ui.second.show()
        restore()

    

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            self.start_program()



 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())