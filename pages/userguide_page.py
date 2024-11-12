from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class UserGuidePage(Page):

    USER_GUIDE_TEXTFIELD =(By.XPATH, "//div[@class='next-event-text']")
    # LESSON_TITLES =(By.CSS_SELECTOR, '[class="ytp-title"] a')
    # VIDEO_BLOCK = (By.CSS_SELECTOR, '.video-block iframe')
    # VIDEO_TITLE = (By.CSS_SELECTOR, '.chatbot-text-h1')
    IFRAME_VIDEO1 = (By.CSS_SELECTOR, '[class="video-block"] [class="embedly-embed"]')
    IFRAME_VIDEO2 = (By.ID, 'player')
    LESSON_TITLES = (By.CSS_SELECTOR, 'a[class*="ytp-title-link"]')


    def verify_user_guide_page_opened(self):
        expected_text = 'User guide'
        self.verify_text(expected_text, *self.USER_GUIDE_TEXTFIELD)

    def verify_lesson_titles(self):
        #video_title_iframe = self.find_element(By.CSS_SELECTOR, '[class="video-block"] [class="embedly-embed"]')
        #self.driver.switch_to.frame(video_title_iframe)
        # self.driver.switch_to.frame('player')
        # title = self.find_element(*self.LESSON_TITLES).text
        # print(f'Title: {title}')
        #expected_text = 'Full overview of Reelly platform'
        #self.verify_text(expected_text, *self.LESSON_TITLES)
            # THE FIRST IFRAME TO SWITCH
            iframe1 = self.driver.find_element(*self.IFRAME_VIDEO1)
            self.driver.switch_to.frame(iframe1)

            # THE SECOND IFRAME TO SWITCH
            iframe2 = self.driver.find_element(*self.IFRAME_VIDEO2)
            self.driver.switch_to.frame(iframe2)

            # NOW LOCATE THE TITLE
            title = self.find_element(*self.LESSON_TITLES).text
            print(f'Title: {title}')  # This will now print the title
