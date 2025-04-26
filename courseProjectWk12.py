#!/usr/bin/env python3
"""
Author: Crystal Chan
Email: ychan1@madisoncollege.edu
Description: <Semester-long course project script which will analyze 
an Apache web log to determine current threats>
"""
import argparse
import subprocess
import requests, bs4


def ipLookup(inIpAddress):
    url = f"http://py.land/geo?host={inIpAddress}"
    print(url)
    response = requests.get(url)
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

    htmlResponse = ipLookup(strMostRequestsIP)
    myHTML = bs4.BeautifulSoup(htmlResponse, features="html.parser")
    listRawIpInfo = myHTML.find_all("dd", class_="col-8 text-monospace")
    print(strMostRequestsIP)
    print("Provider:", listRawIpInfo[-2].text, "(ASN: ", listRawIpInfo[-1].text, ")")
    print("City, State:", listRawIpInfo[0].text, listRawIpInfo[1].text)

    


if __name__ == "__main__":
    main()
