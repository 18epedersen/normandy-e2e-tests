"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.nondestructive
def test_find_recipe_in_table(conf, base_url, selenium):
    """Find recipe on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    home_page, approve_text, recipe_name = home_page.create_approved_recipe(
     conf, False)
    found_recipe, recipe_page = home_page.find_recipe_in_table(recipe_name)
    action_selected = recipe_page.which_action_selected()
    found_rest_api = find_recipe_rest_api(conf, recipe_name)
    assert found_recipe, "recipe name not found"
    assert recipe_page.find_element(*recipe_page.LOCATORS.filtertextbox).text == conf.get('recipe', 'recipe_additional_filters')# noqa
    assert action_selected == conf.get('recipe', 'recipe_action')
    assert recipe_page.find_element(*recipe_page.LOCATORS.actionmessage).get_attribute('value') == conf.get('recipe', 'recipe_message') # noqa
    assert found_rest_api
