import extralifedonations

# run with command: py.test-3 extralifeunittests.py
# or if in venv, just pytest extralifeunittests.py (works better)


# Tests for class Donor
def test_Donor_lt():
    """ Test to make sure comparison works. """
    donor1 = extralifedonations.Donor("donor1", "message", 45)
    donor2 = extralifedonations.Donor("donor2", "message", 30)
    assert donor2 < donor1


# Tests for class Participant
# Come back and develop tests for get_participant_JSON and 
# get_donors after changing the methods to take input
# and return a value. That will be in prep for refactoring.
def test_donor_formatting_message_true():
    """ Make sure the formatting works correctly. """
    p = extralifedonations.Participant()
    donor1 = extralifedonations.Donor("donor1", "message", 45)
    formatted_message = p._donor_formatting(donor1, True)
    assert formatted_message == "donor1 - $45.00 - message"


def test_donor_formatting_message_false():
    """ Make sure the formatting works correctly. """
    p = extralifedonations.Participant()
    donor1 = extralifedonations.Donor("donor1", "message", 45)
    formatted_message = p._donor_formatting(donor1, False)
    assert formatted_message == "donor1 - $45.00"


def test_last5donors_Horizontal():
    """ Does it return the right thing? 

    I include an extra donor to make sure it stops at 5."""
    donor1 = extralifedonations.Donor("donor1", "message1", 10)
    donor2 = extralifedonations.Donor("donor2", "message2", 20)
    donor3 = extralifedonations.Donor("donor3", "message3", 30)
    donor4 = extralifedonations.Donor("donor4", "message4", 40)
    donor5 = extralifedonations.Donor("donor5", "message5", 50)
    donor6 = extralifedonations.Donor("donor6", "message6", 60)
    donor_list = [donor1, donor2, donor3, donor4, donor5, donor6]
    p = extralifedonations.Participant()
    text = p._last5donors(donor_list, False, True)
    assert text == "donor1 - $10.00 | donor2 - $20.00 | donor3 - $30.00 | donor4 - $40.00 | donor5 - $50.00 | "


def test_last5donors_Message_Horizontal():
    """ Does it return the right thing? 

    I include an extra donor to make sure it stops at 5."""
    donor1 = extralifedonations.Donor("donor1", "message1", 10)
    donor2 = extralifedonations.Donor("donor2", "message2", 20)
    donor3 = extralifedonations.Donor("donor3", "message3", 30)
    donor4 = extralifedonations.Donor("donor4", "message4", 40)
    donor5 = extralifedonations.Donor("donor5", "message5", 50)
    donor6 = extralifedonations.Donor("donor6", "message6", 60)
    donor_list = [donor1, donor2, donor3, donor4, donor5, donor6]
    p = extralifedonations.Participant()
    text = p._last5donors(donor_list, True, True)
    assert text == "donor1 - $10.00 - message1 | donor2 - $20.00 - message2 | donor3 - $30.00 - message3 | donor4 - $40.00 - message4 | donor5 - $50.00 - message5 | "


def test_last5donors_Vertical():
    """ Does it return the right thing? 

    I include an extra donor to make sure it stops at 5."""
    donor1 = extralifedonations.Donor("donor1", "message1", 10)
    donor2 = extralifedonations.Donor("donor2", "message2", 20)
    donor3 = extralifedonations.Donor("donor3", "message3", 30)
    donor4 = extralifedonations.Donor("donor4", "message4", 40)
    donor5 = extralifedonations.Donor("donor5", "message5", 50)
    donor6 = extralifedonations.Donor("donor6", "message6", 60)
    donor_list = [donor1, donor2, donor3, donor4, donor5, donor6]
    p = extralifedonations.Participant()
    text = p._last5donors(donor_list, False, False)
    assert text == "donor1 - $10.00\ndonor2 - $20.00\ndonor3 - $30.00\ndonor4 - $40.00\ndonor5 - $50.00\n"


def test_last5donors_Message_Vertical():
    """ Does it return the right thing? 

    I include an extra donor to make sure it stops at 5."""
    donor1 = extralifedonations.Donor("donor1", "message1", 10)
    donor2 = extralifedonations.Donor("donor2", "message2", 20)
    donor3 = extralifedonations.Donor("donor3", "message3", 30)
    donor4 = extralifedonations.Donor("donor4", "message4", 40)
    donor5 = extralifedonations.Donor("donor5", "message5", 50)
    donor6 = extralifedonations.Donor("donor6", "message6", 60)
    donor_list = [donor1, donor2, donor3, donor4, donor5, donor6]
    p = extralifedonations.Participant()
    text = p._last5donors(donor_list, True, False)
    assert text == "donor1 - $10.00 - message1\ndonor2 - $20.00 - message2\ndonor3 - $30.00 - message3\ndonor4 - $40.00 - message4\ndonor5 - $50.00 - message5\n"
# for the file writing don't forget to test donor names and messages with
# characters like ñ and ô and emojis.
