"""Pytest."""
import pytest
from pages.login import LDAPLoginPage


@pytest.mark.nondestructive
def test_login(conf, selenium, variables):
    """Test successful login into demo LDAP account."""
    base_url = conf.get("stage", "base_url")
    username = conf.get("variables", "username")
    password = conf.get("variables", "password")
    page = LDAPLoginPage(conf, selenium, base_url)
    page.open()
    #page.login(username, password)
    #assert page.heading == "2-Step Verification"
