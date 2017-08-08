import pytest
from pages.ldap_login import LDAPLogin
# from tests.conftest import find_recipe_rest_api


@pytest.mark.nondestructive
def test_create_new_recipe(conf, base_url, selenium, qr_code):
    """Test creating a recipe."""
    """Clicking new recipe and filling out recipe form."""
    ldap_page = LDAPLogin(selenium, base_url)
    home_page = ldap_page.setup(conf, qr_code)
    recipes_listing_page = home_page.click_recipes()
    new_recipe_page = recipes_listing_page.click_new_recipe()
    view_recipe_page, recipe_action, recipe_name = new_recipe_page.create_new_recipe(conf) # noqa
    assert view_recipe_page.alert_message == "You are viewing a draft."
    assert view_recipe_page.find_element(
     *view_recipe_page.LOCATORS.edit_button).is_displayed()

    # check that the created values are at the rest api endpoint
