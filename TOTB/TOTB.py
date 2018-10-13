######################################################
#                                                    #
#       TalkOfTheBoard - 0.0.1                       #
#                                                    #
#       by:     Splendid                             #
#                                                    #
#                                                    #
######################################################
from screen import *


class TalkOfTheBoard:

    """
        A tool to grab pictures off threads on multiple imageboards.
    """

    def __init__(self, config_file="config.txt"):
        self.TOTB_CONFIG = {}
        self.totb_setup(config_file)

        # Welcome Screen and ASCII
        welcome()

    def totb_setup(self, config_file="config.txt"):
        """
            Reads the configuration file and sets up the script
            Defaults to config.txt if no configuration file is specified.
            If you want to modify the bot configuration, edit your config.txt.
        """

        with open(config_file, "r") as file_reader:
            for line in file_reader:
                line = line.split(":")
                parameter = line[0].strip()
                value = line[1].strip()

                if parameter in ["SAVE_DIR", "IMAGE_DATES"]:
                    if value != "":
                        self.TOTB_CONFIG[parameter] = set([int(x) for x in value.split(",")])
                    else:
                        self.TOTB_CONFIG[parameter] = set()

        required_parameters = ["SAVE_DIR", "IMAGE_DATES"]
        missing_parameters = []

        for required_parameter in required_parameters:
            if required_parameter not in self.TOTB_CONFIG or self.TOTB_CONFIG[required_parameter] == "":
                missing_parameters.append(required_parameter)

        if len(missing_parameters) > 0:
            self.TOTB_CONFIG = {}
            raise Exception("You must edit {} to included the following missing parameters: \n{}"
                            .format(config_file, ", ".join(missing_parameters)))
