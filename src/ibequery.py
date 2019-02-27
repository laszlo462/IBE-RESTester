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
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


####################################
###        Main Execution        ###
####################################

print("Welcome".center(20, "="))
print("\nDynaLync Query Test Tool".center(20))
ibehost = input(
    "\nPlease enter the IBE IP Address: ")
# TODO: Regex IP validation
# ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$
# TODO: If Rhapsody service is present, execute get_ip().  If IBE_HOST ENV variable is present, use that.
if ibehost == None:
    ibehost = get_ip()
# I don't believe this even works currently
logging.debug('Using IP: ' + ibehost)

# Wait for exit
input("Press any key to exit")
