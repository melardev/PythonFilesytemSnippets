path = 'D:/temp/text_file.txt'
try:
    with open(path, 'rb') as fd:
        file_data = fd.read().decode('utf-8')
        print(file_data)

except FileNotFoundError:
    print('File not found')
