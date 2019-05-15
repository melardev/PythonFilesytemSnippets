'''
Usage of pathlib, available since Python 3.4
'''
from pathlib import Path

file_path = Path('C:/windows')
print('About C:/Windows')
print('exists? %r' % file_path.exists())
print('is dir? %r' % file_path.is_dir())
print('About C:/Windows / System32')
file_path_changed = file_path / 'System32'
print('exists? %r' % file_path_changed.exists())
print('is dir? %r' % file_path_changed.is_dir())

print('About C:/Windows / System32 / nonexistent')
file_path_changed = file_path / 'System32' / 'non_existent'
print('exists? %r' % file_path_changed.exists())
print('is dir? %r' % file_path_changed.is_dir())
