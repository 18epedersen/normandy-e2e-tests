"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.nondestructive
def test_delete_recipe(conf, base_url, selenium):
    """Confirm recipe deleted on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    home_page, approve_text, recipe_name = home_page.create_approved_recipe(
     conf, False)
    found_before_deleted_recipe, recipe_page = home_page.find_recipe_in_table(
     recipe_name)
    home_page = recipe_page.delete_recipe()
    notification_text = home_page.get_notification_text()
    found_after_deleted_recipe, recipe_page = home_page.find_recipe_in_table(
     recipe_name)
    found_recipe_in_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert found_before_deleted_recipe
    assert notification_text == 'Recipe deleted.'
    assert not found_after_deleted_recipe
    assert not found_recipe_in_rest_api
