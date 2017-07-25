import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_approve_recipe(conf, base_url, selenium, qr_code):
    """Test the approval flow of creating a recipe."""
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf, qr_code)
    recipe_page, messages_list = home_page.create_approved_recipe(conf)
    assert 'Approval requested.' in messages_list
    assert recipe_page.find_element(
     *recipe_page.LOCATORS.enable_button).is_displayed()
