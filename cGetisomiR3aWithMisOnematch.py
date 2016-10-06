#!/usr/bin/python
#0

""" Module/Script Description

This Module/Script can help to get isomiR With one mismatch.

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
        print "Usage: "+sys.argv[0]+" miRBaseRelease18/hsa/human_maturemiRNA.list somiR/trimed_hsaisomiR.txt > miRBaseRelease18/hsa/isomiRWithmismatch/a3/trimed_hsaisomiR_a3.txt"
    else:
        ft=open(sys.argv[1])
        miRNA=ft.readline().rstrip("\n\r")
        while miRNA:
            readslist=[""]
            a3aReads=""
            a3cReads=""
            a3gReads=""
            a3tReads=""
            a3aReadsCount=0
            a3cReadsCount=0
            a3gReadsCount=0
            a3tReadsCount=0

            fh=open(sys.argv[2])
            row=fh.readline().rstrip("\n\r")
            while row:
                line=row.split("\t")
                if not cmp(line[3],miRNA):
                    if line[9] not in readslist:
                        if not cmp(line[5],"+"):
                            if string.atoi(line[1])==string.atoi(line[7]) and string.atoi(line[2])==string.atoi(line[8])-1:
                                readslist.append(line[9])
                                mismatch=line[10].split(":")
                                if string.atoi(mismatch[0])>string.atoi(line[2])-string.atoi(line[1])-1:
                                    base=mismatch[1].split(">")
                                    if not cmp(base[1],"A"):
                                        a3aReads=a3aReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3aReadsCount=a3aReadsCount+string.atoi(count[2])
                                    if not cmp(base[1],"C"):
                                        a3cReads=a3cReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3cReadsCount=a3cReadsCount+string.atoi(count[2])
                                    if not cmp(base[1],"G"):
                                        a3gReads=a3gReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3gReadsCount=a3gReadsCount+string.atoi(count[2])
                                    if not cmp(base[1],"T"):
                                        a3tReads=a3tReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3tReadsCount=a3tReadsCount+string.atoi(count[2])
                        else:
                            if string.atoi(line[1])==string.atoi(line[7])+1 and string.atoi(line[2])==string.atoi(line[8]):
                                readslist.append(line[9])
                                mismatch=line[10].split(":")
                                if string.atoi(mismatch[0])>string.atoi(line[2])-string.atoi(line[1])-1:
                                    base=mismatch[1].split(">")
                                    if not cmp(base[1],"T"):
                                        a3aReads=a3aReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3aReadsCount=a3aReadsCount+string.atoi(count[2])
                                    if not cmp(base[1],"G"):
                                        a3cReads=a3cReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3cReadsCount=a3cReadsCount+string.atoi(count[2])
                                    if not cmp(base[1],"C"):
                                        a3gReads=a3gReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3gReadsCount=a3gReadsCount+string.atoi(count[2])
                                    if not cmp(base[1],"A"):
                                        a3tReads=a3tReads+line[9]+"|"+line[10]+";"
                                        count=line[9].split(":")
                                        a3tReadsCount=a3tReadsCount+string.atoi(count[2])
                row=fh.readline().rstrip("\n\r")
            print miRNA+"\t"+a3aReads+"\t"+str(a3aReadsCount)+"\t"+a3cReads+"\t"+str(a3cReadsCount)+"\t"+a3gReads+"\t"+str(a3gReadsCount)+"\t"+a3tReads+"\t"+str(a3tReadsCount)+"\t"
            miRNA=ft.readline().rstrip("\n\r")
