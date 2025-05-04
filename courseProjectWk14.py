#!/usr/bin/env python3
"""
Author: Crystal Chan
Email: ychan1@madisoncollege.edu
Description: <Semester-long course project script which will analyze 
an Apache web log to determine current threats>
"""
import argparse
import subprocess
import requests
import json
import os


def ipLookup(inIpAddress):
    url = f"https://virustotal.com/api/v3/ip_addresses/{inIpAddress}"
    print(url)

    dictHeaders = {}

    credentials_path = os.path.expanduser("~/.credentials-vt")

    with open(credentials_path,"r") as credFile:
        line = credFile.readline().strip()
        key, value = line.split("=", 1)
        dictHeaders = {key.strip(): value.strip()}
        

    response = requests.get(url, headers=dictHeaders)
    return response.text

def ipAddressCount(inApacheLogFileName):
    command = f"cat {inApacheLogFileName} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.decode()
    return output



def main(): 
    
    parser = argparse.ArgumentParser(description = "Analyze Apache log file for top IP address")
    parser.add_argument('-i','--infilename', type=str, required=True, help='Path to Apahe log file')
    parser.add_argument('-o','--outfilename', type=str, help='Output file to save result')

    args = parser.parse_args()

    strLogLines = ipAddressCount(args.infilename)

    listLogLine = strLogLines.strip().split('\n')
    if listLogLine:
        strMostRequestsIP = listLogLine[-1].strip()
        listParts = strMostRequestsIP.split()
        if len(listParts) == 2:
            strMostRequestsIP = listParts[1]
        else:
            strMostRequestsIP = "N/A"



    if args.outfilename:
        with open(args.outfilename, "w") as wrapperLogFile:
            wrapperLogFile.write(strLogLines)


    print(strMostRequestsIP)

    strJSONResponse = ipLookup(strMostRequestsIP)
    
    dictIpInfo = json.loads(strJSONResponse)

    dictData = dictIpInfo.get("data", {})
    dictAttribute = dictData.get("attributes", {})
    dictAnalysis = dictAttribute.get("last_analysis_results", {})
    dictBitdefender = dictAnalysis.get("BitDefender", {})

    print("Bitdefender category:", dictBitdefender.get("category"))


    


if __name__ == "__main__":
    main()
