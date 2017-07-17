"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
# from tests.conftest import find_recipe_rest_api
# import time


@pytest.mark.nondestructive
def test_find_columns_in_table(conf, base_url, selenium):
    """Test disabling a recipe."""
    # time.sleep(120)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page, recipe_name = home_page.create_approved_and_enabled_recipe(
     conf)
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(
     recipe_name)
    assert found_recipe
    assert recipe_name == row_content[0]
    assert conf.get('recipe', 'recipe_action') == row_content[1]
