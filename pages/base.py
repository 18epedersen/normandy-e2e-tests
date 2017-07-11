"""Page object model."""
from pypom import Page
from pages import locators


class Base(Page):
    """Define a base class."""

    LOCATORS = locators.Base

    @property
    def heading(self):
        """H1 Heading."""
        return self.find_element(*self.LOCATORS.heading).text

    @property
    def heading_two(self):
        """H2 heading."""
        return self.find_element(*self.LOCATORS.heading_two).text

    @property
    def error(self):
        """Error heading."""
        return self.find_element(*self.LOCATORS.error).text
