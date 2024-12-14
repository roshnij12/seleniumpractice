from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver

        self.title_your_cart_locator = (By.CLASS_NAME, "Your Cart")
        self.continue_shopping_btn_locator = (By.LINK_TEXT, "Continue Shopping")
        self.checkout_btn_locator = (By.LINK_TEXT, "CHECKOUT")
        self.first_name_locator = (By.ID, "first-name")
        self.last_name_locator = (By.ID, "last-name")
        self.zip_code_locator = (By.ID, "postal-code")
        self.cancel_btn_locator = (By.LINK_TEXT, "CANCEL")
        self.continue_btn_locator = (By.XPATH, "//input[@type='submit']")
        self.title_overview_page_locator = (By.CLASS_NAME, "Checkout: Overview")
        self.finish_btn_locator = (By.LINK_TEXT, "FINISH")
        self.title_finish_page_locator = (By.CLASS_NAME, "Finish")
        self.order_msg_locator = (By.CLASS_NAME, "THANK YOU FOR YOUR ORDER")
        self.amt = (By.XPATH, "//*[@class='inventory_item_price']")
        self.total = (By.XPATH, "//*[@class='summary_subtotal_label']")
        self.tax_amt_locator = (By.XPATH, "//*[@class='summary_tax_label']")
        self.final_amt_locator = (By.XPATH, "//*[@class='summary_total_label']")


    def click_on_checkout_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.checkout_btn_locator)).click()

    def send_keys_shipping_details(self, by_locator, value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(by_locator)).send_keys(value)

    def click_on_continue_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.continue_btn_locator)).click()

    def click_on_finish_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.finish_btn_locator)).click()

    def enter_shipping_details(self, firstname, lastname, zipcode):
        self.send_keys_shipping_details(self.first_name_locator, firstname)
        self.send_keys_shipping_details(self.last_name_locator, lastname)
        self.send_keys_shipping_details(self.zip_code_locator, zipcode)

    def verify_calculation(self, by_loc):
        wait = WebDriverWait(self.driver, 10)
        product_amt = wait.until(expected_conditions.presence_of_element_located(by_loc))
        product_amount = product_amt.text
        amt_bag = product_amount.find("$") + 1

        wait = WebDriverWait(self.driver, 10)
        total_amt = wait.until(expected_conditions.presence_of_element_located(self.total))
        product_total = total_amt.text
        pro_total = product_total.find('$') + 1
        total_value = product_total[pro_total:]

        assert amt_bag.__eq__(total_value)

        wait = WebDriverWait(self.driver, 10)
        tax = wait.until(expected_conditions.presence_of_element_located(self.tax_amt_locator))
        tax_from_page = tax.text
        tx = tax_from_page.find('$') + 1
        tax_value = tax_from_page[tx:]

        float_tax_amt = (float(total_value))
        tax_amt = float_tax_amt * (8 / 100)
        assert tax_value.__eq__(tax_amt)

        wait = WebDriverWait(self.driver, 10)
        final_from_page = wait.until(expected_conditions.presence_of_element_located(self.final_amt_locator))

        final_amt_page = final_from_page.text
        final_value = final_amt_page.find("$") + 1
        checkout_value = final_amt_page[final_value:]
        final_amt = float()+tax_amt
        assert checkout_value.__eq__(final_amt)



    def calculation(self, loc1, loc2, loc3, loc4):
        wait = WebDriverWait(self.driver, 10)
        product_amt = wait.until(expected_conditions.presence_of_element_located(loc1))
        product_amount = product_amt.text
        amt_bag = product_amount.find("$") + 1

        wait = WebDriverWait(self.driver, 10)
        total_amt = wait.until(expected_conditions.presence_of_element_located(loc2))
        product_total = total_amt.text
        pro_total = product_total.find('$') + 1
        total_value = product_total[pro_total:]

        assert amt_bag.__eq__(total_value)
        print("first passed")

        wait = WebDriverWait(self.driver, 10)
        tax = wait.until(expected_conditions.presence_of_element_located(loc3))
        tax_from_page = tax.text
        tx = tax_from_page.find('$') + 1
        tax_value = tax_from_page[tx:]

        float_tax_amt = (float(total_value))
        tax_amt = float_tax_amt * (8 / 100)
        assert tax_value.__eq__(tax_amt)
        print("sec passed")
        wait = WebDriverWait(self.driver, 10)
        final_from_page = wait.until(expected_conditions.presence_of_element_located(loc4))

        final_amt_page = final_from_page.text
        final_value = final_amt_page.find("$") + 1
        checkout_value = final_amt_page[final_value:]
        final_amt = (float() +
                     tax_amt)
        assert checkout_value.__eq__(final_amt)
        print("third passed")
    def call_cal(self):
        self.calculation(self.amt, self.total, self.tax_amt_locator, self.final_amt_locator)










