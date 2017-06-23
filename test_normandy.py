import pytest
import time
import pyotp
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope='session')
def base_url():
    """Grabbing the base url of the Normandy Control UI."""
    return 'https://normandy-admin.stage.mozaws.net/control/recipe/'


def generate_QR_code(secret):
    """Generating the QR code for 2FA."""
    totp = pyotp.TOTP(secret)
    return totp.now()


def login(base_url, selenium, variables):
    """Automatting loginning into Normandy Control UI with demo LDAP
    and authenicating auth0 with 6 digit QR code."""
    selenium.get(base_url)
    WebDriverWait(selenium, timeout=5).until(
        EC.visibility_of_element_located((By.CLASS_NAME,
                                          'auth0-lock-input-username')))
    username = selenium.find_element(By.CLASS_NAME,
                                     'auth0-lock-input-username')
    username.send_keys(variables['username'])
    WebDriverWait(selenium, timeout=5).until(
        EC.visibility_of_element_located((By.NAME, 'password')))
    password = selenium.find_element(By.NAME, 'password')
    password.send_keys(variables['password'])
    selenium.find_element(By.CSS_SELECTOR, ".auth0-lock-submit").click()
    WebDriverWait(selenium, timeout=5).until(
        EC.visibility_of_element_located(
             (By.CLASS_NAME, 'a0-notloggedin')))
    selenium.switch_to_frame(selenium.find_element(By.ID, "duo_iframe"))
    WebDriverWait(selenium, timeout=5).until(
        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, '.device-select-wrapper')))
    select_CSS = '.device-select-wrapper > select:nth-child(1)'
    select = Select(selenium.find_element(By.CSS_SELECTOR, select_CSS))
    select.select_by_value('token')
    passcode_CSS = 'button.positive:nth-child(5)'
    enter_passcode_button = WebDriverWait(selenium, timeout=5).until(
                EC.visibility_of_element_located(
                   (By.CSS_SELECTOR, passcode_CSS)))
    enter_passcode_button.click()
    QR_code = generate_QR_code(variables['secret'])
    passEnter_CSS = 'div.passcode-label:nth-child(1) > input:nth-child(4)'
    passcode_element = WebDriverWait(selenium, timeout=5).until(
                EC.visibility_of_element_located(
                   (By.CSS_SELECTOR, passEnter_CSS)))
    passcode_element.send_keys(QR_code)
    login_CSS = 'button.positive:nth-child(5)'
    login_button = WebDriverWait(selenium, timeout=5).until(
                EC.visibility_of_element_located(
                   (By.CSS_SELECTOR, login_CSS)))
    login_button.click()
    selenium.switch_to_default_content()


def select_form_countries(selenium, CSS, variables_value):
    """Selects a filter for Recipe."""
    print("in select form countires")
    print("CSS ", CSS)
    print("variables_value ", variables_value)
    select = Select(WebDriverWait(selenium, timeout=15).until(
     EC.visibility_of_element_located((
      By.CSS_SELECTOR, CSS))))
    # TODO: (paste issue number)
    # available locale has to be selected twice
    for option in select.options:
        val = option.get_attribute("value")
        print("val is ", val)
        if val == variables_value:
            print("in If statement selected ", val)
            select.select_by_value(val)


def click_form_buttons(selenium, CSS):
    """Clicks button for the available locales \
    and available countries fields."""
    print("in click form buttons")
    add_button = WebDriverWait(selenium, timeout=15).until(
     EC.visibility_of_element_located((
      By.CSS_SELECTOR, CSS)))
    if add_button.is_enabled():
        print("button is enabled")
        add_button.click()
    else:
        print("button is not enabled")


def select_channels(selenium, CSS_list):
    """Select channels for recipe."""
    print("in select channels")
    for css in CSS_list:
        print("css is ", css)
        WebDriverWait(selenium, timeout=15).until(
         EC.visibility_of_element_located((
          By.CSS_SELECTOR, css))).click()


def additional_filters(selenium, name, variables):
    """ Sending in a message for additional filters."""
    print("in additional filters")
    WebDriverWait(selenium, timeout=15).until(
     EC.visibility_of_element_located((
      By.NAME, name))).send_keys(variables['additional filters'])


def action_configuration(selenium, action_name, variables):
    """ Selecting an action."""
    print("in action configuration")
    select = Select(WebDriverWait(selenium, timeout=15).until(
     EC.visibility_of_element_located((
      By.NAME, action_name))))
    select.select_by_value(variables['action'])
    message_box_element_name = "arguments.message"
    WebDriverWait(selenium, timeout=15).until(
     EC.visibility_of_element_located((
      By.NAME, message_box_element_name))).send_keys(variables['message'])


@pytest.mark.nondestructive
def test_create_recipe(base_url, selenium, variables):
    """ Testing creating a new recipe and checking that
    the new elements are there."""
    try:
        login(base_url, selenium, variables)
        add_new_CSS = ".button"
        # adding a new recipe
        add_new_button = WebDriverWait(selenium, timeout=15).until(
         EC.visibility_of_element_located((
          By.CSS_SELECTOR, add_new_CSS)))
        add_new_button.click()
        name_CSS = "label.form-field:nth-child(1) > input:nth-child(2)"
        # naming new recipe
        time.sleep(5)
        WebDriverWait(selenium, timeout=15).until(
         EC.visibility_of_element_located((
          By.CSS_SELECTOR, name_CSS))).send_keys(variables['name'])
        # The available locales form CSS
        available_locales_form_CSS = "div.form-field:nth-child(2) > div:nth-child(1) \
        > fieldset:nth-child(1) > select:nth-child(3)"
        # selecting a specific locale
        time.sleep(5)
        select_form_countries(selenium, available_locales_form_CSS,
                              variables["available_locales"])
        # finding the add locales button
        add_locales_button_css = "div.form-field:nth-child(2) > \
        div:nth-child(1) > fieldset:nth-child(1) > button:nth-child(4)"
        time.sleep(5)
        click_form_buttons(selenium, add_locales_button_css)
        available_countries_form_CSS = "div.form-field:nth-child(3) > \
        div:nth-child(1) > fieldset:nth-child(1) > select:nth-child(3)"
        time.sleep(5)
        select_form_countries(selenium, available_countries_form_CSS,
                              variables["available_countries"])
        add_countries_button_css = "div.form-field:nth-child(3) > \
        div:nth-child(1) > fieldset:nth-child(1) > button:nth-child(4)"
        time.sleep(5)
        click_form_buttons(selenium, add_countries_button_css)
        # selecting developer and release
        release_channels_CSS_list = ["label.checkbox:nth-child(1) > \
        input:nth-child(1)", "label.checkbox:nth-child(4) > \
        input:nth-child(1)"]
        # method to select those channels
        select_channels(selenium, release_channels_CSS_list)
        name = "extra_filter_expression"
        # writing an additional filter message
        additional_filters(selenium, name, variables)
        action_name = "action"
        # selecting an action
        action_configuration(selenium, action_name, variables)
        # clicking save  button
        save_recipe_class_name = "action-new"
        WebDriverWait(selenium, timeout=15).until(
         EC.visibility_of_element_located((
          By.CLASS_NAME, save_recipe_class_name))).click()
        time.sleep(50)
        assert True
    except NoSuchElementException:
        print("exception")
        assert False
