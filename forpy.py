#!/bin/python

import pyshark
import sys
import argparse

#Print usage function

def print_usage():
  print """
=====================================
ForPy - the network forensics toolkit
=====================================

Usage:

forpy.py -f <capturefile>

"""



#Importing the Capture file

globcapture = 0

def import_file(cap_file):
  global globcapture
  globcapture = pyshark.FileCapture(cap_file)
  print globcapture[0] #Test 

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


#Main

def main():
  

  parser = argparse.ArgumentParser(description='Modular Network Forensics tool')

  parser.add_argument('-f', '--file', help="File to be Analysed")
  args = parser.parse_args()
  import_file(args.file)
  


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print_usage()
  else:
    main()
