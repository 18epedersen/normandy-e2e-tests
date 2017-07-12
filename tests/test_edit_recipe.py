"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
from tests.conftest import create_recipe


@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium):
    """Find recipe on home page, and edit recipe."""
    """Check recipe was correctly changed."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    home_page, approve_text = create_recipe(conf, home_page, False)
    found, recipe_page = home_page.find_recipe_in_table(conf)
    home_page, approve_text = recipe_page.edit_recipe_handler(conf, True)
    result, recipe_page = home_page.find_recipe_in_table(conf)
    value = recipe_page.find_recipe_helper()
    recipe_new_filter_message = conf.get('recipe', 'recipe_new_filter_message')
    recipe_new_action = conf.get('recipe', 'recipe_new_action')
    recipe_thanks_message = conf.get('recipe', 'recipe_thanks_message')
    recipe_post_url = conf.get('recipe', 'recipe_post_url')
    recipe_learn_more = conf.get('recipe', 'recipe_learn_more')
    recipe_learn_more_url = conf.get('recipe', 'recipe_learn_more_url')
    assert approve_text == "APPROVED\nLATEST DRAFT"
    assert home_page.find_element(*home_page.LOCATORS.recipetable).is_displayed() # noqa
    assert result, "recipe name not found"
    assert recipe_page.find_element(*recipe_page.LOCATORS.surveyid).get_attribute('value') == recipe_new_filter_message # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.actionmessage).get_attribute('value') == recipe_message # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.thanksmessage).get_attribute('value') == recipe_thanks_message # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.postanswerurl).get_attribute('value') == recipe_post_url # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learnmore).get_attribute('value') == recipe_learn_more # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learnmoreurl).get_attribute('value') == recipe_learn_more_url # noqa
    assert value == recipe_new_action
