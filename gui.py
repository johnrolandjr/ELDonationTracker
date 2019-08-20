#should change from line edits to labels

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from PyQt5 import QtCore

from PyQt5.QtCore import Qt, pyqtSignal #need Qt?

import design, sys, threading

import extralifedonations, call_tracker, call_settings, readparticipantconf

class ELDonationGUI(QMainWindow, design.Ui_MainWindow):
    
    def __init__(self):
        # Super allows us to access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        
        #timer to update the main text
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.setInterval(5000) #milliseconds
        self.timer.timeout.connect(self.getsomeText) 
        self.timer.start()
        
        #instantiate the tracker so we can send signals
        self.tracker = call_tracker.MyForm()
        
        #Connecting all the buttons to methods
        self.SettingsButton.clicked.connect(self.callSettings)
        self.TrackerButton.clicked.connect(self.callTracker)
        self.ProgressBarButton.clicked.connect(self.deadbuton)
        self.RefreshButton.clicked.connect(self.getsomeText)
        self.TestAlertButton.clicked.connect(self.tracker.loadAndUnload)
        self.pushButtonRun.clicked.connect(self.runbutton)
        self.pushButtonStop.clicked.connect(self.stopbutton)
        
    
    def callTracker(self):
        self.tracker.show()
        
    def callSettings(self):
        call_settings.main()
    
    #this is used for buttons that I haven't yet implemented
    def deadbuton(self):
        print("not working yet")
    
    def readFiles(self, folders, files):
        try:
            f = open(f'{folders}/{files}', 'r') 
            text=f.read()
            f.close()
            return text
        except:
            print("file does not exist. Did you update the settings?")
    
    def getsomeText(self):
        # For next refactoring, will use dict to make this just work as a loop
        folders = readparticipantconf.textfolderOnly()
        
        self.RecentDonations.setPlainText(self.readFiles(folders,'last5DonorNameAmts.txt'))
        self.LastDonation.setPlainText(self.readFiles(folders,'LastDonorNameAmnt.txt'))
        self.TopDonation.setPlainText(self.readFiles(folders,'TopDonorNameAmnt.txt'))
        self.TotalRaised.setPlainText(self.readFiles(folders,'totalRaised.txt'))
        self.TotalNumDonations.setPlainText(self.readFiles(folders,'numDonations.txt'))
        self.Goal.setPlainText(self.readFiles(folders,'goal.txt'))
        self.AvgDonation.setPlainText(self.readFiles(folders,'averageDonation.txt'))
    
    def runbutton(self):
        print("run button")
        #need to add some code to keep it from starting more than one thread. 
        self.thread1=donationGrabber()
        self.thread1.start()
        
    def stopbutton(self):
        self.thread1.stop() 

class donationGrabber (threading.Thread):
    counter = 0
    def __init__(self):
        threading.Thread.__init__(self)
        self.counter=0
    def run(self):
        print("Starting " + self.name)
        self.p = extralifedonations.Participant()
        self.p.run()
    def stop(self):
        self.p.stop()

def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = ELDonationGUI()                 # We set the form to be our ELDonationGUI (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
