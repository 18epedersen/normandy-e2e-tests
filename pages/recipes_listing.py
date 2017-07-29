"""Expected conditions method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
from pages.new_recipe import NewRecipe


# LOCATORS = locators.RecipesListing


class RecipesListing(Base):
    """Home Class for Normandy Control UI."""

    LOCATORS = locators.RecipesListing

    def wait_for_page_to_load(self):
        """Wait for visibility of rows on Normandy's home page to load."""
        self.wait.until(EC.visibility_of_all_elements_located(
            self.LOCATORS.tr))
        return self

    def click_new_recipe(self):
        """Click add button to create recipe."""
        # from pages.recipe import Recipe
        self.find_element(*self.LOCATORS.new_recipe_button).click()
        return NewRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def select_top_recipe(self):
        """Click on a random recipe."""
        from pages.view_recipe import ViewRecipe
        view_recipe_page = None
        tbody = self.wait.until(EC.visibility_of_element_located(
          self.LOCATORS.tbody))
        rows = tbody.find_elements(*self.LOCATORS.tr)
        for row in rows:
            cols = row.find_elements(*self.LOCATORS.td)
            for col in cols:
                col.click()
                view_recipe_page = ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load() # noqa
                break
            break
        return view_recipe_page

    # def select_recipe(self, recipe_name):
    #     """Click on a random recipe."""
    #     from pages.view_recipe import ViewRecipe
    #     print("recipe name is ", recipe_name)
    #     view_recipe_page = None
    #     tbody = self.wait.until(EC.visibility_of_element_located(
    #       self.LOCATORS.tbody))
    #     rows = tbody.find_elements(*self.LOCATORS.tr)
    #     found = False
    #     for row in rows:
    #         cols = row.find_elements(*self.LOCATORS.td)
    #         for col in cols:
    #             print("col.text", col.text)
    #             if col.text == recipe_name:
    #                 found = True
    #                 col.click()
    #                 view_recipe_page = ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load() # noqa
    #                 break
    #         if found:
    #             break
    #     return view_recipe_page
