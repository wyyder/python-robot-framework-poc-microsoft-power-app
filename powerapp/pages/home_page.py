from robot.libraries.BuiltIn import BuiltIn

from selenium.webdriver.common.by import By

from library import Browser


class HomePage:
    # Objects
    # Buttons
    _BTN_Login_as_a_Help_Desk_User = (
        By.XPATH, '//div[text()="Login as a Help Desk User"]', 'Login as a Help desk user button.')
    _BTN_Login_as_a_Help_Desk_Admin = (
        By.XPATH, '//div[text()="Login as a Help Desk Admin"]', 'Login as a Help desk admin button.')

    # IFrame
    _IFRAME_Published_App = (By.XPATH, '//iframe[@class="publishedAppIframe"]', 'Published app IFrame.')

    # Label element
    _LBL_Error_No_admin_privilege = (By.XPATH, '//div[text()="We were unable to give you access as an admin as your '
                                               'account does not have admin privileges."]', 'No admin privilege error.')

    def __init__(self, browser: Browser):
        self.browser = browser
        pass

    # Page functions
    def login_as_a_help_desk_user(self):
        self.browser.switch_frame(locator=HomePage._IFRAME_Published_App)
        self.browser.wait_for_element_visible(locator=HomePage._BTN_Login_as_a_Help_Desk_User)
        self.browser.click(locator=HomePage._BTN_Login_as_a_Help_Desk_User)
        self.browser.switch_default_frame()
        pass

    def login_as_a_help_desk_admin(self):
        self.browser.switch_frame(locator=HomePage._IFRAME_Published_App)
        self.browser.wait_for_element_visible(locator=HomePage._BTN_Login_as_a_Help_Desk_Admin)
        self.browser.click(locator=HomePage._BTN_Login_as_a_Help_Desk_Admin)
        self.browser.switch_default_frame()
        pass

    # Verify functions

    # Assert functions
    def assert_help_desk_app_home_page_displayed(self):
        self.browser.switch_frame(locator=HomePage._IFRAME_Published_App)
        self.browser.wait_for_element_visible(locator=HomePage._BTN_Login_as_a_Help_Desk_User)
        BuiltIn().run_keyword('should be true',
                              self.browser.is_element_displayed(locator=HomePage._BTN_Login_as_a_Help_Desk_User),
                              'Help desk Home page displayed.')
        self.browser.switch_default_frame()
        pass

    def assert_login_as_a_help_desk_admin_failure_error(self):
        self.browser.switch_frame(locator=HomePage._IFRAME_Published_App)
        self.browser.wait_for_element_visible(locator=HomePage._LBL_Error_No_admin_privilege)
        BuiltIn().run_keyword('should be true',
                              self.browser.is_element_displayed(locator=HomePage._LBL_Error_No_admin_privilege),
                              'No admin privilege error displayed.')
        self.browser.switch_default_frame()
        pass
