"""Expected conditions."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base import Base
from pages.home import Home
from tests.conftest import generate_QR_code
from pages import locators


class DuoLogin(Base):
    """Duo authenication class."""

    LOCATORS = locators.DuoLogin
    # def __init__(self, conf):
    #     """Create duo login page."""
    #     self.a0notloggedin_locator = conf.get('duo', 'a0notloggedin_locator')
    #     self.duoiframe_locator = conf.get('duo', 'duoiframe_locator')
    #     self.dropdown_locator = conf.get('duo', 'dropdown_locator')
    #     self.value = conf.get('duo', 'value')
    #     self.passcodebutton_locator = conf.get('duo', 'passcodebutton_locator')
    #     self.QRinput_locator = conf.get('duo', 'QRinput_locator')
    #     self.loginbutton_locator = conf.get('duo', 'loginbutton_locator')

    def wait_for_page_to_load(self):
        """Wait for page load method for a0-notloggedin class to load."""
        self.wait.until(EC.visibility_of_element_located(
          self.LOCATORS.a0notloggedin))
        return self

    def login_duo(self, secret):
        """Log into duo."""
        self.switch_to_frame(
         self.find_element(*self.LOCATORS.duoiframe))
        select = Select(self.find_element(*self.LOCATORS.dropdown))
        select.select_by_value(*self.LOCATORS.value)
        self.find_element(*self.LOCATORS.passcodebutton).click()
        QR_code = generate_QR_code(secret)
        self.find_element(*self.LOCATORS.QRinput).send_keys(QR_code)
        self.find_element(*self.LOCATORS.loginbutton).click()
        self.switch_to_default_content()
        return Home(self.selenium, self.base_url).wait_for_page_to_load()
