from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
from pages.edit_recipe import EditRecipe
import time


class ViewRecipe(Base):
    """View Recipe."""

    LOCATORS = locators.ViewRecipe

    @property
    def get_action_name(self):
        """Get recipe action name."""
        action_name = self.find_element(*self.LOCATORS.action_name)
        return action_name.text

    def wait_for_page_to_load(self):
        """Wait for recipe page's submit button."""
        # self.wait.until(EC.visibility_of_element_located(
        #  self.LOCATORS.alert_message))
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.edit_button))
        print("in wait for page to load of view recipe")
        return self

    def click_request_approval(self):
        """Click add button to create recipe."""
        request_approval_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.request_approval_button))
        print("request approval enabled", request_approval_button.is_enabled())
        request_approval_button.click()
        # self.find_element(*self.LOCATORS.request_approval_button).click()
        time.sleep(10)
        # print("in click request approval button")
        # return self
        return ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def click_edit(self):
        """Click add button to create recipe."""
        self.find_element(*self.LOCATORS.edit_button).click()
        return EditRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def click_clone(self):
        """Click add button to create recipe."""
        from pages.clone_recipe import CloneRecipe
        self.find_element(*self.LOCATORS.clone_button).click()
        return CloneRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def click_approval_request(self):
        """Click approval request button."""
        from pages.approval_history import ApprovalHistory
        print("entered click approval request")
        approval_request_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.approval_request_button))
        print("approval enabled", approval_request_button.is_enabled())
        approval_request_button.click()
        # self.find_element(*self.LOCATORS.approval_request_button).click()
        return ApprovalHistory(self.selenium,
                               self.base_url).wait_for_page_to_load()

    def publish_recipe(self):
        """Publish a recipe."""
        publish_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.publish_button))
        print("published enabled", publish_button.is_enabled())
        publish_button.click()
        # self.find_element(*self.LOCATORS.publish_button).click()
        # ok_button = self.wait.until(EC.element_to_be_clickable(
        #   self.LOCATORS.ok_button))
        # print("ok enabled", ok_button.is_enabled())
        # ok_button.click()
        cancel_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.cancel_button))
        print("ok enabled", cancel_button.is_enabled())
        cancel_button.click()
        time.sleep(10)
        # return self

    def disable_recipe(self):
        """Disable a recipe."""
        self.find_element(*self.LOCATORS.disable_button).click()
        self.find_element(*self.LOCATORS.ok_button).click()
