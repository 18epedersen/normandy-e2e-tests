"""Pytest."""
import pytest
import configparser
import pyotp
import json
import requests
from foxpuppet import FoxPuppet
import time


@pytest.fixture
def conf():
    """Read config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@pytest.fixture(scope="session")
def base_url():
    """Return base url fixture."""
    return 'https://normandy.dev.mozaws.net/control-new/'


@pytest.fixture
def browser(foxpuppet):
    """Return Firefox browser window."""
    return foxpuppet.browser


@pytest.fixture
def foxpuppet(selenium):
    """Return foxpuppet."""
    return FoxPuppet(selenium)


@pytest.fixture
def qr_code(conf, worker_id):
    """Return qr code."""
    secret = conf.get('login', 'secret')
    if worker_id == 'master':
        index = 0
    else:
        index = int(worker_id[2:])
    time.sleep(index*30)
    totp = pyotp.TOTP(secret)
    return totp.now()


def find_recipe_rest_api(conf, recipe_name):
    """Find the recipe at the rest api server given the recipe_name."""
    rest_api_url = conf.get('stage', 'rest_api_url')
    response = requests.get(rest_api_url)
    json_data = json.loads(response.text)
    found = False
    for data in json_data:
        recipe = data['recipe']
        if recipe['name'] == recipe_name:
            found = True
    return found
