#!/usr/bin/env python3
# Title:    Python Mail CSV Parser
# Author:   Matthew Williams
# Date:     11/6/2020
import os
import sys
import csv
import argparse
#
# VARIABLE DEFINITION
#
description = """
This program is to parse out an mail address from a csv or a directory with csv's in it.
"""
#
# END OF VARIABLE DEFINITION
#
#
# PROGRAM DEFINITION
#
def main():
    # PARSING Creation
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--directory', dest='csv_directory',  default='none', help='Parse all CSV files in this directory, Ignored by default')
    parser.add_argument('--file', dest='csv_file', default='none', help='CSV to parse')
    parser.add_argument('--email', dest='email', default='nope@nope.org', help='Email to look for')
    args = parser.parse_args()
    try:
        if os.path.exists(args.csv_file) and args.csv_directory == "none":
            with open(args.csv_file, 'rt') as f:
                 reader = csv.reader(f, delimiter=',')
                 for row in reader:
                      for field in row:
                          if field == args.email:
                              print ("is in file")
                              exit_script(0)
        elif args.csv_file == "none":
            for root, dirs, files in os.walk(args.csv_directory):
                for file in files:
                    if file.endswith(".csv"):
                        print(os.path.join(root, file))
                        with open(os.path.join(root, file), 'rt') as f:
                             reader = csv.reader(f, delimiter=',')
                             for row in reader:
                                  for field in row:
                                      if field == args.email:
                                          print (field + " is in file: " + file)
        else:
            print("That file does not exist or you did not select any")
    except Exception as ex:
        print("Cannot parse that csv!")
        print(ex)
        exit_script(1)
    exit_script(0)
def exit_script(exit_code):
    # Function to exit script, will build exception handling in the future
    if exit_code == 1:
        print("something broke...")
    print("Exiting script.")
    sys.exit(exit_code)
#
# PROGRAM DEFINITION
#


if __name__ == '__main__':
    main()
