import json
import time
import unittest
from orangehrmpages.login_page_class import HrmLoginPage
from selenium import webdriver
from AT_Project1.page_class.pim_module_page_class import PIMModulePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert


class PIMModulePageTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        print("Launching my chrome browser before all my test cases start running")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        hrmlpobject = HrmLoginPage(cls.driver)
        pim_actions = ActionChains(cls.driver)

        json_file_path = "C:\\Users\\Hp\\PycharmProjects\\pythonProjectLect1\\AT_Project1\\DataSource\\test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

        hrmlpobject.input_username(cls.data_dict.get("Login_test").get("correct_user_name"))
        hrmlpobject.input_password(cls.data_dict.get("Login_test").get("correct_password"))
        hrmlpobject.click_login_button()
        pim_module = PIMModulePage(cls.driver)
        pim_module.click_pim_menu()
        pim_alert = Alert(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # Add new Employee in PIM Module
    def test_addition_of_employee_details(self):
       pim_module = PIMModulePage(self.driver)
       pim_module.click_add_button()
       pim_module.input_first_name(self.data_dict.get("Add_employee_data").get("First_name"))
       pim_module.input_middle_name(self.data_dict.get("Add_employee_data").get("Middle_name"))
       pim_module.input_last_name(self.data_dict.get("Add_employee_data").get("Last_name"))
       time.sleep(30)
       pim_module.click_save_button()

    #  Edit existing employee in PIM module
    def test_edition_of_existing_employee(self):
        pim_module = PIMModulePage(self.driver)
        pim_module.edit_employee()
        self.driver.execute_script()
        pim_module.input_first_name(self.data_dict.get("Add_employee_data").get("First_name"))
        pim_module.update_employee()
        time.sleep(10)

    # Delete an existing employee in PIM module
    def test_deletion_of_existing_employee(self):
        pim_module = PIMModulePage(self.driver)
        pim_module.delete_employee()
        # pim_alert = Alert(self.driver)
        # pim_alert.accept()
        time.sleep(10)











