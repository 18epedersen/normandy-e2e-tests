"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api
import time


@pytest.mark.nondestructive
def test_delete_recipe(conf, base_url, selenium):
    """Confirm recipe deleted on home page."""
    time.sleep(60)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page, recipe_name = home_page.create_approved_and_enabled_recipe(
     conf)
    home_page = recipe_page.click_home_button()
    found_before_deleted_recipe, recipe_page = home_page.find_recipe_in_table(
     recipe_name)
    home_page = recipe_page.delete_recipe()
    notifications_text_list = home_page.get_notification_texts
    found_after_deleted_recipe, recipe_page = home_page.find_recipe_in_table(
     recipe_name)
    found_recipe_in_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert found_before_deleted_recipe
    assert 'Recipe deleted.' in notifications_text_list
    assert not found_after_deleted_recipe
    assert not found_recipe_in_rest_api
