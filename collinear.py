#!/usr/bin/env python

# Used to calculate length of collinear antenna

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--freq", type=float, default=1420405751.7667, 
                    help="frequency in Hz, hydrogen line if not specified")
args = parser.parse_args()

# Calculate wavelength - use velocity factor of 0.951 for copper wire
c = 299792458.0 * 0.951;
lamda = c/args.freq;

total = lamda/2 + 3*lamda/4 + (3*lamda/4*0.85)

print ("Three sections starting from connector")
print ("Section 1      : %.4f m %.4f in" % (lamda/2, (lamda/2)*39.37))
print ("Section 2      : %.4f m %.4f in" % (3*lamda/4, (3*lamda/4)*39.37))
print ("Section 3      : %.4f m %.4f in" % (3*lamda/4*0.85, (3*lamda/4)*39.37*0.85))
print ("Total          : %.4f m %.4f in" % (total, total*39.37))
print ("1/4 Wavelength : %.4f m %.4f in" % (lamda / 4, lamda*39.37/4))
