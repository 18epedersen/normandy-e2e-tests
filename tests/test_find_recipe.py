"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.run(before='test_edit_recipe')
@pytest.mark.run(after='test_approve_recipe')
@pytest.mark.nondestructive
def test_find_recipe_in_table(conf, base_url, selenium):
    """Find recipe on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    result, recipe_page = home_page.find_recipe_in_table(conf)
    recipe_additional_filters = conf.get('recipe', 'recipe_additional_filters')
    recipe_action = conf.get('recipe', 'recipe_action')
    recipe_message = conf.get('recipe', 'recipe_message')
    value = recipe_page.find_recipe_helper()
    assert result, "recipe name not found"
    assert recipe_page.find_element(*recipe_page.LOCATORS.filtertextbox).text == recipe_additional_filters # noqa
    assert value == recipe_action # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.actionmessage).get_attribute('value') == recipe_message # noqa


@pytest.mark.run(after='test_find_recipe_in_table')
@pytest.mark.nondestructive
def test_find_recipeid_in_rest_api(conf, base_url, selenium):
    """Find recipe on restful api endpoint."""
    result = find_recipe_rest_api(conf)
    assert result
