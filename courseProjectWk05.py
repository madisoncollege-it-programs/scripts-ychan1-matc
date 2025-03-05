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

with open("courseProjectWk05Analysis.txt", "w") as wrapperLogFile:

    for strLogLine in listLogLines:
        listLogLine = strLogLine.split(" ")
        strIPReturnCode = f"{listLogLine[0]} - {listLogLine[8]}"
        print(strIPReturnCode)
        wrapperLogFile.write(f"{strIPReturnCode}\n")

