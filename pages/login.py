"""By method for selenium webdriver."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import BasePage
from pages.duo import DuoLoginPage
from pypom import Page


class LDAPLoginPage(BasePage):
    """Login class for demo LDAP account."""

    def __init__(self, conf, selenium, base_url):
        """Create ldap login page."""
        # URL_TEMPLATE = '/login'
        self.username_locator = conf.get('login', 'username_locator')
        self.password_locator = conf.get('login', 'password_locator')
        self.submit_locator = conf.get('login', 'submit_locator')
        self.base_url = base_url

    def wait_for_page_to_load(self):
        """Wait for page load method for submit."""
        self.wait.until(EC.visibility_of_element_located(self.submit_locator))
        return self

    def login(self, username, password):
        """Return Duo class after logging in with demo LDAP."""
        self.find_element(*self.username_locator).send_keys(username)
        self.find_element(*self.password_locator).send_keys(password)
        self.find_element(*self.submit_locator).click()
        return DuoLoginPage(self.selenium,
                            self.base_url).wait_for_page_to_load()
