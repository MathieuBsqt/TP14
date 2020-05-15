from PySide2.QtWidgets import  *
from PySide2.QtGui import *


class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IMH")
        self.setFixedSize(400,300)
        self.layout = QVBoxLayout()
        self.setWindowIcon(QIcon('fr-flag.png'))

        self.label = QLabel("Laissez un commentaire")
        self.label.setAlignment(Qt.AlignCenter)
        self.Bar=QProgressBar()
        self.Bar.setValue(50)
        self.lineEdit=QLineEdit()
        self.Button=QPushButton()
        self.Button.setToolTip('coucou')

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.Bar)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.Button)

        self.setLayout(self.layout)


if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()

