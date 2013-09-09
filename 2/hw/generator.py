#!/usr/bin/python

import sys
import numpy as np

USAGE = 'Usage: python generator.py <numcolumns> <numlines> [filename]'
DEFAULT_FILENAME = "experiment.dat"
NAN_PORTION = 0.2

def check_cl_params(params):
    '''Function to check whether CL params are correct.

    Parameters
    ----------
    params : str[]
        Raw command line parameters without name of a script
    Returns
    -------
    out : tuple
        Preprocessed params (converted as needed) if possible, else None

    Examples
    --------
    >>> check_cl_params(['4','100','exp1.dat'])
    (4, 100, 'exp1.dat')

    >>> check_cl_params(['4','100'])
    (4, 100)

    >>> preprocessed_params = check_cl_params(['4'])
    >>> print preprocessed_params
    None

    '''

    try:
        return (int(params[0]), int(params[1]), params[2]) \
                if len(params)==3 \
                else (int(params[0]), int(params[1]))
    except Exception, e:
        return None

def generate_file(numcolumns, numlines, filename=None):
    '''Function to generate file with data for filtering.

    Parameters
    ----------
    numcolumns : int
        Number of columns in file (not counting first column with line number).
    numlines : int
        Number of lines.
    filename : str, optional
        Name of output file.

    Examples
    --------
    Creates and fills file with data and default name experiment.dat:

    >>> preprocessed_params = check_cl_params(['4','100'])
    >>> generate_file(*preprocessed_params)

    Creates and fills file with data and default name exper.dat:

    >>> preprocessed_params = check_cl_params(['4','100', 'exper.dat'])
    >>> generate_file(*preprocessed_params)  
    
    '''

    numelements = numlines * numcolumns
    data = np.random.sample((numelements))
    data[np.random.randint(0, numelements, int(NAN_PORTION * numelements))] = np.NaN
    indices = np.arange(1, numlines+1).reshape((numlines,1))
    resulting_array = np.hstack((indices, data.reshape((numlines,numcolumns))))
    header = 'NUM ' + ' '.join(['X'+str(i) for i in range(1,numcolumns+1)])
    np.savetxt(filename if filename else DEFAULT_FILENAME,
            resulting_array,
            fmt="%d" + " %.8e" * numcolumns,
            header=header)

if __name__ == "__main__":
    preprocessed_params = check_cl_params(sys.argv[1:])
    if not preprocessed_params:
        print USAGE
    else:
        generate_file(*preprocessed_params)