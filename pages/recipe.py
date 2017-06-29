import uuid
from selenium.webdriver.support.ui import Select
from pages.base import Base
from pages.approval import Approval


class Recipe(Base):
    """Normandy recipe page for creating a recipe."""

    _name_locator = 'label.form-field:nth-child(1) > input:nth-child(2)'
    _filters_locator = 'extra_filter_expression'
    _action_locator = 'action'
    _actionmessage_locator = 'arguments.message'
    _save_locator = 'action-new'

    def wait_for_page_to_load(self):
        """Wait for method."""
        self.wait.until(EC.visibility_of_element_located(
          self._name_locator))
        return self

    def create_recipe(self, filter_message, action, action_message):
        """Create a recipe with a unique UID."""
        recipe_id = uuid.uuid1()
        self.find_element(*self._name_locator).send_keys(recipe_id)
        self.find_element(*self._filters_locator).send_keys(filter_message)
        select = Select(self.find_element(*self._action_locator))
        select.select_by_value(action)
        self.find_element(*self._actionmessage_locator).send_keys(
         action_message)
        self.find_element(*self._save_locator).click()
        return Approval(self.selenium, self.base_url).wait_for_page_to_load()
