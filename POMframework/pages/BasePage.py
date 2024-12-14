from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def sendkeys(self, by_locator, value):
        # self.driver.find_element(*by_locator).send_keys(value)
        web_wait = WebDriverWait(self.driver, 10)
        web_wait.until(expected_conditions.presence_of_element_located(by_locator)).send_keys(value)

    def click_ele(self, by_locator):
        #self.driver.find_element(*by_locator).click()
        web_wait = WebDriverWait(self.driver, 10)
        web_wait.until(expected_conditions.presence_of_element_located(by_locator)).click()

    def handle_dropdown_visible_text(self, visible_text):
        wait = WebDriverWait(self.driver, 10)
        sort_dropdown=wait.until(expected_conditions.presence_of_element_located(self.product_dropdown_locator_class))
        select = Select(sort_dropdown)
        select.select_by_visible_text(visible_text)

    def move_product_to_cart(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        product = wait.until(expected_conditions.presence_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(product).perform()

