"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_duo_login(conf, base_url, selenium):
    """Test successfully login Normandy."""
    """Pass auth0 by providing the correct QR code."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    assert home_page.heading == 'SHIELD Control Panel'
