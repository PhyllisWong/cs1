class Logger(object):
    '''
    Utility class responsible for logging all interactions of note during the
    simulation.

    log_infection_survival(self, person, did_die_from_infection):
    - Expects person as Person object.
    - Expects bool for did_die_from_infection, with True denoting they died
     from their infection and False denoting they survived and became immune.
    - The format of the log should be "{person.ID} died from infection" or
        "{person.ID} survived infection."
    - Appends the results of the infection to the logfile.

    log_time_step(self, time_step_number):
    - Expects time_step_number as an Int.
    - This method should write a log telling us when one time step ends, and
    the next time step begins.  The format of this log should be:
    "Time step {time_step_number} ended, beginning {time_step_number + 1}..."
    - STRETCH CHALLENGE DETAILS:
    - If you choose to extend this method, the format of the summary statistics
     logged are up to you.
     At minimum, it should contain:
    - The number of people that were infected during this specific time step.
    - The number of people that died on this specific time step.
    - The total number of people infected in the population, including the
     newly infected
    - The total number of dead, including those  died during this time step.
    '''

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed
        # should be the full file name of the file that the logs will be
        # written to.
        # self.file_name = None
        pass

    def write_metadata(self, pop_size, vac_percent, virus, kill_rate,
                       vitality_rate):
        """The simulation class calls this method
        # immediately. to log the specific parameters of the simulation
        # as the first line of the file. This line of metadata is tab-delimited
        # For all other methods, we'll want to use the 'a' mode to append our
        # new log to the end, since 'w' overwrites the file."""
        f = open("./logs/logging.txt", "w")
        line_one = ("{}\t{}\t{}\t{}\t{}\n".format(pop_size, vac_percent,
                                            virus, kill_rate, vitality_rate))
        f.write(line_one)
        f.close()
        return line_one
        pass

    def log_interaction(self, person1, person2, did_infect,
                        person2_vacc, person2_sick):
        """
        Simulation object logs each interaction a sick individual has during
        each time step.
        NOTE:  Think about how the bools passed (or not passed) represent all
        the possible edge cases!
        NOTE: Make sure to end every line with a '/n' character!
        """
        interaction = "{}\t{}\t{}\t{}\t{}\n".format(person1, person2,
                       did_infect, person2_vacc, person2_sick)
        with open("./logs/logging.txt", "a") as f:
            f.write(interaction)

    def log_infection_survival(self, person, did_die_from_infection):
        '''
        Simulation object uses this method to log results of every call of a
        Person object's .resolve_infection() method. If the person survives,
        did_die_from_infection should be False. Otherwise, should be True.
        '''
        result = ""
        if not did_die_from_infection:
            result = "survived infection"
        else:
            result = "died from infection"
        log_line = "{} {}\n".format(person, result)
        with open("./logs/logger.txt", "a") as f:
            f.write(log_line)

    def log_time_step(self, time_step_number):
        # TODO: This method should log when a time step ends,
        # and a new one begins.
        # NOTE: Stretch challenge opportunity!
        # Modify this method so that at the end of each time step, it also logs
        # a summary of what happened in that time step, including the number of
        # people infected, the number of people dead, etc.
        # You may want to create a helper class to compute these statistics
        # for you, as a Logger's job is just to write logs!
        # NOTE: Make sure to end every line with a '/n' character!
        pass
