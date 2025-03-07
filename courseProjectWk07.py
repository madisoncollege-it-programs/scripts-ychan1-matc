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

        dictLogSummary = {}
        for strLogLine in listLogLines:
            listLogLine = strLogLine.split(" ")
            strIP = f"{listLogLine[0]}"
            strReturnCode = f"{listLogLine[8]}" 
            strIPReturnCode = f"{strIP} - {strReturnCode}"
            if strReturnCode >= "400":
                print(strIPReturnCode)
            if strIP in dictLogSummary:
                intCounter = dictLogSummary[strIP]
                intCounter += 1
                dictLogSummary[strIP] = intCounter
            else:
                dictLogSummary[strIP] = 1
        print(dictLogSummary)
        with open("courseProjectWk07Analysis.csv", "w") as wrapperLogFile:
            wrapperLogFile.write(f"IP Address,Hits")
            for strIP, intCounter in dictLogSummary.items():
                if intCounter >= 5:
                    wrapperLogFile.write(f"{strIP},{intCounter}")


