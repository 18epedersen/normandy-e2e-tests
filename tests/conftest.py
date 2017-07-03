import pytest
import configparser


@pytest.fixture
def conf():
    """Read config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@pytest.fixture(scope="session")
def base_url():
    #return conf.get("stage", "base_url")
    return 'https://normandy-admin.stage.mozaws.net/control/recipe/'
