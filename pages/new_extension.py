from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages import locators
import time
import uuid


class NewExtension(Base):
    """Recipe class."""

    LOCATORS = locators.NewRecipe

    def wait_for_page_to_load(self):
        """Wait for recipe page's submit button."""
        self.wait.until(EC.visibility_of_element_located(
         self.LOCATORS.save_button))
        return self

    def upload_extension(self):
        """Upload an extension."""
        extension_name = str(uuid.uuid1().hex)
        extension_name_field = self.wait.until(EC.element_to_be_clickable(
          self.LOCATORS.recipe_name_field))
        extension_name_field.clear()
        extension_name_field.send_keys(extension_name)
        path = '/Users/epedersen/git/Normandy_Test/test.xpi'
        upload_xpi_button = self.find_element(*self.LOCATORS.upload_xpi_button)
        upload_xpi_button.send_keys(path)
