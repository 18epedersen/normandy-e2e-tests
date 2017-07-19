"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_save_recipe(conf, base_url, selenium, qr_code):
    """Test creating a recipe and successfully submitting it."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page = home_page.click_add_recipe()
    recipe_page, recipe_name, messages_list = recipe_page.save_recipe(conf)
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.request_button).is_displayed()
    assert 'Recipe saved.' in messages_list
