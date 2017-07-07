"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_verify_recipe(conf, base_url, selenium):
    """Find recipe on home page."""
    # test to successfully find a recipe in a table, use regions
    # base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    page = LDAPLogin(selenium, base_url).open()
    duo_page = page.login(username, password)
    secret = conf.get('variables', 'secret')
    home_page = duo_page.login_duo(secret)
    recipe_page = home_page.add_recipe()
    additional_filters = conf.get('variables', 'additional_filters')
    action = conf.get('variables', 'action')
    message = conf.get('variables', 'message')
    recipe_page, recipe_id = recipe_page.save_recipe(additional_filters,
                                                     action, message)
    approve_message = conf.get('variables', 'approve')
    home_page, approve_text = recipe_page.approve_recipe(approve_message)
    found_recipe, values = home_page.verify_recipe(recipe_id)
    assert found_recipe
    assert values == (True, True, action, message, additional_filters)
