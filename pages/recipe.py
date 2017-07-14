"""Expected conditions."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from selenium.webdriver.support.ui import Select
from pages import locators
import uuid
import time
# import expected


class Recipe(Base):
    """Recipe class."""

    LOCATORS = locators.Recipe
    TIMEOUT = 60

    @property
    def get_action_selected(self):
        """Return action selected on the recipe page."""
        select = Select(self.find_element(*self.LOCATORS.action))
        value = select.first_selected_option.get_attribute('value')
        return value

    def wait_for_page_to_load(self):
        """Wait for page load method for submit."""
        self.wait.until(EC.visibility_of_element_located(self.LOCATORS.save))
        return self

    def wait_for_request_button(self):
        """Wait for request button to show."""
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.requestbutton))
        return self

    def wait_for_save_draft_button(self):
        """Wait for request button to show."""
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.savedraft))
        return self

    def wait_for_enable_button(self):
        """Wait for enable button to show."""
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.enablebutton))
        return self

    def wait_for_disable_button(self):
        """Wait for disable button to show."""
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.disablebutton))
        return self

    def save_recipe(self, conf):
        """Save recipe with a unique UUID."""
        print("entered save recipe")
        recipe_additional_filters = conf.get('recipe',
                                             'recipe_additional_filters')
        recipe_action = conf.get('recipe', 'recipe_action')
        recipe_name = str(uuid.uuid1().hex)
        name_field = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.name))
        name_field.clear()
        name_field.send_keys(recipe_name)
        self.find_element(*self.LOCATORS.filtertextbox).send_keys(
          recipe_additional_filters)
        self.action_configuration(conf, recipe_action)
        save_new_recipe_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.save))
        save_new_recipe_button.click()
        return Recipe(self.selenium, self.base_url,
                      self.TIMEOUT).wait_for_request_button(), recipe_name

    def approve_new_recipe(self, conf):
        """Approve recipe."""
        print("entered approve new recipe")
        self.approve_recipe_helper(conf)
        return Recipe(self.selenium,
                      self.base_url).wait_for_enable_button()

    def approve_enabled_recipe(self, conf):
        """Approve an existing enabled recipe."""
        print("entered approved enabled recipe")
        self.approve_recipe_helper(conf)
        return Recipe(self.selenium, self.base_url, 60).wait_for_disable_button()

    def approve_recipe_helper(self, conf):
        """Approve recipe helper."""
        print("entered approve recipe helper")
        recipe_approve_message = conf.get('recipe', 'recipe_approve')
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
        time.sleep(5)

    def enable_recipe(self):
        """Enable a recipe."""
        print("entered enable recipe")
        enable_button = self.wait.until(EC.element_to_be_clickable(
              self.LOCATORS.enablebutton))
        enable_button.click()
        confirm_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.confirmbutton))
        confirm_button.click()
        return Recipe(self.selenium, self.base_url,
                      60).wait_for_disable_button()

    def click_home_button(self):
        """Return home object."""
        from pages.home import Home
        time.sleep(10)
        self.wait.until(EC.invisibility_of_element_located(
         self.LOCATORS.messagealert))
        recipes_breadcrumb = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.recipesbreadcrumb))
        recipes_breadcrumb.click()
        return Home(self.selenium, self.base_url).wait_for_page_to_load()

    def edit_enabled_recipe(self, conf):
        """Edit recipe."""
        recipe_new_filter_message = conf.get('recipe',
                                             'recipe_new_filter_message')
        recipe_new_action = conf.get('recipe', 'recipe_new_action')
        filter_textbox = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.filtertextbox))
        filter_textbox.clear()
        filter_textbox.send_keys(recipe_new_filter_message)
        self.action_configuration(conf, recipe_new_action)
        save_draft_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.savedraft))
        save_draft_button.click()
        return self.approve_enabled_recipe(conf)

    def action_configuration(self, conf, recipe_action):
        """Configure action for recipe."""
        print("entered action configuration")
        action_dropdown = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.action))
        select = Select(action_dropdown)
        select.select_by_value(recipe_action)
        action_message = conf.get('recipe', 'recipe_message')
        if recipe_action == 'console-log':
            self.find_element(*self.LOCATORS.actionmessage).clear()
            self.find_element(*self.LOCATORS.actionmessage).send_keys(action_message) # noqa
        if recipe_action == 'show-heartbeat':
            recipe_survey_id = conf.get('recipe', 'recipe_survey_id')
            recipe_thanks_message = conf.get('recipe', 'recipe_thanks_message')
            recipe_post_url = conf.get('recipe', 'recipe_post_url')
            recipe_learn_more = conf.get('recipe', 'recipe_learn_more')
            recipe_learn_more_url = conf.get('recipe', 'recipe_learn_more_url')
            self.find_element(*self.LOCATORS.surveyid).clear()
            self.find_element(*self.LOCATORS.surveyid).send_keys(recipe_survey_id) # noqa
            self.find_element(*self.LOCATORS.actionmessage).clear()
            self.find_element(*self.LOCATORS.actionmessage).send_keys(action_message) # noqa
            self.find_element(*self.LOCATORS.thanksmessage).clear()
            self.find_element(*self.LOCATORS.thanksmessage).send_keys(recipe_thanks_message) # noqa
            self.find_element(*self.LOCATORS.postanswerurl).clear()
            self.find_element(*self.LOCATORS.postanswerurl).send_keys(recipe_post_url) # noqa
            self.find_element(*self.LOCATORS.learnmore).clear()
            self.find_element(*self.LOCATORS.learnmore).send_keys(recipe_learn_more) # noqa
            self.find_element(*self.LOCATORS.learnmoreurl).clear()
            self.find_element(*self.LOCATORS.learnmoreurl).send_keys(recipe_learn_more_url) # noqa
        if recipe_action == 'preference-experiment':
            pass

    def delete_recipe(self):
        """Delete a recipe."""
        from pages.home import Home
        self.find_element(*self.LOCATORS.deletebutton).click()
        confirm_delete = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.confirmdelete))
        confirm_delete.click()
        return Home(self.selenium, self.base_url, 30).wait_for_page_to_load()
