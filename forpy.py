import pyshark
import sys


#Print usage function

def print_usage():
  print """
=====================================
ForPy - the network forensics toolkit
=====================================

Usage:

forpy.py <capturefile>

"""

#Argument Parsing Section

if len(sys.argv) < 2:
  print_usage()
else:
  print sys.argv[1]  


