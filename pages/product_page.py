﻿import time
from .login_page import LoginPage
from .base_page import BasePage

from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        bskt = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        bskt.click()
        time.sleep(2)
        self.solve_quiz_and_get_code()
        time.sleep(999)

    def to_assert(self):
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.ALERTINNER)
        book_name = self.browser.find_element(*ProductPageLocators.ALERTNAME)
        assert book_name_in_basket.text == book_name

    def test_guest_can_go_to_login_page_from_product_page(self):
        go_to_login = self.browser.find_element(*ProductPageLocators.LOGIN_LINK_INVALID)
        go_to_login.click()








#LOGIN_LINK_INVALID


#    def should_be_login_link(self):
#        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

#    def should_be_login_link(self):
#        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
#
#    def go_to_login_page(self):
#        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        #link = self.browser.find_element_by_css_selector("#login_link")
#        link.click()
#        #alert = self.browser.switch_to.alert
#        #alert.accept()
 
