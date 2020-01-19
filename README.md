# python_AXL_examples
tutorial on how to setup a CUCM dcloud environment and making SOAP/AXL calls using python
 
# first thing you’re going to need:
- Python (I use v3.6)
- AXLSQLToolkit (Download from your CUCM Plugins page)
- suds-jurko Python3 library
- A CUCM Environment (Installed on a VMWare Workstation is fine. I’m using v11.5 for testing)

# instructions
- Setup a dcloud demo instance that contains the CUCM VM (title: Cisco Collaboration 12.5 v1 - Transform Work with Collaboration)
- Copy user_env.template to user_env.py
- Edit user_env.py and add your CUCM environment and user details
- Install the suds-jurko Python3 library
- Run one of the .py sample scripts
