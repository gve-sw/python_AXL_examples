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
 - Make sure the user being used has a user rank of 1 or with proper API AXL permissions (Role: Standard AXL API Access Reference: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/9_0_1/ccmsys/CUCM_BK_CD2F83FA_00_cucm-system-guide-90/CUCM_BK_CD2F83FA_00_system-guide_chapter_0100.pdf)
 - Copy user_env.template to user_env.py
 - Edit user_env.py and add your CUCM environment and user details WSDL_PATH = "(path to WSDL file)" CUCM_LOCATION = "(IP Address)" CUCM_USER = "(username without domain Example user: amckenzie)" CUCM_PASSWORD = "(password)"
 - Install the suds-jurko Python3 library
 - Run one of the .py sample scripts
 
 # code output
 - The listPhones() function of the list_subscribers_and_phones.py script will generate a CSV file that has Name,Model,Product,Location for each phone device. Use the returned tags as a reference to what information that can be retrieved. Example: phone.description is the description of the device. 
 
 - The getSubs() function of the list_subscribers_and_phones.py script will generate a text file that has the name of the subscribers. 

 - The listUsers() function of the list_users.py script will generate a CSV file that has First,Last,UserID for each user.

 - The executeQuery() function of the list_devices_and_dns.py script will perform a SQL Query of the CUCM DB using AXL. There are various example queries in that script that return devices and their associated descriptions, device types and DNs that could be useful in extracting extension numbers (DNs) for specific types of devices