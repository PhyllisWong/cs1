import random
from virus_class import Virus
# make a new virus in the person class to test if the function is working
# TODO: Import the virus class


class Person(object):
    '''
    Person objects will populate the simulation.

    _____Attributes______:

    _id: Int.  A unique ID assigned to each person.

    is_vaccinated: Bool.  Determines whether the person object is vaccinated
    against the disease in the simulation.

    is_alive: Bool. All person objects begin alive (value set to true).
    Changed to false if person object dies from an infection.

    Infection: Bool. Set to False for healthy people not infected.
    If a person is infected, set to True.

    __init__(self, _id, is_vaccinated, infected=False):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding
        parameter passed during instantiation.
        - If person is chosen to be infected for first round of simulation,
        then the object should create a Virus object and set it as the value
        for self.infection.  Otherwise, self.infection should be set to None.
        '''

    def __init__(self, _id, is_vaccinated=None, is_alive=True, infected=None):
        '''Initialize person with vaccination/infection properties.'''
        self._id = _id  # simulation auto generates the ID
        self.is_vaccinated = is_vaccinated
        self.is_alive = is_alive
        self.infected = infected

    def did_survive_infection(self, mortality_rate):
        '''
        Check if person survived infection
        Only called if infection attribute is True. Takes no inputs.
        Generates a random number between 0 and 1, Compares random number to
        mortality_rate. If random num is smaller, person dies from disease.
        is_alive is changed to False, else person survives disease.
        is_vaccinated is changed to True, and self.infected is False.
        '''
        rand_num = random.uniform(0, 1)

        print(str(self._id) + " " + str(mortality_rate) + " " + str(rand_num))
        if rand_num < mortality_rate:
            self.is_alive = False
            return False
        else:
            self.is_alive = True
            self.is_vaccinated = True
            self.infected = None
            return True

    def infect_person(self, virus):
        """Infect person."""
        self.infected = virus


if __name__ == '__main__':
    hiv = Virus("HIV", 0.8, 0.3)
    person1 = Person(1, False, hiv)
    print(person1.did_survive_infection())
