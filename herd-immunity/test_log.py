import pytest
import logger
import os
"""Check to see if log outputs as expected."""


def test_write_metadata():
    f = open("./logs/logging.txt", "w")
    f.write("Testing Logs Yo!")
    f.close()
    f = open("./logs/logging.txt", "r")
    line_one = f.readline()
    f.close()
    print(line_one)
    assert line_one == "Testing Logs Yo!"


def test_interactions():
    pass
