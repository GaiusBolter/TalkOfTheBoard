######################################################
#                                                    #
#       TalkOfTheBoard - 0.0.1                       #
#                                                    #
#       by:     Splendid                             #
#                                                    #
#                                                    #
######################################################
import os.path
from core.screen import *
from core.menu import *


class TalkOfTheBoard:

    """
        A tool to grab pictures off threads on multiple imageboards.
    """

    def __init__(self, config_file="config.txt"):
        self.TOTB_CONFIG = {}
        self.totb_setup(config_file)

    def totb_setup(self, config_file="config.txt"):
        """
            Reads the configuration file and sets up the script
            Defaults to config.txt if no configuration file is specified.
            If you want to modify the software configuration, edit your config.txt.
        """
        if os.path.isfile(config_file):
            with open(config_file, "r") as file_reader:
                for line in file_reader:
                    line = line.split(":")
                    parameter = line[0].strip()
                    value = line[1].strip()
                    self.TOTB_CONFIG[parameter] = value
        else:
            open(config_file, "w").close()

        required_parameters = ["SAVE_DIR", "IMAGE_DATES"]
        missing_parameters = []

        for required_parameter in required_parameters:
            if required_parameter not in self.TOTB_CONFIG or self.TOTB_CONFIG[required_parameter] == "":
                missing_parameters.append(required_parameter)

        if len(missing_parameters) > 0:
            self.TOTB_CONFIG = {}
            raise Exception("You must edit {} to included the following missing parameters: \n{}"
                            .format(config_file, ", ".join(missing_parameters)))


def main():
    try:
        clear()  # Clear screen
        welcome()  # Print Welcome logo
        totb = TalkOfTheBoard()  # Store TalkOfTheBoard class in a variable, if you want to grab config out
        get_options(TOTB_PROMPT, menu_options)  # Allow user input, menu_options is the initial menu. hangs
    except KeyboardInterrupt:
        end()
        exit(0)


if __name__ == "__main__":
    main()

