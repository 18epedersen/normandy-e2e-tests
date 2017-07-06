"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators


class Home(Base):
    """Class for Normandy Control UI Home."""

    LOCATORS = locators.Home

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        self.wait.until(EC.visibility_of_element_located(
           self.LOCATORS.addbutton))
        return self

    def add_recipe(self):
        """Click add button to create recipe."""
        from pages.recipe import Recipe
        self.find_element(*self.LOCATORS.addbutton).click()
        return Recipe(self.selenium, self.base_url).wait_for_page_to_load()
