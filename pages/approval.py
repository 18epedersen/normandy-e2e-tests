import time
from pages.base import Base
from pages.home import Home
from selenium.webdriver.support import expected_conditions as EC


class Approval(Base):
    """Normandy page for approving a recipe."""

    _request_locator = 'button.button:nth-child(3)'
    _approve_locator = '.action-approve'
    _approvemessage_locator = ".approve-dropdown > textarea:nth-child(1)"
    _approvemessagebutton_locator = '.mini-button'
    _enable_locator = ".action-enable"
    _confirm_locator = ".submit"
    _recipesbreadcrumb_locator = '.breadcrumbs > \
    span:nth-child(1) > a:nth-child(1)'

    def wait_for_page_to_load(self):
        """Wait method."""
        self.wait.until(EC.visibility_of_element_located(
          self._request_locator))
        return self

    def approve_recipe(self, approve_message):
        """Approve a recipe."""
        self.find_element(*self._request_locator).click()
        self.find_element(*self._approve_locator).click()
        self.find_element(*self._approvemessage_locator).send_keys(
           approve_message)
        self.find_element(*self._approvemessagebutton_locator).click()
        self.find_element(*self._enable_locator).click()
        self.find_element(*self._confirm_locator).click()
        time.sleep(10)
        self.find_element(*self._recipesbreadcrumb_locator).click()
        return Home(self.selenium, self.base_url).wait_for_page_to_load()
