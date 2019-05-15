"""
Copy a file using shutil module
"""
import os
import shutil
import tempfile

# Generate a random file with .txt extension that will leave on the temporary directory without overriding other file
original_file = tempfile.mktemp(".txt")
# create the temporary file
with open(original_file, "w") as fd:
    fd.write('Some random content')

copied_file = original_file + ".copy"
print('Original File: ', original_file, " ;Copied file will reside on: ", copied_file)

shutil.copy(original_file, copied_file)

if os.path.isfile(copied_file):
    print("File has been copied successfully")

print('Reading temp file contents')

with open(copied_file, 'r') as fd:
    print(fd.read())

print('Done')
