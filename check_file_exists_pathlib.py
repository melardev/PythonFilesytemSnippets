"""
Snippet on how to use pathlib to check if a file exists,
I would not use this approach because pathlib is a module introduced in Python 3.4
so your app will crash if you use it with Python 2.7. There are anyways many ways
of checking if file exists in a portable way supporting Python 2.7 and Python 3+
"""
from pathlib import Path

path = 'D:/temp/text_file.txt'
config = Path('D:/temp/text_file.txt')
if config.is_file():
    with open(path, 'rb') as fd:
        file_data = fd.read().decode('utf-8')
        print(file_data)
else:
    print('File not found')
