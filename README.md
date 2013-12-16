# Pyskel

Pyskel contains a bit of "skeleton" code to use for a starting point to a python program.  It is meant to quickly give you the ability to start coding an "Application" class after parsing the commandline options.

There are 2 starting points: 
* skeleton.py
* skeleton_with_config.py

As you may have guessed, the 2nd version allows the use of a configuration file.  Sometimes this is a handy way to specify the default behavior for programs with lots of commandline options.


# Usage

1. Copy skeleton.py and rename to your own command name.
2. Adjust the comments at the top of the file to fill in your own program info.
3. Search for "XXX" to adjust for your own usage.

## Options

Inside Application.parse_args, you will add your own commandline options.  This will initialize the Application class self.options with a dictionary of your commandline options and self.args with a list of the remaining commandline arguments.  

The Application.parse_args and Application.adjust_logging_level routines show how the self.options.verbose value ise setup & used.  

## Config File

See the [python configparser documentation](http://docs.python.org/library/configparser.html) for details on the file format.  If you wanted to specify the verbosity level, it would look like:

    [options]
    verbose: 1

The config file may be located in the current directory or in your home directory.  The name will match the name of your script.  For example, if your script is name cool_script.py, the local directory config will need to be named cool_script.cfg.  If you want a home directory config file, it will be called .cool_script.cfg.  In the home directory case, it will need to be prefaced with a "." per standard unix philosophy. 

