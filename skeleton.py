#!/usr/bin/env python
"""
skeleton.py - a skeleton starting-point for python scripts by Roger Allen.

Any copyright is dedicated to the Public Domain.
http://creativecommons.org/publicdomain/zero/1.0/
You should add your own license here.

TODO customize this
"""

import argparse
import logging
import sys
from typing import List


# ======================================================================
class Application:
    """Application is a class to organize this commandline program.  Feel
    free to rename for your use-case. The main features it enables are an
    argparse Namespace of commandline arguments and automatic setting of
    the logging verbosity.
    TODO customize this comment.
    """

    def __init__(self, argv: List[str]) -> None:
        """Parse commandline arguments and set logging level.

        Args:
            argv: commandline arguments after the executable name.
        """
        self.parse_args(argv)
        self.set_logging_level()

    def parse_args(self, argv: List[str]) -> None:
        """Parse commandline arguments.  Updates self._args

        Args:
            argv: commandline arguments after the executable name.
        """
        parser = argparse.ArgumentParser(description="A python3 skeleton.")
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            action="count",
            default=0,
            help="Increase verbosity (add once for INFO, twice for DEBUG)",
        )
        # TODO add more options here see https://docs.python.org/3/library/argparse.html
        self._args = parser.parse_args(argv)

    def set_logging_level(self):
        """Adjust logging level based on verbosity commandline arguments."""
        log_level = logging.WARNING  # default
        if self._args.verbose == 1:
            log_level = logging.INFO
        elif self._args.verbose >= 2:
            log_level = logging.DEBUG
        logging.basicConfig(
            format="%(levelname)s:%(funcName)s:%(message)s", level=log_level
        )

    def run(self) -> int:
        """The Application main run routine
        TODO update comment
        """
        # Control log messages via -v commandline option
        # we'll always see these
        logging.error("Error Message")
        logging.warning("Warning Message")
        # -v to see info messages
        logging.info("Args: {}".format(self._args))
        # -v -v to see debug messages
        logging.debug("Debug Message")

        # TODO add code
        print("Hello, Skeleton")

        return 0


# ======================================================================
def main(argv: List[str]) -> int:
    """Creates and runs the Application.

    Args:
        argv: list of commandline arguments without the program name

    Returns:
        application run status
    """
    return Application(argv).run()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
