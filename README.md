# python_AXL_examples
 tutorial on how to setup an evironemt for making SOAP/AXL calls using python

 # first thing you’re going to need:
 - Python (I use v3.6)
 - AXLSQLToolkit (Download from your CUCM Plugins page https://developer.cisco.com/docs/axl/#!download-the-axl-wsdl/download-the-axl-wsdl)
 - suds-jurko Python3 library
 - A CUCM Environment (VMs included)
 - VPN to be on the same network as CUCM 

 # instructions
 - Setup a dcloud demo instance that contains the CUCM VM (title: Cisco Collaboration 12.5 v1 - Transform Work with Collaboration is a good environment)
 - Install the AXLSQLToolkit files by going into the CUCM admin page, Go to Application | Plugins. Click on the Download link by the Cisco CallManager AXL SQL Toolkit Plugin. The axlsqltoolkit.zip file contains the complete schema definition for different versions of Cisco Unified CM.
 - Copy user_env.template to user_env.py
 - Edit user_env.py and add your CUCM environment and user details WSDL_PATH = "(path to WSDL file)" CUCM_LOCATION = "(IP Address)" CUCM_USER = "(username without domain)" CUCM_PASSWORD = "(password)"
 - Install the suds-jurko Python3 library
 - Run one of the .py sample scripts
