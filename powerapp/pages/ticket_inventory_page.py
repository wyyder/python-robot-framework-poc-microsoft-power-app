from robot.libraries.BuiltIn import BuiltIn

from selenium.webdriver.common.by import By

from library import Browser


class TicketInventoryPage:
    # Objects
    # Buttons
    _BTN_Create_Ticket = (By.XPATH, '//div[@data-control-name="MyTicketsScreenAddButtonPlus"]', 'Create ticket button.')
    _BTN_Logout = (By.XPATH, '//div[@data-control-name="MyTicketsScreenLogoutIcon"]', 'Logout button.')

    # IFrame
    _IFRAME_Published_App = (By.XPATH, '//iframe[@class="publishedAppIframe"]', 'Published app IFrame.')

    # Label
    _LBL_My_Help_Desk_Tickets = (By.XPATH, '//div[text()="My Help Desk Tickets"]', 'My Help Desk Tickets Header Label.')

    def __init__(self, browser: Browser):
        self.browser = browser
        pass

    # Page functions
    def logout_of_the_help_desk_app(self):
        self.browser.switch_frame(locator=TicketInventoryPage._IFRAME_Published_App)
        self.browser.wait_for_element_visible(locator=TicketInventoryPage._BTN_Logout)
        self.browser.click(locator=TicketInventoryPage._BTN_Logout)
        self.browser.switch_default_frame()
        pass

    # Verify functions

    # Assert functions
    def assert_login_as_a_help_desk_user_success(self):
        self.browser.switch_frame(locator=TicketInventoryPage._IFRAME_Published_App)
        self.browser.wait_for_element_visible(locator=TicketInventoryPage._LBL_My_Help_Desk_Tickets)
        BuiltIn().run_keyword('should be true',
                              self.browser.is_element_displayed(locator=TicketInventoryPage._LBL_My_Help_Desk_Tickets),
                              'My Help desk Ticket header displayed.')
        BuiltIn().run_keyword('should be true',
                              self.browser.is_element_displayed(locator=TicketInventoryPage._BTN_Create_Ticket),
                              'Create Ticket button displayed.')
        BuiltIn().run_keyword('should be true',
                              self.browser.is_element_displayed(locator=TicketInventoryPage._BTN_Logout),
                              'Logout button displayed.')
        self.browser.switch_default_frame()
        pass
