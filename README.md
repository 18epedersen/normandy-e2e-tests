Normandy-e2e-tests
====================


Summary
-------
Suite of e2e tests for Mozilla's Normandy Control UI.

Read about the Normandy Control shield here: https://wiki.mozilla.org/Firefox/Shield 

Github repo for Normandy: https://github.com/mozilla/normandy

Install
-------


To install the requirements for the tests locally:

```
pip install -rrequirements.txt
```

Run
-------
To run the tests locally:

```
tox
```
To run the tests, you need to be connected to the Mozilla VPN server. 

The tests also require a config.ini file with confidental LDAP username, LDAP password, and QR code secret. I've provided a config.ini-dist file, which needs to be copied over into a config.ini in the home directory and values for username, password, and secret need to be filled in. 