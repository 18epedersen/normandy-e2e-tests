Normandy-e2e-tests
====================


Summary
-------
Suite of end-2-end tests for Mozilla's Normandy Control Shield UI. 


Each scripts in the tests subdirectory exercises a different workflow of the UI. The tests are ordered 1-7. The tests run sequentially, and the first (test1) will run first, and the last (test7) test will run last.


The workflows tested are:

1. Adding a new recipe 
2. Filling out the recipe form
3. Editing an existing recipe
4. Approving a recipe
5. Publishing a recipe
6. Disabling a recipe
7. Cloning a recipe


Install
-------


To install the requirements for the tests:

```
pip install -rrequirements.txt
```

Setup
-------

The tests require a config.ini file with variables and confidental credentials. However, I cannot provide the config.ini file here because I cannot disclose the testing account's LDAP username, LDAP password, and QR code secret. Therefore, I've provided a config.ini-dist file as a template.

Please copy over the contents of config.ini-dist into a new file called config.ini in your project home directory. In config.ini, fill in the fields for username, password, and secret. 

Also note if the UI has changed since 8/11/17, you need to update pages/locators.py. Locators.py is the module that stores all the locators for the selenium webdriver.

Run
-------
Note, to run the tests, you must be connected to the Mozilla VPN server.

To run all the tests sequentially:

```
tox
```

If you want to run a specific test, run:

```
tox -e test_name
```

For example:

```
tox -e approve_recipe
```