from PyQt4 import QtGui
from mycritic import *
from mycritic_search import *

Ui_SearchWindow

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    SearchWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    uis = Ui_SearchWindow()
    ui.setupUi(MainWindow)
    uis.setupUi(SearchWindow)
    ui.pushButton.clicked.connect(SearchWindow.show)
    MainWindow.show()
    sys.exit(app.exec_())
