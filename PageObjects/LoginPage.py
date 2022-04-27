import time


class LoginPage:

    textbox_email_id="Email"
    textbox_password_id="Password"
    button_login_xpath="//button[@class='button-1 login-button']"
    link_text_Logout="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(LoginPage.textbox_email_id).clear()
        self.driver.find_element_by_id(LoginPage.textbox_email_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(LoginPage.textbox_password_id).clear()
        self.driver.find_element_by_id(LoginPage.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(LoginPage.button_login_xpath).click()

    def clickLogOut(self):
        time.sleep(5)
        self.driver.find_element_by_link_text(LoginPage.link_text_Logout).click()



