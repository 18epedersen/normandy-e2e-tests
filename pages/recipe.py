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
        self.wait.until(EC.visibility_of_element_located(self.LOCATORS.requestbutton))
        return self

    def save_recipe(self, filter_message, action, action_message):
        """Save recipe with a unique UID."""
        recipe_id = uuid.uuid1().hex
        time.sleep(10)
        self.find_element(*self.LOCATORS.name).send_keys(recipe_id)
        self.find_element(*self.LOCATORS.filtertextbox).send_keys(filter_message)
        time.sleep(10)
        select = Select(self.find_element(*self.LOCATORS.action))
        select.select_by_value(action)
        self.find_element(*self.LOCATORS.actionmessage).send_keys(action_message)
        time.sleep(10)
        self.find_element(*self.LOCATORS.save).click()
        return Recipe(self.selenium, self.base_url).wait_for_request_button(), recipe_id

    def approve_recipe(self, approve_message):
        """Approve recipe."""
        from pages.home import Home
        self.find_element(*self.LOCATORS.requestbutton).click()
        time.sleep(5)
        self.find_element(*self.LOCATORS.approvebutton).click()
        self.find_element(*self.LOCATORS.approvemessagetextbox).send_keys(
         approve_message)
        self.find_element(*self.LOCATORS.approvemessagebutton).click()
        time.sleep(5)
        self.find_element(*self.LOCATORS.enablebutton).click()
        self.find_element(*self.LOCATORS.confirmbutton).click()
        time.sleep(15)
        approve_text = self.find_element(*self.LOCATORS.statustext).text
        self.find_element(*self.LOCATORS.recipesbreadcrumb).click()
        # time.sleep(600)
        return Home(self.selenium, self.base_url).wait_for_page_to_load(), approve_text

    def edit_recipe(self):
        pass
