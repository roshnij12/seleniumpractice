from pages.homepage import HomePage
from pages.loginpage import LoginPage


class Test_Logout:

    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.login_saucedemo('standard_user', 'secret_sauce')

        home_page =HomePage(self.driver)
        home_page.click_on_menu()
        home_page.click_on_logout()

