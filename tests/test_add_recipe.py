"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_add_recipe(conf, base_url, selenium):
    """Test adding a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    recipe_page = home_page.add_recipe()
    assert recipe_page.heading_two == "RecipesAdd New"
