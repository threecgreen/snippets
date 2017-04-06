"""
Basic Python logging configuration with timestamps and the option to save to a file.
"""
import logging


# Set default logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(level=logging.DEBUG,
                    # Optional write logging output to file. If no file, logging will be printed to stdout
                    filename="schecker.log",
                    # a: append (add to the same file), w: write (overwrite every time the program restarts)
                    filemode="a",
                    # Logging formatting with time, name and logging level before message
                    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                    datefmt="%y-%m-%d %H:%M")
