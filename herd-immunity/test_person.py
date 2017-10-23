from person import Person


def setup_for_test():
    """Check that instantiating a person with default values is working."""
    person = Person(1)
    assert person._id == 1
    assert person.is_vaccinated is None
    assert person.is_alive is True
    assert person.infected is None


# _id, is_vaccinated=None, is_alive=True, infected=None
setup_for_test()
