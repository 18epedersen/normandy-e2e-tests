from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
import time


class ApprovalHistory(Base):
    """Home Class for Normandy Control UI."""

    LOCATORS = locators.ApprovalHistory

    @property
    def get_tag(self):
        """Getter for tag."""
        tag_text = self.find_element(*self.LOCATORS.tag).text
        return tag_text

    # need to fix what the approval history page is waiting for when load
    def wait_for_page_to_load(self):
        """Wait for visibility of rows on Normandy's home page to load."""
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.approve))
        return self

    def click_approve(self):
        """Click recipes to go to recipes listing page."""
        approve_button = self.find_element(*self.LOCATORS.approve)
        approve_button.click()
        return self

    def approve_recipe(self, conf):
        """Approve a recipe."""
        comment = conf.get('approve', 'comment')
        self.find_element(*self.LOCATORS.comment).clear()
        self.find_element(*self.LOCATORS.comment).send_keys(comment)
        self.click_approve()
        return ApprovalHistory(self.selenium,
                               self.base_url).wait_for_page_to_load()

    def click_view_recipe_breadcrumb(self):
        """Click on the view recipe breadcrumb."""
        time.sleep(5)
        from pages.view_recipe import ViewRecipe
        self.find_element(*self.LOCATORS.view_recipe_breadcrumb).click()
        return ViewRecipe(self.selenium, self.base_url).wait_for_page_to_load()
