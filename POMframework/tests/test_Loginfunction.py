import time

from Utilities.ExcelUtils import get_cell_data, get_data_from_sheet
from pages.homepage import HomePage
from pages.loginpage import LoginPage
import pytest

class Test_Login:

    def test_login(self):

        login_page = LoginPage(self.driver)
        #login_page.login_saucedemo('standard_user', 'secret_sauce')
        #login_page.login_saucedemo(get_cell_data("C:\\Users\\roshj\\PycharmProjects\\Test\\POMframework\\TestData\\saucedemo_testdata.xlsx","logindata", 2, 1),get_cell_data("C:\\Users\\roshj\\PycharmProjects\\Test\\POMframework\\TestData\\saucedemo_testdata.xlsx","logindata", 2, 2))
        login_page.login_saucedemo((get_data_from_sheet("C:\\Users\\roshj\\PycharmProjects\\Test\\POMframework\\TestData\\saucedemo_testdata.xlsx", "logindata")))
        time.sleep(3)
        home_page = HomePage(self.driver)
        #home_page.click_on_cart()
        time.sleep(3)
