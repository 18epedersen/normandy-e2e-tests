import pytest
from pages.ldap_login_restapi import LDAPLoginRestAPI
import time
from selenium import webdriver
import requests
import json


@pytest.mark.nondestructive
def test_restapi(conf, selenium, qr_code):
    """Test adding a recipe."""
    # cookie = {"_csrf": "PjoxkMyr7H331j70ZBmYUepE"}
    url = "https://normandy.dev.mozaws.net/api/v1/recipe/"
    # ldap_restapi_page = LDAPLoginRestAPI(selenium, url)
    # home_page = ldap_restapi_page.setup(conf, qr_code)
    # time.sleep(5)
    r = requests.get(url)
    cookies = r.cookies
    print("cookiejar", cookies)
    dictionary = requests.utils.dict_from_cookiejar(cookies)
    print("cookies", dictionary)
    response = requests.get(url, cookies=dictionary)
    json_data = json.loads(response.text)
    print(json_data)
    # r = requests.get(url, cookies=cookies)
    # print(r.text)
    # for cookie in r.cookies:
    #     print("cookie is ", cookie)
    # print("cookies are ", r.cookies)

    # with requests.Session() as s:
    #     r = s.get(url)
    #     r = s.post(url, data="username and password data payload")

    # s = requests.session()
    # response = s.get(url)
    # print("response.text", response.text)
