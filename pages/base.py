"""Page object model."""
from pypom import Page
from pages import locators
from selenium.webdriver.support import expected_conditions as EC


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
    def get_notification_texts(self):
        """Return list of notification texts."""
        notif = self.wait.until(EC.visibility_of_element_located(
          self.LOCATORS.notif))
        messages = notif.find_elements(*self.LOCATORS.message_alert)
        notifications_text_list = []
        for message in messages:
            notifications_text_list.append(message.text)
        return notifications_text_list
