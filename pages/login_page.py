﻿from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver




class LoginPage(BasePage):
    #def should_be_login_page(self):

    def should_be_login_url(self):

        assert self.browser.current_url, "URL IS NOT PRESENT"

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN IS NOT PRESENT"

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REG IS NOT PRESENT"