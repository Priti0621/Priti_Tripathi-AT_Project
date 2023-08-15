from selenium.webdriver.common.by import By


class PIMModulePage:
    def __init__(self, driver):
        self.pimpage_driver = driver

    pim_menu_locator = "//span[text()='PIM']"
    add_button_locator = '//button[text()= " Add "]'
    first_name_locator  = "firstName"
    middle_name_locator = "middleName"
    last_name_locator = "lastName"
    save_button_locator = "//button[text()=' Save ']"
    edit_action_locator = "(//button[@class='oxd-icon-button oxd-table-cell-action-space']/i[@class='oxd-icon bi-pencil-fill'])[2]/."
    update_locator = "(//button[text()=' Save '])[1]"
    delete_action_locator = "(//button[@class='oxd-icon-button oxd-table-cell-action-space']/i[@class='oxd-icon bi-trash'])[2]/."

    def click_pim_menu(self):
        self.pimpage_driver.find_element(By.XPATH, self.pim_menu_locator).click()

    def click_add_button(self):
        self.pimpage_driver.find_element(By.XPATH, self.add_button_locator).click()

    def input_first_name(self, firstname):
        self.pimpage_driver.find_element(By.NAME, self.first_name_locator).send_keys(firstname)

    def input_middle_name(self, middlename):
        self.pimpage_driver.find_element(By.NAME, self.middle_name_locator).send_keys(middlename)

    def input_last_name(self, lastname):
        self.pimpage_driver.find_element(By.NAME, self.last_name_locator).send_keys(lastname)

    def click_save_button(self):
        self.pimpage_driver.find_element(By.XPATH, self.save_button_locator).click()

    def edit_employee(self):
        self.pimpage_driver.find_element(By.XPATH, self.edit_action_locator).click()

    def update_employee(self):
        self.pimpage_driver.find_element(By.XPATH, self.update_locator).click()

    def delete_employee(self):
        self.pimpage_driver.find_element(By.XPATH, self.delete_action_locator).click()

