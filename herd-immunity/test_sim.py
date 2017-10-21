import pytest
from simulation import Simulation


def test__create_population():
    '''Check that the simulation creates population accurately.'''
    sim = Simulation(10, 0.2, "HIV", 0.8, 0.5)
    # sim._create_population(2)
    assert sim.pop_size == 10
    print(sim.total_infected)
    assert sim.current_infected == 2
