"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


# fix this test
@pytest.mark.run(before='test_delete_recipe')
@pytest.mark.run(after='test_find_recipe_in_table')
@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium):
    """Find recipe on home page, and edit recipe."""
    """Check recipe was correctly changed."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    found, recipe_page = home_page.find_recipe_in_table(conf)
    home_page, approve_text = recipe_page.edit_recipe_handler(conf)
    assert approve_text == "APPROVED\nLATEST DRAFT"
    assert home_page.find_element(*home_page.LOCATORS.recipetable).is_displayed() # noqa
