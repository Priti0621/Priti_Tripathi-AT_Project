import json
import time
import unittest
from selenium import webdriver

from AT_Project1.page_class.orangehrm_login_page_class import OrangeHrmPage


class LoginPageTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        print("Launching my chrome browser before all my test cases start running")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        json_file_path = "C:\\Users\Hp\\PycharmProjects\\pythonProjectLect1\\AT_Project1\\DataSource\\test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

    @classmethod
    def tearDownClass(cls) -> None:
        print("I am after the test class")


    # Test case_ID  : TC_Login_01
    def test_successful_login(self):
        hrmobject = OrangeHrmPage(self.driver)
        hrmobject.input_username(self.data_dict.get("Login_test").get("correct_user_name"))
        hrmobject.input_password(self.data_dict.get("Login_test").get("correct_password"))
        hrmobject.click_login_button()
        time.sleep(20)

    # Test_case_ID : TC_Login_02
    def test_invalid_credential_display(self):
        hrmobject = OrangeHrmPage(self.driver)
        hrmobject.input_username(self.data_dict.get("Login_test").get("correct_user_name"))
        hrmobject.input_password(self.data_dict.get("Login_test").get("incorrect_password"))
        hrmobject.click_login_button()
        time.sleep(20)
