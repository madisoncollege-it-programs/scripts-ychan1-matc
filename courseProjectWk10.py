#!/usr/bin/env python3
"""
Author: Crystal Chan
Email: ychan1@madisoncollege.edu
Description: <Semester-long course project script which will analyze 
an Apache web log to determine current threats>
"""
import sys
import subprocess






def ipAddressCount(inApacheLogFileName):
    command = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.decode()
    return output



def main(): 
    if len(sys.argv) > 1:
        strUserInput =f"{sys.argv[1]}"
    else:
        strUserInput = input("Would you like to continue? (y/n)\n>>>") 

    if strUserInput.lower() in ['y', 'yes', 'yep', 'yup', 'yeah']:
        with open("courseProjectWk10Analysis.txt", "w") as wrapperLogFile:
            strLogLines = ipAddressCount("06_CP-Access.log")
            wrapperLogFile.write(strLogLines)
            #reserved for maybe future use
            """
            listLogLines = strLogLines.split('\n')
            for strLogLine in listLogLines:
                strLogLine = strLogLine.strip()
                listLogLine = strLogLine.split(" ")
                strIP = f"{listLogLine[1]}"
                strErrorCount = f"{listLogLine[0]}" 
            """
        print(strLogLines)

if __name__ == "__main__":
    main()
