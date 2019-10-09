""" Contains classes pertaining to teams."""

import json
import urllib.request


class Team:
    """Hold Team Data."""
    def __init__(self, team_ID, folder, currency_symbol):
        self.team_url = f"http://www.extra-life.org/api/teams/{team_ID}"
        self.team_participant_url = f"https://extra-life.org/api/teams/{team_ID}/participants"
        self.output_folder = folder
        self.currency_symbol = currency_symbol
        self.team_info = {}
        self.participant_calculation_dict = {}

    def get_team_json(self):
        """Get team info from JSON api."""
        try:
            self.team_json = json.load(urllib.request.urlopen(self.team_url))
        except urllib.error.HTTPError:
            print("""Couldn't get to team URL.
                Check team ID.
                Or server may be unavailable.""")
        self.team_goal = self.team_json["fundraisingGoal"]
        self.team_captain = self.team_json["captainDisplayName"]
        self.total_raised = self.team_json["sumDonations"]
        self.num_donations = self.team_json["numDonations"]
        # dictionary
        self.team_info["Team_goal"] = f"{self.currency_symbol}{self.team_goal:,.2f}"
        self.team_info["Team_captain"] = f"{self.team_captain}"
        self.team_info["Team_totalRaised"] = f"{self.currency_symbol}{self.total_raised:,.2f}"
        self.team_info["Team_numDonations"] = f"{self.num_donations}"
        # debug - print statement below
        # print(self.team_info)

    def get_participants(self):
        """Get team participants."""
        self.participant_list = []
        get_results = ""
        try:
            get_results = urllib.request.urlopen(self.team_participant_url)
        except urllib.error.HTTPError:
            print("Couldn't get to team participant URL.")
        try:
            self.team_participant_json = json.load(get_results)
        except:
            print("Couldn't load JSON")
        if not self.team_participant_json:
            print("No team participants!")
        else:
            self.participant_list = [TeamParticipant(self.team_participant_json[participant]['displayName'], float(self.team_participant_json[participant]['sumDonations'])) for participant in range(0, len(self.team_participant_json))]

    def get_top_5_participants(self):
        """Get team participants."""
        self.top_5_participant_list = []
        get_results = ""
        try:
            get_results = urllib.request.urlopen(f"{self.team_participant_url}?orderBy=sumDonations%20DESC")
        except urllib.error.HTTPError:
            print("Couldn't get to team participant URL.")
        try:
            self.top5_team_participant_json = json.load(get_results)
        except:
            print("Couldn't load JSON")
        if not self.top5_team_participant_json:
            print("No team participants!")
        else:
            self.top_5_participant_list = [TeamParticipant(self.top5_team_participant_json[participant]['displayName'], float(self.top5_team_participant_json[participant]['sumDonations'])) for participant in range(0, len(self.top5_team_participant_json))]

    def _top_participant(self):
        try:
            get_results = urllib.request.urlopen(f"{self.team_participant_url}?orderBy=sumDonations%20DESC")
        except urllib.error.HTTPError:
            print("Couldn't get to team participant URL.")
        try:
            self.top_team_participant_json = json.load(get_results)
        except:
            print("Couldn't load JSON")
        if not self.top_team_participant_json:
            print("No team participants!")
        else:
            return f"{self.top_team_participant_json[0]['displayName']} - ${self.top_team_participant_json[0]['sumDonations']:,.2f}"

    def _participant_calculations(self):
        self.participant_calculation_dict['Team_TopParticipantNameAmnt'] = self._top_participant()
        self.participant_calculation_dict['Team_Top5ParticipantsHorizontal'] = self._top_5_participants(self.top_5_participant_list, True)
        self.participant_calculation_dict['Team_Top5Participants'] = self._top_5_participants(self.top_5_participant_list, False)

    def _top_5_participants(self, participants, horizontal):
        text = ""
        if horizontal:
            for participant in range(0, len(participants)):
                text = text + f"{participants[participant].name} - {self.currency_symbol}{participants[participant].donation_totals} | "
                if participant == 4:
                    break
            return text
        elif not horizontal:
            for participant in range(0, len(participants)):
                text = text + f"{participants[participant].name} - {self.currency_symbol}{participants[participant].donation_totals} \n"
                if participant == 4:
                    break
            return text

    def write_text_files(self, dictionary):
        """Write info to text files."""
        for filename, text in dictionary.items():
            f = open(f'{self.output_folder}/{filename}.txt', 'w')
            f.write(text)
            f.close

    def team_run(self):
        self.get_team_json()
        self.write_text_files(self.team_info)

    def participant_run(self):
        self.get_participants()
        self.get_top_5_participants()
        self._participant_calculations()
        self.write_text_files(self.participant_calculation_dict)


class TeamParticipant:
    """Participant Attributes."""
    def __init__(self, name, donation_totals):
        self.name = name
        self.donation_totals = donation_totals

    def __lt__(self, object):
        """Participant less-than comparison"""
        return self.donation_totals < object.donation_totals


if __name__ == "__main__":
    # debug next line
    folder = "/home/ermesa/programming/donationtxt/"
    myteam = Team(44013, folder, "$")
    myteam.get_team_json()
    myteam.get_participants()
    myteam._participant_calculations()
    myteam.write_text_files(myteam.team_info)
    myteam.write_text_files(myteam.participant_calculation_dict)
