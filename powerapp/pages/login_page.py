from selenium.webdriver.common.by import By

from library import Browser


class LoginPage:
    # Objects
    # Buttons
    _BTN_Next = (By.XPATH, '//input[@type="submit"]', 'Next button.')
    _BTN_Sign_in = (By.XPATH, '//input[@type="submit"]', 'Sign in button.')
    _BTN_No = (By.XPATH, '//input[@type="submit"]', 'No button.')

    # Check box
    _CHK_Dont_show_this_again = (By.XPATH, '//input[@name="DontShowAgain"]', 'Dont show this again check box.')

    # Text / Input
    _TXT_Email_Address = (By.XPATH, '//input[@type="email"]', 'Email Address input field.')
    _TXT_Password = (By.XPATH, '//input[@type="password"]', 'Password input field.')

    def __init__(self, browser: Browser):
        self.browser = browser
        pass

    # Page functions
    def login(self, username: str, password: str):
        self.browser.wait_for_element_visible(locator=LoginPage._TXT_Email_Address)
        self.browser.set_text(locator=LoginPage._TXT_Email_Address, value=username)
        self.browser.click(locator=LoginPage._BTN_Next)

        self.browser.wait_for_element_visible(locator=LoginPage._TXT_Password)
        self.browser.set_text(locator=LoginPage._TXT_Password, value=password)
        self.browser.click(locator=LoginPage._BTN_Sign_in)
        pass

    def skip_stay_signed_in(self):
        self.browser.wait_for_element_visible(locator=LoginPage._CHK_Dont_show_this_again)
        self.browser.click(locator=LoginPage._CHK_Dont_show_this_again)
        self.browser.click(locator=LoginPage._BTN_No)
        pass

    # Verify functions

    # Assert functions
