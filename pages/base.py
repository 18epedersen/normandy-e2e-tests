"""Page object model."""
from pypom import Page


class BasePage(Page):
    """Define a base class."""

    def __init__(self, conf):
        """Create basepage class."""
        self.heading_locator = conf.get('base', 'heading_locator')
        self.error_locator = conf.get('base', 'error_locator')

    @property
    def heading(self):
        """Heading."""
        return self.find_element(*self.heading_locator).text

    @property
    def error(self):
        """Error heading."""
        return self.find_element(*self.error_locator).text
