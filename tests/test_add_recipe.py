"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_add_recipe(conf, base_url, selenium):
    """Test creating a recipe and successfully submitting it."""
    # base_url = conf.get('stage', 'base_url')
    print("entered add test")
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    ldap_page = LDAPLogin(selenium, base_url).open()
    duo_page = ldap_page.login(username, password)
    secret = conf.get('variables', 'secret')
    home_page = duo_page.login_duo(secret)
    recipe_page = home_page.add_recipe()
    print("recipe", recipe_page.heading_two)
    assert recipe_page.heading_two == "RecipesAdd New"
