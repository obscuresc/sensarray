################################################################################
# sensarray
#
# Reads from an array of HVAC sensors, providing means to view and log
#   measurements while showing statistics of the results.
#
# https://pythonhosted.org/pyserial/shortintro.html
# https://docs.python.org/3/library/venv.html
# https://pythonbasics.org/pyqt-grid/
# 
# Jack Arney
# 11-12-2019
################################################################################


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QMessageBox, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pyserial

def buttonStartBehaviour():

    msgBox = QMessageBox()
    msgBox.setWindowTitle("Start Connection")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Connection has been started.")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('Ok clicked')

def window():

    # qt init
    app = QApplication(sys.argv)
    widget = QWidget()

    # labels show text or images
    textLabel = QLabel(widget)
    textLabel.setText("Sensarray")
    textLabel.move(110, 85)

    # start button
    buttonStartConnect = QPushButton(widget)
    buttonStartConnect.setText('Start')
    buttonStartConnect.move(64, 32)
    buttonStartConnect.clicked.connect(buttonStartBehaviour)

    # stop button
    buttonStopConnect = QPushButton(widget)
    buttonStopConnect.setText('Stop')
    buttonStopConnect.move(64, 64)

    # sensor grid
    grid = QGridLayout()


    # start position of window, and size
    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
