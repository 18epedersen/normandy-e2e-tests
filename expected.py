"""No such element."""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class alert_not_present(object):
    """Expect an alert to not to be present."""

    def __call__(self, selenium):
        """Call method."""
        try:
            alert = selenium.find_element(By.CLASS_NAME, 'message success')
            print("entered helper alert not present text is ", alert.text)
            return False
        except NoSuchElementException:
            return True
