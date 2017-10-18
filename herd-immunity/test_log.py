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
    '''
    Expects did_infect, person2_vacc, and person2_sick as Bools, if passed.
    - Between values passed with did_infect, person2_vacc, and person2_sick,
     this method should be able to determine exactly what happened in the
     interaction and create a String saying so.
    - The format of the log should be "{person1.ID} infects {person2.ID}",
     or, for other edge cases, "{person1.ID} didn't infect {person2.ID}
      because {'vaccinated' or 'already sick'}"
    - Appends the interaction to logfile.
    '''
    f = open("./logs/logging.txt", "a")
    log1 = Logger("logging.txt")
    # log1.log_interaction(person1, person2, did_infect,
    #                      person2_vacc, person2_sick)
    f.write("Testing Logs Yo!")
    test_text = f.readline(1)
    f.close()
    print(test_text)
    assert test_text == "Testing Logs Yo!"
