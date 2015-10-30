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



#Importing the Capture file

globcapture = 0

def import_file(cap_file):
  global globcapture
  globcapture = pyshark.FileCapture(cap_file)
  #print capture[0] #Test 

#Print out all IP's in the capture file

def list_ips(capture):
  ip_list = []
  for packet in capture:
    ip_list.append(packet.ip.addr)
  uniq_ip_list = list(set(ip_list))
  print """
=====================================
  Unique IP's 
====================================
"""
  for x in uniq_ip_list: #test
    print x


#Argument Parsing Section

if len(sys.argv) != 2:
  print_usage()
else:
  cap_file = sys.argv[1]
  print "Analysing Capture File: " + cap_file
  import_file(cap_file)
  list_ips(globcapture)

