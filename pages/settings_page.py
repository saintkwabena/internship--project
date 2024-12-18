from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class SettingsPage(Page):
    SETTINGS_MENU = (By.XPATH, "//div[@class='photo_avatar']")
    USER_GUIDE_BTN = (By.CSS_SELECTOR, 'div[class="settings-block-menu"] [href="/user-guide"]')


    # def click_settings(self):
    #     self.click(*self.SETTINGS_MENU)

    def click_user_guide(self):
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, 450);")
        self.click(*self.USER_GUIDE_BTN)