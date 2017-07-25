"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
import time


@pytest.mark.nondestructive
def test_add_recipe(conf, base_url, selenium, qr_code):
    """Test adding a recipe."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    new_recipe_page = recipes_listing_page.click_new_recipe()
    time.sleep(600)
    assert new_recipe_page.find_element(
     *new_recipe_page.LOCATORS.primary).is_displayed()
    # time.sleep(600)
    # recipe_page = home_page.click_add_recipe()
    # assert home_page.heading == 'SHIELD Control Panel'
    # assert recipe_page.heading_two == "RecipesAdd New"
