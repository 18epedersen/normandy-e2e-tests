Normandy-e2e-tests
====================


Summary
-------
Suite of e2e tests for Mozilla's Normandy Control UI. 

The code on the master branch successfully worked against the stage version of the previous UI. 

The code on the dev branch runs against the dev version of the new UI refresh. The readme on the dev branch explains how to install, setup, and run the code for the dev branch. I also submitted several issues explaining test cases that should be added for the dev/admin version of the new UI.


Install
-------


To install the requirements for the tests:

```
pip install -rrequirements.txt
```

Run
-------
In order to run the tests, you need to be connected to the Mozilla VPN server.

To run the tests:

```
tox
```

The tests also require a LDAP username, LDAP password, and QR code secret in a config.ini file in the project home directory. 

To run the tests sucessfully, copy over the contents of config.ini-dist file into a file called config.ini in the home directory. Then add values for username, password, and QR secret. 