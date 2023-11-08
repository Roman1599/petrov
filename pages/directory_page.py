from selenium.webdriver.common.by import By

from base.base_page import BasePage

from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
import time
from selenium.webdriver import Keys

class DirectoryPage(BasePage):

    PAGE_URL = Links.DIRECTORY_PAGE

    EMPLOYEE_NAME = ("xpath","//*[@placeholder='Type for hints...']")
    FIRST_NAME = ("xpath","//span[text()='Luis  Suarez']")
    JOB_TITLE = ("xpath","(//*[@class='oxd-select-text--after'])[1]")
    JOB_ASSISTANT = ("xpath", "//span[text()='QA QC Engineer1275']")
    LOCATION = ("xpath", "(//*[@class='oxd-select-text--after'])[2]")
    CANADIAN_LOC = ("xpath", "//span[text()='Home']")
    SEARCH_BTN = ("xpath", "//*[text()=' Search ']")


    @allure.step("Add fields")
    def add_field_employee(self, new_employee=None):
        employee_field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME))
        employee_field.send_keys(new_employee)
        self.value = new_employee
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME)).click()


    @allure.step("Click on Post button")
    def click_search_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()
