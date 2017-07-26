"""Page object model."""
from pypom import Page
from pages import locators


class Base(Page):
    """Define a base class."""

    LOCATORS = locators.Base

    def __init__(self, selenium, base_url, **url_kwargs):
        """Override Page's init method to set a higher timeout."""
        super(Base, self).__init__(selenium, base_url, timeout=60,
                                   **url_kwargs)

    @property
    def heading(self):
        """H1 Heading."""
        return self.find_element(*self.LOCATORS.heading).text

    @property
    def heading_two(self):
        """H2 heading."""
        return self.find_element(*self.LOCATORS.heading_two).text

    @property
    def alert_message(self):
        """H1 Heading."""
        return self.find_element(*self.LOCATORS.alert_message).text
