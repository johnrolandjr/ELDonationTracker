import extralifedonations

def writetofile(info,filename):
    "Handles all the file writes"
    f = open(extralifedonations.textFolder+filename, 'w')
    f.write(info)
    f.close
    

def readfromfile(filename):
    f = open(extralifedonations.textFolder+filename, 'r')
    if f.mode == 'r':
        return f.read()
    f.close
    
class tracker():
    def __init__(self):
        page = "<HTML><HEAD><meta http-equiv='refresh' content='15'></HEAD><BODY></BODY></HTML>"
        writetofile(page, "tracker.html")

    def updatetrackerwithdonation(self):
        page = "<HTML><HEAD><meta http-equiv='refresh' content='15'></HEAD><BODY><h1>New donation from %s</h1> </BODY></HTML>" % readfromfile("LastDonorNameAmnt.txt")
        writetofile(page, "tracker.html")


    def updatetrackerafterdonation(self):
        page = "<HTML><HEAD><meta http-equiv='refresh' content='15'></HEAD><BODY></BODY></HTML>"
        writetofile(page, "tracker.html")

class MainPage():
    def __init__(self):
    page = "<HTML><HEAD><meta http-equiv='refresh' content='15'></HEAD><BODY></BODY></HTML>"
    writetofile(page, "mainpage.html")
    
    def updatemainpage(self):
        
    
    
if __name__=="__main__":
    tracker1 = tracker()
    
