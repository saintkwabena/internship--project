from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page



class MainPage(Page):

    NEW_SETTINGS_BTN = (By.XPATH, '//a[@href="/settings" and @class="menu-photo_avatar w-inline-block"]')
    MAIN_MENU_BTN = (By.CSS_SELECTOR, '[class="assistant-mobile"] [href="/main-menu"]')


    def open_main(self):
        self.open('https://soft.reelly.io/sign-in')

    # def open_settings_btn(self):
    #     self.wait.until(EC.presence_of_element_located(*self.NEW_SETTINGS_BTN))

    def click_main_btn(self):
        self.find_element(*self.MAIN_MENU_BTN)



    def open_settings_btn(self):
        self.click(*self.MAIN_MENU_BTN)
        sleep(3)
        self.click(*self.NEW_SETTINGS_BTN)

        sleep(5)

