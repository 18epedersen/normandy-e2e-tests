import pytest
from pages.ldap_login import LDAPLogin
# import time


@pytest.mark.nondestructive
def test_clone_recipe(conf, base_url, selenium, qr_code):
    """Test publishing a recipe."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    view_recipe_page = recipes_listing_page.select_top_recipe()
    clone_recipe_page = view_recipe_page.click_clone_recipe()
    view_recipe_page = clone_recipe_page.clone_recipe()
    assert view_recipe_page.alert_message == "You are viewing a draft."
    # check that the recipe does with new parameters exists at the api endpoint
