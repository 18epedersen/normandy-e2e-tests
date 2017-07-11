"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.run(before='test_find_recipe')
@pytest.mark.run(after='test_save_recipe')
@pytest.mark.nondestructive
def test_approve_recipe(conf, base_url, selenium):
    """Test the approval flow of a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    recipe_page = home_page.add_recipe()
    recipe_page.save_recipe_handler(conf)
    home_page, approve_text = recipe_page.approve_recipe_handler(conf)
    assert approve_text == "APPROVED\nLATEST DRAFT"
    assert home_page.find_element(*home_page.LOCATORS.recipetable).is_displayed() # noqa
