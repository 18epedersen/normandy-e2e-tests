import pytest
from pages.ldap_login import LDAPLogin
# import time


@pytest.mark.nondestructive
def test_publish_recipe(conf, base_url, selenium, qr_code):
    """Test publishing a recipe."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    view_recipe_page = recipes_listing_page.select_top_recipe()
    view_recipe_page = view_recipe_page.publish_recipe()
    assert view_recipe_page.alert_message == "This is the published version."
    # check that the recipe exists at the api endpoint
