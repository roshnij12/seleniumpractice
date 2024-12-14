import time

from pages.cartpage import CartPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from tests.test_Loginfunction import Test_Login


class Test_Add_Checkout:

    def test_add_product_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login_saucedemo('standard_user', 'secret_sauce')
        time.sleep(3)
        home_page = HomePage(self.driver)
        home_page.add_first_product_to_cart()
        time.sleep(2)
        home_page.add_second_product_to_cart()
        time.sleep(2)
        home_page.add_third_product_to_cart()
        home_page.click_on_cart()
        time.sleep(2)
        cart_page = CartPage(self.driver)
        cart_page.click_on_checkout_btn()
        cart_page.enter_shipping_details("Flora", "Bing", 80899)
        cart_page.click_on_continue_btn()
        cart_page.click_on_finish_btn()
        time.sleep(2)

    def test_verify_final_amt(self):
        login_page = LoginPage(self.driver)
        login_page.login_saucedemo('standard_user', 'secret_sauce')
        time.sleep(2)
        home_page = HomePage(self.driver)
        home_page.move_first_product_to_cart()
        home_page.click_to_add_first_product_to_cart()
        time.sleep(2)
        home_page.click_on_cart()
        time.sleep(2)
        cart_page = CartPage(self.driver)
        cart_page.click_on_checkout_btn()
        cart_page.enter_shipping_details("Flora", "Bing", 80899)
        cart_page.click_on_continue_btn()
        time.sleep(2)
        #cart_page.verify_calculation()
        cart_page.call_cal()
        time.sleep(2)






