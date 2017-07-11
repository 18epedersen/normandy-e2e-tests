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
    recipe_id = conf.get('variables', 'recipe_id')
    recipe_page = home_page.select_recipe(recipe_id)
    home_page = recipe_page.delete_recipe()
    assert home_page.find_element(*home_page.LOCATORS.successalert).is_displayed() # noqa
    # check no longer in table


@pytest.mark.nondestructive
@pytest.mark.xfails(raises=AssertionError)
def test_deleted_recipe_rest_api(conf):
    """Testing that the deleted recipe is not at the rest api endpoint."""
    found = find_recipe_rest_api(conf)
    assert found
