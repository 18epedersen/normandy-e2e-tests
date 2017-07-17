"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api
# import time


@pytest.mark.nondestructive
def test_disable_recipe(conf, base_url, selenium):
    """Test disabling a recipe."""
    # time.sleep(120)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page, recipe_name = home_page.create_approved_and_enabled_recipe(
     conf)
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(recipe_name)
    recipe_page.disable_recipe()
    notification_texts_list = recipe_page.get_notification_texts
    found_recipe_at_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert "Recipe disabled." in notification_texts_list
    assert not found_recipe_at_rest_api
