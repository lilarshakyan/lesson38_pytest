import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lib import Helper


class PracticePage(Helper):
    alert_button = (By.ID, 'alertbtn')
    text_box = (By.ID, "displayed-text")
    hide_button = (By.XPATH, "//input[@id='hide-textbox']")
    mouse_hover_btn = (By.ID, "mousehover")
    top_btn = (By.XPATH, '//a[text()="Top"]')
    footer = (By.XPATH, "//footer") 
    sign_in_btn = (By.XPATH, "//h1[text()='Practice Page']//preceding::a[text()='Sign In']") 
    title = (By.XPATH, "//title[text()='Practice Page']") 


    def __init__(self, browser, wait):
            self.browser = browser
            self.wait = wait


    def hide_element_check(self):
            try:
                self.find_and_click(self.btn_hide)
                hide_attr = self.get_attribute(self.inp_example, 'style')
                self.test_logger.info(f'Hidden attribute is - {hide_attr}')
                return hide_attr
            except Exception as e:
                self.test_logger.error(f'Hide element check failed: {e}')
                raise      


    

    def click_alert(self):
        logging.info("Clicking alert button")
        self.wait_and_click(self.alert_button)
        popup = self.browser.switch_to.alert
        text = popup.text
        popup.accept()
        return text

    def enter_text_box(self, text):
        logging.info(f"Typing your text: {text}")
        self.wait_and_send_keys(self.text_box, text)

    def hide_text_box(self):
        logging.info("Clicking hide button")
        self.wait_and_click(self.hide_button)

    def get_text_box_style(self):
        logging.info("Getting textbox style attribute")
        text_box = self.browser.find_element(*self.text_box)
        if not text_box.is_displayed():
            attribute = "style"
            value = text_box.get_attribute(attribute)
            return f"Hide Info = Attribute: {attribute}, Value: {value}"
        return "Hide info is still displayed,"

    def scroll_top(self):
        logging.info("Scrolling to Top button")
        hover_element = self.wait_for_visibility(self.mouse_hover_btn)
        actions = ActionChains(self.browser)
        actions.move_to_element(hover_element).perform()
        self.wait_and_click(self.top_btn)

    def scroll_footer(self):
        logging.info("Getting footer text")
        footer_element = self.wait_for_visibility(self.footer)
        return footer_element.text