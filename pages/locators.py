from selenium.webdriver.common.by import By


class Base:
    """Locators for Base."""

    heading = (By.TAG_NAME, "h1")
    error = ()


class LDAPLogin:
    """Locators for LDAPLogin."""

    username = (By.CLASS_NAME, 'auth0-lock-input-username')
    password = (By.NAME, 'password')
    submit = (By.CSS_SELECTOR, ".auth0-lock-submit")


class DuoLogin:
    """Locators for DuoLogin."""

    a0notloggedin = (By.CLASS_NAME, 'a0-notloggedin')
    duoiframe = (By.ID, 'duo_iframe')
    dropdown = (By.CSS_SELECTOR, '.device-select-wrapper > select:nth-child(1)')
    value = 'token'
    passcodebutton = (By.CSS_SELECTOR, 'button.positive:nth-child(5)')
    QRinput = (By.CSS_SELECTOR, 'div.passcode-label:nth-child(1) > input:nth-child(4)')
    loginbutton = (By.CSS_SELECTOR, 'button.positive:nth-child(5)')


class Home:
    """Locators for Home."""

    addbutton = (By.CSS_SELECTOR, ".button")


class Recipe:
    """Locators for Recipe."""

    name = (By.CSS_SELECTOR, 'label.form-field:nth-child(1) > input:nth-child(2)')
    filtertextbox = (By.NAME, 'extra_filter_expression')
    action = (By.NAME, 'action')
    actionmessage = (By.NAME, 'arguments.message')
    saverecipe = (By.CLASS_NAME, 'action-new')
    requestbutton = (By.CSS_SELECTOR, 'button.button:nth-child(3)')
    approvebutton = (By.CSS_SELECTOR, '.action-approve')
    approvemessagetextbox = (By.CSS_SELECTOR, ".approve-dropdown > textarea:nth-child(1)")
    approvemessagebutton = (By.CSS_SELECTOR, '.mini-button')
    enablebutton = (By.CSS_SELECTOR, ".action-enable")
    confirmbutton = (By.CSS_SELECTOR, ".submit")
    recipesbreadcrumb = (By.CSS_SELECTOR, '.breadcrumbs > span:nth-child(1) > a:nth-child(1)')