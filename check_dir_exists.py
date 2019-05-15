"""
This demo file shows how to test if a directory exists or not in python
I check for a directory present only on Windows and other only on Unix based systems
"""
import os
import sys

# Remainder of character formats used: %r calls behind the scenes __repr__, %s is like str()

sys.stdout.write('C:/Windows directory does exist? %r\n' % os.path.isdir("C:/Windows"))
sys.stdout.write('/root does exist? %s\n' % os.path.exists('/root'))
