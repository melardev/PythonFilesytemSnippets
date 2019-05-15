import os.path

file_path = 'D:/workspace/python/PythonSnippets/filesystem_snippets/get_parent_directory.py'

print(os.path.dirname(file_path))

# We can also iterate n levels shallow
levels = 3
print('Getting parent directory 3 levels shallow')
for i in range(0, levels):
    file_path = os.path.dirname(file_path)
    print(file_path)
