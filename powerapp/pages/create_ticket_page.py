from robot.libraries.BuiltIn import BuiltIn

from selenium.webdriver.common.by import By

from library import Browser


class CreateTicketPage:
    # Objects
    # Buttons
    _BTN_Cancel = (By.XPATH, '//button/div/div[text()="CANCEL"]', 'Cancel button.')
    _BTN_Create = (By.XPATH, '//button/div/div[text()="CREATE"]', 'Create button.')
    _BTN_Back = (By.XPATH, '//div[@data-control-name="CreateTicketScreenBack"]', 'Back button.')

    # IFrame
    _IFRAME_Published_App = (By.XPATH, '//iframe[@class="publishedAppIframe"]', 'Published app IFrame.')

    # Label
    _LBL_Create_Ticket = (By.XPATH, '//div[text()="Create Ticket"]', 'Create Ticket Header Label.')

    # List box
    _LST_Category = (By.XPATH, '//input[@name="DontShowAgain"]', 'Category list box.')
    _LST_Priority = (By.XPATH, '//input[@name="DontShowAgain"]', 'Priority list box.')

    # Element
    _ELM_Status = (By.XPATH, '//div[text()="Create Ticket"]', 'Status element.')
    _ELM_Ticket_Id = (By.XPATH, '//div[text()="Create Ticket"]', 'Ticket ID element.')

    # Text / Input
    _TXT_Title = (By.XPATH, '//input[@type="email"]', 'Title input field.')
    _TXT_Description = (By.XPATH, '//input[@type="password"]', 'Description field.')

    def __init__(self, browser: Browser):
        self.browser = browser
        pass

    # Page functions
    def create_ticket(self, title: str, category: str, priority: str, description: str):
        self.browser.switch_frame(locator=CreateTicketPage._IFRAME_Published_App)
        self.browser.wait_for_element_visible(locator=CreateTicketPage._TXT_Title)
        self.browser.switch_default_frame()
        # TODO Implement
        pass

    # Verify functions

    # Assert functions
