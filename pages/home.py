"""By method for selenium webdriver."""
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
from pypom import Region
import time
from tests.conftest import find_approved_recipe


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

    def verify_recipe(self, conf, recipe_id,):
        """Verify Recipe."""
        print("recipe_id", recipe_id)
        # data = self.find_element(*self.LOCATORS.reactabledata)
        recipe_list = self.find_elements(self.LOCATORS.value)
        found_recipe = False
        for recipe in recipe_list:
            print(recipe.text)
            if recipe.text == recipe_id:
                found_recipe = True
        values = find_approved_recipe(recipe_id)
        return found_recipe, values

        # table = self.find_element(*self.LOCATORS.recipetable)
        # print("table ", table)
        # for row in table:
        #     print(table.find_element(*self.LOCATORS.row).txt)
        # print("data ", data)
        # for tr in data:
        #     tr = data.find_element(*self.LOCATORS.row)
        #     print("tr", tr)
        #     for td in tr:
        #         print("td ", td)
        #         print(self.find_element(*self.LOCATORS.value).text)
        # for row in table:
        #     print(table.find_element(*self.LOCATORS.row).text)
        # print(table.find_element(*self.LOCATORS.row).text)
        # time.sleep(500)

    def select_recipe(self, recipe_id):
        """Select a recipe to edit from home."""
        from pages.recipe import Recipe
        recipe_list = self.find_elements(self.LOCATORS.value)
        for recipe in recipe_list:
            print(recipe.text)
            if recipe.text == recipe_id:
                self.find_element(recipe_list.click)
                return Recipe(self.selenium, self.base_url).wait_for_page_to_load()
        return None


    # class Recipe(Region):
    #     """Region for a recipe on the home page."""
    #
    #     LOCATORS_RECIPE = locators.Home
