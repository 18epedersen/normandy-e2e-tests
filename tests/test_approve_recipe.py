"""Pytest."""
import pytest
from page.login import LDAPLogin


# test to successfully approval a recipe
@pytest.mark.destructive
def test_approve_recipe(conf, base_url, selenium):
    """Test the approval flow of a recipe."""
    base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    page = LDAPLogin(selenium, base_url).open()
    duo = page.login(username, password)
    duo.switch_to_frame(
      duo.find_element(*duo.duoiframe_locator))
    secret = conf.get('variables', 'secret')
    home = duo.login_duo(secret)
    home.switch_to_default_content()
    recipe = home.add_recipe()
    additional_filters = conf.get('variables', 'additional_filters')
    action = conf.get('variables', 'action')
    message = conf.get('variables', 'message')
    approval = recipe.create_recipe(additional_filters, action, message)
    approve = conf.get('variables', 'approve')
    home = approval.approve_recipe(approve)
    # fix assert statement
    assert home.heading == "shield"
