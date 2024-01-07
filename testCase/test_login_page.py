import time
import page
import pytest
from selenium import webdriver
from pageObject.LoginPage import Loginpage
from utilities.readproperty import ReadConfig
from utilities.customLogger import LogGen


class Test_01_Login_Page:
    # shifted this section to config.ini input data
    base_url = ReadConfig.get_application_uRL()
    username = ReadConfig.user_email()
    password = ReadConfig.user_password()
    logger = LogGen.loggen()

    # Test home page title and verify
    def test_homepagetitle(self, setup):
        self.logger.info("----Test started-----")
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.info("---------- verifying login title-----------")
        verify_title = self.driver.title
        print(verify_title)
        time.sleep(10)
        if verify_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C://Users//msi1//PycharmProjects//framework_frm_Scratch//screenshots")
            self.logger.info("--------Test failed ----------")
            self.driver.close()
            assert False

    # Test Login
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Loginpage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login_button()
        self.driver.quit()
        self.logger.info('-----------Login Test for cas2 is passed------------')
        # add assertion
