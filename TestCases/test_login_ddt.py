from selenium import webdriver
import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import xlUtilities

class Test_Login:

    baseURL=ReadConfig.getURL()
    username=ReadConfig.getUsername()
    passowrd=ReadConfig.getPassword()

    #### Test data path variable
    path=".\\TestData\LoginData.xlsx"


    #####  To acces
    log=LogGen.loggen()


    # def test_homePage_title(self,setup):
    #     self.driver=setup
    #     # self.driver.get(Test_Login.baseURL)
    #     self.driver.get(self.baseURL)
    #     act_title=self.driver.title
    #     if act_title=="Your store. Login":
    #         assert True
    #         self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage_title.jpg")
    #         self.driver.close()
    #     else:
    #         assert False

    def test_login_DDT(self,setup):
        self.driver = setup
        # self.driver.get(Test_Login.baseURL)
        self.driver.get(self.baseURL)


        #########    Log    ###############
        self.log.info("**********************test_login_DDT********************************")
        self.log.info("**********************Launch application successfully***************")

        self.lp=LoginPage(self.driver)
        # self.lp.setUserName(Test_Login.username)
        # self.lp.setPassword(Test_Login.passowrd)

        # Read from config.ini
        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.passowrd)


        ## Read dataa from Testdata file
        self.rows=xlUtilities.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel:",self.rows)

        lst_status=[]
        for r in range(2,self.rows+1):
            self.user_name=xlUtilities.readData(self.path,'Sheet1',r,1)
            self.user_passowrd=xlUtilities.readData(self.path,'Sheet1',r,2)
            self.exp=xlUtilities.readData(self.path,'Sheet1',r,3)   ###########3  excepected

            self.lp.setUserName(self.user_name)
            self.lp.setPassword(self.user_passowrd)

            self.lp.clickLogin()
            # self.lp.clickLogOut()

        self.log.info("Login is successfull.")
        self.log.info("Login is done")

            # act_title=self.driver.title
            # exp_title="DashDashboard / nopCommerce administration"
            #
            # if act_title==exp_title:
            #     if self.exp=="Pass":
            #         self.log.info("***********  Pass    **********")
            #         self.lp.clickLogOut()
            #         self.log.info("Log Out is successfull.")
            #         lst_status.append("Pass")
            #     elif self.exp=="Fail":
            #         self.log.info("***********  Fail    **********")
            #         self.lp.clickLogOut()
            #         self.log.info("Log Out is successfull.")
            #         lst_status.append("Fail")

        self.driver.close()
        self.log.info("Application closed successfully")

