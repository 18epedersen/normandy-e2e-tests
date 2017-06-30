"""Unique uid."""
import uuid
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base import BasePage
from pages.home import HomePage


class RecipePage(BasePage):
    """Normandy recipe page for creating a recipe."""

    _name_locator = 'label.form-field:nth-child(1) > input:nth-child(2)'
    _filtertextbox_locator = 'extra_filter_expression'
    _action_locator = 'action'
    _actionmessage_locator = 'arguments.message'
    _save_locator = 'action-new'
    _requestbutton_locator = 'button.button:nth-child(3)'
    _approvebutton_locator = '.action-approve'
    _approvemessagetextbox_locator = ".approve-dropdown > textarea:nth-child(1)"
    _approvemessagebutton_locator = '.mini-button'
    _enablebutton_locator = ".action-enable"
    _confirmbutton_locator = ".submit"
    _recipesbreadcrumb_locator = '.breadcrumbs > span:nth-child(1) > a:nth-child(1)'

    def wait_for_page_to_load(self):
        """Wait for page load method."""
        # For approve recipe, want to wait for request locator to show.
        # Is it possible to get two wait methods?
        self.wait.until(EC.visibility_of_element_located(
          self._name_locator))
        return self

    def create_recipe(self, filter_message, action, action_message):
        """Create recipe with a unique UID."""
        recipe_id = uuid.uuid1()
        self.find_element(*self._name_locator).send_keys(recipe_id)
        self.find_element(*self._filtertextbox_locator).send_keys(
          filter_message)
        select = Select(self.find_element(*self._action_locator))
        select.select_by_value(action)
        self.find_element(*self._actionmessage_locator).send_keys(
         action_message)
        self.find_element(*self._save_locator).click()
        # return Approval(self.selenium, self.base_url).wait_for_page_to_load()

    def approve_recipe(self, approve_message):
        """Approve recipe."""
        self.find_element(*self._requestbutton_locator).click()
        self.find_element(*self._approvebutton_locator).click()
        self.find_element(*self._approvemessagetextbox_locator).send_keys(
           approve_message)
        self.find_element(*self._approvemessagebutton_locator).click()
        self.find_element(*self._enablebutton_locator).click()
        self.find_element(*self._confirmbutton_locator).click()
        time.sleep(10)
        self.find_element(*self._recipesbreadcrumb_locator).click()
        return HomePage(self.selenium, self.base_url).wait_for_page_to_load()
