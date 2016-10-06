#!/usr/bin/python
#0

""" Module/Script Description

This Module/Script can help to get a subset of sequences in FASTA format included in or not in the list.

Copyright (c) 2008 Xiaowei Chen <bighanchen2008@gmail.com>
This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file COPYING included with
the distribution).
@status:  experimental
@version: $Revision$
@author:  Xiaowei Chen
@contact: bighanchen2008@gmail.com
"""

# ------------------------------------
# python modules
# ------------------------------------

import sys
import string
import re
import os

# ------------------------------------
# constants
# ------------------------------------

# ------------------------------------
# Misc functions
# ------------------------------------

# ------------------------------------
# Classes
# ------------------------------------

# ------------------------------------
# Main
# ------------------------------------

if __name__=="__main__":
    if len(sys.argv)==1:
        print "Usage: "+sys.argv[0]+" list .fa > sub.fa"
    else:
        flag=0
        start=re.compile("^>")
        sublist=[]

        for row in open(sys.argv[1]):
            row=row.rstrip(os.linesep)
            row=row.split("\t")
            #sublist.append(row[0])

            sublist.append(row[2])

        for line in open(sys.argv[2]):
            line=line.rstrip(os.linesep)
            if start.match(line):
                item=line.split(">")
                if item[1] in sublist:
                    print ">"+item[1]
                    flag=1
                else:
                    flag=0
            else:
                if flag==1:
                    print line
        '''
            miRNAreadsdict[row]=1
            row=ft.readline().rstrip("\n\r")
        mappingreadsdict={}
        fp=open(sys.argv[1])
        row=fp.readline().rstrip("\n\r")
        while row:
            mappingreadsdict[row]=1
            row=fp.readline().rstrip("\n\r")
        
        fh=open(sys.argv[3])
        line=fh.readline().rstrip("\n\r")
        while line:
            if start.match(line) is not None:
                item=line.split(">")
                if item[1] not in miRNAreadsdict and item[1] in mappingreadsdict:
                    reads=item[1].split(":")
                    print ">"+reads[0]+":"+reads[1]+":"+reads[2]
                    flag=1
                else:
                    flag=0
            else:
                if flag==1:
                    print line
            line=fh.readline().rstrip("\n\r")
        #for line in ColumnReader(open(sys.argv[1])):
            #line=line.rstrip("\n\r").split("\t")
        '''
