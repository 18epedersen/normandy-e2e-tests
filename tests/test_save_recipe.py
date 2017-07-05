"""Pytest."""
import pytest
from page.login import LDAPLogin


@pytest.mark.destructive
def test_save_recipe(conf, base_url, selenium):
    """Test creating a recipe and successfully submitting it."""
    base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    ldap_page = LDAPLogin(selenium, base_url).open()
    duo_page = ldap_page.login(username, password)
    secret = conf.get('variables', 'secret')
    home_page = duo_page.login_duo(secret)
    recipe_page = home_page.add_recipe()
    additional_filters = conf.get('variables', 'additional_filters')
    action = conf.get('variables', 'action')
    message = conf.get('variables', 'message')
    recipe_page.save_recipe(additional_filters,
                            action, message)
    # or check that we get a flash of successfully added recipe
    assert recipe_page.find_element(*recipe_page.LOCATORS.requestbutton).is_displayed()
