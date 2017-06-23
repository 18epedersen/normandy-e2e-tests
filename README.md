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

The tests require a variables.json file with LDAP username, LDAP password, QR code secret, and other variables that select options of the Recipe form. I've provided a variables-demo.json file to demonstrate the syntax and content of the variables.json file you need to run the tests.