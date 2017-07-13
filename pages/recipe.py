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
        print("entered save recipe")
        recipe_name = str(uuid.uuid1().hex)
        with open('.recipe_name', 'w') as f:
            f.write(recipe_name)
        name_field = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.name))
        name_field.send_keys(recipe_name)
        self.find_element(*self.LOCATORS.filtertextbox).send_keys(
          recipe_additional_filters)
        self.action_configuration(conf, recipe_action)
        save_new_recipe_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.save))
        save_new_recipe_button.click()
        return Recipe(self.selenium, self.base_url).wait_for_request_button()

    def save_recipe_handler(self, conf):
        """Save recipe handler."""
        print("save recipe handler")
        recipe_additional_filters = conf.get('recipe',
                                             'recipe_additional_filters')
        recipe_action = conf.get('recipe', 'recipe_action')
        self.save_recipe(conf, recipe_additional_filters, recipe_action)

    def approve_recipe(self, recipe_approve_message, recipe_enabled):
        """Approve recipe."""
        from pages.home import Home
        print("entered approve recipe")
        request_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.requestbutton))
        request_button.click()
        approve_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.approvebutton))
        approve_button.click()
        self.find_element(*self.LOCATORS.approvemessagetextbox).send_keys(
         recipe_approve_message)
        approve_message_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.approvemessagebutton))
        approve_message_button.click()
        if recipe_enabled:
            print("recipe is enabled")
            self.find_element(*self.LOCATORS.recipesbreadcrumb).click()
        else:
            print("in recipe.py recipe is not enabled")
            enable_button = self.wait.until(EC.element_to_be_clickable(
              self.LOCATORS.enablebutton))
            enable_button.click()
            confirm_button = self.wait.until(EC.element_to_be_clickable(
              self.LOCATORS.confirmbutton))
            confirm_button.click()
            approve_text = self.wait.until(EC.visibility_of_element_located(
              self.LOCATORS.statustext)).text
            recipes_breadcrumb = self.wait.until(EC.element_to_be_clickable(
              self.LOCATORS.recipesbreadcrumb))
            recipes_breadcrumb.click()
            time.sleep(10)
            # self.find_element(*self.LOCATORS.recipesbreadcrumb).click()
        return Home(self.selenium, self.base_url).wait_for_page_to_load(), approve_text # noqa

    def approve_recipe_handler(self, conf, recipe_enabled):
        """Approve recipe handler."""
        recipe_approve_message = conf.get('recipe', 'recipe_approve')
        return self.approve_recipe(recipe_approve_message, recipe_enabled)

    def edit_recipe(self, conf, recipe_new_filter_message, recipe_new_action,
                    enabled):
        """Edit recipe."""
        time.sleep(5)
        self.find_element(*self.LOCATORS.filtertextbox).clear()
        self.find_element(*self.LOCATORS.filtertextbox).send_keys(recipe_new_filter_message) # noqa
        time.sleep(5)
        self.action_configuration(conf, recipe_new_action)
        time.sleep(5)
        self.find_element(*self.LOCATORS.savedraft).click()
        self.approve_recipe_handler(conf, enabled)

    def edit_recipe_handler(self, conf, enabled):
        """Edit recipe handler."""
        recipe_new_filter_message = conf.get('recipe',
                                             'recipe_new_filter_message')
        recipe_new_action = conf.get('recipe', 'recipe_new_action')
        self.edit_recipe(conf, recipe_new_filter_message, recipe_new_action,
                         enabled)

    def action_configuration(self, conf, recipe_action):
        """Configure action for recipe."""
        print("entered action configuration")
        action_dropdown = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.action))
        select = Select(action_dropdown)
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
            self.find_element(*self.LOCATORS.actionmessage).clear()
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
        element = self.find_element(*self.LOCATORS.confirmdelete)
        if element.is_enabled():
            element.click()
            time.sleep(10)
        else:
            print("confirm delete is not enabled")
        # self.find_element(*self.LOCATORS.confirmdelete).click()
        return Home(self.selenium, self.base_url).wait_for_page_to_load()

    def find_recipe_helper(self):
        """Return which action was selected on the recipe page."""
        select = Select(self.find_element(*self.LOCATORS.action))
        value = select.first_selected_option.get_attribute('value')
        return value
