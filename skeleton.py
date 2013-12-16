#!/usr/bin/env python
"""
skeleton.py - a skeleton starting-point for python scripts by Roger Allen.

Any copyright is dedicated to the Public Domain.
http://creativecommons.org/publicdomain/zero/1.0/
You should add your own license here.

"""
import os
import sys
import logging
from optparse import OptionParser

# ======================================================================
class Application(object):
  def __init__(self,argv):
    self.parse_args(argv)
    self.adjust_logging_level()

  def parse_args(self,argv):
    """parse commandline arguments, use config files to override
    default values. Initializes:
    self.options: a dictionary of your commandline options,
    self.args:    a list of the remaining commandline arguments
    """
    parser = OptionParser()
    # config file has verbosity level
    parser.add_option(
      "-v","--verbose",
      dest="verbose",
      action='count',
      default=0,
      help="Increase verbosity (can use multiple times)"
      )
    # XXX add more options here XXX
    self.options, self.args = parser.parse_args(argv)

  def adjust_logging_level(self):
    """adjust logging level based on verbosity option
    """
    log_level = logging.WARNING # default
    if self.options.verbose == 1:
      log_level = logging.INFO
    elif self.options.verbose >= 2:
      log_level = logging.DEBUG
    logging.basicConfig(level=log_level)
    
  def run(self):
    """The Application main run routine
    XXX extend this XXX
    """
    # -v to see info messages
    logging.info("Options: %s, Args: %s" % (self.options, self.args))
    # -v -v to see debug messages
    logging.debug("Debug Message")
    # we'll always see these
    logging.warn("Warning Message")
    logging.error("Error Message")
    print "Hello, World"
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
