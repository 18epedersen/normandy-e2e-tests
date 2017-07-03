"""Pytest."""
import pytest
from page.login import LDAPLogin


@pytest.mark.destructive
def test_create_recipe(conf, base_url, selenium):
    """Test creating a recipe and successfully submitting it."""
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
    approval = recipe.create_recipe(additional_filters,
                                    action, message)
    # or check that we get a flash of successfully added recipe
    assert approval.heading == "recipes"
