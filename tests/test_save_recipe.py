"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
import time


@pytest.mark.nondestructive
def test_save_recipe(conf, base_url, selenium):
    """Test creating a recipe and successfully submitting it."""
    time.sleep(140)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page = home_page.click_add_recipe()
    recipe_page.save_recipe(conf)
    notifications_text_list = recipe_page.get_notification_texts
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.requestbutton).is_displayed()
    assert 'Recipe saved.' in notifications_text_list
