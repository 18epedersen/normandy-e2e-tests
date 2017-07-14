"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators


class Home(Base):
    """Home Class for Normandy Control UI."""

    LOCATORS = locators.Home

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        # self.wait.until(EC.visibility_of_element_located(
        #    self.LOCATORS.recipetable))
        self.wait.until(EC.visibility_of_all_elements_located(
         self.LOCATORS.tr))
        return self

    def add_recipe(self):
        """Click add button to create recipe."""
        from pages.recipe import Recipe
        print("entered add recipe")
        self.find_element(*self.LOCATORS.addbutton).click()
        return Recipe(self.selenium, self.base_url).wait_for_page_to_load()

    def create_approved_recipe(self, conf, recipe_enabled):
        """Create an approved recipe."""
        recipe_page = self.add_recipe()
        recipe_page, recipe_name = recipe_page.save_recipe(conf)
        home_page, approved_text = recipe_page.approve_recipe(conf,
                                                              recipe_enabled)
        return home_page, approved_text, recipe_name

    def find_recipe_in_table(self, recipe_name):
        """Find Recipe in home page recipe table."""
        from pages.recipe import Recipe
        recipe_page = None
        rows = self.wait.until(EC.visibility_of_all_elements_located(
         self.LOCATORS.tr))
        found = False
        for row in rows:
            cols = self.wait.until(EC.visibility_of_all_elements_located(
             self.LOCATORS.td))
            for col in cols:
                if col.text == recipe_name:
                    found = True
                    col.click()
                    recipe_page = Recipe(self.selenium, self.base_url,
                                         20).wait_for_save_draft_button()
                    break
            if found:
                break
        return found, recipe_page

    def get_notification_text(self):
        """Return text that recipe was successfully deleted."""
        # notif = self.find_element(*self.LOCATORS.notif)
        notif = self.wait.until(EC.visibility_of_element_located(
          self.LOCATORS.notif))
        success = notif.find_element(*self.LOCATORS.successalert)
        return success.text
