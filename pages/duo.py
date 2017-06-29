from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base import Base
from pages.home import Home
import pyotp


def generate_QR_code(secret):
    """Return the QR code for 2FA."""
    totp = pyotp.TOTP(secret)
    return totp.now()


class Duo(Base):
    """Duo authenication class."""

    _a0notloggedin_locator = 'a0-notloggedin'
    _duoiframe_locator = 'duo_iframe'
    _dropdown_locator = '.device-select-wrapper > select:nth-child(1)'
    _token_locator = 'token'
    _passcode_locator = 'button.positive:nth-child(5)'
    _QRinput_locator = 'div.passcode-label:nth-child(1) > input:nth-child(4)'
    _login_locator = 'button.positive:nth-child(5)'

    def wait_for_page_to_load(self):
        """Wait for page load method for a0-notloggedin class to load."""
        self.wait.until(EC.visibility_of_element_located(
          self._a0notloggedin_locator))
        return self

    def login_duo(self, secret):
        """Login into duo."""
        select = Select(self.find_element(*self._dropdown_locator))
        select.select_by_value(*self._token_locator)
        self.find_element(*self._passcode_locator).click()
        QR_code = generate_QR_code(secret)
        self.find_element(*self._QRinput_locator).send_keys(QR_code)
        self.find_element(*self._login_locator).click()
        return Home(self.selenium, self.base_url).wait_for_page_to_load()
