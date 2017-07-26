"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_create_new_recipe(conf, base_url, selenium, qr_code):
    """Test creating a recipe and successfully submitting it."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    new_recipe_page = recipes_listing_page.click_new_recipe()
    view_recipe_page = new_recipe_page.create_new_recipe(conf)
    assert view_recipe_page.alert_message == "You are viewing a draft."
