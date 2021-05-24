import os
import sys

from library import Browser
from powerapp import PowerApp

from robot.api.deco import keyword


class PowerAppDemo:

    def __init__(self):
        self.root_dir = os.path.dirname(sys.modules['__main__'].__file__)
        self.browser: Browser = Browser()
        self.power_app = PowerApp(browser=self.browser)
        pass

    # App Launch keywords
    @keyword
    def open_the_help_desk_power_app(self, power_app_url: str):
        self.browser.launch_chrome_browser(url=power_app_url)
        pass

    @keyword
    def close_the_app(self):
        self.browser.close_browser()
        pass

    # Microsoft Sign in keywords
    @keyword
    def login_to_microsoft_with_username_and_password(self, username: str, password: str):
        self.power_app.pages.login_page.login(username=username, password=password)
        self.power_app.pages.login_page.skip_stay_signed_in()
        pass

    # Help desk app keywords
    @keyword
    def login_as_a_help_desk_user(self):
        self.power_app.pages.home_page.login_as_a_help_desk_user()
        pass

    @keyword
    def logout_of_the_help_desk_app(self):
        self.power_app.pages.ticket_inventory_page.logout_of_the_help_desk_app()
        pass

    @keyword
    def login_as_a_help_desk_admin(self):
        self.power_app.pages.home_page.login_as_a_help_desk_admin()
        pass

    # Assert keywords
    @keyword
    def assert_help_desk_app_home_page_displayed(self):
        self.power_app.pages.home_page.assert_help_desk_app_home_page_displayed()
        pass

    @keyword
    def assert_login_as_help_desk_admin_success(self):
        # TODO Implement with Admin privileged user
        pass

    @keyword
    def assert_no_admin_privilege_error_displayed(self):
        self.power_app.pages.home_page.assert_login_as_a_help_desk_admin_failure_error()
        pass

    @keyword
    def assert_login_as_a_help_desk_user_success(self):
        self.power_app.pages.ticket_inventory_page.assert_login_as_a_help_desk_user_success()
        pass
