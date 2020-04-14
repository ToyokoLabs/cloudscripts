#!/usr/bin/python3

"""
Put the header of one file at the begining of other files.
It needs 'sponge' to work. Linux install:
sudo apt install moreutils
"""

import os
import glob
import subprocess


FILE_WITH_HEADER = '' #la_apr_01.csv

# Get the list of files to put the header in
fl = glob.glob("ar_*.csv")

for f in fl:
    cli = 'head -1 {0} | cat - {1} | sponge {1}'.format(FILE_WITH_HEADER, f)
    out = subprocess.Popen(cli, shell=True)
