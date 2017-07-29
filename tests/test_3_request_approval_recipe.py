"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_request_approval(conf, base_url, selenium, qr_code):
    """Test the approval flow of creating a recipe."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    view_recipe_page = recipes_listing_page.select_top_recipe()
    view_recipe_page = view_recipe_page.click_request_approval()
    assert view_recipe_page.alert_message == "This is a pending approval."
