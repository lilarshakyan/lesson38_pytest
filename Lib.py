from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData import data
import logging

logging.basicConfig(
    filename="test_log.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


class Helper:

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)

    def navigate_to_page(self):
        self.browser.get(data.url)

    def close_browser(self):
        if self.browser:
            self.browser.quit()

    def wait_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def wait_and_send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
        return element

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def write_into_file(self, text, mode="a"):
        with open(data.file_name, mode, encoding="utf_8") as my_file:
            my_file.write(text + "\n")