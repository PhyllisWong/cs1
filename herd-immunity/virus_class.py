import pytest

class Virus(object):
    """Properties and attributes of the virus used in Simulation."""

    def __init__(self, name, mortality_rate, is_dead):
        """Attributes instantiated with each virus."""
        self.name = name
        self.mortality_rate = mortality_rate
        self.is_dead = is_dead


def test_virus_instatiation():
    """Check to make sure that the virus instantiator is working."""
    virus = Virus("HIV", 0.8, False)
    assert virus.name == "HIV"
    assert virus.mortality_rate == 0.8
    assert virus.is_dead is False
