"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.nondestructive
def test_find_recipe_in_table(conf, base_url, selenium):
    """Find recipe on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    result = home_page.find_recipe_in_table(conf)
    assert result, "recipe name not found"


@pytest.mark.nondestructive
def test_find_recipeid_in_rest_api(conf, base_url, selenium):
    """Find recipe on restful api endpoint."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    duo_page.login_duo_handler(conf, selenium, base_url)
    bool_val = find_recipe_rest_api(conf)
    assert bool_val
