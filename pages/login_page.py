from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):

    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BTN = (By.XPATH , "//a[@class='login-button w-button']")

    def login(self, email, password):
        self.find_element(*self.EMAIL_FIELD).send_keys('elkwabena@gmail.com')
        self.find_element(*self.PASSWORD_FIELD).send_keys('FMlithonia1!')
        self.find_element(*self.LOGIN_BTN).click()

