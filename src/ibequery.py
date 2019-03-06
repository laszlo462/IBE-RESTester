#! python3

# ibequery.py - Simple IBE query of a patient based on MRN
# Author: Steve Szabo
# Date: 02/26/2019

import querybuilder as query
import json
import logging
import os
import re
import socket

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


def get_ip():
    # Obtain local IP address via socket module
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def query_select(qmenu):
    # Ask user to select query type
    while True:
        try:
            print("Which query would you like to perform?")
            for index, value in enumerate(qmenu):
                print(index + 1, value)
            qtype = int(input(": "))
        except ValueError:
            print("Please select from the numbers listed.")
            continue
        if 1 >= qtype >= 5:
            print("Please select a valid option.")
            continue
        else:
            break
    return int(qtype - 1)


def ibe_address():
    # Obtain the local IP address for default, ask user to input IP address.
    local_ip = get_ip()
    logging.debug("Obtained a local IP of " + local_ip)
    print("Please enter IBE IP address, or press Enter to accept default shown:")
    ibehost = input("[" + local_ip + "]: ")

    # TODO: Regex IP validation
    # ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$
    # TODO: If Rhapsody service is present, execute get_ip().  If IBE_HOST ENV variable is present, use that.
    return ibehost


def new_or_quit():
    print("Execute another query?")
    newquery = str.upper(
        input("Enter Y to execute another query, or any other key to quit: "))
    return newquery


####################################
###        Main Execution        ###
####################################

qmenu = ["MRN", "EnterpriseID", "First Name", "Last Name", "Date of Birth"]

print("Welcome".center(20, "="))
print("DynaLync Query Test Tool\n".center(20))
ibehost = ibe_address()

# Main execution loops to allow for subsequent queries until the user is done
while True:
    qtype = query_select(qmenu)
    qparam = str(input("Query " + qmenu[qtype] + ": "))
    logging.debug("Querying for " + qparam)

    # Execute querybuilder function based on query type selected
    # Returned request text property loaded as a json string, then dumped
    # in a nice way (indentation and sorted by keys)
    if qtype == 0:  # MRN
        print(json.dumps(json.loads(query.get_mrn(ibehost, qparam).text),
                         indent=4, sort_keys=True))
    if qtype == 1:  # EID
        print(json.dumps(json.loads(query.get_eid(ibehost, qparam).text),
                         indent=4, sort_keys=True))
    if qtype == 2:  # First Name
        print(json.dumps(json.loads(query.get_firstname(ibehost, qparam).text),
                         indent=4, sort_keys=True))
    if qtype == 3:  # Last Name
        print(json.dumps(json.loads(query.get_lastname(ibehost, qparam).text),
                         indent=4, sort_keys=True))
    if qtype == 4:  # DOB
        print(json.dumps(json.loads(query.get_dob(ibehost, qparam).text),
                         indent=4, sort_keys=True))

    if new_or_quit() == "Y":
        continue
    else:
        break

# Wait for exit
input("Press any key to exit")
