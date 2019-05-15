import tempfile
import os
import shutil

# Generate a name of a file that will not override anything on the system temporary folder
temp_dir = tempfile.mktemp(".dir")
os.mkdir(temp_dir)

# Two lines for two folders
# os.mkdir(temp_dir + '/subdir')
# os.mkdir(temp_dir + '/subdir/subdir2')

# One liner for two, or more folders
os.makedirs(temp_dir + '/subdir/subdir2')
open(temp_dir + '/subdir/subdir2/temp.txt', 'w').close()
copied_dir = temp_dir + ".copy"

print('Copying directory tree: ', temp_dir, " ; to: ", copied_dir)
shutil.copytree(temp_dir, copied_dir)

if os.path.isdir(copied_dir) and os.path.isdir(copied_dir + '/subdir/subdir2') \
        and os.path.isfile(copied_dir + '/subdir/subdir2/temp.txt'):
    print("Successfully copied the whole tree")
