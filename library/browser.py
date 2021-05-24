import os
import sys
import time
import logging

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Browser:

    def __init__(self):
        self.driver: Chrome = None
        pass

    # Browser functions
    def launch_chrome_browser(self, url: str):
        # Chrome driver path
        driver_path = os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver.exe')

        # Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=OFF")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            }
        })

        # Launch browser
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)

        # Implicit wait
        self.driver.implicitly_wait(30)

        # Navigate to url / Application load
        self.driver.get(url=url)
        logging.info('Url opened - ' + url)
        pass

    def close_browser(self):
        self.driver.close()
        self.driver.quit()
        logging.info('Browser closed.')
        pass

    def find_element(self, locator: tuple):
        locator, value, description = locator
        if locator == By.XPATH:
            return self.driver.find_element_by_xpath(xpath=value)
        else:
            raise Exception(locator + ' - Locator not implemented.')

    def find_elements(self, locator: tuple):
        locator, value, description = locator
        if locator == By.XPATH:
            return self.driver.find_elements_by_xpath(xpath=value)
        else:
            raise Exception(locator + ' - Locator not implemented.')

    def click(self, locator: tuple):
        self.find_element(locator=locator).click()
        logging.info('Clicked on ' + locator[2])
        pass

    def clear_text(self, locator: tuple):
        self.find_element(locator=locator).clear()
        logging.info('Cleared text on ' + locator[2])
        pass

    def set_text(self, locator: tuple, value: str):
        self.find_element(locator=locator).send_keys(value)
        logging.info('Set text on ' + locator[2])
        pass

    def switch_frame(self, locator: tuple):
        self.driver.switch_to.frame(self.find_element(locator=locator))
        pass

    def switch_default_frame(self):
        self.driver.switch_to.default_content()
        pass

    # Wait functions
    @staticmethod
    def __wait_for_seconds(seconds: int):
        time.sleep(seconds)
        pass

    def __wait_for_jquery(self, timeout: int = 180):
        script = 'return window.jQuery != undefined && jQuery.active === 0'
        self.__wait_for_seconds(seconds=10)
        WebDriverWait(self.driver, timeout).until(lambda x: self.driver.execute_script(script=script))
        pass

    def wait_for_dom(self, timeout: int = 180):
        script = 'return document.readyState;'
        self.__wait_for_seconds(seconds=10)
        WebDriverWait(self.driver, timeout).until(lambda x: self.driver.execute_script(script=script) == 'complete')
        pass

    def wait_for_async(self):
        try:
            self.__wait_for_jquery()
        except TimeoutError:
            pass
        pass

    def wait_for_page_load(self):
        self.wait_for_async()
        try:
            self.wait_for_dom()
        except TimeoutError:
            pass
        pass

    def wait_for_element_present(self, locator: tuple, timeout: int = 180):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((locator[0], locator[1])))
        pass

    def wait_for_element_visible(self, locator: tuple, timeout: int = 180):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((locator[0], locator[1])))
        pass

    def wait_for_element_invisibility(self, locator: tuple, timeout: int = 180):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located((locator[0], locator[1])))
        pass

    # Verify functions
    def is_element_present(self, locator: tuple):
        try:
            self.find_element(locator=locator)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, locator: tuple):
        return not self.is_element_present(locator=locator)

    def is_element_displayed(self, locator: tuple):
        return self.find_element(locator=locator).is_displayed()

    def is_element_not_displayed(self, locator: tuple):
        return not self.is_element_displayed(locator=locator)
