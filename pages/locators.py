from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    def should_be_login_page(self):
        self.should_be_login_url(driver.current_url)

        self.should_be_login_form(By.CSS_SELECTOR, "#login_form")

        self.should_be_register_form(By.CSS_SELECTOR, "#register_form")

