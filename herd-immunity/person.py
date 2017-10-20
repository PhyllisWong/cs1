import random
from virus_class import Virus
# make a new virus in the person class to test if the function is working
# TODO: Import the virus class


class Person(object):
    """
    Person objects will populate the simulation.

    _____Attributes______:

    _id: Int.  A unique ID assigned to each person.

    is_vaccinated: Bool.  Determines whether the person object is vaccinated
    against the disease in the simulation.

    is_alive: Bool. All person objects begin alive (value set to true).
    Changed to false if person object dies from an infection.

    Infection: None/Virus object. Set to None for people that are not infected.
        If a person is infected, will instead be set to the virus object the
        person is infected with.

    _____Methods_____:

    __init__(self, _id, is_vaccinated, infected=False):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding
        parameter passed during instantiation.
        - If person is chosen to be infected for first round of simulation,
        then the object should create a Virus object and set it as the value
        for self.infection.  Otherwise, self.infection should be set to None.

    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's
         infection attribute.
            - If random number is smaller, person has died from disease.
            is_alive is changed to false.
            - If random number is larger, person has survived disease.
            Person's is_vaccinated attribute is changed to True, and set self.
            infected to None.
    """

    def __init__(self, _id, is_vaccinated, infected=None):
        """Initialize person with vaccination/infection properties."""
        self._id = _id  # simulation auto generates the ID
        self.is_vaccinated = is_vaccinated
        self.is_dead = False
        self.infected = infected  # store the mortality_rate

    def did_survive_infection(self):
        """Check if person survived infection."""
        # TODO:  Write Test for method
        # Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False
        # and return False.
        # If person lives, set is_vaccinated = True infected = None return True
        rand_num = random.uniform(0, 1)
        if rand_num < self.infected.mortality_rate:
            self.is_dead = True
            return False
        else:
            self.is_dead = False
            self.is_vaccinated = True
            self.infected = None
            return True
        # print(rand_num)

    def infect_person():
        """"""
        pass


if __name__ == '__main__':
    hiv = Virus("HIV", 0.8, 0.3)
    person1 = Person(1, False, hiv)
    print(person1.did_survive_infection())
