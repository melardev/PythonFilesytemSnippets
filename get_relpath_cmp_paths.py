import os

file_path = 'C:/Users/Melardev/my_file.py'
other_file_path = 'C:/Users/Melardev/example_module/my_other_file.py'

# basically this returns the relative path we have to use from other_file_path
# to get to file_path
print(os.path.relpath(file_path, other_file_path))
