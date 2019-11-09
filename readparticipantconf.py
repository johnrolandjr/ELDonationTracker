"""Provide various files with the ability to load in the config file."""

import json


def loadJSON():
    """Load in the config file."""
    with open('participant.conf') as file:
        return json.load(file)


def CLIvalues():
    """Load in values needed by extralifedonations.py."""
    participantconf = loadJSON()
    return (participantconf['ExtraLifeID'],
            participantconf['textFolder'],
            participantconf['CurrencySymbol'],
            participantconf['TeamID'])


def textfolderOnly():
    """Only load in value of textFolder."""
    participantconf = loadJSON()
    return participantconf['textFolder']


def GUIvalues():
    """Load in values needed by call_settings.py."""
    participantconf = loadJSON()
    return (participantconf['ExtraLifeID'],
            participantconf['textFolder'],
            participantconf['CurrencySymbol'],
            participantconf['TeamID'],
            participantconf['TrackerImage'],
            participantconf['DonationSound'])


def trackerimage():
    """Load in tracker image file."""
    participantconf = loadJSON()
    return participantconf['TrackerImage']


def trackersound():
    """Load in tracker sound file."""
    participantconf = loadJSON()
    return participantconf['DonationSound']
