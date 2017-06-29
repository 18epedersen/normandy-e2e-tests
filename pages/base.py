from pypom import Page
from selenium.webdriver.common.by import By


class Base(Page):
    """Define a base class."""

    _error_locator = ""
    _heading_locator = (By.TAG_NAME, "h1")

    @property
    def error(self):
        """Error heading."""
        return self.find_element(*self._error_locator).text

    @property
    def heading(self):
        """Heading."""
        return self.find_element(*self._heading_locator).text
