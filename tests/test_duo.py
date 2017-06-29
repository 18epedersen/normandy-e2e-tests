import pytest
from pages.login import Login


@pytest.mark.nondestructive
def test_duo(base_url, selenium, variables):
    """Test successfully login Normandy."""
    """Pass auth0 by providing the correct QR code."""
    page = Login(selenium, base_url).open()
    duo = page.login(variables['username'], variables["password"])
    duo.switch_to_frame(
      duo.find_element(*duo._duoiframe_locator))
    home = duo.login_duo(variables['secret'])
    home.switch_to_default_content()
    # fix assert statement
    assert home.heading == "shield"
