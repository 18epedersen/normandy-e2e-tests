"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium, recipe_id):
    """Find recipe on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    recipe_page = home_page.select_recipe(recipe_id)
    recipe_page.edit_recipe_handler(conf)
    assert recipe_page.find_element(*recipe_page.LOCATORS.successalert).is_displayed() # noqa
    # check edited value in table
