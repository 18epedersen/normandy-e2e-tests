"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_save_recipe(conf, base_url, selenium):
    """Test creating a recipe and successfully submitting it."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    recipe_page = home_page.add_recipe()
    recipe_page.save_recipe_handler(conf)
    assert recipe_page.find_element(*recipe_page.LOCATORS.requestbutton).is_displayed() # noqa
