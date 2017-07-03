from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages.duo import DuoLogin
from selenium.webdriver.common.by import By


class LDAPLogin(Base):
    """Login class for demo LDAP account."""

    def __init__(self, conf, base_url, selenium):
        """Create ldap login page."""
        # URL_TEMPLATE = '/login'
        self.username_locator = conf.get('login', 'username_locator')
        self.password_locator = conf.get('login', 'password_locator')
        self.submit_locator = conf.get('login', 'submit_locator')
        # self.base_url = base_url
        self.base_url = conf.get('stage', 'base_url')

    def wait_for_page_to_load(self):
        """Wait for page load method for submit."""
        self.wait.until(EC.visibility_of_element_located(self.submit_locator))
        return self

    def login(self, username, password):
        """Return Duo class after logging in with demo LDAP."""
        self.find_element(*self.username_locator).send_keys(username)
        self.find_element(*self.password_locator).send_keys(password)
        self.find_element(*self.submit_locator).click()
        return DuoLogin(self.selenium,
                            self.base_url).wait_for_page_to_load()
