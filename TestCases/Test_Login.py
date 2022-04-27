from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_Login:

    # baseURL="https://admin-demo.nopcommerce.com/"
    # username="admin@yourstore.com"
    # passowrd="admin"

    #####  To acces
    log=LogGen.loggen()


    def test_homePage_title(self,setup):
        self.driver=setup
        # self.driver.get(Test_Login.baseURL)
        self.driver.get(ReadConfig.getURL())
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage_title.jpg")
            self.driver.close()
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        # self.driver.get(Test_Login.baseURL)
        self.driver.get(ReadConfig.getURL())


        #########    Log    ###############333
        self.log.info("Launch application successfully")

        self.lp=LoginPage(self.driver)
        # self.lp.setUserName(Test_Login.username)
        # self.lp.setPassword(Test_Login.passowrd)

        # Read from config.ini
        self.lp.setUserName(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())

        self.lp.clickLogin()
        self.log.info("Login is successfull.")

        # self.lp.clickLogOut()
        self.log.info("Log Out is successfull.")

        self.driver.close()
        self.log.info("Application closed successfully")

