"""Expected conditions method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
from pages.new_recipe import NewRecipe


class RecipesListing(Base):
    """Home Class for Normandy Control UI."""

    LOCATORS = locators.RecipesListing

    def wait_for_page_to_load(self):
        """Wait for visibility of rows on Normandy's home page to load."""
        self.wait.until(EC.visibility_of_all_elements_located(
         self.LOCATORS.new_recipe_button))
        return self

    def click_new_recipe(self):
        """Click add button to create recipe."""
        # from pages.recipe import Recipe
        self.find_element(*self.LOCATORS.new_recipe_button).click()
        return NewRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def select_most_recent_recipe(self):
        """Click on a random recipe."""
        from pages.view_recipe import ViewRecipe
        recipe_page = None
        row_content = []
        rows = self.wait.until(EC.visibility_of_all_elements_located(
         self.LOCATORS.tr))
        found = False
        for row in rows:
            cols = row.find_elements(*self.LOCATORS.td)
            for col in cols:
                row_content = self.get_row_content(row)
                col.click()
                view_recipe_page = ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load() # noqa
                break
    return recipe_page, row_content
