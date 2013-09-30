#!/usr/bin/python

import sys
import os

#We will use our generator.py script from HW2
#But first we need to tell Python, that he must search for modules
#in that directory
_current_path = os.path.dirname(os.path.abspath((__file__)))
sys.path.append(os.path.join(_current_path, '../../2/hw'))

USAGE_MESSAGE = '''You missed something:)
Usage: python generate.py <numfiles> <numcols> <numlines> [filename]

'''
DEFAULT_FILENAME = "junk"

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print USAGE_MESSAGE
    else:
        import generator

        numfiles = int(sys.argv[1])
        numcols = int(sys.argv[2])
        numlines = int(sys.argv[3])
        filename = DEFAULT_FILENAME if len(sys.argv) != 5 else sys.argv[4]
        for i in range(1, numfiles+1):
            fname = filename + "-%d.dat" % i
            generator.generate_file(numcols, numlines, fname)