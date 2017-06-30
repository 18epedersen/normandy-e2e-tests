"""Pytest."""
import pytest
from page.login import LDAPLoginPage


@pytest.mark.destructive
def test_creating_recipe(base_url, selenium, variables):
    """Test creating a recipe and successfully submitting it."""
    page = LDAPLoginPage(selenium, base_url).open()
    duo = page.login(variables['username'], variables["password"])
    duo.switch_to_frame(
      duo.find_element(*duo._duoiframe_locator))
    home = duo.login_duo(variables['secret'])
    home.switch_to_default_content()
    recipe = home.add_recipe()
    approval = recipe.create_recipe(variables['additional filters'],
                                    variables['action'], variables['message'])
    # or check that we get a flash of successfully added recipe
    assert approval.heading == "recipes"
