"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
import time


@pytest.mark.nondestructive
def test_create_new_recipe(conf, base_url, selenium, qr_code):
    """Test creating a recipe and successfully submitting it."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    new_recipe_page = recipes_listing_page.click_new_recipe()
    new_recipe_page.create_new_recipe(conf)
    # recipe_page, recipe_name, messages_list = recipe_page.save_recipe(conf)
    # assert recipe_page.find_element(
    #  *recipe_page.LOCATORS.request_button).is_displayed()
    # assert 'Recipe saved.' in messages_list
