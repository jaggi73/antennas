#!/usr/bin/env python

# Used to calculate horn antenna aperature and gain from waveguide aperature and
#  and length of panel
# Based off formulas found here:
# http://www.ece.mcmaster.ca/faculty/nikolova/antenna_dload/current_lectures/L18_Horns.pdf

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-a", type=float, help="waveguide h-plane length in meters")
parser.add_argument("-b", type=float, help="waveguide e-plane length in meters")
parser.add_argument("-l", type=float, 
      help="length of panel from opening of waveguide to opening of aperture in meters")
parser.add_argument("-f", "--freq", type=float, default=1420405751.7667, 
                    help="frequency in Hz, hydrogen line if not specified")
args = parser.parse_args()

# Calculate wavelength
c = 299792458.0;
eap = 0.51;
lamda = c/args.freq;

# Calculate aperture width and height
B = 0.5 * (args.b + math.sqrt(math.pow(args.b,2) + 8 * lamda * args.l))
A = 0.5 * (args.a + math.sqrt(math.pow(args.a,2) + 12 * lamda * args.l))

# Calculate length from aperature to Apex in wavefeed
R_a_apex = (args.l * A) / (A - args.a)
R_b_apex = (args.l * B) / (B - args.b)

# Calculate length from aperature to wavefeed
Ra = R_a_apex - ((args.a * R_a_apex) / A)
Rb = R_b_apex - ((args.b * R_b_apex) / B)

# Gain
G = 10 * math.log10((4 * math.pi / math.pow(lamda,2)) * eap * A * B)

print ("H-plane length of Aperture, A : %.4f m %.4f in" % (A, A*39.37))
print ("E-plane length of Aperture, B : %.4f m %.4f in" % (B, B*39.37))
print ("Length of panel to waveguide  : %.4f m %.4f in" % (Ra, Ra*39.37)) 
print ("1/4 Wavelength                : %.4f m %.4f in" % (lamda / 4, lamda*39.37/4))
print ("Gain for optimal efficiency   : %.2f dBi" % (G)) 
# print ("Length of A panel to apex: %.4f m %.4f in" % (R_a_apex, R_a_apex*39.37)) 
# print ("Length of B panel to apex: %.4f m %.4f in" % (R_b_apex, R_b_apex*39.37)) 

