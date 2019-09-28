"""Writes to an IPC value to allow different modules to pass information.

This is used to allow the tracker to know that new data needs to be read
in because a new donation has ocurred.
"""

import sys
import readparticipantconf


def writeIPC(value):
    """Write to the IPC file."""
    folders = readparticipantconf.textfolderOnly()
    try:
        with open(f'{folders}/trackerIPC.txt', 'w') as file:
            file.write(value)
            file.close
    except:
        print("No trackerIPC.txt found.")
