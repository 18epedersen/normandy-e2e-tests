"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
import time


class Home(Base):
    """Home Class for Normandy Control UI."""

    LOCATORS = locators.Home

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        self.wait.until(EC.visibility_of_element_located(
           self.LOCATORS.recipetable))
        return self

    def add_recipe(self):
        """Click add button to create recipe."""
        from pages.recipe import Recipe
        print("entered add recipe")
        self.find_element(*self.LOCATORS.addbutton).click()
        return Recipe(self.selenium, self.base_url).wait_for_page_to_load()

    def find_recipe_in_table(self, conf):
        """Find Recipe in home page recipe table."""
        from pages.recipe import Recipe
        with open('.recipe_name') as f:
            recipe_name = f.read()
        recipe_page = None
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
                    recipe_page = Recipe(self.selenium, self.base_url,
                                         20).wait_for_save_draft_button()
                    break
            if found:
                break
        print("found ", found)
        print("recipe page ", recipe_page)
        return found, recipe_page

    def confirm_deleted_recipe(self):
        """Return text that recipe was successfully deleted."""
        notif = self.find_element(*self.LOCATORS.notif)
        success = notif.find_element(*self.LOCATORS.successalert)
        return success.text
