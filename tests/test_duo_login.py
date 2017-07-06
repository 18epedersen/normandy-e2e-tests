"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_duo_login(conf, base_url, selenium):
    """Test successfully login Normandy."""
    """Pass auth0 by providing the correct QR code."""
    # base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    ldap_page = LDAPLogin(selenium, base_url)
    ldap_page.open()
    duo_page = ldap_page.login(username, password)
    secret = conf.get('variables', 'secret')
    home_page = duo_page.login_duo(secret)
    assert home_page.heading == 'SHIELD Control Panel'
