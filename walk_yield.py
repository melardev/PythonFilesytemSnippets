"""
Snippet on using os.walk along with yield, this is the way to go when looking for files
using os.walk, you can't wait os walk to finish before processing because this may take a long time.
Instead you may want to process files as they are getting found, this is what we achieve with yield in this snippet
If you don't know what yield does, look at my yield snippet on PythonBasicsSnippets on my Github, or google it to
learn more
"""
import os


def func(startpath, searched_extension):
    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in searched_extension:
                yield absolute_path


for interesting_file in func('./', ['py', 'cpp']):
    print(interesting_file)
