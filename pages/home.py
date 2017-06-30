"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from pages.recipe import RecipePage
import pytest
import configparser


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
        # locator for recipe table

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        self.wait.until(EC.visibility_of_element_located(
           self.addrecipe_locator))
        return self

    def add_recipe(self):
        """Add a new recipe."""
        self.find_element(*self.addbutton_locator).click()
        return RecipePage(self.selenium, self.base_url).wait_for_page_to_load()
