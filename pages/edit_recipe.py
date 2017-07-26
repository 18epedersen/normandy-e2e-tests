from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
from pages.view_recipe import configure_action


class EditRecipe(Base):
    """View Recipe."""

    LOCATORS = locators.EditRecipe

    def get_current_action(self):
        """Get current recipe action."""
        action_name = self.find_element(*self.LOCATORS.action_name)
        current_recipe_action = action_name.text
        return current_recipe_action

    def pick_new_random_action(self, current_recipe_action):
        """Return a random recipe action."""
        from random import choice
        actions = ['console-log', 'show-heartbeat', 'preference-experiment']
        new_recipe_action = None
        while new_recipe_action == current_recipe_action:
            new_recipe_action = choice(actions)
        print("action is ", new_recipe_action)
        return new_recipe_action

    def edit_recipe(self, conf):
        """Save recipe with a unique UUID."""
        """Return a recipe page, recipe name, and notification's texts."""
        from pages.view_recipe import ViewRecipe
        current_recipe_action = self.get_current_action()
        new_recipe_action = self.pick_new_random_action(current_recipe_action)
        configure_action(conf, new_recipe_action)
        save_button = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.save_button))
        save_button.click()
        return ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load()
