import os

def connect(dbname):
    try:
        f = open(dbname, 'r+b')
    except IOError: #do the following if the open() function fails
        fd = os.open(dbname, os._O_RDWR | os.O_CREAT)
        #O_CREAT is an open-time flag that will create a flag if file doesn't exist
        #O_RDWR will make the file open for both reading and writing
        f = os.fdopen(fd, 'r+b')
        #connect to the open file object connected to file descriptor fd
    return DBDB(f)
