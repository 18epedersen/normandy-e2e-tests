"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_ldap_login(conf, base_url, selenium):
    """Test successful login into demo LDAP account."""
    # base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    ldap_page = LDAPLogin(selenium, base_url)
    ldap_page.open()
    ldap_page.login(username, password)
    assert ldap_page.heading == '2-Step Verification'
