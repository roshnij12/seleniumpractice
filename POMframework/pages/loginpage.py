from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_textfield_id = (By.ID, "user-name")
        self.password_textfield_id = (By.ID, "password")
        self.login_btn_id = (By.ID, "login-button")

    #def sendkeys(self, by_locator, value):
        #self.driver.find_element(*by_locator).send_keys(value)
        #web_wait = WebDriverWait(self.driver, 10)
        #web_wait.until(expected_conditions.presence_of_element_located(by_locator)).send_keys(value)

    #def click_ele(self, by_locator):
        #self.driver.find_element(*by_locator).click()
        #web_wait = WebDriverWait(self.driver, 10)
        #web_wait.until(expected_conditions.presence_of_element_located(by_locator)).click()
    def login_saucedemo(self, username, password):
        self.sendkeys(self.username_textfield_id, username)
        self.sendkeys(self.password_textfield_id, password)
        self.click_ele(self.login_btn_id)