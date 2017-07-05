from selenium.webdriver.support import expected_conditions as EC
from pages.base import Base
from pages.duo import DuoLogin
from pages import locators


class LDAPLogin(Base):
    """Login class for demo LDAP account."""

    URL_TEMPLATE = "/login"
    LOCATORS = locators.LDAPLogin

    # def __init__(self, conf, base_url, selenium):
    #     """Create ldap login page."""
    #     super(LDAPLogin, self).__init__(conf, selenium, base_url)
    #     # self.username_locator = conf.get('login', 'username_locator')
    #     self.locators = locators.LDAPLogin
    # self.username_locator = locators.LDAPLogin.username
    # self.password_locator = conf.get('login', 'password_locator')
    # self.submit_locator = conf.get('login', 'submit_locator')
    # self.base_url = base_url
    # self.base_url = conf.get('stage', 'base_url')

    def wait_for_page_to_load(self):
        """Wait for page load method for submit."""
        # self.wait.until(EC.visibility_of_element_located(self.submit_locator))
        self.wait.until(EC.visibility_of_element_located(self.LOCATORS.submit))
        return self

    def login(self, username, password):
        """Return Duo class after logging in with demo LDAP."""
        self.find_element(*self.LOCATORS.username).send_keys(username)
        self.find_element(*self.LOCATORS.password).send_keys(password)
        self.find_element(*self.LOCATORS.submit).click()
        return DuoLogin(self.selenium,
                        self.base_url).wait_for_page_to_load()
