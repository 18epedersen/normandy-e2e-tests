"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_ldap_login(conf, base_url, selenium):
    """Test successful login into demo LDAP account."""
    base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    page = LDAPLogin(conf, base_url, selenium)
    page.open()
    page.login(username, password)
    assert page.heading == '2-Step Verification'
