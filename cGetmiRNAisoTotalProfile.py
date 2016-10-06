#!/usr/bin/python
#0

""" Module/Script Description

This Module/Script can help to count reads for every type of isomiR

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
        print "Usage: "+sys.argv[0]+"  miRBaseRelease18/hsa/human_maturemiRNA.list miRBaseRelease18/hsa/trimed_1726_hsamiRNA.txt > miRBaseRelease18/hsa/trimed_1726_hsamiRNA_TotalProfile.txt"
    else:
        fh=open(sys.argv[1])
        line=fh.readline().rstrip("\n\r")
        while line:
            readsstring=""
            readslist=[]
            readscount=[]
            ft=open(sys.argv[2])
            row=ft.readline().rstrip("\n\r")
            while row:
                row=row.split("\t")
                if row[9] not in readslist and not cmp(line,row[3]) and string.atoi(row[12])>16:
                    readslist.append(row[9])
                    if not cmp(row[5],"+"):
                        start=string.atoi(row[7])-string.atoi(row[1])
                        end=string.atoi(row[8])-string.atoi(row[2])
                    else:
                        start=string.atoi(row[2])-string.atoi(row[8])
                        end=string.atoi(row[1])-string.atoi(row[7])
                    read=row[9].split(":")
                    readscount.append(string.atoi(read[2]))
                    readsstring=readsstring+"\t"+str(start)+","+str(end)+"\t"+row[9]+"\t"+read[2]
                row=ft.readline().rstrip("\n\r")
            if len(readscount)>0:
                print line+"\t"+str(max(readscount))+readsstring
            else:
                print line+"\t"+str(0)
            line=fh.readline().rstrip("\n\r")
