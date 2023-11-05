from base.base_page import BasePage

from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
import time
from selenium.webdriver import Keys

class DirectoryPage(BasePage):

    PAGE_URL = Links.BUZZ_PAGE

    EMPLOYEE_NAME = ("xpath","//*[@placeholder='Type for hints...']")
    JOB_TITLE = ("xpath","(//*[@class='oxd-select-text--after'])[1]")
    JOB_ASSISTANT = ("xpath", "//div[@class='oxd-select-option --selected']")
    LOCATION = ("xpath", "(//*[@class='oxd-select-text--after'])[2]")
    CANADIAN_LOC = ("xpath", "//span[text()='Canadian Regional HQ']")
    SEARCH_BTN = ("xpath", "//*[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")


    @allure.step("Add fields")
    def add_field_employee(self, new_employee=None):
        employee_field = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME))
        employee_field.send_keys(new_employee)
        self.value = new_employee

    @allure.step("Add fields")
    def choose_params_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.JOB_TITLE)).click()
        self.wait.until(EC.element_to_be_clickable(self.JOB_ASSISTANT)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOCATION)).click()
        self.wait.until(EC.element_to_be_clickable(self.CANADIAN_LOC)).click()



    @allure.step("Click on Post button")
    def click_search_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()

