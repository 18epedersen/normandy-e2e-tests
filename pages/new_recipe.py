"""Expected conditions."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from selenium.webdriver.support.ui import Select
from pages import locators
import uuid
import time


class NewRecipe(Base):
    """Recipe class."""

    LOCATORS = locators.NewRecipe

    # @property
    # def get_action_selected(self):
    #     """Return action selected on recipe page."""
    #     select = Select(self.find_element(*self.LOCATORS.action))
    #     value = select.first_selected_option.get_attribute('value')
    #     return value

    def wait_for_page_to_load(self):
        """Wait for recipe page's submit button."""
        self.wait.until(EC.visibility_of_element_located(self.LOCATORS.primary))
        return self

    # def wait_for_request_button(self):
    #     """Wait for request button to show."""
    #     self.wait.until(EC.visibility_of_element_located(
    #      self.LOCATORS.request_button))
    #     return self
    #
    # def wait_for_save_draft_button(self):
    #     """Wait for save draft button to show."""
    #     self.wait.until(EC.visibility_of_element_located(
    #      self.LOCATORS.save_draft))
    #     return self
    #
    # def wait_for_enable_button(self):
    #     """Wait for enable button to show."""
    #     self.wait.until(EC.visibility_of_element_located(
    #      self.LOCATORS.enable_button))
    #     return self
    #
    # def wait_for_disable_button(self):
    #     """Wait for disable button to show."""
    #     self.wait.until(EC.visibility_of_element_located(
    #      self.LOCATORS.disable_button))
    #     return self

    def create_new_recipe(self, conf):
        """Save recipe with a unique UUID."""
        """Return a recipe page, recipe name, and notification's texts."""
        extra_filter_expression = conf.get('recipe',
                                           'extra_filter_expression')
        recipe_action = conf.get('recipe', 'action')
        recipe_name = str(uuid.uuid1().hex)
        name = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.name))
        name.clear()
        name.send_keys(recipe_name)
        self.find_element(*self.LOCATORS.extra_filter_expression).send_keys(
          extra_filter_expression)
        self.action_configuration(conf, recipe_action)
        save_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.save_button))
        save_button.click()
        # messages_list = self.message_alert_helper()
        # recipe_page = Recipe(self.selenium, self.base_url)
        # return recipe_page.wait_for_request_button(), recipe_name, messages_list

    def action_configuration(self, conf, recipe_action):
        """Configure action for recipe."""
        select_action_dropdown = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.select_action_dropdown))
        select_action_dropdown.click()
        show_heartbeat = self.find_element(*self.LOCATORS.show_heartbeat)
        show_heartbeat.click()
        time.sleep(500)
        # select = Select(select_action_dropdown)
        # select.select_by_value(recipe_action)
        action_message = conf.get('recipe', 'message')
        if recipe_action == 'console-log':
            self.find_element(*self.LOCATORS.action_message).clear()
            self.find_element(*self.LOCATORS.action_message).send_keys(action_message) # noqa
        if recipe_action == 'show-heartbeat':
            survey_id = conf.get('recipe', 'survey_id')
            thanks_message = conf.get('recipe', 'thanks_message')
            post_url = conf.get('recipe', 'post_url')
            learn_more = conf.get('recipe', 'learn_more')
            learn_more_url = conf.get('recipe', 'learn_more_url')
            self.find_element(*self.LOCATORS.survey_id).clear()
            self.find_element(*self.LOCATORS.survey_id).send_keys(survey_id) # noqa
            self.find_element(*self.LOCATORS.action_message).clear()
            self.find_element(*self.LOCATORS.action_message).send_keys(action_message) # noqa
            self.find_element(*self.LOCATORS.thanks_message).clear()
            self.find_element(*self.LOCATORS.thanks_message).send_keys(thanks_message) # noqa
            self.find_element(*self.LOCATORS.post_answer_url).clear()
            self.find_element(*self.LOCATORS.post_answer_url).send_keys(post_url) # noqa
            self.find_element(*self.LOCATORS.learn_more).clear()
            self.find_element(*self.LOCATORS.learn_more).send_keys(learn_more) # noqa
            self.find_element(*self.LOCATORS.learn_more_url).clear()
            self.find_element(*self.LOCATORS.learn_more_url).send_keys(learn_more_url) # noqa
        if recipe_action == 'preference-experiment':
            pass


    # def message_alert_helper(self):
    #     """Return a list of messages' texts from notifications."""
    #     notif = self.wait.until(EC.visibility_of_element_located(
    #       self.LOCATORS.notif))
    #     messages = notif.find_elements(*self.LOCATORS.message_alert)
    #     messages_list = []
    #     for message in messages:
    #         messages_list.append(message.text)
    #     self.wait.until(EC.invisibility_of_element_located(
    #      self.LOCATORS.message_alert))
    #     return messages_list
    #
    # def approve_new_recipe(self, conf):
    #     """Approve recipe."""
    #     """Return recipe page and list of messages' texts from notifications"""
    #     messages_list = self.approve_recipe_helper(conf)
    #     recipe_page = Recipe(self.selenium, self.base_url)
    #     return recipe_page.wait_for_enable_button(), messages_list
    #
    # def approve_enabled_recipe(self, conf):
    #     """Approve an existing enabled recipe."""
    #     """Return recipe page and list of messages' texts from notifications"""
    #     messages_list = self.approve_recipe_helper(conf)
    #     recipe_page = Recipe(self.selenium, self.base_url)
    #     return recipe_page.wait_for_disable_button(), messages_list
    #
    # def approve_recipe_helper(self, conf):
    #     """Approve recipe helper."""
    #     """Returns list of messages' texts from notifications."""
    #     recipe_approve_message = conf.get('recipe', 'recipe_approve')
    #     request_button = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.request_button))
    #     request_button.click()
    #     approve_button = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.approve_button))
    #     approve_button.click()
    #     self.find_element(*self.LOCATORS.approve_message_textbox).send_keys(
    #      recipe_approve_message)
    #     approve_message_button = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.approve_message_button))
    #     approve_message_button.click()
    #     messages_list = self.message_alert_helper()
    #     return messages_list
    #
    # def enable_recipe(self):
    #     """Enable a recipe."""
    #     """Return recipe page, and messages' texts from notifications."""
    #     enable_button = self.wait.until(EC.element_to_be_clickable(
    #           self.LOCATORS.enable_button))
    #     enable_button.click()
    #     confirm_button = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.confirm_button))
    #     confirm_button.click()
    #     messages_list = self.message_alert_helper()
    #     recipe_page = Recipe(self.selenium, self.base_url)
    #     return recipe_page.wait_for_disable_button(), messages_list
    #
    # def disable_recipe(self):
    #     """Disable a recipe."""
    #     """Return recipe page, and messages' texts from notifications."""
    #     disable_button = self.wait.until(EC.element_to_be_clickable(
    #           self.LOCATORS.disable_button))
    #     disable_button.click()
    #     confirm_delete_button = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.confirm_delete))
    #     confirm_delete_button.click()
    #     messages_list = self.message_alert_helper()
    #     recipe_page = Recipe(self.selenium, self.base_url)
    #     return recipe_page.wait_for_save_draft_button(), messages_list
    #
    # def click_home_button(self):
    #     """Return home object."""
    #     from pages.home import Home
    #     recipes_breadcrumb = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.recipes_breadcrumb))
    #     recipes_breadcrumb.click()
    #     return Home(self.selenium, self.base_url).wait_for_page_to_load()
    #
    # def edit_enabled_recipe(self, conf):
    #     """Edit recipe."""
    #     """Call approve enabled recipe to save and approve edited recipe."""
    #     recipe_new_filter_message = conf.get('recipe',
    #                                          'recipe_new_filter_message')
    #     recipe_new_action = conf.get('recipe', 'recipe_new_action')
    #     filter_textbox = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.filter_textbox))
    #     filter_textbox.clear()
    #     filter_textbox.send_keys(recipe_new_filter_message)
    #     self.action_configuration(conf, recipe_new_action)
    #     save_draft_button = self.wait.until(EC.element_to_be_clickable(
    #       self.LOCATORS.save_draft))
    #     save_draft_button.click()
    #     self.message_alert_helper()
    #     return self.approve_enabled_recipe(conf)
    #
