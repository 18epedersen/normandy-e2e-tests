"""By method."""
from selenium.webdriver.common.by import By


class Base:
    """Locators for Base."""

    heading = (By.TAG_NAME, "h1")
    heading_two = (By.TAG_NAME, "h2")
    alert_message = (By.CLASS_NAME, 'ant-alert-message')


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
                'div.passcode-label:nth-child(1) > input:nth-child(4)')
    value = 'token'


class Home(Base):
    """Locators for Home."""

    logo = (By.CLASS_NAME, 'logo')

    # fix me
    recipe_card = (By.CLASS_NAME, 'ant-card-body')
    a_href = (By.CSS_SELECTOR, 'a')

    # fix me
    recipes = (By.CSS_SELECTOR,
               'div.gw-col:nth-child(1) > div:nth-child(1) \
               > div:nth-child(2) > a:nth-child(3)')


class RecipesListing(Base):
    """Locators for Recipe Listings."""

    # fix me
    new_recipe_button = (By.CSS_SELECTOR,
                         '.ant-col-8 > a:nth-child(1) > button:nth-child(1)')
    tr = (By.TAG_NAME, 'tr')
    td = (By.TAG_NAME, 'td')


class NewRecipe(Base):
    """Locators for Create New Recipe."""

    # general selectors for creating new recipe
    # fix me
    primary = (By.CLASS_NAME, 'primary')
    recipe_name_field = (By.ID, 'name')
    recipe_filter_expression = (By.ID, 'extra_filter_expression')

    # fix me
    select_action_dropdown = (By.CLASS_NAME, 'ant-select-selection--single')

    # fix me
    save_button = (By.CSS_SELECTOR, '.primary > button:nth-child(1)')

    # console log
    action_message = (By.ID, 'arguments.message')

    # fix me
    console_log = (By.CSS_SELECTOR,
                   'li.ant-select-dropdown-menu-item:nth-child(1)')

    # heart beat
    # fix me
    show_heartbeat = (By.CSS_SELECTOR,
                      'li.ant-select-dropdown-menu-item:nth-child(2)')
    survey_id = (By.ID, 'arguments.surveyId')
    thanks_message = (By.ID, 'arguments.thanksMessage')
    post_answer_url = (By.ID, 'arguments.postAnswerUrl')
    learn_more = (By.ID, 'arguments.learnMoreMessage')
    learn_more_url = (By.ID, 'arguments.learnMoreUrl')

    # preference experiment

    # fix me
    preference_experiment = (By.CSS_SELECTOR,
                             'li.ant-select-dropdown-menu-item:nth-child(3)')
    experiment_name = (By.ID, 'arguments.slug')
    experiment_document_url = (By.ID, 'arguments.experimentDocumentUrl')
    preference_name = (By.ID, 'arguments.preferenceName')

    # fix me
    branch_name = (By.CSS_SELECTOR,
                   '.branch-fields > div:nth-child(1) > div:nth-child(2) > \
                   div:nth-child(1) > input:nth-child(1)')


class ViewRecipe(Base):
    """Locators for view recipe."""

    # fix me
    request_approval_button = (By.CSS_SELECTOR, 'button.ant-btn:nth-child(3)')

    # fix me
    edit_button = (By.CSS_SELECTOR,
                   '.details-action-bar > a:nth-child(2) \
                   > button:nth-child(1)')

    # fix me
    clone_button = (By.CSS_SELECTOR,
                    '.details-action-bar > a:nth-child(1) \
                     > button:nth-child(1)')

    alert_message = (By.CLASS_NAME, 'ant-alert-message')


class EditRecipe(Base):
    """Locators for editing a recipe."""

    # fix me
    action_name = (By.CSS_SELECTOR,
                   'div.ant-card:nth-child(2) > div:nth-child(2) \
                   > dl:nth-child(1) > dd:nth-child(2)')
