from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver
        self.menu_btn_locator_xpath = (By.XPATH, "//button[text()='Open Menu']")
        self.logout_btn_locator_link_text = (By.LINK_TEXT, "Logout")
        self.cart_btn_locator_id = (By.ID, "shopping_cart_container")
        self.product_dropdown_locator_class = (By.CLASS_NAME, "product_sort_container")
        #products
        self.first_product_locator_xpath = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
        self.second_product_locator_xpath = (By.XPATH, "//div[text()='Sauce Labs Bike Light']")
        self.third_product_locator_xpath = (By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']")
        self.fourth_product_locator_xpath = (By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")
        self.fifth_product_locator_xpath = (By.XPATH, "//div[text()='Sauce Labs Onesie']")
        self.sixth_product_locator_xpath = (By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']")
        #addtocartbuttons
        self.first_add_to_cart_btn_xpath = (By.XPATH, "(//button[text()='ADD TO CART'])[1]")
        self.second_add_to_cart_btn_xpath = (By.XPATH, "(//button[text()='ADD TO CART'])[2]")
        self.third_add_to_cart_btn_xpath = (By.XPATH, "(//button[text()='ADD TO CART'])[3]")
        self.fourth_add_to_cart_btn_xpath = (By.XPATH, "(//button[text()='ADD TO CART'])[4]")
        self.fifth_add_to_cart_btn_xpath = (By.XPATH, "(//button[text()='ADD TO CART'])[5]")
        self.sixth_add_to_cart_btn_xpath = (By.XPATH, "(//button[text()='ADD TO CART'])[6]")
        #price

        self.amt = (By.XPATH, "//*[@class='inventory_item_price'][1]")

    def pro_amt(self):
        wait = WebDriverWait(self.driver, 10)
        product_amt = wait.until(expected_conditions.presence_of_element_located(self.amt))
        product_amount = product_amt.text

    def click(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(by_locator)).click()

    def click_on_menu(self):
        self.click(self.menu_btn_locator_xpath)

    def click_on_logout(self):
        self.click(self.logout_btn_locator_link_text)

    def click_on_cart(self):
        self.click(self.cart_btn_locator_id)

    def select_product_dropdown(self):
        self.click(self.product_dropdown_class)

    def handle_dropdown_visible_text(self, visible_text):
        wait = WebDriverWait(self.driver, 10)
        sort_dropdown = wait.until(expected_conditions.presence_of_element_located(self.product_dropdown_locator_class))
        select = Select(sort_dropdown)
        select.select_by_visible_text(visible_text)

    def add_first_product_to_cart(self):
        self.move_product_to_cart(self.first_product_locator_xpath)
        self.click(self.first_add_to_cart_btn_xpath)

    def add_second_product_to_cart(self):
        self.move_product_to_cart(self.second_product_locator_xpath)
        self.click(self.second_add_to_cart_btn_xpath)

    def add_third_product_to_cart(self):
        self.move_product_to_cart(self.third_product_locator_xpath)
        self.click(self.third_add_to_cart_btn_xpath)

    def add_forth_product_to_cart(self):
        self.move_product_to_cart(self.fourth_product_locator_xpath)
        self.click(self.fourth_add_to_cart_btn_xpath)

    def add_fifth_product_to_cart(self):
        self.move_product_to_cart(self.fifth_product_locator_xpath)
        self.click(self.fifth_add_to_cart_btn_xpath)

    def add_sixth_product_to_cart(self):
        self.move_product_to_cart(self.sixth_product_locator_xpath)
        self.click(self.sixth_add_to_cart_btn_xpath)

    def verify_price_of_first_product(self):
        print(self.amt)



