"""System info: Take a user specified directory and using python display all the files in that directory
and all the environment variables present in the system
"""

from sys import argv
import os

# User Input
path = argv[1]

try:
    # Directory File List
    dir_path = os.listdir(path)
    print(dir_path)
    # Environment Variables
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))
except: # Error Handling
    print("Not Correct Input")


