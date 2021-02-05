from unittest import mock

from eldonationtracker.api.participant import Participant
import eldonationtracker.api.participant

config = ("12345", "textfolder", "$", "45678", "5")
fake_participant_conf = mock.Mock()
fake_participant_conf.get_cli_values.return_value = config

config_no_team = ("12345", "textfolder", "$", None, "5")
fake_participant_conf_no_team = mock.Mock()
fake_participant_conf_no_team.get_cli_values.return_value = config_no_team

fake_participant_info = {"displayName": "Eric Mesa", "fundraisingGoal": 600.00, "participantID": 449263.0,
                         "eventName": "Extra Life 2021", "teamName": "Twitchclub", "isTeamCaptain": False,
                         "avatarImageURL": "//assets.donordrive.com/extralife/images/$avatars$/constituent_D4DC394A-C293-34EB-4162ECD2B8BF4C17.jpg",
                         "streamIsLive": False,
                         "links":
                             {"donate":
                                  "https://www.extra-life.org/index.cfm?fuseaction=donorDrive.participant&participantID=449263#donate",
                              "stream": "https://player.twitch.tv/?channel=djotaku",
                              "page":
                                  "https://www.extra-life.org/index.cfm?fuseaction=donorDrive.participant&participantID=449263"},
                         "createdDateUTC": "2021-01-03T21:45:29.523+0000", "eventID": 550.0, "sumDonations": 75.00,
                         "sumPledges": 0.00, "numDonations": 2.0}
fake_donations = {"displayName": "Sean Gibson", "participantID": 401280, "amount": 25.00, "donorID": "54483486D840B7EA",
                  "avatarImageURL": "//assets.donordrive.com/clients/extralife/img/avatar-constituent-default.gif",
                  "createdDateUTC": "2020-02-11T17:22:23.963+0000", "eventID": 547, "teamID": 50394,
                  "donationID": "861A3C59D235B4DA"}, {"displayName": "Eric Mesa", "participantID": 401280,
                                                      "amount": 25.00, "donorID": "4162ECD2B8BF4C17",
                                                      "avatarImageURL": "//assets.donordrive.com/extralife/images/$avat"
                                                                        "ars$/constituent_D4DC394A-C293-34EB-4162ECD2B"
                                                                        "8BF4C17.jpg",
                                                      "createdDateUTC": "2020-01-05T20:35:28.897+0000",
                                                      "eventID": 547, "teamID": 50394, "donationID": "7D430E9E9AF79686"}

donor1_json = {"displayName": "donor1", "sumDonations": "45", "donorID": 1000111,
               'avatarImageURL': "http://someplace.com/image.jpg", "numDonations": 2}
donor1 = eldonationtracker.api.donor.Donor(donor1_json)
fake_top_donor_json = [{"displayName": "Top Donor", "sumDonations": "100", "donorID": 1000111,
                       'avatarImageURL': "http://someplace.com/image.jpg", "numDonations": 2}]

fake_extralife_io = mock.Mock()
fake_extralife_io.get_json.return_value = fake_participant_info
fake_extralife_io.get_JSON_donations.return_value = fake_donations
fake_extralife_io.get_JSON_no_json.return_value = {}
fake_extralife_io.get_JSON_donations_no_json.return_value = {}
fake_extralife_io.get_JSON_top_donor_no_json.return_value = {}

magic_fake_extralife_io = mock.MagicMock()
magic_fake_extralife_io.get_JSON_top_donor.return_value = fake_top_donor_json

fake_participant = mock.Mock()
fake_participant.write_text_files.return_value = None
fake_participant._format_donation_information_for_output.return_value = None
fake_participant._format_donor_information_for_output.return_value = None

fake_participant_for_run = mock.Mock()
fake_participant_for_run.update_participant_attributes.return_value = None
fake_participant_for_run.output_participant_data.return_value = None
fake_participant_for_run.write_ipc.return_value = None
fake_participant_for_run.update_donation_data.return_value = None
fake_participant_for_run.output_donation_data.return_value = None
fake_participant_for_run.update_donor_data.return_value = None
fake_participant_for_run.output_donor_data.return_value = None
fake_participant_for_run.my_team.team_run.return_value = None
fake_participant_for_run.my_team.participant_run.return_value = None


def test_api_variables():
    """Test that API variables are properly assigned."""
    my_participant = Participant(fake_participant_conf)
    assert (my_participant.extralife_id, my_participant.text_folder,
            my_participant.currency_symbol, my_participant.team_id,
            my_participant.donors_to_display) == ("12345", "textfolder", "$", "45678", "5")


def test_urls():
    """Make sure the API URLs are properly constructed."""
    my_participant = Participant(fake_participant_conf)
    assert my_participant.participant_url == "https://www.extra-life.org/api/participants/12345"
    assert my_participant.donation_url == "https://www.extra-life.org/api/participants/12345/donations"
    assert my_participant.participant_donor_url == "https://www.extra-life.org/api/participants/12345/donors"


def test_str_with_a_team():
    """Test the str(participant) string if the participant is part of a team."""
    my_participant = Participant(fake_participant_conf)
    assert str(my_participant) == "A participant with Extra Life ID 12345. Team info: A team found at https://www.extra-life.org/api/teams/45678. "


def test_str_without_a_team():
    """Test the str(participant) string if the participant is not part of a team."""
    my_participant = Participant(fake_participant_conf_no_team)
    assert str(my_participant) == "A participant with Extra Life ID 12345."


@mock.patch.object(eldonationtracker.utils.extralife_io, "get_json", fake_extralife_io.get_json)
def test_get_participant_info():
    """Make sure the API info for the participant is properly assigned."""
    my_participant = Participant(fake_participant_conf)
    assert my_participant._get_participant_info() == (75.0, 2, 600, "//assets.donordrive.com/extralife/images/$avatars$/constituent_D4DC394A-C293-34EB-4162ECD2B8BF4C17.jpg",
                                                      'Extra Life 2021', 'https://www.extra-life.org/index.cfm?fuseaction=donorDrive.participant&participantID=449263#donate',
                                                      'https://player.twitch.tv/?channel=djotaku',
                                                      'https://www.extra-life.org/index.cfm?fuseaction=donorDrive.participant&participantID=449263',
                                                      '2021-01-03T21:45:29.523+0000', False, 0, 'Twitchclub', False,
                                                      'Eric Mesa')


@mock.patch.object(eldonationtracker.utils.extralife_io, "get_json", fake_extralife_io.get_JSON_no_json)
def test_get_participant_info_no_json():
    """Ensure that the proper values are returned if the JSON values are not retrieved from the API."""
    my_participant = Participant(fake_participant_conf)
    assert my_participant._get_participant_info() == (0, 0, 0, '', '', '', '', '', '', False, 0, '', False, '')


def test_format_participant_info_for_output():
    """Make sure the right values are grabbed from the participant properties."""
    my_participant = Participant(fake_participant_conf)
    my_participant._total_raised = 400
    my_participant._average_donation = 100
    my_participant._goal = 1000
    assert my_participant._format_participant_info_for_output(my_participant.total_raised) == "$400.00"
    assert my_participant._format_participant_info_for_output(my_participant.average_donation) == "$100.00"
    assert my_participant._format_participant_info_for_output(my_participant.goal) == "$1,000.00"


def test_fill_participant_dictionary():
    """Make sure the output formatted dictionary has the right info."""
    my_participant = Participant(fake_participant_conf)
    my_participant._total_raised = 400
    my_participant._average_donation = 100
    my_participant._goal = 1000
    my_participant._fill_participant_dictionary()
    assert my_participant._participant_formatted_output["totalRaised"] == "$400.00"
    assert my_participant._participant_formatted_output["averageDonation"] == "$100.00"
    assert my_participant._participant_formatted_output["goal"] == "$1,000.00"


def test_calculate_average_donation():
    """Make sure the average donation is properly calculated."""
    my_participant = Participant(fake_participant_conf)
    my_participant._total_raised = 100
    my_participant._number_of_donations = 2
    assert my_participant._calculate_average_donation() == 50


def test_calculate_average_donation_no_donations():
    """Make sure the average donation is properly calculated if there haven't been any donations yet."""
    my_participant = Participant(fake_participant_conf)
    my_participant._total_raised = 0
    my_participant._number_of_donations = 0
    assert my_participant._calculate_average_donation() == 0


@mock.patch.object(eldonationtracker.utils.extralife_io, "get_json", fake_extralife_io.get_JSON_top_donor_no_json)
def test_get_top_donor_no_json():
    """Make sure the top donor works correctly if the JSON was not returned."""
    my_participant = Participant(fake_participant_conf)
    my_participant._top_donor = donor1
    my_participant._top_donor = my_participant._get_top_donor()
    assert my_participant._top_donor == donor1


@mock.patch.object(eldonationtracker.utils.extralife_io, "get_json", magic_fake_extralife_io.get_JSON_top_donor)
def test_get_top_donor():
    """Make sure we get the correct top donor."""
    my_participant = Participant(fake_participant_conf)
    my_participant._top_donor = donor1
    my_participant._top_donor = my_participant._get_top_donor()
    assert my_participant._top_donor.name == "Top Donor"


def test_format_donor_information_for_output():
    """Make sure the donor information is properly formatted for the users."""
    my_participant = Participant(fake_participant_conf)
    my_participant._top_donor = donor1
    my_participant._format_donor_information_for_output()
    assert my_participant._donor_formatted_output['TopDonorNameAmnt'] == "donor1 - $45.00"


def test_format_donation_information_for_output():
    """Test donation output for the users."""
    my_participant = Participant(fake_participant_conf)
    donation1 = eldonationtracker.api.donation.Donation("Donor 1", "Good job! From Donor 1", 34.51, "4939d",
                                                                "http://image.png",
                                                                "2020-02-11T17:22:23.963+0000", "fakedonationid")
    donation2 = eldonationtracker.api.donation.Donation("Donor 2", None, 34.51, "4939d",
                                                                "http://image.png",
                                                                "2020-02-11T17:22:23.963+0000", "fakedonationid")
    donation3 = eldonationtracker.api.donation.Donation(None, "Good job! From Donor 3", 34.51, "4939d",
                                                                "http://image.png",
                                                                "2020-02-11T17:22:23.963+0000", "fakedonationid")
    my_participant._donation_list = [donation3, donation2, donation1]
    my_participant._format_donation_information_for_output()
    assert my_participant._donation_formatted_output['LastDonationNameAmnt'] == "Anonymous - $34.51"
    assert my_participant._donation_formatted_output['lastNDonationNameAmts'] == "Anonymous - $34.51\nDonor 2 - $34.51" \
                                                                                "\nDonor 1 - $34.51\n"
    assert my_participant._donation_formatted_output['lastNDonationNameAmtsMessage'] == "Anonymous - $34.51 - Good job" \
                                                                                       "! From Donor 3\nDonor 2 - $34" \
                                                                                       ".51 - None\nDonor 1 - $34.51" \
                                                                                       " - Good job! From Donor 1\n"
    assert my_participant._donation_formatted_output['lastNDonationNameAmtsMessageHorizontal'] == "Anonymous - $34.51" \
                                                                                                 " - Good job! From " \
                                                                                                 "Donor 3 | Donor 2 -" \
                                                                                                 " $34.51 - None | " \
                                                                                                 "Donor 1 - $34.51 - " \
                                                                                                 "Good job! From " \
                                                                                                 "Donor 1 | "
    assert my_participant._donation_formatted_output['lastNDonationNameAmtsHorizontal'] == "Anonymous - $34.51" \
                                                                                          " | Donor 2 - $34.51" \
                                                                                          " | Donor 1 - $34.51 | "


def test_update_donation_data_no_donations():
    """Make sure the donation data is updated correction if there are no donations."""
    my_participant = Participant(fake_participant_conf)
    my_participant.update_donation_data()
    assert my_participant._donation_list == []


@mock.patch.object(eldonationtracker.utils.extralife_io, "get_json", fake_extralife_io.get_JSON_donations)
def test_update_donation_data_preexisting_donations():
    my_participant = Participant(fake_participant_conf)
    my_participant._number_of_donations = 2
    my_participant.update_donation_data()
    assert my_participant._donation_list[0].name == "Sean Gibson"


def test_update_donor_data_no_donations():
    my_participant = Participant(fake_participant_conf)
    my_participant.update_donor_data()
    assert my_participant._top_donor is None


@mock.patch.object(eldonationtracker.utils.extralife_io, "get_json", magic_fake_extralife_io.get_JSON_top_donor)
def test_update_donor_data():
    my_participant = Participant(fake_participant_conf)
    my_participant._number_of_donations = 2
    my_participant.update_donor_data()
    assert my_participant._top_donor.name == "Top Donor"


# note: order matters - this one needs to go before the one where _format_donation...output is called or the not called
# fails.
@mock.patch.object(eldonationtracker.api.participant.Participant, 'write_text_files', fake_participant.write_text_files)
@mock.patch.object(eldonationtracker.api.participant.Participant, '_format_donation_information_for_output',
                   fake_participant._format_donation_information_for_output)
def test_output_donation_data_no_donations():
    my_participant = Participant(fake_participant_conf)
    my_participant.output_donation_data()
    assert my_participant._donation_list == []
    fake_participant._format_donation_information_for_output.assert_not_called()
    fake_participant.write_text_files.assert_called()


@mock.patch.object(eldonationtracker.api.participant.Participant, 'write_text_files', fake_participant.write_text_files)
@mock.patch.object(eldonationtracker.api.participant.Participant, '_format_donation_information_for_output',
                   fake_participant._format_donation_information_for_output)
def test_output_donation_data():
    my_participant = Participant(fake_participant_conf)
    my_participant._donation_list = ["a donor", "another_donor"]
    my_participant.output_donation_data()
    fake_participant._format_donation_information_for_output.assert_called()
    fake_participant.write_text_files.assert_called()


@mock.patch.object(eldonationtracker.api.participant.Participant, 'write_text_files', fake_participant.write_text_files)
@mock.patch.object(eldonationtracker.api.participant.Participant, '_format_donor_information_for_output',
                   fake_participant._format_donor_information_for_output)
def test_output_donor_data_no_donations():
    my_participant = Participant(fake_participant_conf)
    my_participant.output_donor_data()
    fake_participant._format_donor_information_for_output.assert_not_called()
    fake_participant.write_text_files.assert_called()


@mock.patch.object(eldonationtracker.api.participant.Participant, 'write_text_files', fake_participant.write_text_files)
@mock.patch.object(eldonationtracker.api.participant.Participant, '_format_donor_information_for_output',
                   fake_participant._format_donor_information_for_output)
def test_output_donor_data():
    my_participant = Participant(fake_participant_conf)
    my_participant._donation_list = ["a donor", "another_donor"]
    my_participant._top_donor = "a top donor"
    my_participant.output_donor_data()
    assert fake_participant._format_donor_information_for_output.called
    assert fake_participant.write_text_files.called


@mock.patch.object(eldonationtracker.api.participant.Participant, 'update_participant_attributes',
                   fake_participant_for_run.update_participant_attributes)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'output_participant_data',
                   fake_participant_for_run.output_participant_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'update_donation_data',
                   fake_participant_for_run.update_donation_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'output_donation_data',
                   fake_participant_for_run.output_donation_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'update_donor_data',
                   fake_participant_for_run.update_donor_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'output_donor_data',
                   fake_participant_for_run.output_donor_data)
@mock.patch.object(eldonationtracker.api.team.Team, 'team_run', fake_participant_for_run.my_team.team_run)
@mock.patch.object(eldonationtracker.api.team.Team, 'participant_run',
                   fake_participant_for_run.my_team.participant_run)
def test_run():
    my_participant = Participant(fake_participant_conf)
    assert my_participant.number_of_donations == 0
    assert my_participant._first_run
    my_participant.run()
    fake_participant_for_run.update_participant_attributes.assert_called_once()
    fake_participant_for_run.output_participant_data.assert_called_once()
    fake_participant_for_run.update_donation_data.assert_called_once()
    fake_participant_for_run.output_donation_data.assert_called_once()
    fake_participant_for_run.update_donor_data.assert_called_once()
    fake_participant_for_run.output_donor_data.assert_called_once()
    fake_participant_for_run.my_team.team_run.assert_called_once()
    assert my_participant._first_run is False
    my_participant.run()
    assert fake_participant_for_run.update_participant_attributes.call_count == 2
    assert fake_participant_for_run.output_participant_data.call_count == 2
    fake_participant_for_run.update_donation_data.assert_called_once()
    fake_participant_for_run.output_donation_data.assert_called_once()
    fake_participant_for_run.update_donor_data.assert_called_once()
    fake_participant_for_run.output_donor_data.assert_called_once()
    assert fake_participant_for_run.my_team.team_run.call_count == 2


@mock.patch.object(eldonationtracker.utils.extralife_io, "get_json", fake_extralife_io.get_json)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'output_participant_data',
                   fake_participant_for_run.output_participant_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'update_donation_data',
                   fake_participant_for_run.update_donation_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'output_donation_data',
                   fake_participant_for_run.output_donation_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'update_donor_data',
                   fake_participant_for_run.update_donor_data)
@mock.patch.object(eldonationtracker.api.participant.Participant, 'output_donor_data',
                   fake_participant_for_run.output_donor_data)
@mock.patch.object(eldonationtracker.api.team.Team, 'team_run', fake_participant_for_run.my_team.team_run)
@mock.patch.object(eldonationtracker.api.team.Team, 'participant_run',
                   fake_participant_for_run.my_team.participant_run)
def test_run_get_a_donation():
    fake_participant_for_run.output_participant_data.reset_mock()
    fake_participant_for_run.update_donation_data.reset_mock()
    fake_participant_for_run.output_donation_data.reset_mock()
    fake_participant_for_run.update_donor_data.reset_mock()
    fake_participant_for_run.output_donor_data.reset_mock()
    fake_participant_for_run.my_team.team_run.reset_mock()
    fake_participant_for_run.my_team.participant_run.reset_mock()
    my_participant = Participant(fake_participant_conf)
    assert my_participant.number_of_donations == 0
    my_participant._first_run = False  # to simulate that this is after one run already
    my_participant.run()
    fake_participant_for_run.output_participant_data.assert_called_once()
    fake_participant_for_run.update_donation_data.assert_called_once()
    fake_participant_for_run.output_donation_data.assert_called_once()
    fake_participant_for_run.update_donor_data.assert_called_once()
    fake_participant_for_run.output_donor_data.assert_called_once()
    fake_participant_for_run.my_team.team_run.assert_called_once()


def test_participant_properties():
    """Check that the properties are all properly set."""
    pass
