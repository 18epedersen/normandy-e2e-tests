"""Page object model."""
from pypom import Page
from pages import locators


class Base(Page):
    """Define a base class."""

    LOCATORS = locators.Base

    # def __init__(self, conf, selenium, base_url):
    #     """Create basepage class."""
    #     super(Base, self).__init__(selenium, base_url)
    #     self.heading_locator = conf.get('base', 'heading_locator')
    #     self.error_locator = conf.get('base', 'error_locator')

    @property
    def heading(self):
        """H1 Heading."""
        return self.find_element(*self.LOCATORS.heading).text

    @property
    def heading_two(self):
        """H2 heading."""
        return self.find_elemenet(*self.LOCATORS.heading_two).text

    @property
    def error(self):
        """Error heading."""
        return self.find_element(*self.LOCATORS.error).text
