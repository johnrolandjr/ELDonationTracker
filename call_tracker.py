import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene, QGraphicsPixmapItem
from tracker import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtMultimedia import QSound

import readparticipantconf
import IPC


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene(self)
        self.pixmap = QtGui.QPixmap()
        self.loadimage()
        self.ui.graphicsView.setScene(self.scene)
        QSound donation("/home/ermesa/Music/Lana_Del_Rey/Serial_Killer/Lana Del Rey - Serial Killer.mp3")

        # timer to update the main text
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(20000)  # milliseconds
        self.timer.timeout.connect(self.loadAndUnload) 
        self.timer.start()

    def loadimage(self):
        self.tracker_image = readparticipantconf.trackerimage()
        self.pixmap.load(self.tracker_image)
        self.item = QGraphicsPixmapItem(self.pixmap.scaledToHeight(131))

    def loadAndUnloadTest(self):
        self.loadimage()
        self.loadElements()
        unloadtimer = QtCore.QTimer(self)
        unloadtimer.setSingleShot(True)
        unloadtimer.setInterval(5000)  # milliseconds
        unloadtimer.timeout.connect(self.unloadElements)
        unloadtimer.start()

    def loadAndUnload(self):
        IPC = "0"
        folders = readparticipantconf.textfolderOnly()
        try:
            with open(f'{folders}/trackerIPC.txt') as file:
                IPC = file.read(1)
                file.close()
        except:
            print("""tackerIPC.txt not found.
                Have you updated the settings?
                Have you hit the 'run' button?""")
        if IPC == "1":
            self.loadimage()
            self.loadElements()
            unloadtimer = QtCore.QTimer(self)
            unloadtimer.setSingleShot(True)
            unloadtimer.setInterval(5000)  # milliseconds
            unloadtimer.timeout.connect(self.unloadElements)
            unloadtimer.start()

    def loadElements(self):
        self.scene.addItem(self.item)
        # want to also play a sound
        folders = readparticipantconf.textfolderOnly()
        try:
            with open(f'{folders}/LastDonorNameAmnt.txt') as file:
                donorAndAmt = file.read()
                file.close
            self.ui.Donation_label.setText(donorAndAmt)
        except:
            self.ui.Donation_label.setText("TEST 1...2...3...")

    def unloadElements(self):
        self.scene.removeItem(self.item)
        self.ui.Donation_label.setText("")
        IPC.writeIPC("0")


def main():
    w = MyForm()
    w.exec()       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
