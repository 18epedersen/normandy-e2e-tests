import pytest
import time
import uuid
import pyotp
from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope='session')
def base_url():
    """Grab the base url of the Normandy Control UI."""
    return 'https://normandy-admin.stage.mozaws.net/control/recipe/'


def generate_QR_code(secret):
    """Return the QR code for 2FA."""
    totp = pyotp.TOTP(secret)
    return totp.now()


class Base(Page):
    """Define a base class."""

    _error_locator = ""
    _heading_locator = (By.TAG_NAME, "h1")

    @property
    def error(self):
        """Error heading."""
        return self.find_element(*self._error_locator).text

    @property
    def heading(self):
        """Heading."""
        return self.find_element(*self._heading_locator).text


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
        # return Duo(self.selenium, self.base_url).wait_for_page_to_load()


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


class Home(Base):
    """Class for Normandy Control UI Home."""

    _addrecipe_locator = ".button"
    # locator for recipe table

    def wait_for_page_to_load(self):
        """Wait for page to load."""
        self.wait.until(EC.visibility_of_element_located(
           self._addrecipe_locator))
        return self

    def add_recipe(self):
        """Add a new recipe."""
        self.find_element(*self._addrecipe_locator).click()
        return Recipe(self.selenium, self.base_url).wait_for_page_to_load()


class Recipe(Base):
    """Normandy recipe page for creating a recipe."""

    _name_locator = 'label.form-field:nth-child(1) > input:nth-child(2)'
    _filters_locator = 'extra_filter_expression'
    _action_locator = 'action'
    _actionmessage_locator = 'arguments.message'
    _save_locator = 'action-new'

    def wait_for_page_to_load(self):
        """Wait for method."""
        self.wait.until(EC.visibility_of_element_located(
          self._name_locator))
        return self

    def create_recipe(self, filter_message, action, action_message):
        """Create a recipe with a unique UID."""
        recipe_id = uuid.uuid1()
        self.find_element(*self._name_locator).send_keys(recipe_id)
        self.find_element(*self._filters_locator).send_keys(filter_message)
        select = Select(self.find_element(*self._action_locator))
        select.select_by_value(action)
        self.find_element(*self._actionmessage_locator).send_keys(
         action_message)
        self.find_element(*self._save_locator).click()
        return Approval(self.selenium, self.base_url).wait_for_page_to_load()


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


@pytest.mark.nondestructive
def test_login(base_url, selenium, variables):
    """Test successful login into demo LDAP account."""
    page = Login(selenium, base_url).open()
    page.login(variables['username'], variables['password'])
    assert page.heading == "2-Step Verification"


@pytest.mark.nondestructive
def test_duo(base_url, selenium, variables):
    """Test successfully login Normandy."""
    """Pass auth0 by providing the correct QR code."""
    page = Login(selenium, base_url).open()
    duo = page.login(variables['username'], variables["password"])
    duo.switch_to_frame(
      duo.find_element(*duo._duoiframe_locator))
    home = duo.login_duo(variables['secret'])
    home.switch_to_default_content()
    # fix assert statement
    assert home.heading == "shield"


@pytest.mark.destructive
def test_creating_recipe(base_url, selenium, variables):
    """Test creating a recipe and successfully submitting it."""
    page = Login(selenium, base_url).open()
    duo = page.login(variables['username'], variables["password"])
    duo.switch_to_frame(
      duo.find_element(*duo._duoiframe_locator))
    home = duo.login_duo(variables['secret'])
    home.switch_to_default_content()
    recipe = home.add_recipe()
    approval = recipe.create_recipe(variables['additional filters'],
                                    variables['action'], variables['message'])
    # or check that we get a flash of successfully added recipe
    assert approval.heading == "recipes"


# test to successfully approval a recipe
@pytest.mark.destructive
def test_approving_recipe(base_url, selenium, variables):
    """Test the approval flow of a recipe."""
    page = Login(selenium, base_url).open()
    duo = page.login(variables['username'], variables["password"])
    duo.switch_to_frame(
      duo.find_element(*duo._duoiframe_locator))
    home = duo.login_duo(variables['secret'])
    home.switch_to_default_content()
    recipe = home.add_recipe()
    approval = recipe.create_recipe(variables['additional filters'],
                                    variables['action'], variables['message'])
    home = approval.approve_recipe(variables['approve'])
    # fix assert statement
    assert home.heading == "shield"

# test to successfully find a recipe in a table, use regions
