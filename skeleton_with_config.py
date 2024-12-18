#!/usr/bin/env python3
"""
skeleton.py - a skeleton starting-point for python scripts by Roger Allen.

Any copyright is dedicated to the Public Domain.
http://creativecommons.org/publicdomain/zero/1.0/
You should add your own license here.

"""
import os
import sys
import logging
import argparse
import configparser

# ======================================================================
class Config(object):
    """Config Class.  Use a configuration file to control your program
    when you have too much state to pass on the command line.
    Reads the <program_name>.cfg or ~/.<program_name>.cfg file for
    configuration options.
    Handles booleans, integers and strings inside your cfg file.
    """
    def __init__(self,program_name=None):
        self.config_parser = configparser.ConfigParser()
        if not program_name:
            program_name = os.path.basename(sys.argv[0].replace('.py',''))
        self.config_parser.read([program_name+'.cfg',
                                 os.path.expanduser('~/.'+program_name+'.cfg')])
    def get(self,section,name,default):
        """returns the value from the config file, tries to find the
        'name' in the proper 'section', and coerces it into the default
        type, but if not found, return the passed 'default' value.
        """
        try:
            if type(default) == type(bool()):
                return self.config_parser.getboolean(section,name)
            elif type(default) == type(int()):
                return self.config_parser.getint(section,name)
            else:
                return self.config_parser.get(section,name)
        except:
            return default

# ======================================================================
class Application(object):
    def __init__(self,argv):
        self.config = Config()
        self.parse_args(argv)
        self.adjust_logging_level()

    def parse_args(self,argv):
        """parse commandline arguments, use config files to override
        default values. Initializes:
        self.args: a dictionary of your commandline options,
        """
        parser = argparse.ArgumentParser(description="A python3 skeleton.")
        parser.add_argument(
            "-v","--verbose",
            dest="verbose",
            action='count',
            default=self.config.get("options","verbose",0),
            help="Increase verbosity (add once for INFO, twice for DEBUG)"
        )
        # more args https://docs.python.org/3/library/argparse.html
        # XXX add more options here XXX
        self.args = parser.parse_args(argv)

    def adjust_logging_level(self):
        """adjust logging level based on verbosity option
        """
        log_level = logging.WARNING # default
        if self.args.verbose == 1:
            log_level = logging.INFO
        elif self.args.verbose >= 2:
            log_level = logging.DEBUG
        logging.basicConfig(level=log_level)

    def run(self):
        """The Application main run routine
        XXX extend this XXX
        """
        # -v to see info messages
        logging.info("Args: {}".format(self.args))
        # -v -v to see debug messages
        logging.debug("Debug Message")
        # we'll always see these
        logging.warn("Warning Message")
        logging.error("Error Message")
        print("Hello, Skeleton")
        return 0

# ======================================================================
def main(argv):
    """ The main routine creates and runs the Application.
    argv: list of commandline arguments without the program name
    returns application run status
    """
    app = Application(argv)
    return app.run()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
