"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_ldap_login(conf, base_url, selenium):
    """Test successful login into demo LDAP account."""
    LDAP = LDAPLogin(selenium, base_url)
    ldap_page = LDAP.login_handler(conf, selenium, base_url)
    assert ldap_page.heading == '2-Step Verification'
