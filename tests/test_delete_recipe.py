"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import find_recipe_rest_api


@pytest.mark.run(after='test_edit_recipe')
@pytest.mark.nondestructive
def test_delete_recipe(conf, base_url, selenium):
    """Confirm recipe deleted on home page."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    found, recipe_page = home_page.find_recipe_in_table(conf)
    home_page = recipe_page.delete_recipe()
    text = home_page.confirm_deleted_recipe()
    assert found
    assert text == 'Recipe deleted.'


@pytest.mark.run(after='test_delete_recipe')
@pytest.mark.nondestructive
def test_deleted_recipe_at_rest_api(conf):
    """Testing that the deleted recipe is not at the rest api endpoint."""
    found = find_recipe_rest_api(conf)
    assert not found
