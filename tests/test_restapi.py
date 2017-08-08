import pytest
from pages.ldap_login_restapi import LDAPLoginRestAPI
import time
from selenium import webdriver
import requests
import json


@pytest.mark.nondestructive
def test_restapi(conf, base_url, selenium, qr_code):
    """Test adding a recipe."""
    # driver = webdriver.Firefox()
    # driver.implicitly_wait(30)
    # driver.maximize_window()
    url = "https://normandy.dev.mozaws.net/api/v1/recipe/"
    # driver.get(url)
    ldap_restapi_page = LDAPLoginRestAPI(selenium, url)
    home_page = ldap_restapi_page.setup(conf, qr_code)
    time.sleep(5)
    r = requests.get(url)
    print(r.text)
    # print("after r")
    # json_data = json.loads(r.text)
    # print(json_data)
    # time.sleep(100)
    # recipes_listing_page = home_page.click_recipes()
    # new_recipe_page = recipes_listing_page.click_new_recipe()
    # assert new_recipe_page.heading_two == "Create New Recipe"
    # assert new_recipe_page.find_element(
    #  *new_recipe_page.LOCATORS.save_button).is_displayed()
