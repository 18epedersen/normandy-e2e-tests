import pytest
import configparser
import pyotp


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
