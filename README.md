# Python AXL examples
Tutorial on how to setup an environment for making SOAP/AXL calls using python

 # First thing you’re going to need:
 - Python 3 (tested with 3.6 and 3.9)  
 - AXLSQLToolkit (Download from your CUCM Plugins page https://developer.cisco.com/docs/axl/#!download-the-axl-wsdl/download-the-axl-wsdl)  
 - suds-jurko Python3 library  
 - A CUCM Environment (VMs included)  
 - VPN to be on the same network as CUCM  

 # Instructions
 - Optional: Setup a Cisco dCloud demo instance that contains the CUCM VM (the [Cisco Collaboration 12.5 v1 - Transform Work with Collaboration](https://dcloud2-rtp.cisco.com/content/demo/578984) demo is a good environment)  
 - Install the AXLSQLToolkit files by going into the CUCM admin page, Go to Application | Plugins. Click on the Download link by the Cisco CallManager AXL SQL Toolkit Plugin. The axlsqltoolkit.zip file contains the complete schema definition for different versions of Cisco Unified CM.  
   NOTE: This YouTube video shows exactly how to install the AXLSQLToolkit files and how to set up a CUCM user with permissions to access the AXL SOAP API: https://www.youtube.com/watch?v=wtnDzPQVdRE&t=248s  
 - Make sure the user being used has a user rank of 1 or with proper API AXL permissions (Role: Standard AXL API Access Reference: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/9_0_1/ccmsys/CUCM_BK_CD2F83FA_00_cucm-system-guide-90/CUCM_BK_CD2F83FA_00_system-guide_chapter_0100.pdf)  
 - Copy user_env.template to user_env.py  
 - Edit `user_env.py` and add your CUCM environment and user details:  
   - WSDL_PATH = path to WSDL file on your local machine or server where the code is running.  
   - CUCM_LOCATION = IP Address of the CUCM server. For use with Cisco Collaboration 12.5 v1 dCloud demo after you have connected via VPN you can use: "198.18.133.3"  
   - CUCM_USER = username without the domain. For use with Cisco Collaboration 12.5 v1 dCloud demo you can use: "amckenzie"  
   - CUCM_PASSWORD = password for the CUCM_USER with AXL SOAP API priviledges. For use with Cisco Collaboration 12.5 v1 dCloud demo you can use: "dCloud12345!"  
 - Install the suds-jurko Python3 library: `pip install suds-jurko`.  You can also use the included `requirements.txt` file to install it issuing the command `pip install -r requirements.txt`   
 - Run one of the .py sample scripts , for example: `python3 list_users.py`  
 

 # Code output
 - The listPhones() function of the `list_subscribers_and_phones.py` script will generate a CSV file that has Name,Model,Product,Location for each phone device. Use the returned tags as a reference to what information that can be retrieved. Example: phone.description is the description of the device.  
 
 - The getSubs() function of the `list_subscribers_and_phones.py` script will generate a text file that has the name of the subscribers.  

 - The listUsers() function of the `list_users.py` script will generate a CSV file that has First, Last, UserID, telephoneNumber, mobileNumber, homeNumber for each user.  

 - The executeQuery() function of the `list_devices_and_dns.py` script will perform a SQL Query of the CUCM DB using AXL. There are various example queries in that script that return devices and their associated descriptions, device types and DNs that could be useful in extracting extension numbers (DNs) for specific types of devices  
