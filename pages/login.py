from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages.duo import Duo


class Login(Base):
    """Login class for demo LDAP account."""

    URL_TEMPLATE = '/login'
    _username_locator = (By.CLASS_NAME, 'auth0-lock-input-username')
    _password_locator = (By.NAME, 'password')
    _submit_locator = (By.CSS_SELECTOR, ".auth0-lock-submit")

    def wait_for_page_to_load(self):
        """Wait for page load method for submit."""
        self.wait.until(EC.visibility_of_element_located(self._submit_locator))
        return self

    def login(self, username, password):
        """Return Duo class after logging in with demo LDAP."""
        self.find_element(*self._username_locator).send_keys(username)
        self.find_element(*self._password_locator).send_keys(password)
        self.find_element(*self._submit_locator).click()
        return Duo(self.selenium, self.base_url).wait_for_page_to_load()
