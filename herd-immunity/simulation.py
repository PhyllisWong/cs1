import random, sys
random.seed(42)
from person import Person
from logger import Logger

class Simulation(object):
    '''
    Main class that runs the herd immunity simulation program.
    Expects init parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.
    The population size, percentage that are vaccinated, and the initial num
    of infected people are variables that are set when the program is run.

    _____Attributes______

    logger: Logger object. The helper object that will be responsible for
    writing all logs to the simulation.

    pop_size: Int. The size of the population for this simulation.

    population: [Person]. A list of person objects representing all people in
        the population.

    next_id: Int. The next available id value for all a new person
    object. Each person has a unique _id value.

    virus_name: String.  The name of the virus for the simulation.
    This will be passed to the Simulation object upon instantiation.

    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.

    basic_repro_num: Float between 0 and 1. This will be passed
    to the Virus object upon instantiation.

    vacc_percentage: Float between 0 and 1. Represents the total percentage
    of population vaccinated for the given simulation.

    current_infected: Int. The number of people in the population currently
    infected with the disease in in each time_step(generation).

    total_infected: Int. The running total of people that have been infected
    since the simulation began, including any people currently infected.

    total_dead: Int. The number of people that have died as a result of the
    infection during this simulation. Starts at zero.

    '''

    def __init__(self, pop_size, vacc_percentage, virus,
                 mortality_rate, basic_repro_num, initial_infected=1):
        '''Initializer uses the command line input to start the sim.'''
        self.pop_size = pop_size
        self.population = []
        self.total_infected = initial_infected
        self.current_infected = 0
        self.next_id = 0
        self.vacc_percentage = vacc_percentage
        self.virus = virus
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus, pop_size, vacc_percentage, initial_infected)
        self.population = self._create_population(initial_infected)
        self.logger = Logger("./logs/logger.txt")
        # This attribute will be used to keep track of all the people that
        # catch the infection during a given time step. Store each newly
        # infected person's .ID attribute in here.
        self.newly_infected = []

    def _create_population(self, initial_infected):
        self.current_infected = initial_infected
        self.population = []
        infected_count = 0
        # Instantiate new instances of Person until population == pop_size
        while len(self.population) != self.pop_size:
            self.next_id += 1
            # Instantiate Person objects with infection=virus
            if infected_count != initial_infected:
                person_sick = Person(self.next_id, False, infected=self.virus)
                self.population.append(person_sick)
                infected_count += 1
            else:
                # Randomly instantiate Person object with vaccination
                if random.uniform(0, 1) < self.vacc_percentage:
                    self.population.append(Person(self.next_id, True))
                else:
                    # Instantiate Person with no vaccination or infection
                    self.population.append(Person(self.next_id, False))
        return self.population

    def _simulation_should_continue(self):
        '''
        Returns True if the sim should cont./False if it should not.
        Sim ends if the entire population is dead.
        OR: There are zero infected people in the population.
        '''
        for person in self.population:
            if person.is_alive and person.infected:
                return True
        return False

    def run(self):
        '''
        This method runs the simulation until everyone is dead, or everyone is
        vaccinated in the population. We call _simulation_should_continue()
        to see if the simulation should run another time_step.

        This method keeps track of the number of time steps that
        have passed using the time_step_counter variable.
        This method calles logger's log_time_step(time_step_counter)
        at the end of each time step!
        '''
        # Log start of simulation
        self.logger.write_metadata(self.pop_size, self.vacc_percentage,
                                   self.virus, self.mortality_rate,
                                   self.basic_repro_num)
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            should_continue = self._simulation_should_continue()
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        '''
        Method computes one time step in the simulation. Each infected person
        in the population has 100 random interactions.
        Each interaction calls simulation.interaction(person, random_person)
        and increments the counter by 1 until reaches 100. Then goes to the
        next iteration of an infected person.
        '''
        for person in self.population:
            if person.infected is not None:
                counter = 0
                while counter < 100:
                    random_id = random.randint(1, len(self.population)-1)
                    random_person = self.population[random_id]
                    if person.is_alive is True and random_person.is_alive is True:
                        print("Random dude: " + str(random_person._id))
                        self.interaction(person, random_person)
                    counter += 1
            person.did_survive_infection(self.mortality_rate)
        self.total_infected += len(self.newly_infected)
        print("Update infection")
        self.update_infection_state()
        print("Update infection happened")

    def interaction(self, person, random_person):
        '''
        This method is called any time two living people are selected for
        an interaction. Person will always be infected, random_person could
        have 3 different states of vaccination or infection. Assert statements
        are included to make sure that only living people interact.
        All interactions are logged.
        '''
        assert person.infected is not None
        assert person.is_alive is True
        assert random_person.is_alive is True
        # both people are vaccinated, then both people cant be infected
        # random_person is infected, nothing happens
        if random_person.infected:
            # print("HERE")
            self.logger.log_interaction(person, random_person, False, random_person.is_vaccinated,
            random_person.infected)
        # random_person is vaccinated, nothing happens
        elif random_person.is_vaccinated:
            # print("NOT HERE")
            self.logger.log_interaction(person, random_person, False, random_person.is_vaccinated,
            random_person.infected)
        # random_person not vaccinated or infected
        else:
            rand_num = random.uniform(0, 1)
            if rand_num < self.basic_repro_num:
                if not random_person.infected:
                    print("YES HERE")
                    random_person.infect_person(self.virus)
                    self.newly_infected.append(random_person._id)
                else:
                    # print("HERE?")
                    # print(self.newly_infected)
                    self.logger.log_interaction(person, random_person, "Did infect",
                    random_person.is_vaccinated, random_person.infected)

    def update_infection_state(self):
        """Update the infection state of all newly infected people."""
        # Update total_infected with num of newly_infected each time_step
        print("Here: " + str(self.newly_infected))
        self.newly_infected.sort()
        if len(self.newly_infected) < 1:
            return
        for person in self.population:
            if self.newly_infected[0] == person._id:
                person.infect_person(self.virus)
                del self.newly_infected[0]
            if len(self.newly_infected) == 0:
                break
        print("Here2: " + str(self.newly_infected))
        # self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    sim = Simulation(pop_size, vacc_percentage, virus,
                     mortality_rate, basic_repro_num, initial_infected)
    sim.run()

#
# sim = Simulation(100, 0.2, "HIV", 0.8, 0.5, 20)
# for person in sim.population:
#     print("ID: {}\tVacc: {}\tInfected: {}".format(person._id,
#             person.is_vaccinated, person.infected))
# sim._simulation_should_continue()
# print(sim.pop_size)
# print(sim.current_infected)
