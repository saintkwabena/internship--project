from pages.base_page import Page


class MainPage(Page):
    def open_main(self):
        self.open('https://soft.reelly.io/sign-in')
