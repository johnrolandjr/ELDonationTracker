"""Contains classes pertaining to teams."""
from eldonationtracker import extralife_io as extralife_io
from eldonationtracker import base_api_url
from eldonationtracker.team_participant import TeamParticipant


class Team:
    """Hold Team API Data.

    API Variables:
        :param self.team_url: URL to the team JSON API
        :param self.team_participant_url: URL to the JSON api for participants\
        in the team.
        :param self.team_info: a dictionary to hold the following:

                   - Team_goal: fundraising goal
                   - Team_captain: team captain's name
                   - Team_totalRaised: total amount raised by team
                   - Team_numDonations: total number of donations to the team

        :param self.participant_list: a list of the most recent participants
        :param self.top_5_participant_list: a list of the top 5 team participants\
        by amount donated.

        Helper Variables:

        :param self.output_folder: the folder that will contain the output txt files
        :param currency_symbol: for formatting text
        :param self.participant_calculation_dict: dictionary holding output for txt\
        files:

                   - Team_Top5Participants: top 5 participants by
                     donation amount
                   - Team_Top5ParticipantsHorizontal: same, but horizontal
                   - Team_TopParticipantNameAmnt: Top participant and amount"""

    def __init__(self, team_id: str, folder: str, currency_symbol: str):
        """Set the team variables."""
        self.team_id = team_id
        # urls
        team_url_base: str = f"{base_api_url}/teams/"
        self.team_url: str = f"{team_url_base}{team_id}"
        self.team_participant_url: str = f"{self.team_url}/participants"
        # misc
        self.output_folder: str = folder
        self.currency_symbol: str = currency_symbol
        self.team_info = {}
        self.participant_calculation_dict: dict = {}
        self.top_5_participant_list = []
        self.team_json: dict = {}

    def get_team_json(self):
        """Get team info from JSON api."""
        self.team_json = extralife_io.get_JSON(self.team_url)
        if not self.team_json:
            print("Could not get team JSON")
        else:
            self.team_goal = self.team_json["fundraisingGoal"]
            self.team_captain = self.team_json["captainDisplayName"]
            self.total_raised = self.team_json["sumDonations"]
            self.num_donations = self.team_json["numDonations"]
            # dictionary
            self.team_info["Team_goal"] = f"{self.currency_symbol}{self.team_goal:,.2f}"
            self.team_info["Team_captain"] = f"{self.team_captain}"
            self.team_info["Team_totalRaised"] = f"{self.currency_symbol}{self.total_raised:,.2f}"
            self.team_info["Team_numDonations"] = f"{self.num_donations}"

    def get_participants(self):
        """Get team participant info from API."""
        self.participant_list = []
        self.team_participant_json = extralife_io.get_JSON(self.team_participant_url)
        if not self.team_participant_json:
            print("couldn't get to URL")
        elif len(self.team_participant_json) == 0:
            print("No team participants!")
        else:
            self.participant_list = [TeamParticipant(self.team_participant_json[participant]) for participant in range(0, len(self.team_participant_json))]

    def get_top_5_participants(self):
        """Get team participants."""
        self.top5_team_participant_json = extralife_io.get_JSON(self.team_participant_url, True)
        if not self.top5_team_participant_json:
            print("Couldn't get top 5 team participants")
        elif len(self.top5_team_participant_json) == 0:
            print("No team participants!")
        else:
            self.top_5_participant_list = [TeamParticipant(self.top5_team_participant_json[participant]) for participant in range(0, len(self.top5_team_participant_json))]

    def _top_participant(self):
        """Get Top Team Participant.

        This should just grab element 0 from above instead of hitting API twice
        """
        if len(self.top_5_participant_list) == "0":
            print("No participants")
        else:
            return (f"{self.top_5_participant_list[0].name} - $"
                    f"{self.top_5_participant_list[0].amount:,.2f}")

    def _participant_calculations(self):
        self.participant_calculation_dict['Team_TopParticipantNameAmnt'] = self._top_participant()
        self.participant_calculation_dict['Team_Top5ParticipantsHorizontal'] = extralife_io.multiple_format(self.top_5_participant_list, False, True, self.currency_symbol, 5)
        self.participant_calculation_dict['Team_Top5Participants'] = extralife_io.multiple_format(self.top_5_participant_list, False, False, self.currency_symbol, 5)

    def write_text_files(self, dictionary: dict):
        """Write info to text files.

        :param dictionary: The dictionary containing the values to write out to text files.
        """
        extralife_io.write_text_files(dictionary, self.output_folder)

    def team_run(self):
        """Get team info from API."""
        self.get_team_json()
        self.write_text_files(self.team_info)

    def participant_run(self):
        """Get and calculate team participant info."""
        self.get_participants()
        self.get_top_5_participants()
        self._participant_calculations()
        self.write_text_files(self.participant_calculation_dict)

    def __str__(self):
        team_info = ""
        if self.team_json:
            team_info = f"Team goal is {self.team_info['Team_goal']}."
        if self.team_id:
            return f"A team found at {self.team_url} {team_info}."
        else:
            return "Not a valid team - no team_id."


if __name__ == "__main__":
    # debug next line
    folder = "/home/ermesa/Programming Projects/python/extralife/testOutput"
    myteam = Team(44013, folder, "$")
    myteam.get_team_json()
    myteam.get_participants()
    myteam._participant_calculations()
    myteam.write_text_files(myteam.team_info)
    myteam.write_text_files(myteam.participant_calculation_dict)
