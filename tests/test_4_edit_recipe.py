"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium, foxpuppet, qr_code):
    """Select a recipe on home page, and edit recipe."""
    """Check recipe was correctly changed."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    view_recipe_page = recipes_listing_page.select_top_recipe()
    edit_recipe_page = view_recipe_page.click_edit()
    new_recipe_action = edit_recipe_page.edit_recipe(conf)
    home_page = edit_recipe_page.click_home_breadcrumb()
    recipes_listing_page = home_page.click_recipes()
    view_recipe_page = recipes_listing_page.select_top_recipe()
    edit_recipe_page = view_recipe_page.click_edit()
    assert new_recipe_action == edit_recipe_page.get_selected_action()
