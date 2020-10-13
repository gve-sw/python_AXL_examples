"""AXL <executeSQLQuery> sample script, using the SUDS-Jurko library

Script Dependencies:
    suds
    logging (optional)

Depencency Installation:
    $ pip install suds-jurko

Copyright (c) 2018 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pathlib
# import pydash
import ssl
from suds.client import Client
from suds.xsd.doctor import Import
from suds.xsd.doctor import ImportDoctor

import os
import sys

# Get the absolute path for the project root
project_root = os.path.abspath(os.path.dirname(__file__))

# Extend the system path to include the project root and import the env file
sys.path.insert(0, project_root)
import user_env

#Disable HTTPS certificate validation check - not recommended for production
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

tns = 'http://schemas.cisco.com/ast/soap/'
imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add(tns)

axl = Client("file://"+user_env.WSDL_PATH,
    location="https://"+user_env.CUCM_LOCATION+"/axl/",
    faults=False,plugins=[ImportDoctor(imp)],
    username=user_env.CUCM_USER,
    password=user_env.CUCM_PASSWORD)
                
def executeQuery(thequery):
    res = axl.service.executeSQLQuery(sql=thequery)
    if res[1]['return']:
        return(res[1]['return']['row'])

print("Executing first SQL Query....")
aQuery="select d.name, d.description, n.dnorpattern as DN from device as d, numplan as n, devicenumplanmap as dnpm where dnpm.fkdevice = d.pkid and dnpm.fknumplan = n.pkid and d.tkclass = 1"
result=executeQuery(aQuery)
f= open("output_firstquery.csv","w+")
f.write("Name," + "DN" + "\n")
for device in result:
    f.write( device['name'] + ","  + device['dn'] + "\n")

print("Executing second SQL Query....")
aQuery="select d.description, d.tkmodel, d.tkproduct ,n.dnorpattern as DN from device as d, numplan as n, devicenumplanmap as dnpm where dnpm.fkdevice = d.pkid and dnpm.fknumplan = n.pkid and d.tkclass = 1"
result=executeQuery(aQuery)
f= open("output_secondquery.csv","w+")
f.write("Description," + "TKModel," + "TKProduct," + "DN" + "\n")
for device in result:
    f.write( device['description'] + ","+device['tkmodel'] + ","+device['tkproduct'] + ","  + device['dn'] + "\n")


#third query returns a very long result , skipping
#aQuery="select tm.name, tp.name, d.description, d.tkmodel, d.tkproduct ,n.dnorpattern as DN from device as d, numplan as n, devicenumplanmap as dnpm, typemodel as tm, typeproduct as tp where dnpm.fkdevice = d.pkid and dnpm.fknumplan = n.pkid and d.tkclass = 1 and tm.tkclass = d.tkclass and tp.tkmodel = d.tkmodel"

print("Executing fourth SQL Query....")
aQuery="select tp.name, d.description, d.tkmodel, d.tkproduct ,n.dnorpattern as DN from device as d, numplan as n, devicenumplanmap as dnpm, typeproduct as tp where dnpm.fkdevice = d.pkid and dnpm.fknumplan = n.pkid and d.tkclass = 1 and tp.tkmodel = d.tkmodel"
result=executeQuery(aQuery)
f= open("output_fourthquery.csv","w+")
f.write("Name," + "Description," + "TKModel," + "TKProduct," + "DN" + "\n")
for device in result:
    f.write( device['name'] + "," +device['description'] + ","+device['tkmodel'] + ","+device['tkproduct'] + ","  + device['dn'] + "\n")
