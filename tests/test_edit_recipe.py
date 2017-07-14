"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin


@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium):
    """Find recipe on home page, and edit recipe."""
    """Check recipe was correctly changed."""
    LDAP = LDAPLogin(selenium, base_url)
    duo_page = LDAP.login_handler(conf, selenium, base_url)
    home_page = duo_page.login_duo_handler(conf, selenium, base_url)
    home_page, approve_text, recipe_name = home_page.create_approved_recipe(
     conf, False)
    found, recipe_page = home_page.find_recipe_in_table(recipe_name)
    home_page, approve_text = recipe_page.edit_recipe(conf, True)
    found_recipe, recipe_page = home_page.find_recipe_in_table(recipe_name)
    action_selected = recipe_page.which_action_selected()
    assert approve_text == "APPROVED\nLATEST DRAFT"
    assert home_page.find_element(*home_page.LOCATORS.recipetable).is_displayed() # noqa
    assert found_recipe, "recipe name not found"
    assert recipe_page.find_element(*recipe_page.LOCATORS.surveyid).get_attribute('value') == conf.get('recipe', 'recipe_new_filter_message') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.actionmessage).get_attribute('value') == recipe_message # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.thanksmessage).get_attribute('value') == conf.get('recipe', 'recipe_thanks_message') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.postanswerurl).get_attribute('value') == conf.get('recipe', 'recipe_post_url') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learnmore).get_attribute('value') == conf.get('recipe', 'recipe_learn_more')  # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learnmoreurl).get_attribute('value') == conf.get('recipe', 'recipe_learn_more_url') # noqa
    assert action_selected == conf.get('recipe', 'recipe_new_action')
