import os

path = "c:\\"

current_level_deep = 0
for (path, dirs, files) in os.walk(path):
    print(path)
    print(dirs)
    print(files)
    # some depth, otherwise this may take a while to traverse the whole tree
    current_level_deep += 1
    if current_level_deep >= 2:
        break
