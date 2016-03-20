from PyQt4 import QtGui
from mycritic import *
from mycritic_search import *
from search import *
import urllib.request

class RouterClass:
    def populateLabels():
        text = uis.lineEdit.text()
        query = main(text)
        uis.label_6.setText(query[0][1])
        uis.label_7.setText("Id: " + str(query[0][0]))
        
        url = "https://image.tmdb.org/t/p/w185" + query[0][2]
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        uis.label_2.setScaledContents(True)
        uis.label_2.setPixmap(QtGui.QPixmap(image))
        
        uis.label_8.setText(query[1][1])
        uis.label_9.setText("Id: " + str(query[1][0]))
        
        url = "https://image.tmdb.org/t/p/w185" + query[1][2]
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        uis.label_3.setScaledContents(True)
        uis.label_3.setPixmap(QtGui.QPixmap(image))
        
        uis.label_10.setText(query[2][1])
        uis.label_11.setText("Id: " + str(query[2][0]))
        
        url = "https://image.tmdb.org/t/p/w185" + query[2][2]
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        uis.label_4.setScaledContents(True)
        uis.label_4.setPixmap(QtGui.QPixmap(image))
        
        uis.label_12.setText(query[3][1])
        uis.label_13.setText("Id: " + str(query[3][0]))
        
        url = "https://image.tmdb.org/t/p/w185" + query[3][2]
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        uis.label_5.setScaledContents(True)
        uis.label_5.setPixmap(QtGui.QPixmap(image))
        
        print(query)

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
    uis.pushButton.clicked.connect(RouterClass.populateLabels)
    MainWindow.show()
    sys.exit(app.exec_())
