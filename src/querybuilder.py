# querybuilder.py
# IBE Query Builder module for LCS-RESTester project

import requests


def get_mrn(ibehost, mrn):
    pathstring = 'identifier=' + mrn
    return requests.get(_urlparticipants(ibehost, pathstring))


def get_eid(ibehost, eid):
    pathstring = 'enterpriseidentifier=' + eid
    return requests.get(_urlparticipants(ibehost, pathstring))


def get_firstname(ibehost, firstname):
    pathstring = 'first_name=' + firstname
    return requests.get(_urlparticipants(ibehost, pathstring))


def get_lastname(ibehost, lastname):
    pathstring = 'last_name=' + lastname
    return requests.get(_urlparticipants(ibehost, pathstring))


def get_dob(ibehost, dob):
    pathstring = 'date_of_birth=' + dob
    return requests.get(_urlparticipants(ibehost, pathstring))


def get_worklist(ibehost, mrn):
    return requests.get(_urlworklist(ibehost, mrn))


def _urlparticipants(host, path):
    return 'http://' + host + ':4342/IBEDynaLyncSvc/participants?' + path


def _urlworklist(host, mrn):
    return 'http://' + host + ':4342/IBEDynaLyncSvc/worklists?identifier=' + mrn + '&procedure_modality=CT'
