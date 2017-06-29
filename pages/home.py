from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages.recipe import Recipe


class Home(Base):
    """Class for Normandy Control UI Home."""

    _addrecipe_locator = ".button"
    # locator for recipe table

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        self.wait.until(EC.visibility_of_element_located(
           self._addrecipe_locator))
        return self

    def add_recipe(self):
        """Add a new recipe."""
        self.find_element(*self._addrecipe_locator).click()
        return Recipe(self.selenium, self.base_url).wait_for_page_to_load()
