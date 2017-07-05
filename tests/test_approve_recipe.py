"""Pytest."""
import pytest
from page.login import LDAPLogin


# test to successfully approval a recipe
@pytest.mark.destructive
def test_approve_recipe(conf, base_url, selenium):
    """Test the approval flow of a recipe."""
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
    recipe_page.save_recipe(additional_filters, action, message)
    approve = conf.get('variables', 'approve')
    home = recipe_page.approve_recipe(approve)
    # fix assert statement
    assert home.heading == "SHIELD Control Panel"
