import pytest
from simulation import Simulation


def setup_for_test():
    sim = Simulation(10, 0.2, "HIV", 0.8, 0.5)
    return sim


def test__create_population():
    '''Check that the simulation creates population accurately.'''
    sim = setup_for_test()
    sim._create_population(2)
    assert sim.pop_size == 10
    assert sim.current_infected == 2


def test_simulation_should_continue():
    sim = setup_for_test()
    # print(sim.population)
    for person in sim.population:
        # print(person)
        assert sim.person.is_alive is True
        assert sim.person.infected is True
