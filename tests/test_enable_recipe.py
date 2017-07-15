"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
import time


@pytest.mark.nondestructive
def test_enable_recipe(conf, base_url, selenium):
    """Test the approval flow of creating a recipe."""
    time.sleep(120)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page, recipe_name = home_page.create_approved_and_enabled_recipe(
     conf)
    notification_text_list = recipe_page.get_notification_texts
    assert "Recipe enabled." in notification_text_list
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.disablebutton).is_displayed()
