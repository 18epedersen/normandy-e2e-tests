"""By method."""
from selenium.webdriver.common.by import By


class Base:
    """Locators for Base."""

    error = ()
    heading = (By.TAG_NAME, "h1")
    heading_two = (By.TAG_NAME, "h2")


class LDAPLogin(Base):
    """Locators for LDAPLogin."""

    password = (By.NAME, 'password')
    submit = (By.CSS_SELECTOR, ".auth0-lock-submit")
    username = (By.CLASS_NAME, 'auth0-lock-input-username')


class DuoLogin(Base):
    """Locators for DuoLogin."""

    a0notloggedin = (By.CLASS_NAME, 'a0-notloggedin')
    dropdown = (By.CSS_SELECTOR,
                '.device-select-wrapper > select:nth-child(1)')
    duoiframe = (By.ID, 'duo_iframe')
    loginbutton = (By.CSS_SELECTOR, 'button.positive:nth-child(5)')
    passcodebutton = (By.CSS_SELECTOR, 'button.positive:nth-child(5)')
    QRinput = (By.CSS_SELECTOR,
               'div.passcode-label:nth-child(1) > input:nth-child(4)')
    value = 'token'


class Home(Base):
    """Locators for Home."""

    addbutton = (By.CSS_SELECTOR, '.button')
    notif = (By.CLASS_NAME, 'notifications')
    recipetable = (By.CLASS_NAME, 'recipe-list')
    tbody = (By.TAG_NAME, 'tbody')
    successalert = (By.CLASS_NAME, 'message')
    td = (By.TAG_NAME, 'td')
    tr = (By.TAG_NAME, 'tr')


class Recipe(Base):
    """Locators for Recipe."""

    action = (By.NAME, 'action')
    actionmessage = (By.NAME, 'arguments.message')
    approvebutton = (By.CSS_SELECTOR, '.action-approve')
    approvemessagetextbox = (By.CSS_SELECTOR,
                             '.approve-dropdown > textarea:nth-child(1)')
    approvemessagebutton = (By.CSS_SELECTOR, '.mini-button')
    confirmbutton = (By.CSS_SELECTOR, ".submit")
    confirmdelete = (By.CLASS_NAME, 'delete')
    deletebutton = (By.CLASS_NAME, 'action-delete')
    disablebutton = (By.CLASS_NAME, 'action-disable')
    enablebutton = (By.CSS_SELECTOR, ".action-enable")

    filtertextbox = (By.NAME, 'extra_filter_expression')
    learnmore = (By.NAME, 'arguments.learnMoreMessage')
    learnmoreurl = (By.NAME, 'arguments.learnMoreUrl')
    name = (By.NAME, 'name')
    postanswerurl = (By.NAME, 'arguments.postAnswerUrl')
    recipesbreadcrumb = (By.CSS_SELECTOR,
                         '.breadcrumbs > span:nth-child(1) > a:nth-child(1)')
    requestbutton = (By.CLASS_NAME, 'action-request')
    save = (By.CLASS_NAME, 'action-new')
    savedraft = (By.CLASS_NAME, 'action-save')
    statustext = (By.CLASS_NAME, "status-text")
    successalert = (By.CLASS_NAME, 'message success')
    surveyid = (By.NAME, 'arguments.surveyId')
    thanksmessage = (By.NAME, 'arguments.thanksMessage')
