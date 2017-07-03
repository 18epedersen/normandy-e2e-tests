"""Pytest."""
import pytest
from pages.login import LDAPLogin


@pytest.mark.nondestructive
def test_duo_login(conf, base_url, selenium):
    """Test successfully login Normandy."""
    """Pass auth0 by providing the correct QR code."""
    base_url = conf.get('stage', 'base_url')
    username = conf.get('variables', 'username')
    password = conf.get('variables', 'password')
    page = LDAPLogin(selenium, base_url).open()
    duo = page.login(username, password)
    duo.switch_to_frame(
      duo.find_element(*duo.duoiframe_locator))
    secret = conf.get('variables', 'secret')
    home = duo.login_duo(secret)
    home.switch_to_default_content()
    # fix assert statement
    assert home.heading == 'shield'
