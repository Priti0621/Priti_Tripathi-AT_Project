from selenium.webdriver.common.by import By


class OrangeHrmPage:

    def __init__(self,driver):
        self.loginpage_driver = driver

    username_locator = "username"
    password_locator = "password"
    login_locator ="//button[text()=' Login ']"

    def input_username(self,username):
            self.loginpage_driver.find_element(By.NAME, self.username_locator).send_keys(username)

    def input_password(self, password):
            self.loginpage_driver.find_element(By.NAME, self.password_locator).send_keys(password)

    def click_login_button(self):
            self.loginpage_driver.find_element(By.XPATH, self.login_locator).click()
