"""Pytest."""
import pytest
from pages.ldap_login import LDAPLogin
import time


@pytest.mark.nondestructive
def test_edit_recipe(conf, base_url, selenium):
    """Find recipe on home page, and edit recipe."""
    """Check recipe was correctly changed."""
    time.sleep(90)
    LDAP = LDAPLogin(selenium, base_url)
    home_page = LDAP.setup(conf)
    recipe_page, recipe_name = home_page.create_approved_and_enabled_recipe(
     conf)
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page, row_content = home_page.find_recipe_in_table(recipe_name)
    recipe_page = recipe_page.edit_enabled_recipe(conf)
    home_page = recipe_page.click_home_button()
    found_recipe, recipe_page = home_page.find_recipe_in_table(recipe_name)
    action_selected = recipe_page.get_action_selected
    assert found_recipe
    assert recipe_page.find_element(*recipe_page.LOCATORS.surveyid).get_attribute('value') == conf.get('recipe', 'recipe_survey_id') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.actionmessage).get_attribute('value') == conf.get('recipe', 'recipe_message') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.thanksmessage).get_attribute('value') == conf.get('recipe', 'recipe_thanks_message') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.postanswerurl).get_attribute('value') == conf.get('recipe', 'recipe_post_url') # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learnmore).get_attribute('value') == conf.get('recipe', 'recipe_learn_more')  # noqa
    assert recipe_page.find_element(*recipe_page.LOCATORS.learnmoreurl).get_attribute('value') == conf.get('recipe', 'recipe_learn_more_url') # noqa
    assert action_selected == conf.get('recipe', 'recipe_new_action')
