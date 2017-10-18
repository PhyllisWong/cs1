import pytest
from logger import Logger
from person import Person
import os
"""Check to see if log outputs as expected."""


def setup_for_test():
    f = open("./logs/logging.txt", "w")
    f.write("Testing Logs Yo!")
    f.close()
    return f


def test_write_metadata():
    log1 = Logger("log1.txt")
    metadata = log1.write_metadata("100", "0.5", "HIV", "0.5", "0.1")
    print(log1)
    assert metadata == "100\t0.5\tHIV\t0.5\t0.1\n"


'''
log_interaction(self, person1, person2, did_infect=None,
                    person2_vacc=None, person2_sick=None)
'''

# TODO: The Simulation object logs each interaction a sick individual
# has during each time step.
# This method should accomplish this by using the information
# from person1 (the infected person), person2 (the person randomly
# chosen for the interaction), & the optional keyword arguments passed
# into the method. See documentation for info on the format of logs
#  this method writes.


def test_log_interaction():
    pass
