"""Expected conditions."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base import Base
from pages.home import Home
from tests.conftest import generate_QR_code
from pages import locators
import time


class DuoLogin(Base):
    """Duo authenication class."""

    LOCATORS = locators.DuoLogin

    def wait_for_page_to_load(self):
        """Wait for page load method for a0-notloggedin class to load."""
        self.wait.until(EC.visibility_of_element_located(
          self.LOCATORS.a0notloggedin))
        return self

    def login_duo(self, secret):
        """Log into duo."""
        QR_code = generate_QR_code(secret)
        self.selenium.switch_to_frame(
         self.find_element(*self.LOCATORS.duoiframe))
        time.sleep(10)
        select = Select(self.find_element(*self.LOCATORS.dropdown))
        select.select_by_value(self.LOCATORS.value)
        self.find_element(*self.LOCATORS.passcodebutton).click()
        # QR_code = generate_QR_code(secret)
        self.find_element(*self.LOCATORS.QRinput).send_keys(QR_code)
        self.find_element(*self.LOCATORS.loginbutton).click()
        self.selenium.switch_to_default_content()
        return Home(self.selenium, self.base_url).wait_for_page_to_load()
