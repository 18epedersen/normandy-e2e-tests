"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base import BasePage
import pytest
import configparser
import uuid
import time


@pytest.fixture
def conf():
    """Read config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


class HomePage(BasePage):
    """Class for Normandy Control UI Home."""

    def __init__(self, conf):
        """Create home page."""
        self.addbutton_locator = conf.get('home', 'addbutton_locator')
        self.name_locator = conf.get('recipe', 'name_locator')
        self.filtertextbox_locator = conf.get('recipe',
                                              'filtertextbox_locator')
        self.action_locator = conf.get('recipe', 'action')
        self.actionmessage_locator = conf.get('recipe',
                                              'actionmessage_locator')
        self.save_locator = conf.get('recipe', 'save_locator')
        self.requestbutton_locator = conf.get('recipe',
                                              'requestbutton_locator')
        self.approvebutton_locator = conf.get('recipe',
                                              'approvebutton_locator')
        self.approvemessagetextbox_locator = conf.get('recipe',
                                                      'approvemessagetextbox_locator')
        self.approvemessagebutton_locator = conf.get('recipe',
                                                     'approvemessagebutton_locator')
        self.enablebutton_locator = conf.get('recipe', 'enablebutton_locator')
        self.confirmbutton_locator = conf.get('recipe',
                                              'confirmbutton_locator')
        self.recipesbreadcrumb_locator = conf.get('recipe',
                                                  'recipesbreadcrumb_locator')
        # locator for recipe table

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        self.wait.until(EC.visibility_of_element_located(
           self.addrecipe_locator))
        return self

    def create_recipe(self, filter_message, action, action_message):
        """Create recipe with a unique UID."""
        self.find_element(*self.addbutton_locator).click()
        recipe_id = uuid.uuid1()
        self.find_element(*self.name_locator).send_keys(recipe_id)
        self.find_element(*self.filtertextbox_locator).send_keys(
          filter_message)
        select = Select(self.find_element(*self.action_locator))
        select.select_by_value(action)
        self.find_element(*self.actionmessage_locator).send_keys(
         action_message)
        self.find_element(*self.save_locator).click()
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
