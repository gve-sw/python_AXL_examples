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

# To list all users that have been marked for deletion by ActiveDirectory sync
# use the following SQL query:
#select userid, deletedtimestamp from enduser where status = "2"
# if you wish to test first with users that are active, change the query to look for status = "1"

print("Executing  SQL Query....")
aQuery='select userid, deletedtimestamp from enduser where status = "2"'
result=executeQuery(aQuery)

f= open("users_to_delete.csv","w+")
f.write("UserID," + "Timestamp" + "\n")
if result:
    for user in result:
        f.write( user['userid'] + ","  + user['deletedtimestamp'] + "\n")

