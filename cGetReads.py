#!/usr/bin/python
#0

""" Module/Script Description

This Module/Script can help to get Reads from Trim-adapter file

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
        print "Usage: "+sys.argv[0]+" trimed.fastq > trimed.reads"
    else:
        fh=open(sys.argv[1])
        line=fh.readline().rstrip("\n\r")
        j=1
        while line:
            if j%4==2:
                print line
            line=fh.readline().rstrip("\n\r")
            j=j+1
