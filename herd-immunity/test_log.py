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
    """Should log_interactions."""
    log1 = Logger("./logs/logging.txt")
    with open("./logs/logging.txt", "r") as f:
        log1.log_interaction("person1", "person2", "did_infect",
                             "person2_vacc", "person2_sick")
        first_line = f.readline()
        first_line = f.readline()
        assert first_line == "person1\tperson2\tdid_infect\tperson2_vacc\tperson2_sick\n"


def test_log_infection_survival():
    """Should log_infection_survival."""
    with open("./logs/logging.txt", "r") as f:
        log = Logger("./logs/logging.txt")
        line_one = f.readline()
        assert line_one == "{} died from infection".format(log.person._id)


def log_time_step():
    """Log when time step ends and a new one begins."""
    log = Logger("./logs/logging.txt")
    log.log_time_step(log.time_step_number)
    with open("./logs/logging.txt", "r") as f:
        line_one = f.readline()
        assert line_one == ("~~~~ End of {} Timestep ~~~~\n\nStart of {} timestep\n"
                            .format(log.time_step_number, log.time_step_number+1))
