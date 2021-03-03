import os
import sys
import beatbox
import datetime

sf = beatbox._tPartnerNS

# "salesforceusername and password"
username = 'hmedfrias@resilient-narwhal-hdgymy.com'
password = "H9Mekaaq"
token    = 'cXHXhY4XKqZxa2TuAQcG2rcm'

"""connectt and authenticate"""
svc = beatbox.Client()
svc.login(username, password+token)

"""execut SOQL query"""
# res = svc.query("SELECT Id, Email FROM Contact WHERE LastName = 'xMedina'")

print("\ncreate")
a = {'type': 'Account',
    'Name': 'My 3rd Account from API',
    'Website': 'http://www.hectormedinaphoto.com/',
    'Description': 'This is a new field I inserted on xml'
}
sr = svc.create([a])

if str(sr[sf.success]) == 'true':
    print("id " + str(sr[sf.id]))
    #self.__idToDelete = str(sr[sf.id])
else:
    print("error " + str(sr[sf.errors][sf.statusCode]) + ":" + str(sr[sf.errors][sf.message]))


"""prints results in console"""
# print(res)