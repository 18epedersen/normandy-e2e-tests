"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
import time


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

    def find_recipe_in_table(self, conf):
        """Find Recipe in home page recipe table."""
        with open('.recipe_name') as f:
            recipe_name = f.read()
        recipe_table = self.find_element(*self.LOCATORS.recipetable)
        tbody = recipe_table.find_element(*self.LOCATORS.tbody)
        time.sleep(5)
        rows = tbody.find_elements(*self.LOCATORS.tr)
        found = False
        for row in rows:
            cols = row.find_elements(*self.LOCATORS.td)
            for col in cols:
                if col.text == recipe_name:
                    found = True
                    col.click()
                    break
            if found:
                break
        return found
