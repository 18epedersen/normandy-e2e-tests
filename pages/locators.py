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

    # TODO: add a unique id for the recipes card on the home page
    recipe_card = (By.CLASS_NAME, 'ant-card-body')
    a_href = (By.CSS_SELECTOR, 'a')

    # TODO: add a unique id for the 'recipes' button on the recipes card
    recipes = (By.CSS_SELECTOR,
               'div.gw-col:nth-child(1) > div:nth-child(1) \
               > div:nth-child(2) > a:nth-child(3)')


class RecipesListing(Base):
    """Locators for Recipe Listings."""

    # TODO: add a unique id for the new recipe button
    new_recipe_button = (By.CSS_SELECTOR,
                         '.ant-col-8 > a:nth-child(1) > button:nth-child(1)')
    tr = (By.TAG_NAME, 'tr')
    td = (By.TAG_NAME, 'td')


class NewRecipe(Base):
    """Locators for Create New Recipe."""

    # general selectors for creating new recipe

    recipe_name_field = (By.ID, 'name')
    recipe_filter_expression = (By.ID, 'extra_filter_expression')

    # TODO: add a unique id for the recipe action dropdown
    select_action_dropdown = (By.CLASS_NAME, 'ant-select-selection--single')

    # TODO: add a unique id for the save button
    save_button = (By.CSS_SELECTOR, '.primary > button:nth-child(1)')

    # console log
    action_message = (By.ID, 'arguments.message')

    # TODO: add a unique id or value for the console-log action
    console_log = (By.CSS_SELECTOR,
                   'li.ant-select-dropdown-menu-item:nth-child(1)')

    # heart beat

    # TODO: add a unique id or value for the show_heartbeat action
    show_heartbeat = (By.CSS_SELECTOR,
                      'li.ant-select-dropdown-menu-item:nth-child(2)')
    survey_id = (By.ID, 'arguments.surveyId')
    thanks_message = (By.ID, 'arguments.thanksMessage')
    post_answer_url = (By.ID, 'arguments.postAnswerUrl')
    learn_more = (By.ID, 'arguments.learnMoreMessage')
    learn_more_url = (By.ID, 'arguments.learnMoreUrl')

    # preference experiment

    # TODO: add a unique id or value for the preference_experiment action
    preference_experiment = (By.CSS_SELECTOR,
                             'li.ant-select-dropdown-menu-item:nth-child(3)')
    experiment_name = (By.ID, 'arguments.slug')
    experiment_document_url = (By.ID, 'arguments.experimentDocumentUrl')
    preference_name = (By.ID, 'arguments.preferenceName')

    # TODO: add a unique id or value for the console-log action
    branch_name = (By.CSS_SELECTOR,
                   '.branch-fields > div:nth-child(1) > div:nth-child(2) > \
                   div:nth-child(1) > input:nth-child(1)')


class ViewRecipe(Base):
    """Locators for view recipe."""

    # TODO: add a unique id for the request approval button
    request_approval_button = (By.CSS_SELECTOR, 'button.ant-btn:nth-child(3)')

    # TODO: add a unique id or value for the edit button
    edit_button = (By.CSS_SELECTOR,
                   '.details-action-bar > a:nth-child(2) \
                   > button:nth-child(1)')

    # TODO: add a unique id or value for the clone button
    clone_button = (By.CSS_SELECTOR,
                    '.details-action-bar > a:nth-child(1) \
                     > button:nth-child(1)')

    alert_message = (By.CLASS_NAME, 'ant-alert-message')


class EditRecipe(Base):
    """Locators for editing a recipe."""

    # TODO: add a unique id the action name on the edit recipe page
    action_name = (By.CSS_SELECTOR,
                   'div.ant-card:nth-child(2) > div:nth-child(2) \
                   > dl:nth-child(1) > dd:nth-child(2)')
