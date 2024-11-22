from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



class LoginPage(Page):

    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BTN = (By.XPATH , "//a[@class='login-button w-button']")
    PAGE_BODY = (By.CSS_SELECTOR, '.login-body')


    def login(self, email, password):
        self.find_element(*self.EMAIL_FIELD).send_keys('elkwabena@gmail.com')
        self.find_element(*self.PASSWORD_FIELD).send_keys('FMlithonia1!')
        sleep(5)
        actions = ActionChains(self.driver)
        reely_page = self.find_element(*self.PAGE_BODY)
        actions.move_to_element(reely_page).click().perform()
        sleep(5)
        self.find_element(*self.LOGIN_BTN).click()

