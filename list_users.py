"""AXL <listUsers>  sample script, using the SUDS-Jurko library

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
    

def listUsers():
    f= open("output_users.csv","w+")

    # edit returnedTags to receive different information
    res = axl.service.listUser({'userid': '%'}, returnedTags={
                'firstName': '', 'lastName': '','userid': '', 'telephoneNumber':'',  'mobileNumber':'', 'homeNumber':'',
                })
    f.write("First," + "Last,"  + "UserID," + "telephoneNumber,"+ "mobileNumber,"+ "homeNumber" + "\n")
    if res[1]['return']:
        users = res[1]['return']['user']
        for user in users:
            theFirst=''
            theLast=''
            theUserID=''
            theTelephoneNumber=''
            theMobileNumber=''
            theHomeNumber=''
            if user.firstName:
                theFirst=user.firstName
            if user.lastName:
                theLast=user.lastName
            if user.userid:
                theUserID=user.userid
            if user.telephoneNumber:
                theTelephoneNumber=user.telephoneNumber
            if user.mobileNumber:
                theMobileNumber=user.mobileNumber
            if user.homeNumber:
                theHomeNumber=user.homeNumber

            f.write( theFirst + ","  + theLast + ","  + theUserID + ","+ theTelephoneNumber+ "," + theMobileNumber+ "," + theHomeNumber + "\n")
    f.close()



listUsers()
