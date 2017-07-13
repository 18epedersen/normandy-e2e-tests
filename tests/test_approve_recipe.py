"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import create_recipe


@pytest.mark.nondestructive
def test_approve_recipe(conf, base_url, selenium):
    """Test the approval flow of a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    home_page, approve_text = create_recipe(conf, home_page, False)
    assert approve_text == "APPROVED\nLATEST DRAFT"
    assert home_page.find_element(
     *home_page.LOCATORS.recipetable).is_displayed()
