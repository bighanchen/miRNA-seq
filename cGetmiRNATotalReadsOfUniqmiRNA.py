#!/usr/bin/python
#0

""" Module/Script Description

This Module/Script can help to Get total reads number if miRNA is located in many loci.Some parameters are different when dealing with libraries from different species.

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
        print "Usage: "+sys.argv[0]+" human_maturemiRNA.list hsamiRNA_combined.txt > hsamiRNA_Expression.txt"
    else:
        fh=open(sys.argv[1])
        line=fh.readline().rstrip("\n\r")
        while line:
            readslist=[""]
            for i in range(0,19):
                readslist.append("")
            score=[0]
            for i in range(0,19):
                score.append(0)
            ft=open(sys.argv[2])
            row=ft.readline().rstrip("\n\r")
            while row:
                row=row.split("\t")
                if not cmp(line,row[3]):
                    for i in range(0,20):
                        currentlist=readslist[i].split(";")
                        newlist=row[2*i+6].split(";")
                        for item in newlist:
                            if item not in currentlist:
                                readslist[i]=readslist[i]+item+";"
                                item=item.split(":")
                                score[i]=score[i]+string.atoi(item[2])
                row=ft.readline().rstrip("\n\r")
            print line+"\t",
            for i in range(0,19):
                print readslist[i]+"\t"+str(score[i])+"\t",
            print readslist[19]+"\t"+str(score[19])

            line=fh.readline().rstrip("\n\r")
