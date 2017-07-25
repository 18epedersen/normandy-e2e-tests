"""By method."""
from selenium.webdriver.common.by import By


class Base:
    """Locators for Base."""

    heading = (By.TAG_NAME, "h1")
    heading_two = (By.TAG_NAME, "h2")
    notif = (By.CLASS_NAME, 'notifications')
    message_alert = (By.CLASS_NAME, 'message')


# class Login(Base):
#     """Locators for Login."""
#
#     login_button = (By.CLASS_NAME, 'button')
#     password = (By.NAME, 'password')
#     username = (By.NAME, 'username')

class LDAPLogin(Base):
    """Locators for LDAPLogin."""

    password = (By.NAME, 'password')
    submit = (By.CSS_SELECTOR, ".auth0-lock-submit")
    username = (By.CLASS_NAME, 'auth0-lock-input-username')


class DuoLogin(Base):
    """Locators for DuoLogin."""

    a0_not_logged_in = (By.CLASS_NAME, 'a0-notloggedin')
    dropdown = (By.CSS_SELECTOR,
                '.device-select-wrapper > select:nth-child(1)')
    duo_iframe = (By.ID, 'duo_iframe')
    login_button = (By.CSS_SELECTOR, 'button.positive:nth-child(5)')
    passcode_button = (By.CSS_SELECTOR, 'button.positive:nth-child(5)')
    QR_input = (By.CSS_SELECTOR,
               'div.passcode-label:nth-child(1) > input:nth-child(4)') # noqa
    value = 'token'


class Home(Base):
    """Locators for Home."""

    logo = (By.CLASS_NAME, 'logo')
    recipe_card = (By.CLASS_NAME, 'ant-card-body')
    a_href = (By.CSS_SELECTOR, 'a')
    recipes = (By.CSS_SELECTOR,
               'div.gw-col:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3)') # noqa


class RecipesListing(Base):
    """Locators for Recipe Listings."""

    new_recipe_button = (By.CSS_SELECTOR,
                         '.ant-col-8 > a:nth-child(1) > button:nth-child(1)')


class NewRecipe(Base):
    """Locators for Create New Recipe."""

    primary = (By.CLASS_NAME, 'primary')
    name = (By.ID, 'name')
    extra_filter_expression = (By.ID, 'extra_filter_expression')
    select_action_dropdown = (By.CLASS_NAME, 'ant-select-selection--single')
    action_message = (By.ID, 'arguments.message')
    save_button = (By.CSS_SELECTOR, '.primary > button:nth-child(1)')
    console_log = (By.CSS_SELECTOR, 'li.ant-select-dropdown-menu-item:nth-child(1)')
    show_heartbeat = (By.CSS_SELECTOR, 'li.ant-select-dropdown-menu-item:nth-child(2)')
    survey_id = (By.ID, 'arguments.surveyId')
    thanks_message = (By.ID, 'arguments.thanksMessage')
    post_answer_url = (By.ID, 'arguments.postAnswerUrl')
    learn_more = (By.ID, 'arguments.learnMoreMessage')
    learn_more_url = (By.ID, 'arguments.learnMoreUrl')




class Recipe(Base):
    """Locators for Recipe."""

    action = (By.NAME, 'action')
    action_message = (By.NAME, 'arguments.message')
    approve_button = (By.CSS_SELECTOR, '.action-approve')
    approve_message_button = (By.CSS_SELECTOR, '.mini-button')
    approve_message_textbox = (By.CSS_SELECTOR,
                             '.approve-dropdown > textarea:nth-child(1)') # noqa
    confirm_button = (By.CSS_SELECTOR, ".submit")
    confirm_delete = (By.CLASS_NAME, 'delete')
    delete_button = (By.CLASS_NAME, 'action-delete')
    disable_button = (By.CLASS_NAME, 'action-disable')
    enable_button = (By.CSS_SELECTOR, ".action-enable")
    experiment_doc_url = (By.NAME, 'arguments.experimentDocumentUrl')
    filter_textbox = (By.NAME, 'extra_filter_expression')
    learn_more = (By.NAME, 'arguments.learnMoreMessage')
    learn_more_url = (By.NAME, 'arguments.learnMoreUrl')
    name = (By.NAME, 'name')
    post_answer_url = (By.NAME, 'arguments.postAnswerUrl')
    preference_branch = (By.NAME, 'arguments.preferenceBranchType')
    preference_name = (By.NAME, 'arguments.preferenceName')
    preference_type = (By.NAME, 'arguments.preferenceType')
    recipes_breadcrumb = (By.CSS_SELECTOR,
                         '.breadcrumbs > span:nth-child(1) > a:nth-child(1)') # noqa
    request_button = (By.CLASS_NAME, 'action-request')
    save = (By.CLASS_NAME, 'action-new')
    save_draft = (By.CLASS_NAME, 'action-save')
    slug = (By.NAME, 'arguments.slug')
    status_text = (By.CLASS_NAME, "status-text")
    survey_id = (By.NAME, 'arguments.surveyId')
    thanks_message = (By.NAME, 'arguments.thanksMessage')
