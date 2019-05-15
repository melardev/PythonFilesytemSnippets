import os
import stat
import errno
import sys


def dir_exists(dir_path):
    try:
        dir_exists = stat.S_ISDIR(os.stat(dir_path).st_mode)
        return dir_exists
    except OSError as e:
        if e.errno == errno.ENOENT:
            return False

    return False  # unknown error


sys.stdout.write('C:/Windows dir exists? %r\n' % dir_exists('C:/Windows'))
sys.stdout.write('/root Dir exists? %r\n' % dir_exists('/root'))
