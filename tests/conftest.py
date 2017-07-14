"""Pytest."""
import pytest
import configparser
import pyotp
import json
import requests


@pytest.fixture
def conf():
    """Read config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@pytest.fixture(scope="session")
def base_url():
    """Return base url fixture."""
    # return conf.get("stage", "base_url")
    return 'https://normandy-admin.stage.mozaws.net/control/recipe/'


def generate_QR_code(secret):
    """Return the QR code for 2FA."""
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
