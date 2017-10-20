from person import Person


def setup_for_test():
    """Check that instantiating a person with default values is working."""
    person = Person(1, False, False)
    assert person._id == 1
    assert person.is_vaccinated is False
    assert person.is_dead is False
    assert person.infected is False


setup_for_test()
