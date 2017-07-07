"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium, recipe_id):
    """Find recipe on home page."""
    # test to successfully find a recipe in a table, use regions
    # base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    page = LDAPLogin(selenium, base_url).open()
    duo_page = page.login(username, password)
    secret = conf.get('variables', 'secret')
    home_page = duo_page.login_duo(secret)
    recipe_page = home_page.select_recipe(recipe_id)
