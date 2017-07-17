"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api
import time


@pytest.mark.nondestructive
def test_find_recipe_in_table(conf, base_url, selenium):
    """Find recipe on home page."""
    time.sleep(120)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page, recipe_name, row_content = home_page.create_approved_and_enabled_recipe(conf) # noqa
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page = home_page.find_recipe_in_table(recipe_name)
    action_selected = recipe_page.get_action_selected
    found_recipe_at_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert found_recipe, "recipe name not found"
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.filtertextbox).text == conf.get('recipe',
                                                           'recipe_additional_filters') # noqa
    assert action_selected == conf.get('recipe', 'recipe_action')
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.actionmessage).get_attribute('value') == conf.get(
      'recipe', 'recipe_message')
    assert found_recipe_at_rest_api
