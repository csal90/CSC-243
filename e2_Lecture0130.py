# safeOpen() that opens a file and handles the exception when the file doesn't exists
# It returns the file object returned from opening the file or nothing when
# such exception occurs.

def safeOpen(fname):
    try:
        return open(fname, 'r')
    except FileNotFoundError:
        pass
