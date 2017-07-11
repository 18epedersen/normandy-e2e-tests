"""Expected conditions."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from selenium.webdriver.support.ui import Select
from pages import locators
import uuid
import time


class Recipe(Base):
    """Recipe class."""

    LOCATORS = locators.Recipe
    RECIPE = 'recipe'

    def wait_for_page_to_load(self):
        """Wait for page load method for submit."""
        # self.wait.until(EC.visibility_of_element_located(self.submit_locator))
        self.wait.until(EC.visibility_of_element_located(self.LOCATORS.save))
        return self

    def wait_for_request_button(self):
        """Wait for request button to show."""
        self.wait.until(EC.visibility_of_element_located(self.LOCATORS.requestbutton)) # noqa
        return self

    def wait_for_save_draft_button(self):
        """Wait for request button to show."""
        self.wait.until(EC.visibility_of_element_located(self.LOCATORS.savedraft)) # noqa
        return self

    def save_recipe(self, conf, recipe_additional_filters, recipe_action):
        """Save recipe with a unique UID."""
        recipe_name = str(uuid.uuid1().hex)
        with open('.recipe_name', 'w') as f:
            f.write(recipe_name)
        time.sleep(10)
        self.find_element(*self.LOCATORS.name).send_keys(recipe_name)
        self.find_element(*self.LOCATORS.filtertextbox).send_keys(recipe_additional_filters) # noqa
        time.sleep(10)
        self.action_configuration(conf, recipe_action)
        time.sleep(15)
        self.find_element(*self.LOCATORS.save).click()
        return Recipe(self.selenium, self.base_url, 40).wait_for_request_button() # noqa

    def save_recipe_handler(self, conf):
        """Save recipe handler."""
        recipe_additional_filters = conf.get('recipe',
                                             'recipe_additional_filters')
        recipe_action = conf.get('recipe', 'recipe_action')
        self.save_recipe(conf, recipe_additional_filters, recipe_action)

    def approve_recipe(self, recipe_approve_message):
        """Approve recipe."""
        from pages.home import Home
        self.find_element(*self.LOCATORS.requestbutton).click()
        time.sleep(5)
        self.find_element(*self.LOCATORS.approvebutton).click()
        self.find_element(*self.LOCATORS.approvemessagetextbox).send_keys(
         recipe_approve_message)
        self.find_element(*self.LOCATORS.approvemessagebutton).click()
        time.sleep(10)
        self.find_element(*self.LOCATORS.enablebutton).click()
        self.find_element(*self.LOCATORS.confirmbutton).click()
        time.sleep(15)
        approve_text = self.find_element(*self.LOCATORS.statustext).text
        self.find_element(*self.LOCATORS.recipesbreadcrumb).click()
        return Home(self.selenium, self.base_url).wait_for_page_to_load(), approve_text # noqa

    def approve_recipe_handler(self, conf):
        """Approve recipe handler."""
        recipe_approve_message = conf.get('recipe', 'recipe_approve')
        return self.approve_recipe(recipe_approve_message)

    def edit_recipe(self, conf, recipe_new_filter_message, recipe_new_action):
        """Edit recipe."""
        time.sleep(10)
        self.find_element(*self.LOCATORS.filtertextbox).clear()
        self.find_element(*self.LOCATORS.filtertextbox).send_keys(recipe_new_filter_message) # noqa
        time.sleep(10)
        self.action_configuration(conf, recipe_new_action)
        time.sleep(15)
        self.find_element(*self.LOCATORS.savedraft).click()
        self.approve_recipe_handler(conf)

    def edit_recipe_handler(self, conf):
        """Edit recipe handler."""
        recipe_new_filter_message = conf.get('recipe',
                                             'recipe_new_filter_message')
        recipe_new_action = conf.get('recipe', 'recipe_new_action')
        self.edit_recipe(conf, recipe_new_filter_message, recipe_new_action)

    def action_configuration(self, conf, recipe_action):
        """Configure action for recipe."""
        select = Select(self.find_element(*self.LOCATORS.action))
        select.select_by_value(recipe_action)
        action_message = conf.get('recipe', 'recipe_message')
        if recipe_action == 'console-log':
            self.find_element(*self.LOCATORS.actionmessage).send_keys(action_message) # noqa
        if recipe_action == 'show-heartbeat':
            recipe_survey_id = conf.get('recipe', 'recipe_survey_id')
            recipe_thanks_message = conf.get('recipe', 'recipe_thanks_message')
            recipe_post_url = conf.get('recipe', 'recipe_post_url')
            recipe_learn_more = conf.get('recipe', 'recipe_learn_more')
            recipe_learn_more_url = conf.get('recipe', 'recipe_learn_more_url')
            self.find_element(*self.LOCATORS.surveyid).send_keys(recipe_survey_id) # noqa
            self.find_element(*self.LOCATORS.actionmessage).send_keys(action_message) # noqa
            self.find_element(*self.LOCATORS.thanksmessage).send_keys(recipe_thanks_message) # noqa
            self.find_element(*self.LOCATORS.postanswerurl).send_keys(recipe_post_url) # noqa
            self.find_element(*self.LOCATORS.learnmore).send_keys(recipe_learn_more) # noqa
            self.find_element(*self.LOCATORS.learnmoreurl).send_keys(recipe_learn_more_url) # noqa

    def delete_recipe(self):
        """Delete a recipe."""
        from pages.home import Home
        self.find_element(*self.LOCATORS.deletebutton).click()
        time.sleep(10)
        self.find_element(*self.LOCATORS.confirmdelete).click()
        time.sleep(10)
        return Home(self.selenium, self.base_url).wait_for_page_to_load()

    def find_recipe_helper(self):
        """Return which action was selected on the recipe page."""
        select = Select(self.find_element(*self.LOCATORS.action))
        value = select.first_selected_option.get_attribute('value')
        return value
