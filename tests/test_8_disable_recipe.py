import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.nondestructive
def test_disable_recipe(conf, base_url, selenium, qr_code):
    """Test disabling a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page, recipe_name, messages_list = home_page.create_approved_and_enabled_recipe(conf) # noqa
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(
     recipe_name)
    recipe_page, messages_list = recipe_page.disable_recipe()
    found_recipe_at_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert "Recipe disabled." in messages_list
    assert not found_recipe_at_rest_api
