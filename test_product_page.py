﻿import time
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


#def test_guest_can_add_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_basket()
#    page.to_assert()
#    time.sleep(3)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()



#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com"
#    page = MainPage(browser, link)
#    page.open()
#    page.go_to_login_page()
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()
#
#def test_login_url(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_url()
#
#def test_login_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()


#    page.should_be_login_form()


#
#def test_register_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_register_form()



