import pytest
from logger import Logger
# from person import Person
import os
"""Check to see if log outputs as expected."""


def setup_for_test():
    f = open("./logs/logging.txt", "w")
    f.write("Testing Logs Yo!")
    f.close()
    return f


def test_write_metadata():
    f = open("./logs/logging.txt", "a")
    # log1 = Logger("logging.txt")
    log1 = Logger("log1.txt")
    metadata = log1.write_metadata("100", "0.5", "HIV", "0.5", "0.1")
    print(log1)
    assert metadata == "100\t0.5\tHIV\t0.5\t0.1\n"


def test_log_interaction():
    '''Test if log_interactions func appends to the logfile.'''
    log1 = Logger("./logs/logging.txt")
    with open("./logs/logging.txt", "r") as f:
        log1.log_interaction("person1", "person2", "did_infect",
                             "person2_vacc", "person2_sick")
        first_line = f.readline()
        first_line = f.readline()
        # print(test_text)
        assert first_line == "person1\tperson2\tdid_infect\tperson2_vacc\tperson2_sick\n"


def test_log_infection_survival():
        # TODO: he Simulation object should use this method to log
        # the results of every call of a Person object's .resolve_infection() method.
        # If the person survives, did_die_from_infection should be False. Otherwise,
        # did_die_from_infection should be True. See the documentation for more details
        # on the format of the log.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        with open("./logs/logging.txt", "r") as f:
            log1 = Logger("./logs/logging.txt")
            line_one = f.readline()
            # assert line_one == "{} died from infection".format("person.ID")
            # "{person.ID} survived infection."
            pass


def log_time_step():
        # TODO: Finish this method.  This method should log when a time step ends, and a
        # new one begins.  See the documentation for more information on the format of the log.
        # NOTE: Stretch challenge opportunity! Modify this method so that at the end of each time
        # step, it also logs a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.  You may want to create a helper class
        # to compute these statistics for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        pass
