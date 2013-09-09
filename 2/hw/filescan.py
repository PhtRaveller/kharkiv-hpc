#!/usr/bin/python

import sys

USAGE_MESSAGE = '''Filename is missing.
Usage: python filescan.py FILENAME'''
SUFFIX = "_filtered."

def scan(filein, fileout=None):
    '''Main work is done here. This function must read file with filename filein,
    scan it and then output filtered data into file with name fileout.

    Parameters
    ----------
    filein : str
        Filename of file to filter.
    fileout : str, optional
        Filename of the output file. If None, filename for output file
        will be contructed using default suffix.

    Examples
    --------
    >>> scan('experiment254.dat')

    >>> scan('experiment254.dat', 'experiment254_filtered.dat')
    '''
    if not fileout:
    	fileout = SUFFIX.join(filein.rsplit('.',1))

    #TODO: Enter your code here

if __name__ == "__main__":
    #Checking, whether command line arguments are passed correctly
    #Remember, that sys.argv[0] contains script name. filescan.py, in this case
    if len(sys.argv) != 2:
        print USAGE_MESSAGE
    else:
        #Reading input filename
        filein = sys.argv[1]
        scan(filein)