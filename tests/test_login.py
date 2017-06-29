import pytest
from page.login import Login


@pytest.mark.nondestructive
def test_login(base_url, selenium, variables):
    """Test successful login into demo LDAP account."""
    page = Login(selenium, base_url).open()
    page.login(variables['username'], variables['password'])
    assert page.heading == "2-Step Verification"
