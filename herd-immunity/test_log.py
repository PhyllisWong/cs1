import pytest
from logger import Logger
import os
"""Check to see if log outputs as expected."""


def setup_for_test():
    f = open("./logs/logging.txt", "w")
    f.write("Testing Logs Yo!")
    f.close()
    return f


def test_write_metadata():
    # setup_for_test()
    # f = open("./logs/logging.txt", "r")
    # line_one = f.readline()
    # f.close()
    Logger.write_metadata("100", "0.5", "HIV", "0.5", "0.1")
    # print(line_one)
    assert line_one == "100\t0.5\tHIV\t0.5\t0.1"


def test_interactions():
    pass
