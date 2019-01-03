#!/usr/bin/python3

import json
import urllib.request
import time
import unicodedata

#variables to change
ExtraLifeID=348774
textFolder="/home/ermesa/Dropbox/ELtracker/"
#textFolder="/home/ermesa/Streaming Overlays/donations/"
CurrencySymbol="$"
TeamID=None #change to TeamID=None if you aren't in a team

#create URLs
participant="http://www.extra-life.org/api/participants/"+str(ExtraLifeID)
donors="http://www.extra-life.org/api/participants/"+str(ExtraLifeID)+"/donations"
team="http://www.extra-life.org/api/teams/"+str(TeamID)

#api info at https://github.com/DonorDrive/PublicAPI


NumberofDonations = 0
NewNumberofDonations = 0

def writetofile(info,filename):
    "Handles all the file writes"
    f = open(textFolder+filename, 'w')
    f.write(info)
    f.close

def writetofiletuple(tuple):
    "Handles all the file writes"
    f = open(textFolder+tuple[1], 'w')
    f.write(tuple[0])
    f.close

#****** Participant INFO *******
def ParticpantTotalRaised(JSON):
    totalRaised=CurrencySymbol+'{:.2f}'.format(JSON['sumDonations'])
    return(totalRaised,"totalRaised.txt")

def ParticipantNumDonations(JSON):
    return(str(JSON['numDonations']), "numDonations.txt")

def ParticipantAvgDonation(JSON):
    try: 
        average = CurrencySymbol+'{:.2f}'.format(JSON['sumDonations']/JSON['numDonations'])
    except ZeroDivisionError:
        average = CurrencySymbol+'0.00'
    return(average,"averageDonation.txt")

def ParticipantGoal(JSON):
    goal=CurrencySymbol+'{:.2f}'.format(JSON['fundraisingGoal'])
    return(goal,"goal.txt")
    
def ParticipantLastDonorNameAmnt(JSON):
    try: 
        LastDonorNameAmnt=str(JSON[0]['displayName'])+" - "+CurrencySymbol+'{:.2f}'.format(JSON[0]['amount'])
    except: 
        LastDonorNameAmnt="No donors yet"
    return(LastDonorNameAmnt,"LastDonorNameAmnt.txt")

def ParticipantTopDonor(JSON):
    TopDonorIndex=0
    TopDonorNameAmnt=""
    for donor in range(0,len(JSON)):
        #need to deal with donations where they hid the donationAmount
        if JSON[donor]['amount'] == None:
            print("skipping a null donation amount")
        elif int(JSON[donor]['amount'])>int(JSON[TopDonorIndex]['amount']):
            TopDonorIndex=donor
        TopDonorNameAmnt=str(JSON[TopDonorIndex]['displayName'])+" - "+CurrencySymbol+'{:.2f}'.format(JSON[TopDonorIndex]['amount'])
    return(TopDonorNameAmnt,"TopDonorNameAmnt.txt")

def Participantlast5DonorNameAmts(JSON):
    last5DonorNameAmts=""
    for donor in range(0, len(JSON)):
        last5DonorNameAmts=last5DonorNameAmts+str(JSON[donor]['displayName'])+" - "+CurrencySymbol+str(JSON[donor]['amount'])+"0\n"
        if donor==4:
            break
    return(last5DonorNameAmts,"last5DonorNameAmts.txt")

def Participantlast5DonorNameAmtsMessage(JSON):
    last5DonorNameAmts=""
    for donor in range(0, len(JSON)):
        if JSON[donor]['message'] != None: 
            last5DonorNameAmts="%s%s - %s%.2f - %s\n" % (last5DonorNameAmts, JSON[donor]['displayName'], CurrencySymbol,JSON[donor]['amount'],unicodedata.normalize('NFKD',JSON[donor]['message']).encode('ascii','ignore'))
        else:
            last5DonorNameAmts="%s%s - %s%.2f - %s\n" % (last5DonorNameAmts, JSON[donor]['displayName'], CurrencySymbol,JSON[donor]['amount'],"")
        if donor==4:
            break
    return(last5DonorNameAmts,"last5DonorNameAmtsMessage.txt")
        
def  Participantlast5DonorNameAmtsMessageHorizontal(JSON):   
    # This is for a scrolling type update in OBS or XSplit
    last5DonorNameAmts=""
    for donor in range(0, len(JSON)):
        if JSON[donor]['message'] != None:
            last5DonorNameAmts="%s%s - %s%.2f - %s | " % (last5DonorNameAmts, JSON[donor]['displayName'], CurrencySymbol,JSON[donor]['amount'],unicodedata.normalize('NFKD',JSON[donor]['message']).encode('ascii','ignore'))
        else:
            last5DonorNameAmts="%s%s - %s%.2f - %s | " % (last5DonorNameAmts, JSON[donor]['displayName'], CurrencySymbol,JSON[donor]['amount'],"")
        if donor==4:
            break
    return(last5DonorNameAmts,"last5DonorNameAmtsMessageHorizontal.txt")

#****** Team Info *******

def TheTeamGoal(JSON):
    TeamGoal=CurrencySymbol+'{:.2f}'.format(JSON['fundraisingGoal'])
    writetofile(TeamGoal,"TeamGoal.txt")
    
def TheTeamTotalRaised(JSON):
    TeamTotalRaised=CurrencySymbol+'{:.2f}'.format(JSON['sumDonations'])
    writetofile(TeamTotalRaised,"TeamTotalRaised.txt")
    
def CountDonors(JSON):
    return int(JSON['numDonations'])


#***** LOOPS ******* 

def ParticipantLoop():
    try:
        participantJSON=json.load(urllib.request.urlopen(participant))
    except urllib.error.HTTPError:
        print("Couldn't get to participant URL. Check ExtraLifeID. Or server may be unavailable. (participant loop)")
    try:
        donorJSON=json.load(urllib.request.urlopen(donors))
    except urllib.error.HTTPError:
        print("Couldn't get to donor URL. Check ExtraLifeID. Or server may be unavailable. (participant loop)")
    writetofiletuple(ParticpantTotalRaised(participantJSON))
    writetofiletuple(ParticipantGoal(participantJSON))
    writetofiletuple(ParticipantNumDonations(participantJSON))
    writetofiletuple(ParticipantAvgDonation(participantJSON))
    writetofiletuple(ParticipantLastDonorNameAmnt(donorJSON))
    writetofiletuple(ParticipantTopDonor(donorJSON))
    writetofiletuple(Participantlast5DonorNameAmts(donorJSON))
    writetofiletuple(Participantlast5DonorNameAmtsMessage(donorJSON))
    writetofiletuple(Participantlast5DonorNameAmtsMessageHorizontal(donorJSON))

def TeamLoop():
    if TeamID != None:
        teamJSON=json.load(urllib.request.urlopen(team))
        TheTeamGoal(teamJSON)
        TheTeamTotalRaised(teamJSON)

def main():
    print ("It's GO TIME!")
    print (time.strftime("%H:%M:%S"))
    ParticipantLoop()
    TeamLoop()
    try:
        participantJSON=json.load(urllib.request.urlopen(participant))
    except urllib.error.HTTPError:
        print("Couldn't get to participant URL. Check ExtraLifeID. Or server may be unavailable.")    
    NumberofDonations = CountDonors(participantJSON)
    NewNumberofDonations = NumberofDonations
    
    while True:
        print (time.strftime("%H:%M:%S"))
        try:
            participantJSON=json.load(urllib.request.urlopen(participant))
        except urllib.error.HTTPError:
            print("Couldn't get to participant URL. Check ExtraLifeID. Or server may be unavailable.")
        NewNumberofDonations = CountDonors(participantJSON)
        if NewNumberofDonations > NumberofDonations:
            #for debugging
            print("We got a new donor!")
            NumberofDonations = NewNumberofDonations
            ParticipantLoop()
            TeamLoop()
        time.sleep(30)


if __name__=="__main__":
    main()
