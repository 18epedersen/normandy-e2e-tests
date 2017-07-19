"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_add_recipe(conf, base_url, selenium, qr_code):
    """Test adding a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page = home_page.click_add_recipe()
    assert home_page.heading == 'SHIELD Control Panel'
    assert recipe_page.heading_two == "RecipesAdd New"
    assert recipe_page.find_element(*recipe_page.LOCATORS.save).is_displayed()
