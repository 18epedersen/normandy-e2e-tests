"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_enable_recipe(conf, base_url, selenium, qr_code):
    """Test the approval flow of creating a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page, recipe_name, messages_list = home_page.create_approved_and_enabled_recipe(conf) # noqa
    assert "Recipe enabled." in messages_list
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.disable_button).is_displayed()
