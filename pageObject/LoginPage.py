from selenium.webdriver.common.by import By


class Loginpage:
    # Locators
    textbox_username = "Email"
    textbox_password = "Password"
    button_login = "//button[contains(@type,'submit')]"
    link_text_logout = "Logout"
    label_login ="LOG IN"

# create a constructor to initialize the driver : invoke at the time of object creation.
    def __init__(self, driver):
        self.driver = driver

# create base actions for setting username
    def set_username(self,username):
        self.driver.find_element(By.ID, self.textbox_username).click()
        self.driver.find_element(By.ID, self.textbox_username).clear()
        self.driver.find_element(By.ID, self.textbox_username).send_keys(username)

# create base action for filling password
    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password).clear()
        self.driver.find_element(By. ID, self.textbox_password).send_keys(password)

# create action to click login button
    def click_login_button(self):
        if self.driver.find_element(By.XPATH, self.button_login).text == self.label_login:
            self.driver.find_element(By.XPATH, self.button_login).click()
        else:
            print("Login button text is incorrect")

#  create action to click logout
    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_text_logout).click()


