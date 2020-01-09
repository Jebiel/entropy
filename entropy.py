#!/usr/bin/env python
'''
Calculate Shannon Entropy (min bits per byte-character)
original source: https://www.kennethghartman.com/calculate-file-entropy/
'''

__version__ = '0.1'
__description__ = 'Calculate Shannon Entropy for given file'

import sys
import math
import collections

def main():
    entropy()

def entropy():
    print('Opening file {}...'.format(sys.argv[1]))
    with open(sys.argv[1], 'rb') as f:
        byteArr = list(f.read())
    fileSize = len(byteArr)
    print
    print('File size in bytes: {:,d}'.format(fileSize))
    # calculate the frequency of each byte value in the file
    print('Calculating Shannon entropy of file. Please wait...')
    e = 0
    counter = collections.Counter(byteArr)
    l = len(byteArr)
    for count in counter.values():
        # count is always > 0
        p_x = count / l
        e += - p_x * math.log2(p_x)
    print('Shannon entropy: {}'.format(e))
    print


if __name__== "__main__":
    main()
