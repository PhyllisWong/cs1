class Logger(object):
    """ Utility class responsible for logging all interactions of note during
    the simulation."""

    def __init__(self, file_name):
        """Initialize the file_name using the full file name passed in.
        All log events are written to this file."""
        self.file_name = file_name

    def write_metadata(self, pop_size, vac_percent, virus, kill_rate,
                       vitality_rate):
        """The simulation class calls this method immediately to log the
        specific parameters of the simulation as the first line of the file.
        This line of metadata is tab-delimited."""

        f = open("./logs/logger.txt", "w")
        line_one = ("{}\t{}\t{}\t{}\t{}\n".format(pop_size, vac_percent,
                    virus, kill_rate, vitality_rate))
        f.write(line_one)
        f.close()
        return line_one

    def log_interaction(self, person1, person2, did_infect,
                        person2_vacc, person2_sick):
        """Simulation object logs each interaction a sick individual has during
        each time step."""
        interaction = ("{}\t{}\t{}\t{}\t{}\n".format(person1, person2,
                       did_infect, person2_vacc, person2_sick))
        with open("./logs/logger.txt", "a") as f:
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
