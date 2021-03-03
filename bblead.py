import os
import sys
import beatbox
import datetime
import csv

sf = beatbox._tPartnerNS

# "salesforceusername and password"
username = 'hmedfrias@resilient-narwhal-hdgymy.com'
password = "H9Mekaaq"
token    = 'cXHXhY4XKqZxa2TuAQcG2rcm'

"""connect and authenticate"""
svc = beatbox.Client()
svc.login(username, password+token)

def new_lead(fname, lname, company):
    print("\ncreate")
    a = {'type': 'Lead',
        'FirstName': fname,
        'LastName': lname,
        'Company': company,
        'Status': 'Open - Not Contacted',
        'Description': 'Inserted with api call'
    }
    sr = svc.create([a])

    if str(sr[sf.success]) == 'true':
        print("id " + str(sr[sf.id]))
    else:
        print("error " + str(sr[sf.errors][sf.statusCode]) + ":" + str(sr[sf.errors][sf.message]))


"""Leer archivo y ejecutar servicio de alta de Leads"""
with open("leads.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0

    for line in csv_reader:
        #para headers
        if line_count==0:
            line_count += 1
        else:
            print("insertando: %s %s %s" % (line[0], line[1], line[2]))
            new_lead(line[0], line[1], line[2])
            line_count += 1

