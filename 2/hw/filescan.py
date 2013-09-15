#!/usr/bin/python

import sys
import os

USAGE_MESSAGE = '''Filename is missing.
Usage: python filescan.py FILENAME'''
SUFFIX = "_filtered."

def scan_straightforward(filein, fileout=None):
    '''Main work is done here. This function must read file with filename filein,
    scan it and then output filtered data into file with name fileout.

    Parameters
    ----------
    filein : str
        Filename of file to filter.
    fileout : str, optional
        Filename of the output file. If None, filename for output file
        will be contructed using default suffix.

    Returns
    -------
    result : boolean
        True if filtering was succesful (i.e. filtered file was successfully written), False otherwise

    Examples
    --------
    >>> scan_straightforward('experiment254.dat')

    >>> scan_straightforward('experiment254.dat', 'experiment254_filtered.dat')
    '''
    if not fileout:
    	fileout = SUFFIX.join(filein.rsplit('.',1))
    #Check if output file already exists
    if os.path.exists(fileout):
        print "File %s already exists." % (fileout)
        return False

    try:
        fin = open(filein, 'r')
        fout = open(fileout, 'w')
        #Scaning through input file
        for line in fin:
            #Have we 'nan' in this line?
            if line.find('nan') != -1:
                continue
            #Is this a header line?
            if line.find('#') != -1:
                fout.write(line)
                continue
            #Now we know it's data line. Translating text into numbers
            numbers = []
            for strnum in line.split(' ')[1:]:
                numbers.append(float(strnum))
            #Check if criterion is satisfied and writing line to output file
            if sum(numbers) < .5 * len(numbers):
                fout.write(line)
        #Closing files
        fin.close()
        fout.close()
        return True
    except (IOError, ValueError) as e:
        print e
        return False

def scan_clean(filein, fileout=None):
    '''Cleaner implementation of scaning using Python's with statement and list comprehensions.

    Parameters
    ----------
    filein : str
        Filename of file to filter.
    fileout : str, optional
        Filename of the output file. If None, filename for output file
        will be contructed using default suffix.

    Returns
    -------
    result : boolean
        True if filtering was succesful (i.e. filtered file was successfully written), False otherwise

    Examples
    --------
    >>> scan_clean('experiment254.dat')

    >>> scan_clean('experiment254.dat', 'experiment254_filtered.dat')
    '''
    if not fileout:
        fileout = SUFFIX.join(filein.rsplit('.',1))
    if os.path.exists(fileout):
        print "File %s already exists." % (fileout)
        return False

    try:
        with open(filein, 'r') as fin, open(fileout, 'w') as fout:
            for line in fin:
                if line.find('#') != -1:
                    fout.write(line)
                    continue
                numbers = [float(strnum) for strnum in line.lower().split(' ')[1:]]
                if sum(numbers) < .5 * len(numbers):
                    fout.write(line)
        return True
    except (IOError, ValueError) as e:
        print e
        return False

def scan(filein, fileout=None):
    scan_clean(filein, fileout)

if __name__ == "__main__":
    #Checking, whether command line arguments are passed correctly
    #Remember, that sys.argv[0] contains script name. filescan.py, in this case
    if len(sys.argv) != 2:
        print USAGE_MESSAGE
    else:
        #Reading input filename
        filein = sys.argv[1]
        scan(filein)