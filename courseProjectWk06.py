#!/usr/bin/env python3
"""
Author: Crystal Chan
Email: ychan1@madisoncollege.edu
Description: <Semester-long course project script which will analyze 
an Apache web log to determine current threats>
"""
import sys


if len(sys.argv) > 1:
    strUserInput =f"{sys.argv[1]}"
else:
    strUserInput = input("Would you like to continue? (y/n)\n>>>") 

if strUserInput.lower() in ['y', 'yes', 'yep', 'yup', 'yeah']:
    with open("06_CP-Access.log") as hFile:
        strLogLines = hFile.read()
    listLogLines = strLogLines.split('\n')
    with open("courseProjectWk06Anlysis.txt", "w") as wrapperLogFile:
        for strLogLine in listLogLines:
            listLogLine = strLogLine.split(" ")
            strReturnCode = f"{listLogLine[8]}" 
            strIPReturnCode = f"{listLogLine[0]} - {strReturnCode}"
            if strReturnCode >= "400":
                print(strIPReturnCode)
            if strReturnCode >= "500":
                wrapperLogFile.write(f"{strIPReturnCode}\n")

