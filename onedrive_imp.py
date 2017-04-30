#!/home/carter/anaconda3/bin/python
"""
The OneDrive synchronizer (https://github.com/skilion/onedrive) I was using on Linux was causing problems by 
duplicating certain file types. This script cleans up the duplicates on running.

Example:
    With default configuration with ~/OneDrive as the location of the OneDrive directory
    $ python onedrive_imp.py 
    
    Running with a different OneDrive location.
    $ python onedrive_imp.py --path /home/example/Documents/OneDrive

Logging directory: /var/log/onedrive-imp.log
"""
import argparse
import logging
import os
import socket
from subprocess import Popen, PIPE, STDOUT


def cleanup_duplicate_files(top_directory: str=os.path.expanduser("~/OneDrive")):
    logging.info("Cleaning up any duplicate files.")
    if not os.path.exists(top_directory):
        logging.critical("{} does not exist. Program exiting".format(top_directory))
        raise OSError("{} does not exist.".format(top_directory))

    # Duplicate files appended with -{computer_name}.extension
    computer_name = socket.gethostname()

    for root, dirs, files in os.walk(top_directory):
        for file in files:
            if "-" + computer_name in file:
                os.remove(os.path.join(root, file))
                logging.info("{} was deleted.".format(os.path.join(root, file)))


def log_subprocess_output(pipe):
    for line in iter(pipe.readline, b''): # b'\n'-separated lines
        logging.info('Line from subprocess: %r', line)


def onedrive() -> int:
    logging.info("Starting OneDrive sync.")
    try:
        process = Popen("onedrive", stdout=PIPE, stderr=STDOUT)
        with process.stdout as pipe:
            log_subprocess_output(pipe)
    except (OSError, ChildProcessError) as exc:
        logging.warning("Exception occurred: {}".format(exc))
        logging.critical("Subprocess failed.")
        raise exc
    return process.wait()


def main(top_directory):
    logging.info("Starting OneDrive-imp.")
    if onedrive():
        exit(-1)
    if onedrive():
        exit(-1)
    if top_directory is None:
        cleanup_duplicate_files()
    else:
        cleanup_duplicate_files(top_directory)
    logging.info("Successfully completed sync.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        # Optional write logging output to file. If no file, logging will be printed to stdout
                        filename=os.path.expanduser("~/bin/log/onedrive-imp.log"),
                        # a: append (add to the same file), w: write (overwrite every time the program restarts)
                        filemode="a",
                        # Logging formatting with time, name and logging level before message
                        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                        datefmt="%y-%m-%d %H:%M")

    parser = argparse.ArgumentParser(
        description="Improved OneDrive syncing for Linux.",
    )
    parser.add_argument("-p", "--path", type=str, required=False, help="Path to OneDrive directory.")
    args = parser.parse_args()
    main(args.path)
