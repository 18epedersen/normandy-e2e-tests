"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_verify_col_names(conf, base_url, selenium, qr_code):
    """Test that column values of a recipe is correctly saved."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page, recipe_name, messages_list = home_page.create_approved_and_enabled_recipe(conf) # noqa
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(
     recipe_name)
    assert found_recipe
    assert recipe_name == row_content[0]
    assert conf.get('recipe', 'recipe_action') == row_content[1]
