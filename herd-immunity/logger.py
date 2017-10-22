class Logger(object):
    """ Utility class responsible for logging all interactions of note during
    the simulation."""

    def __init__(self, file_name):
        # TODO:  Finish this initialization method.  The file_name passed
        # should be the full file name of the file that the logs will be
        # written to.
        # self.file_name = None
        pass

    def write_metadata(self, pop_size, vac_percent, virus, kill_rate,
                       vitality_rate):
        """The simulation class calls this method immediately to log the
        specific parameters of the simulation as the first line of the file.
        This line of metadata is tab-delimited."""

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
        interaction = ("{}\t{}\t{}\t{}\t{}\n".format(person1, person2,
                       did_infect, person2_vacc, person2_sick))
        with open("./logs/logging.txt", "a") as f:
            f.write(interaction)

    def log_infection_survival(self, person, did_die_from_infection):
        """ Simulation object uses this method to log results of every call of a
        Person object's .resolve_infection() method. If the person survives,
        did_die_from_infection should be False. Otherwise, should be True.
        """
        result = ""
        if not did_die_from_infection:
            result = "survived infection"
        else:
            result = "died from infection"
        log_line = "{} {}\n".format(person, result)
        with open("./logs/logger.txt", "a") as f:
            f.write(log_line)

    def log_time_step(self, time_step_number):
        """Logs when a time step ends, and a new one begins."""
        with open("./logs/logger.txt", "a") as f:
            f.write("~~~~ End of {} Timestep ~~~~\n, \nStart of {} timestep\n"
                    .format(time_step_number, time_step_number+1))
