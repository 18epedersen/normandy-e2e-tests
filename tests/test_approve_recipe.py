"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
import time


@pytest.mark.nondestructive
def test_approve_recipe(conf, base_url, selenium):
    """Test the approval flow of creating a recipe."""
    time.sleep(30)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page = home_page.create_approved_recipe(conf)
    notification_text_list = recipe_page.get_notification_texts
    assert 'Recipe saved.' in notification_text_list
    assert 'Approval requested.' in notification_text_list
    assert "Revision was approved." in notification_text_list
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.enable_button).is_displayed()
