from PySide2.QtWidgets import  *
from PySide2.QtGui import *

class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IMH")
        self.layout = QGridLayout()
        self.label = QLabel("Laissez un commentaire")
        self.Text = QTextEdit()
        self.button = QPushButton("Sucess")

        self.button2 = QPushButton("Cancel")


        self.layout.addWidget(self.label,0,1,1,2)
        self.layout.addWidget(self.Text,1,1,1,2)

        self.layout.addWidget(self.button,2,1,1,1)
        self.layout.addWidget(self.button2,2,2,1,1)

        self.setLayout(self.layout)
        

if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()

