#!/usr/bin/python
#0

""" Module/Script Description

This Module/Script can help to get mapped reads in BED format.

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
        print "Usage: "+sys.argv[0]+" file1 file2..."
    else:
        ft=open(sys.argv[1])
        row=ft.readline().rstrip("\n\r")
        while row:
            row=row.split("\t")
            end=string.atoi(row[3])+len(row[4])
            print row[2]+"\t"+row[3]+"\t"+str(end)+"\t"+row[0]+"\t"+row[7]+"\t"+row[1]
            row=ft.readline().rstrip("\n\r")
