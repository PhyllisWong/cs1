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
    This will be passed to the Virus object upon instantiation.

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

    def __init__(self, pop_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        '''Initializer uses the command line input to start the sim.'''
        self.pop_size = pop_size
        self.population = []
        self.total_infected = initial_infected
        self.current_infected = 0
        self.next_id = 0
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        self._create_population(initial_infected)

        # TODO: Create a Logger object and bind it to self.logger.
        # Use this logger object to log all events during the sim.
        # Don't forget to call the logger methods in the corresponding parts
        # of the simulation!
        self.logger = None

        # This attribute will be used to keep track of all the people that
        # catch the infection during a given time step. Store each newly
        # infected person's .ID attribute in here.
        # At the end of each time step, we call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.newly_infected = []
        # TODO: Call self._create_population() and pass in the correct
        # parameters. Store the array that this method will return in the
        # self.population attribute.

    def _create_population(self, initial_infected):
        self.current_infected = initial_infected
        self.population = []
        infected_count = 0
        while len(self.population) != self.pop_size:
            if infected_count != initial_infected:
                infected_count += 1
                self.current_infected += 1
                self.next_id += 1
                person_sick = Person(self.next_id, is_vaccinated=None,
                                     infected=True)
                self.population.append(person_sick)
            else:
                self.next_id += 1
                rand_num = random.uniform(0, 1)
                if rand_num < self.vacc_percentage:
                    person_vacc = Person(self.next_id, is_vaccinated=True,
                                         infected=False)
                    self.population.append(person_vacc)
                else:
                    person = Person(self.next_id, is_vaccinated=False,
                                    infected=False)
                    self.population.append(person)
        for person in self.population:
            print("ID: {}\tVacc: {}\tInfected: {}".format(person._id, person.is_vaccinated,
                  person.infected))
        return self.population

    def _simulation_should_continue(self):
        '''
        Returns True if the sim should cont./False if it should not.
        Sim ends if the entire population is dead.
        OR: There are zero infected people in the population.
        '''
        for person in self.population:
            if person.is_alive:
                # print("Sim should keep running")
                if person.infected:
                    # print("Sim should keep running")
                    return True
        print("Sim should stop")
        return False

    def run(self):
        '''
        This method runs the simulation until everyone in the simulation is
        dead, or no one is infected in the population.
        We call _simulation_should_continue() to check whether or not we
        should continue the simulation and run at least 1 more time_step.

        This method keeps track of the number of time steps that
        have passed using the time_step_counter variable.
        This method calles logger's log_time_step() at the end of each time
        step passing in the time_step_counter variable!
        '''
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            print("Another time step")
            should_continue = self._simulation_should_continue()
            time_step_counter += 1
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        # TODO: This method should contain all the basic logic for computing
        # one time step in the simulation. This includes:
            # - For each infected person in the population:
            # - Repeat for 100 total interactions:
            # - Grab a random person from the population.
            # - If the person is dead, continue and grab another new
            # person from the population. Since we don't interact
            # with dead people, this does not count as an interaction.
            # - Else:
            # - Call simulation.interaction(person, random_person)
            # - Increment interaction counter by 1.
            pass

    def interaction(self, person, random_person):
        '''
        This method is called any time two living people are selected for
        an interaction. Assert statements are included to make sure that
        only living people interact. If both people are vaccinated, nothing
        happens, if one person either person is infected and the other
        unvaccinated, there is a chance they can get infected. All interactions
        are logged.
        '''
        assert person.is_alive is True
        assert random_person.is_alive is True
        # both people are vaccinated, then both people cant be infected
        if person.vaccinated is True:
            if random_person.vaccinated is True:
                self.logger.log_interaction()
        # Both people are infected, then both cant be vaccinated
        elif person.infected is True:
            if random_person.infected is True:
                self.logger.log_interaction()
        # Both are not vaccinated and not infected
        elif person.vaccinated is False and person.infected is False:
            if random_person.vaccinated is False and random_person.infected is False:
                self.logger.log_interaction()
        # person is vaccinated not infected, random_person not vacc or infected
        elif person.vaccinated is True:
            if random_person.vaccinated is False and random_person.infected is False:
                self.logger.log_interaction()
        # random_person is vaccinated not infected, person not vacc or infected
        elif random_person.vaccinated is True:
            if person.vaccinated is False and person.infected is False:
                self.logger.log_interaction()
        # person is vaccinated not infected, random_person is infected
        elif person.vaccinated is True:
            if random_person.infected is True:
                self.logger.log_interaction()
        # random_person is vaccinated not infected, person is infected
        elif random_person.vaccinated is True:
            if person.infected is True:
                self.logger.log_interaction()
        # person is not vaccinated or infected, random_person is infected
        elif person.vaccinated is False and person.infected is False:
            if random_person.infected is True:
                rand_num = random.uniform(0, 1)
                if rand_num < self.basic_repro_num:
                    print("random_person contracts the virus")
                    self.newly_infected.append(random_person._id)
                    self.logger.log_interaction()
        # random_person is not vaccinated or infected, person is infected
        elif random_person.vaccinated is False and random_person.infected is False:
            if person.infected is True:
                rand_num = random.uniform(0, 1)
                if rand_num < self.basic_repro_num:
                    print("random_person contracts the virus")
                    self.newly_infected.append(random_person._id)
                    self.logger.log_interaction()
        pass

    def _infect_newly_infected(self):
        self.newly_infected.sort()
        for person in self.population:
            if self.newly_infected[0] == person._id:
                person.infected = True
                del self.newly_infected[0]
        if len(self.newly_infected) == 0:
            break


# if __name__ == "__main__":
#     params = sys.argv[1:]
#     pop_size = int(params[0])
#     vacc_percentage = float(params[1])
#     virus_name = str(params[2])
#     mortality_rate = float(params[3])
#     basic_repro_num = float(params[4])
#     if len(params) == 6:
#         initial_infected = int(params[5])
#     else:
#         initial_infected = 1
#     sim = Simulation(pop_size, vacc_percentage, virus_name,
#                      mortality_rate, basic_repro_num, initial_infected)
#     sim.run()


sim = Simulation(10, 0.2, "HIV", 0.8, 0.5)
for person in sim.population:
    print(person.infected)
sim._simulation_should_continue()
print(sim.pop_size)
print(sim.total_infected)
