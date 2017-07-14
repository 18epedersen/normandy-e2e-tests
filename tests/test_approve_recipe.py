"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_approve_recipe(conf, base_url, selenium):
    """Test the approval flow of a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    home_page, approved_text, recipe_name = home_page.create_approved_recipe(
     conf, False)
    assert approved_text == "APPROVED\nLATEST DRAFT"
    assert home_page.find_element(
     *home_page.LOCATORS.recipetable).is_displayed()
