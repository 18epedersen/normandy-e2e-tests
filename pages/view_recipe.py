from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
from pages.edit_recipe import EditRecipe
import time


class ViewRecipe(Base):
    """View Recipe."""

    LOCATORS = locators.ViewRecipe

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
        self.find_element(*self.LOCATORS.request_approval_button).click()
        time.sleep(5)
        print("in click request approval button")
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
        self.find_element(*self.LOCATORS.approval_request_button).click()
        return ApprovalHistory(self.selenium,
                               self.base_url).wait_for_page_to_load()

    def publish_recipe(self):
        """Publish a recipe."""
        self.find_element(*self.LOCATORS.pubilsh_button).click()
        self.find_element(*self.LOCATORS.ok_button).click()
        return self

    def disable_recipe(self):
        """Disable a recipe."""
        self.find_element(*self.LOCATORS.disable_button).click()
        self.find_element(*self.LOCATORS.ok_button).click()
