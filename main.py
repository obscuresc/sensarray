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
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import serial

class GroupBox(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("GroupBox")
        layout = QGridLayout()
        self.setLayout(layout)

        groupbox = QGroupBox("GroupBox Example")
        groupbox.setCheckable(True)
        layout.addWidget(groupbox)

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)

        radiobutton = QRadioButton("RadioButton 1")
        vbox.addWidget(radiobutton)

        radiobutton = QRadioButton("RadioButton 2")
        vbox.addWidget(radiobutton)

        radiobutton = QRadioButton("RadioButton 3")
        vbox.addWidget(radiobutton)

        radiobutton = QRadioButton("RadioButton 4")
        vbox.addWidget(radiobutton)

def buttonStartBehaviour():

    msgBox = QMessageBox()
    msgBox.setWindowTitle("Start Connection")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Connection has been started.")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('Ok clicked')

def buttonSaveBehaviour():

    msgBox = QMessageBox()
    msgBox.setWindowTitle("Start Connection")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Connection has been started.")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

def window():

    # qt init
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setGeometry(50, 50, 320, 320)
    widget.setWindowTitle("Sensarray")
    vbLayout = QVBoxLayout()
    widget.setLayout(vbLayout)

    ### serial settings groupbox
    gbSerial = QGroupBox("Serial Settings")
    glSerial = QGridLayout()
    gbSerial.setLayout(glSerial)

    # port name
    lPortName = QLabel()
    lPortName.setText("Port Name:")
    glSerial.addWidget(lPortName, 0, 0)

    # port combo
    cbPorts = QComboBox()
    cbPorts.addItem('COM1')
    cbPorts.addItem('COM2')
    cbPorts.addItem('COM3')
    glSerial.addWidget(cbPorts, 0, 1)

    # baud rate
    lBaudRate = QLabel()
    lBaudRate.setText("Baud Rate:")
    glSerial.addWidget(lBaudRate, 1, 0)

    # baud combo
    cbBaudRate = QComboBox()
    cbBaudRate.addItem('9600')
    cbBaudRate.addItem('19200')
    cbBaudRate.addItem('38400')
    cbBaudRate.addItem('57600')
    cbBaudRate.addItem('115200')
    glSerial.addWidget(cbBaudRate, 1, 1)

    # data bits
    lDataBits = QLabel()
    lDataBits.setText('Data Bits:')
    glSerial.addWidget(lDataBits, 2, 0)

    # data bits QComboBox
    cbDataBits = QComboBox()
    cbDataBits.addItem('8')
    cbDataBits.addItem('7')
    glSerial.addWidget(cbDataBits, 2, 1)

    # parity
    lParity = QLabel()
    lParity.setText('Parity:')
    glSerial.addWidget(lParity, 3, 0)

    # parity combo
    cbParity = QComboBox()
    cbParity.addItem('None')
    cbParity.addItem('Even')
    cbParity.addItem('Odd')
    glSerial.addWidget(cbParity, 3, 1)

    # stop bits
    lStopBits = QLabel()
    lStopBits.setText('Stop Bits:')
    glSerial.addWidget(lStopBits, 4, 0)

    # stop bits combo
    cbStopBits = QComboBox()
    cbStopBits.addItem('One')
    cbStopBits.addItem('Two')
    cbStopBits.addItem('None')
    glSerial.addWidget(cbStopBits, 4, 1)

    # add items
    vbLayout.addWidget(gbSerial)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
