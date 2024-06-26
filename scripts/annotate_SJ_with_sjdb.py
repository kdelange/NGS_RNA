#!/usr/bin/env python3

### GAD PIPELINE ###
## annotate_SJ_with_sjdb.py
## Description : annotate a SJ file with data from  sjdb file generated by star2 2 pass
## Usage : python annotate_SJ_with_sjdb.py -i <input file> -o <output file> -j <sjdb file>
## Output : a tabulated SJ file containing sjdb annotation
## Requirements : python 2.7

## Author : Emilie.Tisserant u-bourgogne fr, yannis.duffourd u-bourgogne fr
## Creation Date : 20170331
## last revision date : 20201009
## Known bugs : None

import getopt
import os
import sys


# Options
try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:j:o:')
    for opt, arg in opts:
        if opt in ("-i"):
            infile = arg
        elif opt in ("-j"):
            sjdb = arg
        elif opt in ("-o"):
            sys.stdout = open(arg, 'w')
except getopt.GetoptError:
    print('usage : ')
    sys.exit(1)

junclist, juncslist, juncelist = [], [], []
stream = open(sjdb, 'r')
for line in stream:
    line = line.strip()
    tabs = line.split('\t')
    junclist.append(tabs[0]+":"+tabs[1]+"-"+tabs[2])
    juncslist.append(tabs[0]+":"+tabs[1])
    juncelist.append(tabs[0]+":"+tabs[2])
stream.close()


# TODO strand

instream = open(infile, 'r')
for line in instream:
    line = line.strip()
    tabs = line.split('\t')
    chrm = tabs[0]
    start = int(tabs[1])
    end = int(tabs[2])
    if chrm+":"+str(start)+"-"+str(end) in junclist:
        print(line+"\tAnnotated")
    elif chrm+":"+str(start) in juncslist and chrm+":"+str(end) in juncelist:
        print(line+"\tBoth")
    elif chrm+":"+str(start) in juncslist or chrm+":"+str(end) in juncelist:
        print(line+"\tOne")
    else:
        print(line+"\tNeither")
instream.close()
