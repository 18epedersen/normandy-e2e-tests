from selenium.webdriver.common.by import By


class Base:
    """Locators for Base."""

    heading = (By.TAG_NAME, "h1")
    heading_two = (By.TAG_NAME, "h2")
    alert_message = (By.CLASS_NAME, 'ant-alert-message')

    # TODO: make unique id
    home_breadcrumb = (By.CSS_SELECTOR,
                       '.ant-breadcrumb > span:nth-child(1) > span:nth-child(1) \
                       > a:nth-child(1)')


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

    recipe_card = (By.ID, 'gw-recipes-card')
    a_href = (By.CSS_SELECTOR, 'a')
    recipes = (By.ID, 'gw-recipes-link')


class RecipesListing(Base):
    """Locators for Recipe Listings."""

    new_recipe_button = (By.ID, 'lab-recipe-button')
    tr = (By.TAG_NAME, 'tr')
    td = (By.TAG_NAME, 'td')
    tbody = (By.CLASS_NAME, 'ant-table-tbody')


class NewRecipe(Base):
    """Locators for Create New Recipe."""

    # general selectors for creating new recipe

    recipe_name_field = (By.ID, 'name')
    recipe_filter_expression = (By.ID, 'extra_filter_expression')

    action_dropdown = (By.ID, 'rf-action-select')

    save_button = (By.ID, 'rf-save-button')

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
    experiment_doc_url = (By.ID, 'arguments.experimentDocumentUrl')
    preference_name = (By.ID, 'arguments.preferenceName')

    # TODO: add a unique branch button id
    add_branch_button = (By.CSS_SELECTOR, 'button.ant-btn:nth-child(2)')

    # TODO: add unique id for true value
    true_preference = (By.CSS_SELECTOR,
                       'label.ant-radio-button-wrapper:nth-child(1)')

    # TODO: add unique id for false value
    false_preference = (By.CSS_SELECTOR,
                        'label.ant-radio-button-wrapper:nth-child(2)')

    branch_name = (By.ID, 'pef-branch-name')

    # TODO: add unique id for opt-out-study, and currently opt-out-study feature is broken.
    # opt-out-study
    opt_out_study = (By.CSS_SELECTOR, 'li.ant-select-dropdown-menu-item:nth-child(4)')


class ViewRecipe(Base):
    """Locators for view recipe."""

    request_approval_button = (By.ID, 'dab-request-approval')
    edit_button = (By.ID, 'dab-edit-button')
    clone_button = (By.ID, 'dab-clone-button')
    content = (By.CLASS_NAME, 'ant-layout-content')
    approval_request_button = (By.ID, 'dab-approval-status')


class EditRecipe(NewRecipe):
    """Locators for editing a recipe."""

    selected_action_name = (By.CLASS_NAME,
                            'ant-select-selection-selected-value')


class ApprovalHistory(Base):
    """Locators for approval history."""

    # TODO: unique name for recipe card on approval history page
    recipe_card = (By.CSS_SELECTOR, '.recipe-details > div:nth-child(1)')

    # TODO: unique name for approve button on approval history page
    approve = (By.CSS_SELECTOR, 'button.ant-btn:nth-child(2)')

    comment = (By.ID, 'comment')

    tag = (By.CLASS_NAME, 'ant-tag-text')
