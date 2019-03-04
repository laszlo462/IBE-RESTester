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

### TO BE REMOVED ###
""" def executequery(queryurl):
    logging.debug('executing the query')
    r = None
    try:
        r = requests.get(queryurl)
    except:
        print('IBE Connection Failed...')

    logging.debug('IBE Response: ' + r.text)
    parsed = json.loads(r.text)
    return parsed


def showresponse(parsedresponse):
    str = "Search Results"
    print(str.center(20, "="))
    print(json.dumps(parsedresponse, indent=4, sort_keys=True)) """


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


def query_select():
    # Ask user to select query type
    qmenu = ["MRN", "EnterpriseID", "First Name", "Last Name", "Date of Birth"]

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


def ibe_address():
    # Obtain the local IP address for default, ask user to input IP address.
    local_ip = get_ip()
    logging.debug(local_ip)
    print("Please enter IBE IP address, or press Enter to accept default shown:")
    ibehost = input("[" + local_ip + "]: ")

    # TODO: Regex IP validation
    # ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$
    # TODO: If Rhapsody service is present, execute get_ip().  If IBE_HOST ENV variable is present, use that.
    return ibehost


def new_or_quit():
    pass

####################################
###        Main Execution        ###
####################################


print("Welcome".center(20, "="))
print("DynaLync Query Test Tool\n".center(20))
ibehost = ibe_address()

query_select()
# Wait for exit
input("Press any key to exit")
