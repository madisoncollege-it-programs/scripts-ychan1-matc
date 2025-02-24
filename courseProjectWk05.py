#!/usr/bin/env python3
"""
Author: Crystal Chan
Email: ychan1@madisoncollege.edu
Description: <Semester-long course project script which will analyze 
an Apache web log to determine current threats>
"""

with open("05_CP-Access.log") as hFile:
    strLogLines = hFile.read()

 
listLogLines = strLogLines.split('\n')

for strLogLine in listLogLines:
    listLogLine = strLogLine.split(" ")
    print(f"{listLogLine[0]}" + " - " + f" {listLogLine[8]}")
