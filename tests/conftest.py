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


def find_approved_recipe(conf, recipe_id):
    """Find the recipe given the recipe_id."""
    rest_api_url = conf.get('stage', 'rest_api_url')
    response = requests.get(rest_api_url)
    json_data = json.loads(response.text)
    enabled, approved, action, message, filter_expression = None, None, None,
    None, None
    for data in json_data:
        recipe = data['recipe']
        if recipe['name'] == recipe_id:
            enabled = recipe['enabled']
            approved = recipe['is_approved']
            action = recipe['action']
            message = recipe['arguments']['message']
            filter_expression = recipe['filter_expression']
    return (enabled, approved, action, message, filter_expression)
