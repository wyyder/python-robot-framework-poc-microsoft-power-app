from library import Browser

from powerapp.pages.login_page import LoginPage
from powerapp.pages.home_page import HomePage
from powerapp.pages.ticket_inventory_page import TicketInventoryPage


class PowerAppPages:

    def __init__(self, browser: Browser):
        self.browser = browser
        self.login_page = LoginPage(browser=self.browser)
        self.home_page = HomePage(browser=self.browser)
        self.ticket_inventory_page = TicketInventoryPage(browser=self.browser)
        pass
