from pages.base import Base
from pages import locators
from pages.edit_recipe import EditRecipe


class ViewRecipe(Base):
    """View Recipe."""

    LOCATORS = locators.ViewRecipe

    def click_request_approval(self):
        """Click add button to create recipe."""
        self.find_element(*self.LOCATORS.request_approval_button).click()
        return ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def click_edit(self):
        """Click add button to create recipe."""
        self.find_element(*self.LOCATORS.edit_button).click()
        return EditRecipe(self.selenium, self.base_url).wait_for_page_to_load()

    def click_clone(self):
        """Click add button to create recipe."""
        self.find_element(*self.LOCATORS.clone_button).click()
        return EditRecipe(self.selenium, self.base_url).wait_for_page_to_load()
