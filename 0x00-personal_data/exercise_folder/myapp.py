# myapp.py

import logging # Imports the logging module, which provides a flexible framework for emitting log messages from Python programs.
import mylib   # Imports mylib.py from the current directory. Imports a module named mylib. This module is assumed to contain a function named do_something() which will be called later in the code.

logger = logging.getLogger(__name__) # Creates a logger object with the name __name__. The __name__ variable is set to the name of the current module.
# Retrieves a logger instance with the name '__main__'. This logger will be used to log messages in this module and any other modules that import this one.

def main(): # Defines a function called main()
    logging.info('Started') # Logs an INFO message with the string 'Started'. The logging module provides a set of functions for logging messages at different levels (e.g., INFO, WARNING, ERROR, etc.). that will be executed when the program starts.
    mylib.do_something() # Calls the do_something() function from mylib.py.
    logging.info('Finished') # Logs an INFO message with the string 'Finished'. that will be executed when the program finishes. This is an example of importing and using a library in a Python program.
    
if __name__ == '__main__': # Checks if the module is being run as the main program. If it is, the code block below will be executed.
    main() # Calls the main() function. This is the entry point of the program. The main() function logs messages and calls the do_something() function from mylib.py.
