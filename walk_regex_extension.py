"""
Basic os walk with regex module snippet on how to find python files
If you are looking to move this to a function and to be efficient look the walk_yield demo
"""
import os
import re

root_path = "./"
# Math .py at the end of the string
contains = "\.py$"

for scanned_path, list_dirs, list_files in os.walk(root_path):
    for file in list_files:
        match = re.search(contains, file)
        if match is not None:
            print("[+] Found match in " + os.path.join(scanned_path, file))
