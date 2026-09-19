import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lib import Helper


class LoginPage(Helper):
    sign_in = (By.XPATH, "//a[contains(text(),'Sign In')]")
    email = (By.ID, "email")
    password = (By.ID, "login-password")
    login = (By.ID, "login")
    incorrect_msg = (By.ID, "incorrectdetails")

    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def click_sign_in_login(self, email, password):
        logging.info("Clicking Sign In button")
        self.wait_and_click(self.sign_in)

        logging.info(f"Logging in with email: {email}")
        self.wait_and_send_keys(self.email, email)
        self.wait_and_send_keys(self.password, password)
        self.wait_and_click(self.login)

    def get_incorrect_text(self):
        logging.info("Getting incorrect login message")
        return self.wait_for_visibility(self.incorrect_msg).text