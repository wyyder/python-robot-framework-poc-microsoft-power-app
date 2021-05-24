from library import Browser

from powerapp.pages import PowerAppPages


class PowerApp:

    def __init__(self, browser: Browser):
        self.browser = browser
        self.pages = PowerAppPages(browser=self.browser)
        pass
