"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.nondestructive
def test_find_recipe_in_table(conf, base_url, selenium, qr_code):
    """Find recipe on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page, recipe_name, messages_list = home_page.create_approved_and_enabled_recipe(conf) # noqa
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(
     recipe_name)
    action_selected = recipe_page.get_action_selected
    found_recipe_at_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert found_recipe, "recipe name not found"
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.filter_textbox).text == conf.get('recipe',
                                                           'recipe_additional_filters') # noqa
    assert action_selected == conf.get('recipe', 'recipe_action')
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.action_message).get_attribute('value') == conf.get(
      'recipe', 'recipe_message')
    assert found_recipe_at_rest_api
