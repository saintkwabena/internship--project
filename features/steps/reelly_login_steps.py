from selenium.webdriver.common.by import By

from behave import given, when, then
from time import sleep




@given('Open main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(5)


@when('Log in to the page')
def login(context):
    context.app.login_page.login("elkwabena@gmail.com","FMlithonia1!")

# @when('Click on settings option')
# def click_settings(context):
#     context.app.settings_page.click_settings()

@when('Click on settings option')
def open_settings_btn(context):
    context.app.main_page.open_settings_btn()


@when('Click continue')
def click_continue(context):
    LOGIN_BTN = (By.XPATH, "//a[@class='login-button w-button']")
    context.driver.find_element(*LOGIN_BTN).click()


    #context.driver.execute_script("window.scrollBy(0, 1000);")


@when('Click on User Guide option')
def click_user_guide(context):
    context.app.settings_page.click_user_guide()

@then('Verify the right page opens')
def verify_right_page(context):
    context.app.user_guide_page.verify_user_guide_page_opened()
    sleep(5)

@then( 'Verify all lesson videos contain titles')
def verify_lesson_titles(context):
    context.app.user_guide_page.verify_lesson_titles()

    sleep(5)