"""Grabs donor JSON data and outputs to files."""

import time

import readparticipantconf
import IPC
import team
import extralife_IO

# api info at https://github.com/DonorDrive/PublicAPI


class Donor:
    """Donor Attributes.

    Class exists to provide attributes for a donor based on what comes in from
    the JSON so that it doesn't have to be traversed each time a donor action
    needs to be taken.
    """

    def __init__(self, name, message, amount):
        """Load in values from class initialization."""
        if name is not None:
            self.name = name
        else:
            self.name = "Anonymous"
        self.message = message
        self.amount = amount

    def __lt__(self, object):
        """Donor less than comparison.

        Returns True if this Donor has a donation
        amount less than comparision.
        """
        return self.amount < object.amount


class Participant:
    """Owns all the attributes under the participant API.

    Also owns the results of any calculated data.
    """

    def __init__(self):
        """Load in config from participant.conf and creates the URLs."""
        participant_conf = extralife_IO.ParticipantConf()
        (self.ExtraLifeID, self.textFolder, self.CurrencySymbol,
         self.TeamID) = participant_conf.get_CLI_values()
        # urls
        self.participantURL = f"http://www.extra-life.org/api/participants/{self.ExtraLifeID}"
        self.donorURL = f"http://www.extra-life.org/api/participants/{self.ExtraLifeID}/donations"
        self.participant_donor_URL = f"http://www.extra-life.org/api/participants/{self.ExtraLifeID}/donors"
        # donor calculations
        self.donorcalcs = {}
        self.donorcalcs['LastDonorNameAmnt'] = "No Donors Yet"
        self.donorcalcs['TopDonorNameAmnt'] = "No Donors Yet"
        self.donorcalcs['last5DonorNameAmts'] = "No Donors Yet"
        self.donorcalcs['last5DonorNameAmtsMessage'] = "No Donors Yet"
        self.donorcalcs['last5DonorNameAmtsMessageHorizontal'] = "No Donors Yet"
        self.donorcalcs['last5DonorNameAmtsHorizontal'] = "No Donors Yet"
        self.participantinfo = {}

        # misc
        self.loop = True
        IPC.writeIPC("0")
        self.myteam = team.Team(self.TeamID,
                                self.textFolder,
                                self.CurrencySymbol)

    def get_participant_JSON(self):
        """Get JSON data for participant information.

        Some values that I will want to track as
        numbers will go as class attributes, but all of them will
        go into the dictionary participantinfo in the way they'll
        be written to files.
        """
        self.participantJSON = extralife_IO.get_JSON(self.participantURL)
        self.ParticipantTotalRaised = self.participantJSON['sumDonations']
        self.ParticipantNumDonations = self.participantJSON['numDonations']
        try:
            self.averagedonation = self.ParticipantTotalRaised/self.ParticipantNumDonations
        except ZeroDivisionError:
            self.averagedonation = 0
        self.participantgoal = self.participantJSON['fundraisingGoal']

        # the dictionary:
        self.participantinfo['totalRaised'] = self.CurrencySymbol+'{:.2f}'.format(self.participantJSON['sumDonations'])
        self.participantinfo["numDonations"] = str(self.participantJSON['numDonations'])
        self.participantinfo["averageDonation"] = self.CurrencySymbol+'{:.2f}'.format(self.averagedonation)
        self.participantinfo["goal"] = self.CurrencySymbol+'{:.2f}'.format(self.participantgoal)

    def get_donors(self):
        """Get the donors from the JSON and creates the donor objects."""
        self.donorlist = []
        self.donorJSON = extralife_IO.get_JSON(self.donorURL)
        if len(self.donorJSON) == 0:
            print("No donors!")
        else:
            self.donorlist = [Donor(self.donorJSON[donor].get('displayName'),
                                    self.donorJSON[donor].get('message'),
                                    self.donorJSON[donor]['amount']) for donor in range(0, len(self.donorJSON))]

    def _top_donor(self):
        """Grab Top Donor from server."""
        top_donor_JSON = extralife_IO.get_JSON(self.participant_donor_URL,
                                               True)
        top_donor = Donor(top_donor_JSON[0]['displayName'], "", top_donor_JSON[0]['sumDonations'])
        return extralife_IO.single_format(top_donor, False,
                                          self.CurrencySymbol)

    def _donor_calculations(self):
        self.donorcalcs['LastDonorNameAmnt'] = extralife_IO.single_format(self.donorlist[0], False, self.CurrencySymbol)
        self.donorcalcs['TopDonorNameAmnt'] = self._top_donor()
        self.donorcalcs['last5DonorNameAmts'] = extralife_IO.multiple_format(self.donorlist, False, False, self.CurrencySymbol, 5)
        self.donorcalcs['last5DonorNameAmtsMessage'] = extralife_IO.multiple_format(self.donorlist, True, False, self.CurrencySymbol, 5)
        self.donorcalcs['last5DonorNameAmtsMessageHorizontal'] = extralife_IO.multiple_format(self.donorlist, True, True, self.CurrencySymbol, 5)
        self.donorcalcs['last5DonorNameAmtsHorizontal'] = extralife_IO.multiple_format(self.donorlist, False, True, self.CurrencySymbol, 5)

    def write_text_files(self, dictionary):
        """Write info to text files."""
        extralife_IO.write_text_files(dictionary, self.textFolder)

    def run(self):
        """Run things.

        This should run getParticipantJSON, getDonors,
        the calculations methnods, and the methods to
        write to text files.
        """
        self.get_participant_JSON()
        number_of_dononations = self.ParticipantNumDonations
        self.write_text_files(self.participantinfo)
        self.get_donors()
        if self.donorlist:
            self._donor_calculations()
            self.write_text_files(self.donorcalcs)
        if self.TeamID:
            self.myteam.team_run()
        while self.loop:
            self.get_participant_JSON()
            self.write_text_files(self.participantinfo)
            if self.TeamID:
                self.myteam.participant_run()
            if self.ParticipantNumDonations > number_of_dononations:
                print("A new donor!")
                number_of_dononations = self.ParticipantNumDonations
                self.get_donors()
                self._donor_calculations()
                self.write_text_files(self.donorcalcs)
                IPC.writeIPC("1")
            if self.TeamID:
                self.myteam.team_run()
            print(time.strftime("%H:%M:%S"))
            time.sleep(30)

    def stop(self):
        """Stop the loop."""
        print("stopping now...")
        self.loop = False


if __name__ == "__main__":
    p = Participant()
    p.run()
