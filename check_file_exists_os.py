import os

path = 'D:/temp/text_file.txt'
if os.path.isfile('D:/temp/text_file.txt'):
    with open(path, 'rb') as fd:
        file_data = fd.read().decode('utf-8')
        print(file_data)
else:
    print('File does not exist')
