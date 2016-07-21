# Pyskel

Each of these python files contains "skeleton" code to use for a starting point to a python program.  It is meant to quickly give you the ability to start coding an "Application" class after parsing the commandline options.

There are 4 starting points:
* skeleton3.py
* skeleton_with_config3.py
* skeleton.py
* skeleton_with_config.py

As you may have guessed, the 2nd version allows the use of a configuration file.  Sometimes this is a good way to specify the default behavior for programs with lots of commandline options.  The 3rd & 4th files are python2 variants.  For any new programs you really ought to be using python 3 as python 2 will be deprecated soon.

This code is originally from my repository on https://bitbucket.org/rallen/pyskel  Moving it here for latest updates.

# Usage

1. Copy skeleton3.py (or skeleton_with_config3.py) and rename to your own command name.
2. Adjust the comments at the top of the file to fill in your own program info, including the license.
3. Search for "XXX" to adjust for your own usage & start extending the Application class.

## Options

Inside Application.parse_args, you will add your own commandline options.  This will initialize the Application class self.args with a dictionary of your commandline options.

The Application.parse_args and Application.adjust_logging_level routines show how the self.args.verbose value ise setup & used.

## Config File

See the [python configparser documentation](http://docs.python.org/library/configparser.html) for details on the file format.  If you wanted to specify the verbosity level, it would look like:

    [options]
    verbose: 1

The config file may be located in the current directory or in your home directory.  The name will match the name of your script.  For example, if your script is named cool_script.py, the local directory config will need to be named cool_script.cfg.  If you want a config file in your home directory, it will be called .cool_script.cfg.  In the home directory case, it will need to be (prefaced with a "." per standard unix practice).

# License

Any copyright is dedicated to the Public Domain.
http://creativecommons.org/publicdomain/zero/1.0/

You should add your own license to the files after you modify them.
